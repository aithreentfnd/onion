# telegram_bot.py
# SpaceZone Telegram Bot — v10.0
# Full-featured bot with stats, reports, config management, sub-group management, and password change

import asyncio
import os
import re
import httpx
from datetime import datetime, timedelta

from main import (
    LINKS,
    make_link,
    remove_link,
    set_link_active,
    vless_link_for_link,
    get_host,
    fmt_bytes,
    is_link_allowed,
    logger,
    PROTOCOLS,
    DEFAULT_PROTOCOL,
    FINGERPRINTS,
    DEFAULT_FINGERPRINT,
    DEFAULT_ALPN_BY_PROTOCOL,
    DEFAULT_PORT,
    MIN_PORT,
    MAX_PORT,
    parse_size_to_bytes,
    parse_speed_to_bytes,
    SUBS,
    create_sub_group,
    set_link_sub,
    remove_sub_group,
    stats,
    connections,
    AUTH,
    hash_password,
    save_state,
)

BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", "").strip()
_admin_ids_raw = os.environ.get("TELEGRAM_ADMIN_IDS", "").strip()
ADMIN_IDS = {int(x) for x in _admin_ids_raw.replace(" ", "").split(",") if x.isdigit()} if _admin_ids_raw else set()

API_BASE = f"https://api.telegram.org/bot{BOT_TOKEN}"
PAGE_SIZE = 6

_client: httpx.AsyncClient | None = None
_poll_task: asyncio.Task | None = None
_running = False
_pending: dict = {}

WIZARD_STEPS = ["label", "protocol", "fingerprint", "alpn", "port", "volume", "speed", "iplimit", "days"]

PROTOCOL_LABELS = {
    "vless-ws": "VLESS + WebSocket",
    "xhttp-packet-up": "XHTTP (packet-up)",
    "xhttp-stream-up": "XHTTP (stream-up)",
}

def _protocol_label(p: str) -> str:
    return PROTOCOL_LABELS.get(p, p)

def _fp_label(fp: str) -> str:
    return fp.capitalize()

_VOLUME_RE = re.compile(r"^([\d.]+)\s*(GB|MB|KB)?$", re.IGNORECASE)
_SPEED_RE = re.compile(r"^([\d.]+)\s*(MBIT|MBPS|MB|KB)?$", re.IGNORECASE)

def _parse_volume_text(text: str):
    m = _VOLUME_RE.match(text.strip())
    if not m:
        return None
    try:
        value = float(m.group(1))
    except ValueError:
        return None
    if value <= 0:
        return 0
    unit = (m.group(2) or "GB").upper()
    return parse_size_to_bytes(value, unit)

def _parse_speed_text(text: str):
    m = _SPEED_RE.match(text.strip())
    if not m:
        return None
    try:
        value = float(m.group(1))
    except ValueError:
        return None
    if value <= 0:
        return 0
    unit_raw = (m.group(2) or "MBIT").upper()
    unit = "MBIT" if unit_raw in ("MBIT", "MBPS") else unit_raw
    return parse_speed_to_bytes(value, unit)

def _parse_nonneg_int(text: str):
    try:
        n = int(text.strip())
    except ValueError:
        return None
    return max(0, n)

async def _call(method: str, **params):
    if _client is None:
        return None
    try:
        r = await _client.post(f"{API_BASE}/{method}", json=params, timeout=40)
        data = r.json()
        if not data.get("ok"):
            logger.warning(f"Telegram API {method} failed: {data}")
        return data
    except Exception as e:
        logger.warning(f"Telegram API {method} error: {e}")
        return None

async def _send(chat_id: int, text: str, kb: dict | None = None):
    payload = {"chat_id": chat_id, "text": text, "parse_mode": "HTML", "disable_web_page_preview": True}
    if kb:
        payload["reply_markup"] = kb
    return await _call("sendMessage", **payload)

async def _edit(chat_id: int, message_id: int, text: str, kb: dict | None = None):
    payload = {"chat_id": chat_id, "message_id": message_id, "text": text, "parse_mode": "HTML", "disable_web_page_preview": True}
    if kb:
        payload["reply_markup"] = kb
    res = await _call("editMessageText", **payload)
    if res is None or not res.get("ok"):
        await _send(chat_id, text, kb)

async def _answer_cb(cb_id: str, text: str = ""):
    await _call("answerCallbackQuery", callback_query_id=cb_id, text=text)

def _is_admin(chat_id: int) -> bool:
    return chat_id in ADMIN_IDS

# ── Keyboards ────────────────────────────────────────────────────────────────

def _main_menu_kb():
    return {"inline_keyboard": [
        [{"text": "📊 Dashboard", "callback_data": "dashboard"}],
        [{"text": "📋 List Configs", "callback_data": "list:0"}],
        [{"text": "➕ New Config", "callback_data": "newcfg"}],
        [{"text": "🗂 Subscription Groups", "callback_data": "subs:0"}],
        [{"text": "📈 Stats", "callback_data": "stats"}],
        [{"text": "📄 Report", "callback_data": "report"}],
        [{"text": "🔑 Change Panel Password", "callback_data": "changepw"}],
        [{"text": "🔄 Refresh", "callback_data": "menu"}],
    ]}

def _links_list_kb(page: int):
    items = sorted(LINKS.items(), key=lambda kv: kv[1].get("created_at", ""), reverse=True)
    total = len(items)
    start = page * PAGE_SIZE
    chunk = items[start:start + PAGE_SIZE]
    rows = []
    for uid, l in chunk:
        dot = "🟢" if is_link_allowed(l) else "🔴"
        rows.append([{"text": f"{dot} {l.get('label','?')[:28]}", "callback_data": f"view:{uid}"}])
    nav = []
    if start > 0:
        nav.append({"text": "◀ Prev", "callback_data": f"list:{page-1}"})
    if start + PAGE_SIZE < total:
        nav.append({"text": "Next ▶", "callback_data": f"list:{page+1}"})
    if nav:
        rows.append(nav)
    rows.append([{"text": "➕ New Config", "callback_data": "newcfg"}])
    rows.append([{"text": "⬅ Main Menu", "callback_data": "menu"}])
    return {"inline_keyboard": rows}

def _link_detail_kb(uid: str, active: bool):
    return {"inline_keyboard": [
        [{"text": "🔗 Show Link", "callback_data": f"link:{uid}"}],
        [{"text": "📊 Config Stats", "callback_data": f"cfgstats:{uid}"}],
        [{"text": "🗂 Sub Group", "callback_data": f"cfggroup:{uid}"}],
        [{"text": ("⛔ Deactivate" if active else "✅ Activate"), "callback_data": f"toggle:{uid}"}],
        [{"text": "✏️ Edit", "callback_data": f"editcfg:{uid}"}],
        [{"text": "🗑 Delete", "callback_data": f"del:{uid}"}],
        [{"text": "⬅ Back to List", "callback_data": "list:0"}],
    ]}

def _confirm_delete_kb(uid: str):
    return {"inline_keyboard": [
        [{"text": "✅ Yes, delete", "callback_data": f"delok:{uid}"},
         {"text": "❌ Cancel", "callback_data": f"view:{uid}"}],
    ]}

def _wizard_cancel_kb():
    return {"inline_keyboard": [[{"text": "❌ Cancel", "callback_data": "w:cancel"}]]}

def _wizard_protocol_kb():
    rows = [[{"text": _protocol_label(p), "callback_data": f"w:proto:{p}"}] for p in PROTOCOLS]
    rows.append([{"text": "❌ Cancel", "callback_data": "w:cancel"}])
    return {"inline_keyboard": rows}

def _wizard_fp_kb():
    rows, row = [], []
    for fp in FINGERPRINTS:
        row.append({"text": _fp_label(fp), "callback_data": f"w:fp:{fp}"})
        if len(row) == 3:
            rows.append(row); row = []
    if row:
        rows.append(row)
    rows.append([{"text": "❌ Cancel", "callback_data": "w:cancel"}])
    return {"inline_keyboard": rows}

def _wizard_skip_kb(step_key: str, label: str):
    return {"inline_keyboard": [
        [{"text": label, "callback_data": f"w:skip:{step_key}"}],
        [{"text": "❌ Cancel", "callback_data": "w:cancel"}],
    ]}

ALPN_PRESET_MAP = {"p1": "http/1.1", "p2": "h2,http/1.1", "p3": "h2"}

def _wizard_alpn_kb():
    return {"inline_keyboard": [
        [{"text": "🔤 http/1.1 (recommended)", "callback_data": "w:alpnpreset:p1"}],
        [{"text": "🔤 h2,http/1.1", "callback_data": "w:alpnpreset:p2"}],
        [{"text": "🔤 h2", "callback_data": "w:alpnpreset:p3"}],
        [{"text": "⏭ Protocol Default", "callback_data": "w:skip:alpn"}],
        [{"text": "❌ Cancel", "callback_data": "w:cancel"}],
    ]}

def _wizard_unlimited_kb(step_key: str):
    return _wizard_skip_kb(step_key, "♾ Unlimited")

def _wizard_confirm_kb():
    return {"inline_keyboard": [
        [{"text": "✅ Create Config", "callback_data": "w:confirm"}],
        [{"text": "❌ Cancel", "callback_data": "w:cancel"}],
    ]}

def _wizard_prompt(step: str, data: dict) -> str:
    n = WIZARD_STEPS.index(step) + 1 if step in WIZARD_STEPS else len(WIZARD_STEPS)
    head = f"🧩 New Config — Step {n}/{len(WIZARD_STEPS)}\n\n"
    if step == "label":
        return head + "✏️ Enter a label/name for this config:"
    if step == "protocol":
        return head + "🌐 Select protocol:"
    if step == "fingerprint":
        return head + "🖐 Select uTLS fingerprint:"
    if step == "alpn":
        return head + "🔤 Select ALPN (or type custom, e.g. h2,http/1.1):"
    if step == "port":
        return head + f"🔌 Enter port ({MIN_PORT}-{MAX_PORT}) or use default ({DEFAULT_PORT}):"
    if step == "volume":
        return head + "📦 Enter volume limit (e.g. 10GB, 500MB) or choose Unlimited:"
    if step == "speed":
        return head + "🚀 Enter speed limit in Mbps (e.g. 20) or choose Unlimited:"
    if step == "iplimit":
        return head + "👥 Max concurrent IPs/users (0 = unlimited):"
    if step == "days":
        return head + "📅 Expiry in days (0 = never):"
    return head

def _wizard_summary(data: dict) -> str:
    limit = "Unlimited" if not data.get("limit_bytes") else fmt_bytes(data["limit_bytes"])
    speed = "Unlimited" if not data.get("speed_limit_bytes") else f"{data['speed_limit_bytes']*8/1024/1024:.1f} Mbps"
    iplim = data.get("ip_limit", 0) or "Unlimited"
    days = data.get("expires_days", 0)
    days_txt = "Never" if not days else f"{days} days"
    proto = data.get("protocol", DEFAULT_PROTOCOL)
    alpn = data.get("alpn") or f"Default ({DEFAULT_ALPN_BY_PROTOCOL.get(proto, 'http/1.1')})"
    return (
        "🧩 New Config Summary — Confirm:\n\n"
        f"Label: <b>{data.get('label','?')}</b>\n"
        f"Protocol: {_protocol_label(proto)}\n"
        f"Fingerprint: {_fp_label(data.get('fingerprint', DEFAULT_FINGERPRINT))}\n"
        f"ALPN: {alpn}\n"
        f"Port: {data.get('port', DEFAULT_PORT)}\n"
        f"Volume Limit: {limit}\n"
        f"Speed Limit: {speed}\n"
        f"IP Limit: {iplim}\n"
        f"Expiry: {days_txt}"
    )

def _format_detail(uid: str, l: dict) -> str:
    status = "🟢 Active" if is_link_allowed(l) else "🔴 Inactive/Expired"
    limit = "Unlimited" if not l.get("limit_bytes") else fmt_bytes(l["limit_bytes"])
    speed = "Unlimited" if not l.get("speed_limit_bytes") else f"{l['speed_limit_bytes']*8/1024/1024:.1f} Mbps"
    exp = l.get("expires_at")
    exp_txt = exp.split("T")[0] if exp else "Never"
    proto = l.get("protocol", DEFAULT_PROTOCOL)
    alpn = l.get("alpn") or f"Default ({DEFAULT_ALPN_BY_PROTOCOL.get(proto, 'http/1.1')})"
    return (
        f"<b>{l.get('label','?')}</b>\n"
        f"Status: {status}\n"
        f"Usage: {fmt_bytes(l.get('used_bytes',0))} / {limit}\n"
        f"Speed Limit: {speed}\n"
        f"IP Limit: {l.get('ip_limit',0) or 'Unlimited'}\n"
        f"Protocol: {_protocol_label(proto)}\n"
        f"Fingerprint: {_fp_label(l.get('fingerprint', DEFAULT_FINGERPRINT))}\n"
        f"ALPN: {alpn}\n"
        f"Port: {l.get('port', DEFAULT_PORT)}\n"
        f"Expiry: {exp_txt}\n"
        f"UUID: <code>{uid}</code>"
    )

def _group_public_url(s: dict) -> str:
    host = get_host()
    return f"https://{host}/p/{s.get('uuid_key','')}"

def _subs_list_kb(page: int):
    items = sorted(SUBS.items(), key=lambda kv: kv[1].get("created_at", ""), reverse=True)
    total = len(items)
    start = page * PAGE_SIZE
    chunk = items[start:start + PAGE_SIZE]
    rows = []
    for sid, s in chunk:
        cnt = len(s.get("link_ids", []))
        rows.append([{"text": f"🗂 {s.get('name','?')[:26]} ({cnt})", "callback_data": f"subview:{sid}"}])
    nav = []
    if start > 0:
        nav.append({"text": "◀ Prev", "callback_data": f"subs:{page-1}"})
    if start + PAGE_SIZE < total:
        nav.append({"text": "Next ▶", "callback_data": f"subs:{page+1}"})
    if nav:
        rows.append(nav)
    rows.append([{"text": "➕ New Group", "callback_data": "newsub"}])
    rows.append([{"text": "⬅ Main Menu", "callback_data": "menu"}])
    return {"inline_keyboard": rows}

def _format_sub_detail(sid: str, s: dict) -> str:
    cnt = len(s.get("link_ids", []))
    pw = "🔒 Has password" if s.get("password_hash") else "No password"
    desc = s.get("desc") or "—"
    return (
        f"🗂 <b>{s.get('name','?')}</b>\n"
        f"Description: {desc}\n"
        f"Configs in group: {cnt}\n"
        f"Password: {pw}\n\n"
        f"🔗 Public group link:\n<code>{_group_public_url(s)}</code>"
    )

def _sub_detail_kb(sid: str):
    return {"inline_keyboard": [
        [{"text": "➕ Add Config to Group", "callback_data": f"subaddlink:{sid}:0"}],
        [{"text": "🗑 Delete Group", "callback_data": f"subdel:{sid}"}],
        [{"text": "⬅ Back to Groups", "callback_data": "subs:0"}],
    ]}

def _confirm_subdel_kb(sid: str):
    return {"inline_keyboard": [
        [{"text": "✅ Yes, delete", "callback_data": f"subdelok:{sid}"},
         {"text": "❌ Cancel", "callback_data": f"subview:{sid}"}],
    ]}

def _pick_link_for_group_kb(sid: str, page: int):
    items = sorted(LINKS.items(), key=lambda kv: kv[1].get("created_at", ""), reverse=True)
    total = len(items)
    start = page * PAGE_SIZE
    chunk = items[start:start + PAGE_SIZE]
    rows = []
    for uid, l in chunk:
        in_this = "✅ " if l.get("sub_id") == sid else ""
        rows.append([{"text": f"{in_this}{l.get('label','?')[:28]}", "callback_data": f"subaddlinkdo:{uid}"}])
    nav = []
    if start > 0:
        nav.append({"text": "◀ Prev", "callback_data": f"subaddlink:{sid}:{page-1}"})
    if start + PAGE_SIZE < total:
        nav.append({"text": "Next ▶", "callback_data": f"subaddlink:{sid}:{page+1}"})
    if nav:
        rows.append(nav)
    rows.append([{"text": "⬅ Back to Group", "callback_data": f"subview:{sid}"}])
    return {"inline_keyboard": rows}

def _cfg_group_kb(uid: str):
    link = LINKS.get(uid, {})
    sid = link.get("sub_id")
    if sid and sid in SUBS:
        return {"inline_keyboard": [
            [{"text": "➖ Remove from Group", "callback_data": f"cfgungroup:{uid}"}],
            [{"text": "⬅ Back", "callback_data": f"view:{uid}"}],
        ]}
    rows = []
    for sid2, s in sorted(SUBS.items(), key=lambda kv: kv[1].get("created_at", ""), reverse=True)[:8]:
        rows.append([{"text": f"➕ Add to «{s.get('name','?')[:24]}»", "callback_data": f"cfgaddgroup:{sid2}"}])
    rows.append([{"text": "🆕 New Group + Add", "callback_data": f"cfgnewgroup:{uid}"}])
    rows.append([{"text": "⬅ Back", "callback_data": f"view:{uid}"}])
    return {"inline_keyboard": rows}

def _format_cfg_group(uid: str) -> str:
    link = LINKS.get(uid, {})
    sid = link.get("sub_id")
    if sid and sid in SUBS:
        s = SUBS[sid]
        return (
            f"🗂 Config «{link.get('label','?')}» is in group «{s.get('name','?')}».\n\n"
            f"🔗 Public group link:\n<code>{_group_public_url(s)}</code>"
        )
    return (
        f"Config «{link.get('label','?')}» is not in any group.\n\n"
        "To get a professional subscription page, add it to a group or create a new one."
    )

def _format_stats() -> str:
    total_configs = len(LINKS)
    active_configs = sum(1 for l in LINKS.values() if is_link_allowed(l))
    total_groups = len(SUBS)
    active_connections = len(connections)
    total_traffic_mb = round(stats.get("total_bytes", 0) / (1024 ** 2), 2)
    total_requests = stats.get("total_requests", 0)
    total_errors = stats.get("total_errors", 0)
    return (
        "📊 <b>SpaceZone Dashboard</b>\n\n"
        f"📋 Configs: <b>{total_configs}</b> (Active: <b>{active_configs}</b>)\n"
        f"🗂 Groups: <b>{total_groups}</b>\n"
        f"🔌 Active Connections: <b>{active_connections}</b>\n"
        f"📈 Total Traffic: <b>{total_traffic_mb:.2f} MB</b>\n"
        f"📨 Total Requests: <b>{total_requests}</b>\n"
        f"⚠️ Total Errors: <b>{total_errors}</b>"
    )

def _format_report() -> str:
    if not LINKS:
        return "📄 No configs found."
    lines = ["📄 <b>Full Config Report</b>\n"]
    for uid, l in LINKS.items():
        status = "🟢 Active" if is_link_allowed(l) else "🔴 Inactive"
        limit = "∞" if not l.get("limit_bytes") else fmt_bytes(l["limit_bytes"])
        used = fmt_bytes(l.get("used_bytes", 0))
        lines.append(f"• <b>{l.get('label','?')}</b> [{status}] — {used} / {limit}")
    return "\n".join(lines)

# ── Update handling ──────────────────────────────────────────────────────────

async def _handle_message(msg: dict):
    chat_id = msg.get("chat", {}).get("id")
    text = (msg.get("text") or "").strip()
    if chat_id is None:
        return
    if not _is_admin(chat_id):
        await _send(chat_id, "⛔ You are not authorized to use this bot.")
        return

    if text in ("/start", "/menu"):
        _pending.pop(chat_id, None)
        await _send(chat_id, "👋 Welcome to <b>SpaceZone Bot</b> v10.0.\nUse the buttons below to manage your configs and groups:", _main_menu_kb())
        return

    if text in ("/stop", "/cancel"):
        _pending.pop(chat_id, None)
        await _send(chat_id, "🛑 Operation cancelled.", _main_menu_kb())
        return

    if text == "/help":
        await _send(chat_id, (
            "🤖 <b>SpaceZone Bot Help</b>\n\n"
            "/start - Show main menu\n"
            "/menu - Same as start\n"
            "/cancel - Cancel any ongoing operation\n"
            "/stop - Same as cancel\n"
            "/help - Show this message\n"
            "/stats - Show dashboard stats\n"
            "/report - Generate full config report\n\n"
            "You can manage configs and subscription groups directly from the buttons."
        ), _main_menu_kb())
        return

    if text == "/stats":
        await _send(chat_id, _format_stats(), _main_menu_kb())
        return

    if text == "/report":
        await _send(chat_id, _format_report(), _main_menu_kb())
        return

    pending = _pending.get(chat_id)

    if pending and pending.get("action") == "newsub" and pending.get("step") == "name" and text:
        name = text[:60]
        sid, s = await create_sub_group(name=name)
        link_uid = pending.get("link_uid")
        _pending.pop(chat_id, None)
        if link_uid and link_uid in LINKS:
            await set_link_sub(link_uid, sid)
            await _send(chat_id, f"✅ Group created and config added.\n\n{_format_cfg_group(link_uid)}", _cfg_group_kb(link_uid))
        else:
            await _send(chat_id, f"✅ Group created.\n\n{_format_sub_detail(sid, s)}", _sub_detail_kb(sid))
        return

    if pending and pending.get("action") == "changepw" and pending.get("step") == "current":
        pending["data"] = {"current": text}
        pending["step"] = "new"
        await _send(chat_id, "🔑 Enter <b>new password</b> (minimum 4 characters):", _wizard_cancel_kb())
        return

    if pending and pending.get("action") == "changepw" and pending.get("step") == "new":
        new_pw = text.strip()
        if len(new_pw) < 4:
            await _send(chat_id, "❌ Password must be at least 4 characters. Try again:", _wizard_cancel_kb())
            return
        pending["data"]["new"] = new_pw
        pending["step"] = "confirm"
        await _send(chat_id, f"🔑 Confirm new password:\n<code>{new_pw}</code>\n\nType <b>YES</b> to confirm, or <b>/cancel</b> to abort.", _wizard_cancel_kb())
        return

    if pending and pending.get("action") == "changepw" and pending.get("step") == "confirm":
        if text.upper() == "YES":
            current = pending["data"].get("current", "")
            new_pw = pending["data"].get("new", "")
            if hash_password(current) != AUTH["password_hash"]:
                _pending.pop(chat_id, None)
                await _send(chat_id, "❌ Current password is wrong. Operation cancelled.", _main_menu_kb())
                return
            AUTH["password_hash"] = hash_password(new_pw)
            await save_state()
            _pending.pop(chat_id, None)
            await _send(chat_id, "✅ Panel password changed successfully.", _main_menu_kb())
        else:
            _pending.pop(chat_id, None)
            await _send(chat_id, "❌ Password change cancelled.", _main_menu_kb())
        return

    if pending and pending.get("action") == "wizard" and text:
        step = pending["step"]
        data = pending["data"]

        if step == "label":
            data["label"] = text[:60] or "New Config"
            pending["step"] = "protocol"
            await _send(chat_id, _wizard_prompt("protocol", data), _wizard_protocol_kb())
            return

        if step in ("protocol", "fingerprint"):
            kb = _wizard_protocol_kb() if step == "protocol" else _wizard_fp_kb()
            await _send(chat_id, "Please select one from the buttons above 👆", kb)
            return

        if step == "alpn":
            data["alpn"] = text.strip()[:100]
            pending["step"] = "port"
            await _send(chat_id, _wizard_prompt("port", data), _wizard_skip_kb("port", f"⏭ Default ({DEFAULT_PORT})"))
            return

        if step == "port":
            try:
                p = int(text.strip())
            except ValueError:
                p = None
            if p is None or not (MIN_PORT <= p <= MAX_PORT):
                await _send(chat_id, f"❗ Invalid port. Enter a number between {MIN_PORT} and {MAX_PORT}:", _wizard_skip_kb("port", f"⏭ Default ({DEFAULT_PORT})"))
                return
            data["port"] = p
            pending["step"] = "volume"
            await _send(chat_id, _wizard_prompt("volume", data), _wizard_unlimited_kb("volume"))
            return

        if step == "volume":
            parsed = _parse_volume_text(text)
            if parsed is None:
                await _send(chat_id, "❗ Invalid format. Use e.g. 10GB or 500MB:", _wizard_unlimited_kb("volume"))
                return
            data["limit_bytes"] = parsed
            pending["step"] = "speed"
            await _send(chat_id, _wizard_prompt("speed", data), _wizard_unlimited_kb("speed"))
            return

        if step == "speed":
            parsed = _parse_speed_text(text)
            if parsed is None:
                await _send(chat_id, "❗ Invalid format. Enter a number (e.g. 20 for Mbps):", _wizard_unlimited_kb("speed"))
                return
            data["speed_limit_bytes"] = parsed
            pending["step"] = "iplimit"
            await _send(chat_id, _wizard_prompt("iplimit", data), _wizard_unlimited_kb("iplimit"))
            return

        if step == "iplimit":
            n = _parse_nonneg_int(text)
            if n is None:
                await _send(chat_id, "❗ Enter a valid integer:", _wizard_unlimited_kb("iplimit"))
                return
            data["ip_limit"] = n
            pending["step"] = "days"
            await _send(chat_id, _wizard_prompt("days", data), _wizard_unlimited_kb("days"))
            return

        if step == "days":
            n = _parse_nonneg_int(text)
            if n is None:
                await _send(chat_id, "❗ Enter a valid integer (days):", _wizard_unlimited_kb("days"))
                return
            data["expires_days"] = n
            pending["step"] = "confirm"
            await _send(chat_id, _wizard_summary(data), _wizard_confirm_kb())
            return

    await _send(chat_id, "Use the buttons below:", _main_menu_kb())

async def _handle_callback(cb: dict):
    chat_id = cb.get("message", {}).get("chat", {}).get("id")
    message_id = cb.get("message", {}).get("message_id")
    data = cb.get("data", "")
    cb_id = cb.get("id")

    if chat_id is None or not _is_admin(chat_id):
        await _answer_cb(cb_id, "⛔ Access denied")
        return
    await _answer_cb(cb_id)

    if data == "menu":
        _pending.pop(chat_id, None)
        await _edit(chat_id, message_id, "SpaceZone Management Menu:", _main_menu_kb())
        return

    if data == "dashboard":
        await _edit(chat_id, message_id, _format_stats(), _main_menu_kb())
        return

    if data == "stats":
        await _edit(chat_id, message_id, _format_stats(), _main_menu_kb())
        return

    if data == "report":
        await _edit(chat_id, message_id, _format_report(), _main_menu_kb())
        return

    if data == "changepw":
        _pending[chat_id] = {"action": "changepw", "step": "current", "data": {}}
        await _edit(chat_id, message_id, "🔑 Enter <b>current password</b>:", _wizard_cancel_kb())
        return

    if data.startswith("list:"):
        page = int(data.split(":", 1)[1] or 0)
        if not LINKS:
            await _edit(chat_id, message_id, "No configs created yet.", _main_menu_kb())
            return
        await _edit(chat_id, message_id, f"📋 Configs ({len(LINKS)} items):", _links_list_kb(page))
        return

    if data.startswith("subs:"):
        page = int(data.split(":", 1)[1] or 0)
        if not SUBS:
            await _edit(chat_id, message_id, "No groups yet.\n\nCreate a group first to get a professional subscription page.", _subs_list_kb(0))
            return
        await _edit(chat_id, message_id, f"🗂 Groups ({len(SUBS)} items):", _subs_list_kb(page))
        return

    if data == "newsub":
        _pending[chat_id] = {"action": "newsub", "step": "name", "link_uid": None}
        await _edit(chat_id, message_id, "✏️ Enter a name for the new group:", _wizard_cancel_kb())
        return

    if data.startswith("subview:"):
        sid = data.split(":", 1)[1]
        s = SUBS.get(sid)
        if not s:
            await _edit(chat_id, message_id, "This group no longer exists.", _main_menu_kb())
            return
        await _edit(chat_id, message_id, _format_sub_detail(sid, s), _sub_detail_kb(sid))
        return

    if data.startswith("subaddlink:"):
        _, sid, page_s = data.split(":", 2)
        if sid not in SUBS:
            await _edit(chat_id, message_id, "This group no longer exists.", _main_menu_kb())
            return
        if not LINKS:
            await _edit(chat_id, message_id, "No configs to add.", _sub_detail_kb(sid))
            return
        _pending[chat_id] = {"action": "subaddlink_ctx", "sid": sid}
        await _edit(chat_id, message_id, "Which config should I add to this group?", _pick_link_for_group_kb(sid, int(page_s or 0)))
        return

    if data.startswith("subaddlinkdo:"):
        uid = data.split(":", 1)[1]
        ctx = _pending.get(chat_id) or {}
        sid = ctx.get("sid") if ctx.get("action") == "subaddlink_ctx" else None
        if not sid or sid not in SUBS:
            await _answer_cb(cb_id, "This operation has expired. Try again from group menu.")
            return
        ok = await set_link_sub(uid, sid)
        if not ok:
            await _answer_cb(cb_id, "Config no longer exists")
            return
        _pending.pop(chat_id, None)
        s = SUBS.get(sid)
        await _edit(chat_id, message_id, f"✅ Config added.\n\n{_format_sub_detail(sid, s)}", _sub_detail_kb(sid))
        return

    if data.startswith("subdel:"):
        sid = data.split(":", 1)[1]
        s = SUBS.get(sid)
        if not s:
            await _edit(chat_id, message_id, "This group no longer exists.", _main_menu_kb())
            return
        await _edit(chat_id, message_id, f"❗ Delete group «{s.get('name')}»? Configs inside will not be deleted, just removed from the group.", _confirm_subdel_kb(sid))
        return

    if data.startswith("subdelok:"):
        sid = data.split(":", 1)[1]
        name = await remove_sub_group(sid)
        if name is None:
            await _edit(chat_id, message_id, "This group was already deleted.", _main_menu_kb())
        else:
            await _edit(chat_id, message_id, f"🗑 Group «{name}» deleted.", _main_menu_kb())
        return

    if data.startswith("cfggroup:"):
        uid = data.split(":", 1)[1]
        if uid not in LINKS:
            await _edit(chat_id, message_id, "Config no longer exists.", _main_menu_kb())
            return
        _pending[chat_id] = {"action": "cfg_group_ctx", "uid": uid}
        await _edit(chat_id, message_id, _format_cfg_group(uid), _cfg_group_kb(uid))
        return

    if data.startswith("cfgungroup:"):
        uid = data.split(":", 1)[1]
        await set_link_sub(uid, None)
        l = LINKS.get(uid)
        if not l:
            await _edit(chat_id, message_id, "Config no longer exists.", _main_menu_kb())
            return
        await _edit(chat_id, message_id, _format_detail(uid, l), _link_detail_kb(uid, l["active"]))
        return

    if data.startswith("cfgaddgroup:"):
        sid = data.split(":", 1)[1]
        ctx = _pending.get(chat_id) or {}
        uid = ctx.get("uid") if ctx.get("action") == "cfg_group_ctx" else None
        if not uid or uid not in LINKS:
            await _answer_cb(cb_id, "This operation has expired. Please re-enter from the config view.")
            return
        ok = await set_link_sub(uid, sid)
        if not ok:
            await _answer_cb(cb_id, "Group no longer exists")
            return
        _pending.pop(chat_id, None)
        await _edit(chat_id, message_id, f"✅ Config added to group.\n\n{_format_cfg_group(uid)}", _cfg_group_kb(uid))
        return

    if data.startswith("cfgnewgroup:"):
        uid = data.split(":", 1)[1]
        if uid not in LINKS:
            await _edit(chat_id, message_id, "Config no longer exists.", _main_menu_kb())
            return
        _pending[chat_id] = {"action": "newsub", "step": "name", "link_uid": uid}
        await _edit(chat_id, message_id, "✏️ Enter name for the new group. The config will be automatically added:", _wizard_cancel_kb())
        return

    if data.startswith("editcfg:"):
        uid = data.split(":", 1)[1]
        l = LINKS.get(uid)
        if not l:
            await _edit(chat_id, message_id, "Config no longer exists.", _main_menu_kb())
            return
        # Simplified edit via re-creation wizard with pre-filled data
        _pending[chat_id] = {"action": "wizard", "step": "label", "data": {"edit_uid": uid, "label": l.get("label", "New Config")}}
        await _edit(chat_id, message_id, "✏️ Enter new label (or send /cancel to abort):", _wizard_cancel_kb())
        return

    if data == "newcfg":
        _pending[chat_id] = {"action": "wizard", "step": "label", "data": {}}
        await _edit(chat_id, message_id, _wizard_prompt("label", {}), _wizard_cancel_kb())
        return

    if data == "w:cancel":
        _pending.pop(chat_id, None)
        await _edit(chat_id, message_id, "Operation cancelled.", _main_menu_kb())
        return

    if data.startswith("w:"):
        pending = _pending.get(chat_id)
        if not pending or pending.get("action") != "wizard":
            await _edit(chat_id, message_id, "This step is no longer valid. Restart from menu.", _main_menu_kb())
            return

        step = pending["step"]
        wdata = pending["data"]

        if data.startswith("w:proto:") and step == "protocol":
            proto = data.split(":", 2)[2]
            wdata["protocol"] = proto if proto in PROTOCOLS else DEFAULT_PROTOCOL
            pending["step"] = "fingerprint"
            await _edit(chat_id, message_id, _wizard_prompt("fingerprint", wdata), _wizard_fp_kb())
            return

        if data.startswith("w:fp:") and step == "fingerprint":
            fp = data.split(":", 2)[2]
            wdata["fingerprint"] = fp if fp in FINGERPRINTS else DEFAULT_FINGERPRINT
            pending["step"] = "alpn"
            await _edit(chat_id, message_id, _wizard_prompt("alpn", wdata), _wizard_alpn_kb())
            return

        if data.startswith("w:alpnpreset:") and step == "alpn":
            code = data.split(":", 2)[2]
            wdata["alpn"] = ALPN_PRESET_MAP.get(code, "")
            pending["step"] = "port"
            await _edit(chat_id, message_id, _wizard_prompt("port", wdata), _wizard_skip_kb("port", f"⏭ Default ({DEFAULT_PORT})"))
            return

        if data == "w:skip:alpn" and step == "alpn":
            wdata["alpn"] = ""
            pending["step"] = "port"
            await _edit(chat_id, message_id, _wizard_prompt("port", wdata), _wizard_skip_kb("port", f"⏭ Default ({DEFAULT_PORT})"))
            return

        if data == "w:skip:port" and step == "port":
            wdata["port"] = DEFAULT_PORT
            pending["step"] = "volume"
            await _edit(chat_id, message_id, _wizard_prompt("volume", wdata), _wizard_unlimited_kb("volume"))
            return

        if data == "w:skip:volume" and step == "volume":
            wdata["limit_bytes"] = 0
            pending["step"] = "speed"
            await _edit(chat_id, message_id, _wizard_prompt("speed", wdata), _wizard_unlimited_kb("speed"))
            return

        if data == "w:skip:speed" and step == "speed":
            wdata["speed_limit_bytes"] = 0
            pending["step"] = "iplimit"
            await _edit(chat_id, message_id, _wizard_prompt("iplimit", wdata), _wizard_unlimited_kb("iplimit"))
            return

        if data == "w:skip:iplimit" and step == "iplimit":
            wdata["ip_limit"] = 0
            pending["step"] = "days"
            await _edit(chat_id, message_id, _wizard_prompt("days", wdata), _wizard_unlimited_kb("days"))
            return

        if data == "w:skip:days" and step == "days":
            wdata["expires_days"] = 0
            pending["step"] = "confirm"
            await _edit(chat_id, message_id, _wizard_summary(wdata), _wizard_confirm_kb())
            return

        if data == "w:confirm" and step == "confirm":
            expires_days = wdata.get("expires_days", 0)
            expires_at = (datetime.now() + timedelta(days=expires_days)).isoformat() if expires_days > 0 else None
            uid, link = await make_link(
                label=wdata.get("label") or "New Config",
                limit_bytes=wdata.get("limit_bytes", 0),
                expires_at=expires_at,
                protocol=wdata.get("protocol", DEFAULT_PROTOCOL),
                fingerprint=wdata.get("fingerprint", DEFAULT_FINGERPRINT),
                alpn=wdata.get("alpn", ""),
                port=wdata.get("port", DEFAULT_PORT),
                ip_limit=wdata.get("ip_limit", 0),
                speed_limit_bytes=wdata.get("speed_limit_bytes", 0),
            )
            _pending.pop(chat_id, None)
            await _edit(chat_id, message_id, f"✅ Config created.\n\n{_format_detail(uid, link)}", _link_detail_kb(uid, link["active"]))
            return

        await _answer_cb(cb_id, "This button is no longer valid.")
        return

    if data.startswith("view:"):
        uid = data.split(":", 1)[1]
        l = LINKS.get(uid)
        if not l:
            await _edit(chat_id, message_id, "Config no longer exists.", _main_menu_kb())
            return
        await _edit(chat_id, message_id, _format_detail(uid, l), _link_detail_kb(uid, l["active"]))
        return

    if data.startswith("cfgstats:"):
        uid = data.split(":", 1)[1]
        l = LINKS.get(uid)
        if not l:
            await _edit(chat_id, message_id, "Config no longer exists.", _main_menu_kb())
            return
        conn_count = sum(1 for c in connections.values() if c.get("uuid") == uid)
        msg = (
            f"📊 <b>Config Stats</b>\n\n"
            f"Label: <b>{l.get('label','?')}</b>\n"
            f"UUID: <code>{uid}</code>\n"
            f"Status: {'🟢 Active' if is_link_allowed(l) else '🔴 Inactive'}\n"
            f"Usage: {fmt_bytes(l.get('used_bytes',0))} / {fmt_bytes(l.get('limit_bytes',0)) if l.get('limit_bytes',0) > 0 else '∞'}\n"
            f"Active Connections: <b>{conn_count}</b>\n"
            f"IP Limit: {l.get('ip_limit',0) or 'Unlimited'}\n"
            f"Speed Limit: {l.get('speed_limit_bytes',0) or 'Unlimited'}\n"
            f"Expiry: {l.get('expires_at', 'Never')}"
        )
        await _edit(chat_id, message_id, msg, _link_detail_kb(uid, l["active"]))
        return

    if data.startswith("toggle:"):
        uid = data.split(":", 1)[1]
        l = await set_link_active(uid, not LINKS.get(uid, {}).get("active", True))
        if not l:
            await _edit(chat_id, message_id, "Config no longer exists.", _main_menu_kb())
            return
        await _edit(chat_id, message_id, _format_detail(uid, l), _link_detail_kb(uid, l["active"]))
        return

    if data.startswith("link:"):
        uid = data.split(":", 1)[1]
        l = LINKS.get(uid)
        if not l:
            await _answer_cb(cb_id, "Config not found")
            return
        host = get_host()
        vless = vless_link_for_link(l, uid, host)
        sub_url = f"https://{host}/sub/{uid}"
        msg = f"🔗 Connection link for «{l.get('label')}»:\n\n<code>{vless}</code>\n\nSimple subscription link (plain text):\n<code>{sub_url}</code>"
        sid = l.get("sub_id")
        if sid and sid in SUBS:
            msg += f"\n\n✨ Professional group link:\n<code>{_group_public_url(SUBS[sid])}</code>"
        else:
            msg += "\n\nℹ️ This config is not in any group. For a professional subscription page, add it to a group via the 'Sub Group' button."
        await _send(chat_id, msg)
        return

    if data.startswith("del:"):
        uid = data.split(":", 1)[1]
        l = LINKS.get(uid)
        if not l:
            await _edit(chat_id, message_id, "Config no longer exists.", _main_menu_kb())
            return
        await _edit(chat_id, message_id, f"❗ Delete «{l.get('label')}»? This cannot be undone.", _confirm_delete_kb(uid))
        return

    if data.startswith("delok:"):
        uid = data.split(":", 1)[1]
        label = await remove_link(uid)
        if label is None:
            await _edit(chat_id, message_id, "Config was already deleted.", _main_menu_kb())
        else:
            await _edit(chat_id, message_id, f"🗑 Config «{label}» deleted.", _main_menu_kb())
        return

# ── Polling loop ─────────────────────────────────────────────────────────────

async def _poll_loop():
    global _running
    offset = 0
    logger.info(f"🤖 Telegram bot polling started (admins: {len(ADMIN_IDS)})")
    while _running:
        try:
            res = await _call("getUpdates", offset=offset, timeout=30, allowed_updates=["message", "callback_query"])
            if not res or not res.get("ok"):
                await asyncio.sleep(3)
                continue
            for upd in res.get("result", []):
                offset = upd["update_id"] + 1
                try:
                    if "message" in upd:
                        await _handle_message(upd["message"])
                    elif "callback_query" in upd:
                        await _handle_callback(upd["callback_query"])
                except Exception as e:
                    logger.warning(f"Telegram update handling error: {e}")
        except asyncio.CancelledError:
            break
        except Exception as e:
            logger.warning(f"Telegram poll loop error: {e}")
            await asyncio.sleep(3)

# ── Lifecycle ────────────────────────────────────────────────────────────────

async def start_bot():
    global _client, _poll_task, _running
    if not BOT_TOKEN:
        logger.info("Telegram bot: TELEGRAM_BOT_TOKEN not set. Bot disabled.")
        return
    if not ADMIN_IDS:
        logger.warning("Telegram bot: TELEGRAM_ADMIN_IDS not set. No one can manage (bot runs but rejects all).")
    _client = httpx.AsyncClient(timeout=httpx.Timeout(40.0, connect=10.0))
    _running = True
    _poll_task = asyncio.create_task(_poll_loop())

async def stop_bot():
    global _running, _client
    _running = False
    if _poll_task:
        _poll_task.cancel()
    if _client:
        await _client.aclose()
        _client = None
