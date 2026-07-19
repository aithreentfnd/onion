LOGO_URL = "https://uploadkon.ir/uploads/7e7c16_26InShot-20260628-102209067.jpg"

LOGIN_HTML = r"""<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>ورود · SpaceZone</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@3.19.0/dist/tabler-icons.min.css">
<style>
*{margin:0;padding:0;box-sizing:border-box}
:root{--bg:#080c1a;--bg-card:rgba(12,20,44,0.65);--accent:#6366F1;--accent2:#818CF8;--accent3:#A5B4FC;--accent-glow:rgba(99,102,241,0.35);--text:#E8F0FE;--text-muted:#94A3B8;--text-dim:#475569;--border:rgba(99,102,241,0.15);--border-glow:rgba(99,102,241,0.30);--shadow:0 20px 60px rgba(0,0,0,0.50);--shadow-inner:inset 0 2px 4px rgba(255,255,255,0.05),inset 0 -2px 4px rgba(0,0,0,0.20);--radius:24px;--radius-sm:14px;--transition:0.35s cubic-bezier(0.4,0,0.2,1);--font:'Vazirmatn',sans-serif}
[data-theme="light"]{--bg:#E8EEF8;--bg-card:rgba(255,255,255,0.55);--accent:#4F46E5;--accent2:#6366F1;--accent3:#818CF8;--accent-glow:rgba(79,70,229,0.20);--text:#0F172A;--text-muted:#334155;--text-dim:#64748B;--border:rgba(79,70,229,0.12);--border-glow:rgba(79,70,229,0.25);--shadow:0 20px 60px rgba(0,0,0,0.08);--shadow-inner:inset 0 2px 4px rgba(255,255,255,0.40),inset 0 -2px 4px rgba(0,0,0,0.04)}
html,body{height:100%;overflow:hidden}
body{font-family:var(--font);background:var(--bg);display:flex;align-items:center;justify-content:center;padding:20px;transition:background var(--transition),color var(--transition)}
.bg-layer{position:fixed;inset:0;z-index:0;background:radial-gradient(ellipse 70% 55% at 50% 0%,rgba(99,102,241,0.12),transparent 72%),radial-gradient(ellipse 50% 40% at 80% 80%,rgba(139,92,246,0.06),transparent 60%),var(--bg);transition:background var(--transition)}
.glow-orb{position:fixed;border-radius:50%;filter:blur(120px);z-index:0;animation:floatGlow 14s ease-in-out infinite alternate;pointer-events:none}
.glow-orb-1{width:450px;height:450px;background:rgba(99,102,241,0.08);top:-150px;right:-100px}
.glow-orb-2{width:350px;height:350px;background:rgba(139,92,246,0.06);bottom:-120px;left:-80px;animation-delay:6s}
@keyframes floatGlow{0%{transform:translateY(0)scale(1);opacity:.6}100%{transform:translateY(-30px)scale(1.08);opacity:1}}
.grid-pattern{position:fixed;inset:0;z-index:0;background-image:linear-gradient(rgba(99,102,241,0.03)1px,transparent 1px),linear-gradient(90deg,rgba(99,102,241,0.03)1px,transparent 1px);background-size:52px 52px;pointer-events:none}
.wrap{position:relative;z-index:10;width:100%;max-width:420px}
.card{background:var(--bg-card);backdrop-filter:blur(24px);-webkit-backdrop-filter:blur(24px);border:1px solid var(--border);border-radius:var(--radius);padding:44px 38px 38px;box-shadow:var(--shadow),var(--shadow-inner);transition:all var(--transition);position:relative;overflow:hidden}
.card::before{content:'';position:absolute;top:-50%;left:-50%;width:200%;height:200%;background:radial-gradient(circle at 30% 20%,rgba(99,102,241,0.03),transparent 60%);pointer-events:none}
.card:hover{background:var(--bg-card-hover,var(--bg-card));border-color:var(--border-glow);box-shadow:var(--shadow),var(--shadow-inner),0 0 60px var(--accent-glow)}
.brand{display:flex;align-items:center;gap:16px;margin-bottom:32px;position:relative;z-index:1}
.brand-img{width:56px;height:56px;border-radius:50%;overflow:hidden;border:2px solid var(--border-glow);box-shadow:0 0 40px var(--accent-glow),0 0 20px var(--accent-glow);flex-shrink:0;transition:box-shadow var(--transition)}
.brand-img img{width:100%;height:100%;object-fit:cover}
.brand-text{flex:1}
.brand-name{font-size:20px;font-weight:800;color:var(--text);letter-spacing:-0.02em;transition:color var(--transition)}
.brand-version{font-size:11px;color:var(--text-dim);font-weight:500;margin-top:2px;transition:color var(--transition)}
h1{font-size:24px;font-weight:700;color:var(--text);margin-bottom:6px;letter-spacing:-0.02em;transition:color var(--transition);position:relative;z-index:1}
.sub{font-size:13px;color:var(--text-muted);margin-bottom:28px;line-height:1.8;transition:color var(--transition);position:relative;z-index:1}
.hint{display:flex;align-items:center;gap:12px;background:rgba(99,102,241,0.06);border:1px solid var(--border);border-radius:var(--radius-sm);padding:12px 18px;margin-bottom:24px;transition:all var(--transition);position:relative;z-index:1}
.hint:hover{background:rgba(99,102,241,0.10);border-color:var(--border-glow)}
.hint-label{font-size:11px;color:var(--text-dim);font-weight:600;flex:1;transition:color var(--transition)}
.hint-val{font-family:ui-monospace,monospace;font-size:14px;font-weight:700;color:var(--accent2);background:rgba(99,102,241,0.10);border:1px solid var(--border-glow);padding:5px 14px;border-radius:10px;cursor:pointer;transition:all var(--transition);letter-spacing:0.08em}
.hint-val:hover{background:rgba(99,102,241,0.20);box-shadow:0 0 30px var(--accent-glow);transform:scale(1.02)}
.field{margin-bottom:22px;position:relative;z-index:1}
.field label{display:block;font-size:10.5px;font-weight:700;color:var(--text-muted);margin-bottom:8px;text-transform:uppercase;letter-spacing:0.08em;transition:color var(--transition)}
.inp-wrap{position:relative}
.inp-wrap input[type=password]{width:100%;padding:15px 52px 15px 20px;border-radius:var(--radius-sm);border:1.5px solid var(--border);background:rgba(0,0,0,0.15);color:var(--text);font-family:var(--font);font-size:15px;outline:none;transition:all var(--transition);box-shadow:var(--shadow-inner)}
[data-theme="light"] .inp-wrap input[type=password]{background:rgba(255,255,255,0.50)}
.inp-wrap input[type=password]:focus{border-color:var(--accent2);background:rgba(0,0,0,0.22);box-shadow:0 0 0 4px var(--accent-glow),var(--shadow-inner)}
.inp-wrap input[type=password]::placeholder{color:var(--text-dim);opacity:.6}
.inp-wrap .ic{position:absolute;left:18px;top:50%;transform:translateY(-50%);color:var(--text-dim);font-size:20px;pointer-events:none;transition:color var(--transition)}
.inp-wrap input:focus+.ic{color:var(--accent2)}
.err{display:none;background:rgba(239,68,68,0.08);border:1px solid rgba(239,68,68,0.20);border-radius:var(--radius-sm);padding:12px 18px;margin-bottom:18px;font-size:12.5px;color:#F87171;align-items:center;gap:10px;transition:all var(--transition);position:relative;z-index:1}
.err.show{display:flex}
.btn-login{width:100%;padding:15px;border-radius:var(--radius-sm);border:none;cursor:pointer;background:linear-gradient(135deg,var(--accent),var(--accent2),var(--accent3));color:#fff;font-family:var(--font);font-size:15px;font-weight:700;display:flex;align-items:center;justify-content:center;gap:10px;box-shadow:0 8px 32px var(--accent-glow),var(--shadow-inner);transition:all var(--transition);position:relative;overflow:hidden;z-index:1}
.btn-login::before{content:'';position:absolute;inset:0;background:linear-gradient(135deg,rgba(255,255,255,0.12),transparent);opacity:0;transition:opacity var(--transition)}
.btn-login:hover::before{opacity:1}
.btn-login:hover{transform:translateY(-3px);box-shadow:0 12px 44px var(--accent-glow),var(--shadow-inner)}
.btn-login:active{transform:translateY(0)scale(0.97)}
.btn-login:disabled{opacity:.5;cursor:not-allowed;transform:none}
.footer{margin-top:26px;padding-top:22px;border-top:1px solid var(--border);display:flex;align-items:center;justify-content:center;gap:12px;font-size:11px;color:var(--text-dim);transition:border var(--transition),color var(--transition);position:relative;z-index:1}
@keyframes spin{to{transform:rotate(360deg)}}
@keyframes fadeSlide{from{opacity:0;transform:translateY(16px)scale(0.96)}to{opacity:1;transform:translateY(0)scale(1)}}
.card{animation:fadeSlide .6s ease}
@media(max-width:480px){.card{padding:30px 22px 26px}.brand-img{width:48px;height:48px}.brand-name{font-size:17px}h1{font-size:20px}.btn-login{padding:13px;font-size:14px}}
</style>
</head>
<body>
<div class="bg-layer"></div>
<div class="glow-orb glow-orb-1"></div>
<div class="glow-orb glow-orb-2"></div>
<div class="grid-pattern"></div>
<div class="wrap">
<div class="card">
<div class="brand">
<div class="brand-img"><img src="https://uploadkon.ir/uploads/7e7c16_26InShot-20260628-102209067.jpg" alt="SpaceZone"></div>
<div class="brand-text"><div class="brand-name">SpaceZone</div><div class="brand-version">v10.3</div></div>
</div>
<h1>ورود به پنل</h1>
<p class="sub">رمز عبور را برای دسترسی به داشبورد وارد کنید</p>
<div class="err" id="err"><i class="ti ti-alert-circle"></i><span id="err-text"></span></div>
<div class="hint"><span class="hint-label">رمز پیش‌فرض</span><span class="hint-val" onclick="document.getElementById('pw').value='SpaceZone2025';document.getElementById('pw').focus()">SpaceZone2025</span></div>
<form id="form">
<div class="field">
<label>رمز عبور</label>
<div class="inp-wrap">
<input type="password" id="pw" placeholder="رمز عبور را وارد کنید" autofocus required>
<i class="ti ti-lock ic"></i>
</div>
</div>
<button class="btn-login" type="submit" id="btn"><i class="ti ti-login-2"></i> ورود به داشبورد</button>
</form>
<div class="footer">SpaceZone v10.3</div>
</div>
</div>
<script>
document.getElementById('form').addEventListener('submit',async e=>{
e.preventDefault();
const btn=document.getElementById('btn');
const err=document.getElementById('err');
const et=document.getElementById('err-text');
err.classList.remove('show');
btn.disabled=true;
btn.innerHTML='<i class="ti ti-loader-2" style="animation:spin 1s linear infinite"></i> در حال ورود...';
try{
const r=await fetch('/api/login',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({password:document.getElementById('pw').value})});
if(!r.ok){const d=await r.json().catch(()=>({}));throw new Error(d.detail||'خطا');}
location.href='/dashboard';
}catch(e){
et.textContent=e.message;
err.classList.add('show');
btn.disabled=false;
btn.innerHTML='<i class="ti ti-login-2"></i> ورود به داشبورد';
}
});
</script>
</body></html>"""


DASHBOARD_HTML = r"""<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>SpaceZone v10.3</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@3.19.0/dist/tabler-icons.min.css">
<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.umd.js"></script>
<style>
*{margin:0;padding:0;box-sizing:border-box}
:root{--bg:#080c1a;--bg2:#0c1430;--bg3:#101a3a;--bg-card:rgba(12,20,44,0.60);--bg-card-hover:rgba(12,20,44,0.80);--border:rgba(99,102,241,0.12);--border-hover:rgba(99,102,241,0.28);--accent:#6366F1;--accent2:#818CF8;--accent3:#A5B4FC;--accent-d:rgba(99,102,241,0.10);--accent-glow:rgba(99,102,241,0.25);--green:#10B981;--green-bg:rgba(16,185,129,0.08);--green-t:#34D399;--red:#EF4444;--red-bg:rgba(239,68,68,0.08);--red-t:#F87171;--amber:#F59E0B;--amber-bg:rgba(245,158,11,0.08);--amber-t:#FCD34D;--purple:#8B5CF6;--purple-bg:rgba(139,92,246,0.08);--t1:#E8F0FE;--t2:#94A3B8;--t3:#475569;--shadow:0 12px 48px rgba(0,0,0,0.40);--shadow-hover:0 20px 60px rgba(0,0,0,0.50);--shadow-inner:inset 0 2px 4px rgba(255,255,255,0.04),inset 0 -2px 4px rgba(0,0,0,0.20);--radius:20px;--radius-sm:12px;--transition:0.32s cubic-bezier(0.4,0,0.2,1);--font:'Vazirmatn',sans-serif;--sidebar-w:260px}
[data-theme="light"]{--bg:#E8EEF8;--bg2:#DCE4F2;--bg3:#CED8EC;--bg-card:rgba(255,255,255,0.55);--bg-card-hover:rgba(255,255,255,0.75);--border:rgba(79,70,229,0.10);--border-hover:rgba(79,70,229,0.22);--accent:#4F46E5;--accent2:#6366F1;--accent3:#818CF8;--accent-d:rgba(79,70,229,0.06);--accent-glow:rgba(79,70,229,0.15);--green:#059669;--green-bg:rgba(5,150,105,0.06);--green-t:#065F46;--red:#DC2626;--red-bg:rgba(220,38,38,0.06);--red-t:#991B1B;--amber:#D97706;--amber-bg:rgba(217,119,6,0.06);--amber-t:#92400E;--purple:#7C3AED;--purple-bg:rgba(124,58,237,0.06);--t1:#0F172A;--t2:#334155;--t3:#64748B;--shadow:0 12px 40px rgba(0,0,0,0.06);--shadow-hover:0 20px 52px rgba(0,0,0,0.10);--shadow-inner:inset 0 2px 4px rgba(255,255,255,0.40),inset 0 -2px 4px rgba(0,0,0,0.04)}
html,body{height:100%}
body{font-family:var(--font);background:var(--bg);color:var(--t1);min-height:100vh;display:flex;font-size:14px;transition:background var(--transition),color var(--transition)}
::-webkit-scrollbar{width:5px;height:5px}
::-webkit-scrollbar-track{background:var(--bg)}
::-webkit-scrollbar-thumb{background:var(--bg3);border-radius:4px}
::-webkit-scrollbar-thumb:hover{background:var(--accent2)}
.sidebar{width:var(--sidebar-w);min-height:100vh;background:var(--bg-card);backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px);border-left:1px solid var(--border);display:flex;flex-direction:column;flex-shrink:0;position:fixed;right:0;top:0;bottom:0;z-index:200;transition:transform var(--transition),background var(--transition),border var(--transition);box-shadow:var(--shadow)}
[data-theme="light"] .sidebar{box-shadow:var(--shadow)}
.logo{display:flex;align-items:center;gap:14px;padding:24px 20px 18px;border-bottom:1px solid var(--border);transition:border var(--transition)}
.logo-img{width:42px;height:42px;border-radius:50%;overflow:hidden;border:2px solid var(--border-hover);box-shadow:0 0 30px var(--accent-glow);flex-shrink:0}
.logo-img img{width:100%;height:100%;object-fit:cover}
.logo-name{font-size:14px;font-weight:800;color:var(--t1);letter-spacing:-0.01em}
.logo-version{font-size:9.5px;color:var(--t3);margin-top:1px;font-weight:500}
.sb-close{display:none;position:absolute;left:14px;top:18px;background:var(--accent-d);border:1px solid var(--border);color:var(--t2);width:34px;height:34px;border-radius:var(--radius-sm);font-size:18px;align-items:center;justify-content:center;cursor:pointer;transition:all var(--transition)}
.sb-close:hover{background:var(--red-bg);color:var(--red-t);border-color:rgba(239,68,68,0.25)}
.nav-wrap{flex:1;overflow-y:auto;padding:12px 0 8px}
.nav-section{padding:18px 18px 6px;font-size:9px;letter-spacing:0.14em;text-transform:uppercase;color:var(--t3);font-weight:700}
.nav-item{display:flex;align-items:center;gap:12px;padding:10px 18px;color:var(--t3);font-size:12.5px;cursor:pointer;border-right:3px solid transparent;transition:all var(--transition);margin:2px 10px;border-radius:var(--radius-sm)}
.nav-item i{font-size:18px;width:22px;text-align:center;flex-shrink:0}
.nav-item:hover{background:var(--accent-d);color:var(--t2)}
.nav-item.active{background:var(--accent-d);color:var(--t1);border-right-color:var(--accent);font-weight:600}
.nav-badge{margin-right:auto;background:var(--accent-d);color:var(--accent2);font-size:9px;padding:2px 10px;border-radius:20px;font-weight:700}
.sb-footer{padding:14px 18px;border-top:1px solid var(--border);transition:border var(--transition)}
.theme-btn{display:flex;align-items:center;justify-content:center;gap:8px;background:var(--accent-d);color:var(--t2);border-radius:var(--radius-sm);padding:10px;font-size:12px;font-weight:600;font-family:var(--font);border:1px solid var(--border);cursor:pointer;width:100%;transition:all var(--transition);margin-bottom:8px;backdrop-filter:blur(8px)}
.theme-btn:hover{background:var(--border);color:var(--t1)}
.logout-btn{display:flex;align-items:center;justify-content:center;gap:8px;background:var(--red-bg);color:var(--red-t);border-radius:var(--radius-sm);padding:10px;font-size:12px;font-weight:600;font-family:var(--font);border:1px solid rgba(239,68,68,0.15);cursor:pointer;width:100%;transition:all var(--transition);margin-top:6px}
.logout-btn:hover{background:rgba(239,68,68,0.18)}
.mob-top{display:none;position:fixed;top:0;right:0;left:0;height:58px;background:var(--bg-card);backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px);border-bottom:1px solid var(--border);z-index:150;align-items:center;justify-content:space-between;padding:0 18px;transition:background var(--transition),border var(--transition)}
.mob-top .ml{display:flex;align-items:center;gap:12px}
.mob-logo{width:32px;height:32px;border-radius:50%;overflow:hidden;box-shadow:0 0 16px var(--accent-glow)}
.mob-logo img{width:100%;height:100%;object-fit:cover}
.mob-title{color:var(--t1);font-size:13px;font-weight:700}
.mob-right{display:flex;gap:6px}
.menu-btn,.theme-mob{background:var(--accent-d);border:1px solid var(--border);color:var(--t2);width:38px;height:38px;border-radius:var(--radius-sm);font-size:18px;display:flex;align-items:center;justify-content:center;cursor:pointer;transition:all var(--transition)}
.menu-btn:hover,.theme-mob:hover{background:var(--border);color:var(--t1)}
.overlay{display:none;position:fixed;inset:0;background:rgba(0,0,0,0.50);z-index:190;backdrop-filter:blur(4px)}
.overlay.show{display:block}
.main{margin-right:var(--sidebar-w);flex:1;padding:32px 34px 60px;min-width:0;transition:margin var(--transition)}
.page{display:none}
.page.active{display:block;animation:fadeSlide .4s ease}
@keyframes fadeSlide{from{opacity:0;transform:translateY(12px)}to{opacity:1;transform:translateY(0)}}
.topbar{display:flex;align-items:flex-start;justify-content:space-between;margin-bottom:26px;flex-wrap:wrap;gap:12px}
.tb-title{font-size:20px;font-weight:800;color:var(--t1);display:flex;align-items:center;gap:12px;letter-spacing:-0.02em}
.tb-title i{color:var(--accent);font-size:22px}
.tb-sub{font-size:11.5px;color:var(--t3);margin-top:4px}
.tb-right{display:flex;align-items:center;gap:10px;flex-wrap:wrap}
.badge{font-size:10px;padding:4px 14px;border-radius:20px;font-weight:700;display:inline-flex;align-items:center;gap:6px;white-space:nowrap;backdrop-filter:blur(8px)}
.badge-green{background:var(--green-bg);color:var(--green-t);border:1px solid rgba(16,185,129,0.12)}
.badge-blue{background:var(--accent-d);color:var(--accent2);border:1px solid var(--border)}
.badge-amber{background:var(--amber-bg);color:var(--amber-t);border:1px solid rgba(245,158,11,0.12)}
.badge-red{background:var(--red-bg);color:var(--red-t);border:1px solid rgba(239,68,68,0.12)}
.badge-purple{background:var(--purple-bg);color:#A78BFA;border:1px solid rgba(139,92,246,0.12)}
.dot{width:7px;height:7px;border-radius:50%;flex-shrink:0;display:inline-block}
.dot-green{background:var(--green)}
.dot-red{background:var(--red)}
.dot-amber{background:var(--amber)}
.dot-blue{background:var(--accent)}
.pulse{animation:pulse 2s infinite}
@keyframes pulse{0%,100%{opacity:1}50%{opacity:.25}}
.metrics{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;margin-bottom:22px}
.metric{background:var(--bg-card);backdrop-filter:blur(16px);-webkit-backdrop-filter:blur(16px);border:1px solid var(--border);border-radius:var(--radius);padding:20px 20px 16px;transition:all var(--transition);position:relative;overflow:hidden;cursor:default;box-shadow:var(--shadow-inner)}
.metric::after{content:'';position:absolute;top:0;right:0;width:4px;height:100%;background:linear-gradient(180deg,var(--accent),var(--accent2));opacity:0;transition:opacity var(--transition)}
.metric:hover{background:var(--bg-card-hover);border-color:var(--border-hover);transform:translateY(-4px);box-shadow:var(--shadow-hover),var(--shadow-inner)}
.metric:hover::after{opacity:1}
.metric-success::after{background:linear-gradient(180deg,var(--green),#059669)}
.metric-danger::after{background:linear-gradient(180deg,var(--red),#DC2626)}
.metric-purple::after{background:linear-gradient(180deg,var(--purple),#7C3AED)}
.m-icon{width:38px;height:38px;border-radius:var(--radius-sm);background:var(--accent-d);display:flex;align-items:center;justify-content:center;margin-bottom:12px;color:var(--accent);font-size:19px;backdrop-filter:blur(8px)}
.m-icon-success{background:var(--green-bg);color:var(--green)}
.m-icon-danger{background:var(--red-bg);color:var(--red)}
.m-icon-purple{background:var(--purple-bg);color:var(--purple)}
.m-label{font-size:10px;color:var(--t3);margin-bottom:5px;font-weight:700;text-transform:uppercase;letter-spacing:0.06em}
.m-value{font-size:27px;font-weight:800;color:var(--t1);line-height:1;letter-spacing:-0.02em}
.m-unit{font-size:12px;font-weight:400;color:var(--t3)}
.m-sub{font-size:10px;color:var(--t3);margin-top:6px;display:flex;align-items:center;gap:4px}
.vless-box{background:var(--bg-card);backdrop-filter:blur(16px);-webkit-backdrop-filter:blur(16px);border:1px solid var(--border);border-radius:var(--radius);padding:24px 26px;margin-bottom:22px;box-shadow:var(--shadow),var(--shadow-inner);position:relative;overflow:hidden;transition:all var(--transition)}
.vless-box:hover{background:var(--bg-card-hover);border-color:var(--border-hover);box-shadow:var(--shadow-hover),var(--shadow-inner)}
.vless-box::before{content:'';position:absolute;top:-80px;left:-80px;width:240px;height:240px;background:radial-gradient(circle,var(--accent-d),transparent 72%);pointer-events:none}
.vl-header{display:flex;align-items:center;justify-content:space-between;margin-bottom:14px;flex-wrap:wrap;gap:8px;position:relative;z-index:1}
.vl-title{color:var(--t2);font-size:11px;display:flex;align-items:center;gap:8px;font-weight:700;text-transform:uppercase;letter-spacing:0.08em}
.vl-title i{color:var(--accent);font-size:16px}
.vl-code{background:rgba(0,0,0,0.18);border:1px solid var(--border);border-radius:var(--radius-sm);padding:14px 18px;font-size:11px;font-family:ui-monospace,monospace;color:var(--accent2);word-break:break-all;line-height:2;letter-spacing:0.01em;position:relative;z-index:1;backdrop-filter:blur(8px)}
[data-theme="light"] .vl-code{background:rgba(0,0,0,0.04)}
.vl-actions{display:flex;gap:10px;margin-top:14px;flex-wrap:wrap;position:relative;z-index:1}
.btn{font-family:var(--font);font-size:12px;font-weight:600;border-radius:var(--radius-sm);padding:10px 18px;cursor:pointer;display:inline-flex;align-items:center;gap:7px;border:none;transition:all var(--transition);white-space:nowrap;backdrop-filter:blur(8px)}
.btn i{font-size:14px}
.btn:disabled{opacity:.4;cursor:not-allowed}
.btn-primary{background:linear-gradient(135deg,var(--accent),var(--accent2));color:#fff;box-shadow:0 4px 24px var(--accent-glow),var(--shadow-inner)}
.btn-primary:hover{transform:translateY(-2px);box-shadow:0 8px 36px var(--accent-glow),var(--shadow-inner)}
.btn-primary:active{transform:translateY(0)scale(0.97)}
.btn-outline{background:transparent;border:1.5px solid var(--border);color:var(--t2)}
.btn-outline:hover{background:var(--accent-d);border-color:var(--border-hover)}
.btn-ghost{background:var(--accent-d);color:var(--accent2);border:1px solid var(--border)}
.btn-ghost:hover{background:rgba(99,102,241,0.18)}
.btn-danger{background:var(--red-bg);color:var(--red-t);border:1px solid rgba(239,68,68,0.15)}
.btn-danger:hover{background:rgba(239,68,68,0.18)}
.btn-purple{background:var(--purple-bg);color:#A78BFA;border:1px solid rgba(139,92,246,0.15)}
.btn-purple:hover{background:rgba(139,92,246,0.18)}
.btn-amber{background:var(--amber-bg);color:var(--amber-t);border:1px solid rgba(245,158,11,0.15)}
.btn-amber:hover{background:rgba(245,158,11,0.18)}
.btn-sm{padding:5px 12px;font-size:10.5px;border-radius:8px}
.btn-icon{width:34px;height:34px;padding:0;justify-content:center;border-radius:8px}
.card{background:var(--bg-card);backdrop-filter:blur(16px);-webkit-backdrop-filter:blur(16px);border:1px solid var(--border);border-radius:var(--radius);padding:22px 24px;transition:all var(--transition);box-shadow:var(--shadow-inner)}
.card:hover{background:var(--bg-card-hover);border-color:var(--border-hover);box-shadow:var(--shadow-hover),var(--shadow-inner)}
.card-title{font-size:13px;font-weight:700;color:var(--t1);margin-bottom:16px;display:flex;align-items:center;gap:8px}
.card-title i{font-size:17px;color:var(--accent)}
.card-title .badge{margin-right:auto}
.grid-2{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-bottom:18px}
.grid-3{display:grid;grid-template-columns:2fr 1fr;gap:16px;margin-bottom:18px}
.mb-16{margin-bottom:16px}
.stat-row{display:flex;align-items:center;justify-content:space-between;padding:10px 0;border-bottom:1px solid rgba(99,102,241,0.04);font-size:12px}
.stat-row:last-child{border-bottom:none}
.stat-key{color:var(--t2);display:flex;align-items:center;gap:8px}
.stat-key i{font-size:13px;color:var(--t3)}
.stat-value{color:var(--t1);font-weight:600;font-size:11.5px}
.chart-wrap{position:relative;height:230px}
.chart-wrap-lg{position:relative;height:330px}
.chart-wrap-sm{position:relative;height:185px}
.progress-bar{height:5px;border-radius:4px;background:var(--accent-d);margin-top:6px;overflow:hidden}
.progress-fill{height:100%;border-radius:4px;background:linear-gradient(90deg,var(--accent),var(--accent2));transition:width .8s ease}
.exp-chip{font-size:9px;padding:3px 10px;border-radius:6px;font-weight:700;display:inline-flex;align-items:center;gap:4px}
.exp-ok{background:var(--green-bg);color:var(--green-t)}
.exp-warn{background:var(--amber-bg);color:var(--amber-t)}
.exp-exp{background:var(--red-bg);color:var(--red-t)}
.exp-inf{background:var(--accent-d);color:var(--accent2)}
.toggle{width:22px;height:36px;border-radius:20px;background:rgba(100,116,139,0.20);position:relative;cursor:pointer;transition:background var(--transition);flex-shrink:0;border:none}
.toggle::after{content:'';position:absolute;width:15px;height:15px;border-radius:50%;background:#fff;left:3.5px;bottom:3.5px;transition:all var(--transition);box-shadow:0 1px 6px rgba(0,0,0,0.25)}
.toggle.on{background:var(--green)}
.toggle.on::after{bottom:17.5px}
.form-row{display:flex;gap:10px;flex-wrap:wrap;align-items:flex-end}
.form-group{display:flex;flex-direction:column;gap:5px}
.form-group label{font-size:10px;color:var(--t3);font-weight:700;text-transform:uppercase;letter-spacing:0.08em}
.form-input,.form-select{padding:10px 16px;border-radius:var(--radius-sm);border:1px solid var(--border);background:rgba(0,0,0,0.10);color:var(--t1);font-family:var(--font);font-size:12px;outline:none;transition:all var(--transition);min-width:100px;backdrop-filter:blur(8px)}
[data-theme="light"] .form-input,[data-theme="light"] .form-select{background:rgba(255,255,255,0.40)}
.form-input::placeholder{color:var(--t3)}
.form-input:focus,.form-select:focus{border-color:var(--accent2);background:rgba(0,0,0,0.16);box-shadow:0 0 0 4px var(--accent-d)}
.form-select option{background:var(--bg2)}
[data-theme="light"] .form-select option{background:#fff}
.info-box{background:var(--accent-d);border:1px solid var(--border);border-radius:var(--radius-sm);padding:12px 16px;font-size:11px;color:var(--t2);display:flex;gap:10px;align-items:flex-start;line-height:1.8;margin-top:12px;backdrop-filter:blur(8px)}
.info-box i{font-size:15px;color:var(--accent);margin-top:1px;flex-shrink:0}
.info-box-amber{background:var(--amber-bg);border-color:rgba(245,158,11,0.15);color:var(--amber-t)}
.info-box-amber i{color:var(--amber)}
.empty-state{text-align:center;padding:50px 20px;color:var(--t3)}
.empty-state i{font-size:40px;opacity:.3;margin-bottom:12px;display:block}
.empty-state p{font-size:12.5px;margin-top:4px}
.cfg-grid{display:flex;flex-direction:column;gap:10px}
.cfg-card{background:var(--bg-card);backdrop-filter:blur(16px);-webkit-backdrop-filter:blur(16px);border:1px solid var(--border);border-radius:var(--radius);padding:0;transition:all var(--transition);position:relative;overflow:hidden;box-shadow:var(--shadow-inner)}
.cfg-card:hover{background:var(--bg-card-hover);border-color:var(--border-hover);box-shadow:var(--shadow-hover),var(--shadow-inner)}
.cfg-card-inactive{opacity:.6}
.cfg-card-expired{opacity:.78}
.cfg-row{display:flex;align-items:center;gap:18px;padding:14px 20px}
.cfg-status-dot{width:10px;height:10px;border-radius:50%;background:var(--green);flex-shrink:0;box-shadow:0 0 0 3px var(--green-bg)}
.cfg-card-inactive .cfg-status-dot{background:var(--red);box-shadow:0 0 0 3px var(--red-bg)}
.cfg-card-expired .cfg-status-dot{background:var(--amber);box-shadow:0 0 0 3px var(--amber-bg)}
.cfg-identity{display:flex;flex-direction:column;gap:3px;min-width:150px;flex-shrink:0}
.cfg-label{font-size:13.5px;font-weight:700;color:var(--t1);display:flex;align-items:center;gap:8px}
.cfg-meta{display:flex;align-items:center;gap:8px;font-size:10px;color:var(--t3)}
.cfg-uuid-mini{font-family:ui-monospace,monospace;font-size:9.5px;color:var(--accent2);background:var(--accent-d);padding:2px 10px;border-radius:6px;cursor:pointer;transition:all var(--transition)}
.cfg-uuid-mini:hover{background:rgba(99,102,241,0.18)}
.cfg-divider{width:1px;align-self:stretch;background:var(--border);flex-shrink:0}
.cfg-usage{flex:1;min-width:160px;display:flex;flex-direction:column;gap:5px}
.usage-bar{height:5px;border-radius:4px;background:rgba(99,102,241,0.06);overflow:hidden}
.usage-fill{height:100%;border-radius:4px;transition:width .5s ease}
.usage-text{font-size:10px;color:var(--t3);display:flex;justify-content:space-between}
.cfg-expiry{flex-shrink:0;min-width:110px}
.cfg-badges{display:flex;flex-direction:column;gap:5px;flex-shrink:0;align-items:flex-end}
.cfg-actions{display:flex;gap:5px;flex-shrink:0}
.proto-chip{font-size:9px;padding:3px 10px;border-radius:6px;font-weight:700;white-space:nowrap}
.proto-ws{background:var(--accent-d);color:var(--accent2)}
.proto-xhttp{background:var(--purple-bg);color:#A78BFA}
.proto-ultra{background:var(--green-bg);color:var(--green-t)}
.cfg-tag{font-size:9.5px;color:var(--t3);display:flex;align-items:center;gap:4px;white-space:nowrap}
.cfg-tag i{color:var(--purple);font-size:11px}
@media(max-width:880px){.cfg-row{flex-wrap:wrap}.cfg-divider{display:none}.cfg-usage{min-width:100%;order:5}}
@media(max-width:768px){.cfg-grid{display:grid;grid-template-columns:1fr;gap:13px}.cfg-card{border-radius:var(--radius)}.cfg-row{flex-direction:column;align-items:stretch;gap:12px;padding:16px}.cfg-identity{min-width:0;flex:1}.cfg-usage{min-width:0}.cfg-expiry{min-width:0}.cfg-badges{flex-direction:row;align-items:center;flex-wrap:wrap}.cfg-actions{flex-wrap:wrap;border-top:1px solid var(--border);padding-top:10px;margin-top:2px;width:100%}}
.create-panel{background:var(--bg-card);backdrop-filter:blur(16px);-webkit-backdrop-filter:blur(16px);border:1px solid var(--border);border-radius:var(--radius);padding:0;overflow:hidden;box-shadow:var(--shadow),var(--shadow-inner);margin-bottom:18px;position:relative}
.create-panel::before{content:'';position:absolute;top:-80px;left:-80px;width:260px;height:260px;background:radial-gradient(circle,var(--accent-d),transparent 72%);pointer-events:none}
.cp-head{display:flex;align-items:center;gap:16px;padding:24px 28px 18px;position:relative;z-index:1}
.cp-icon{width:48px;height:48px;border-radius:var(--radius-sm);background:linear-gradient(135deg,var(--accent),var(--accent2));display:flex;align-items:center;justify-content:center;color:#fff;font-size:22px;flex-shrink:0;box-shadow:0 6px 24px var(--accent-glow)}
.cp-text{flex:1;min-width:0}
.cp-title{font-size:15px;font-weight:800;color:var(--t1);letter-spacing:-0.01em}
.cp-sub{font-size:11px;color:var(--t3);margin-top:2px}
.cp-body{padding:2px 28px 26px;position:relative;z-index:1}
.cp-row{display:grid;grid-template-columns:1.3fr 1fr;gap:16px;margin-bottom:16px}
.cp-block{background:rgba(0,0,0,0.06);border:1px solid var(--border);border-radius:var(--radius-sm);padding:14px 18px;backdrop-filter:blur(8px)}
[data-theme="light"] .cp-block{background:rgba(255,255,255,0.20)}
.cp-block-label{font-size:10px;font-weight:800;color:var(--t2);text-transform:uppercase;letter-spacing:0.08em;display:flex;align-items:center;gap:8px;margin-bottom:12px}
.cp-block-label i{color:var(--accent);font-size:14px}
.cp-input{width:100%;padding:10px 16px;border-radius:var(--radius-sm);border:1px solid var(--border);background:rgba(0,0,0,0.10);color:var(--t1);font-family:var(--font);font-size:12.5px;outline:none;transition:all var(--transition)}
[data-theme="light"] .cp-input{background:rgba(255,255,255,0.30)}
.cp-input:focus{border-color:var(--accent2);box-shadow:0 0 0 4px var(--accent-d)}
.cp-input::placeholder{color:var(--t3)}
.cp-mini-row{display:flex;gap:8px;margin-top:10px}
.cp-quota-inputs{display:flex;gap:8px}
.cp-quota-inputs .cp-input{flex:1}
.cp-quota-inputs select.cp-input{flex:0 0 76px}
.chip-row{display:flex;gap:6px;flex-wrap:wrap;margin-top:10px}
.chip{font-size:10.5px;font-weight:700;padding:5px 14px;border-radius:8px;background:var(--accent-d);color:var(--t2);border:1px solid var(--border);cursor:pointer;transition:all var(--transition);white-space:nowrap}
.chip:hover{background:rgba(99,102,241,0.16);color:var(--accent2)}
.chip-active{background:linear-gradient(135deg,var(--accent),var(--accent2));color:#fff;border-color:var(--accent);box-shadow:0 4px 16px var(--accent-glow)}
.proto-cards{display:grid;grid-template-columns:repeat(3,1fr);gap:10px}
.proto-card{border:1.5px solid var(--border);border-radius:var(--radius-sm);padding:14px 12px;cursor:pointer;transition:all var(--transition);text-align:center;position:relative;background:rgba(0,0,0,0.04)}
[data-theme="light"] .proto-card{background:rgba(255,255,255,0.20)}
.proto-card:hover{border-color:var(--border-hover);transform:translateY(-2px)}
.proto-card-active{border-color:var(--accent);background:var(--accent-d);box-shadow:0 0 0 4px var(--accent-d)}
.proto-card-check{position:absolute;top:7px;left:7px;width:18px;height:18px;border-radius:50%;background:var(--accent);color:#fff;font-size:10px;display:flex;align-items:center;justify-content:center;opacity:0;transform:scale(.5);transition:all var(--transition)}
.proto-card-active .proto-card-check{opacity:1;transform:scale(1)}
.proto-icon{width:34px;height:34px;border-radius:var(--radius-sm);background:var(--accent-d);color:var(--accent);display:flex;align-items:center;justify-content:center;font-size:17px;margin:0 auto 8px}
.proto-card-active .proto-icon{background:var(--accent);color:#fff}
.proto-name{font-size:11px;font-weight:800;color:var(--t1)}
.proto-desc{font-size:9px;color:var(--t3);margin-top:3px;line-height:1.5}
.cp-footer{display:flex;align-items:center;justify-content:space-between;gap:12px;padding-top:16px;border-top:1px solid var(--border);flex-wrap:wrap}
.cp-note{display:flex;align-items:center;gap:8px;font-size:10.5px;color:var(--t3);line-height:1.7;flex:1;min-width:220px}
.cp-note i{color:var(--accent);font-size:15px;flex-shrink:0}
.cp-submit{background:linear-gradient(135deg,var(--accent),var(--accent2));color:#fff;border:none;border-radius:var(--radius-sm);padding:13px 30px;font-family:var(--font);font-size:13px;font-weight:800;cursor:pointer;display:flex;align-items:center;gap:8px;box-shadow:0 6px 24px var(--accent-glow);transition:all var(--transition);white-space:nowrap}
.cp-submit:hover{transform:translateY(-3px);box-shadow:0 10px 36px var(--accent-glow)}
.cp-submit:active{transform:translateY(0)scale(.97)}
@media(max-width:760px){.cp-row{grid-template-columns:1fr}.proto-cards{grid-template-columns:1fr}.cp-footer{flex-direction:column;align-items:stretch}.cp-submit{justify-content:center}}
.conn-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:16px}
.conn-card{background:var(--bg-card);backdrop-filter:blur(16px);-webkit-backdrop-filter:blur(16px);border:1px solid var(--border);border-radius:var(--radius);padding:0;overflow:hidden;transition:all var(--transition);position:relative;box-shadow:var(--shadow-inner)}
.conn-card:hover{background:var(--bg-card-hover);border-color:var(--border-hover);transform:translateY(-4px);box-shadow:var(--shadow-hover),var(--shadow-inner)}
.conn-card-glow{position:absolute;top:-40px;left:-40px;width:140px;height:140px;background:radial-gradient(circle,rgba(16,185,129,0.06),transparent 72%);pointer-events:none}
.conn-top{display:flex;align-items:center;gap:14px;padding:16px 18px 13px;position:relative;z-index:1}
.conn-avatar{width:44px;height:44px;border-radius:var(--radius-sm);background:linear-gradient(135deg,var(--green),#0D9668);display:flex;align-items:center;justify-content:center;color:#fff;font-size:19px;flex-shrink:0;position:relative;box-shadow:0 4px 20px rgba(16,185,129,0.25)}
.conn-avatar::after{content:'';position:absolute;inset:-4px;border-radius:var(--radius-sm);border:1.5px solid var(--green);opacity:.4;animation:breathe 2.4s ease-in-out infinite}
@keyframes breathe{0%,100%{transform:scale(1);opacity:.4}50%{transform:scale(1.12);opacity:0}}
.conn-id{flex:1;min-width:0}
.conn-ip{font-family:ui-monospace,monospace;font-size:14px;font-weight:800;color:var(--t1);display:flex;align-items:center;gap:7px}
.conn-ip-copy{background:none;border:none;color:var(--t3);cursor:pointer;font-size:12px;padding:2px;display:flex;transition:color var(--transition)}
.conn-ip-copy:hover{color:var(--accent)}
.conn-label{font-size:10.5px;color:var(--t3);margin-top:2px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.conn-pill{font-size:9px;font-weight:800;padding:4px 12px;border-radius:20px;background:var(--green-bg);color:var(--green-t);display:flex;align-items:center;gap:4px;white-space:nowrap;flex-shrink:0}
.conn-divider{height:1px;background:linear-gradient(90deg,transparent,var(--border)15%,var(--border)85%,transparent);margin:0 18px}
.conn-body{padding:14px 18px 16px}
.conn-proto-row{margin-bottom:12px}
.conn-stat-row{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-bottom:12px}
.conn-stat{display:flex;align-items:center;gap:9px}
.conn-stat-icon{width:28px;height:28px;border-radius:8px;background:var(--accent-d);color:var(--accent);display:flex;align-items:center;justify-content:center;font-size:13px;flex-shrink:0}
.conn-stat-icon-time{background:var(--purple-bg);color:var(--purple)}
.conn-stat-label{font-size:8.5px;color:var(--t3);font-weight:700;text-transform:uppercase;letter-spacing:.04em}
.conn-stat-value{font-size:11.5px;font-weight:700;color:var(--t1);margin-top:1px}
.conn-duration-track{height:5px;border-radius:4px;background:var(--accent-d);overflow:hidden;position:relative}
.conn-duration-fill{height:100%;border-radius:4px;background:linear-gradient(90deg,var(--green),#3FD79C);position:relative;overflow:hidden}
.conn-duration-fill::after{content:'';position:absolute;inset:0;background:linear-gradient(90deg,transparent,rgba(255,255,255,0.25),transparent);width:40%;animation:shimmer 1.8s linear infinite}
@keyframes shimmer{0%{transform:translateX(-120%)}100%{transform:translateX(280%)}}
.conn-empty{text-align:center;padding:70px 20px;background:var(--bg-card);backdrop-filter:blur(16px);border:1px dashed var(--border);border-radius:var(--radius)}
.conn-empty-icon{width:64px;height:64px;border-radius:var(--radius);background:var(--accent-d);display:flex;align-items:center;justify-content:center;font-size:28px;color:var(--t3);margin:0 auto 16px}
.conn-empty-title{font-size:13.5px;font-weight:700;color:var(--t2);margin-bottom:5px}
.conn-empty-sub{font-size:11px;color:var(--t3)}
.sub-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(340px,1fr));gap:16px;margin-bottom:18px}
.sub-card{background:var(--bg-card);backdrop-filter:blur(16px);-webkit-backdrop-filter:blur(16px);border:1px solid var(--border);border-radius:var(--radius);padding:0;overflow:hidden;transition:all var(--transition);position:relative;box-shadow:var(--shadow-inner)}
.sub-card:hover{background:var(--bg-card-hover);border-color:var(--border-hover);transform:translateY(-4px);box-shadow:var(--shadow-hover),var(--shadow-inner)}
.sub-top{background:linear-gradient(155deg,var(--purple-bg),transparent 65%);padding:20px 20px 16px;position:relative}
.sub-top::before{content:'';position:absolute;top:-30px;left:-30px;width:130px;height:130px;background:radial-gradient(circle,rgba(139,92,246,0.10),transparent 72%);pointer-events:none}
.sub-head{display:flex;align-items:flex-start;gap:14px;position:relative;z-index:1}
.sub-icon{width:48px;height:48px;border-radius:var(--radius-sm);background:linear-gradient(135deg,var(--purple),#6D48D6);display:flex;align-items:center;justify-content:center;color:#fff;font-size:21px;flex-shrink:0;box-shadow:0 6px 24px rgba(139,92,246,0.30)}
.sub-titles{flex:1;min-width:0}
.sub-name{font-size:15.5px;font-weight:800;color:var(--t1);letter-spacing:-0.01em;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.sub-desc{font-size:11px;color:var(--t3);margin-top:3px;line-height:1.6;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden}
.sub-lock{flex-shrink:0;width:28px;height:28px;border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:13px}
.sub-lock-locked{background:var(--amber-bg);color:var(--amber-t)}
.sub-lock-open{background:var(--green-bg);color:var(--green-t)}
.sub-stats{display:grid;grid-template-columns:repeat(3,1fr);gap:0;position:relative;z-index:1;margin-top:16px;background:rgba(0,0,0,0.04);border:1px solid var(--border);border-radius:var(--radius-sm);overflow:hidden}
[data-theme="light"] .sub-stats{background:rgba(124,58,237,0.02)}
.sub-stat{padding:11px 8px;text-align:center;border-left:1px solid var(--border)}
.sub-stat:last-child{border-left:none}
.sub-stat-value{font-size:15px;font-weight:800;color:var(--t1);line-height:1.2}
.sub-stat-label{font-size:8.5px;color:var(--t3);font-weight:700;text-transform:uppercase;letter-spacing:.05em;margin-top:4px}
.sub-url-row{margin:14px 20px 0;background:rgba(139,92,246,0.05);border:1px dashed rgba(139,92,246,0.18);border-radius:var(--radius-sm);padding:9px 12px;display:flex;align-items:center;gap:9px}
.sub-url-text{font-family:ui-monospace,monospace;font-size:9.5px;color:#A78BFA;flex:1;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.sub-url-copy{background:none;border:none;color:var(--purple);cursor:pointer;font-size:14px;padding:3px;display:flex;flex-shrink:0;transition:all var(--transition)}
.sub-url-copy:hover{color:#A78BFA;transform:scale(1.1)}
.sub-bottom{padding:14px 20px 18px;display:flex;gap:7px;flex-wrap:wrap}
.sub-bottom .btn{flex:1;justify-content:center;min-width:fit-content}
.subs-empty{text-align:center;padding:70px 20px;background:var(--bg-card);backdrop-filter:blur(16px);border:1px dashed var(--border);border-radius:var(--radius);grid-column:1/-1}
.subs-empty-icon{width:64px;height:64px;border-radius:var(--radius);background:var(--purple-bg);display:flex;align-items:center;justify-content:center;font-size:28px;color:var(--purple);margin:0 auto 16px}
.subs-empty-title{font-size:13.5px;font-weight:700;color:var(--t2);margin-bottom:5px}
.subs-empty-sub{font-size:11px;color:var(--t3)}
.modal-bg{display:none;position:fixed;inset:0;background:rgba(0,0,0,0.60);z-index:500;align-items:center;justify-content:center;backdrop-filter:blur(6px)}
.modal-bg.open{display:flex}
.modal{background:var(--bg-card);backdrop-filter:blur(24px);-webkit-backdrop-filter:blur(24px);border:1px solid var(--border);border-radius:var(--radius);padding:32px 30px;max-width:520px;width:calc(100% - 32px);max-height:90vh;overflow-y:auto;position:relative;animation:fadeSlide .3s ease;box-shadow:var(--shadow-hover),var(--shadow-inner)}
.modal-close{position:absolute;top:14px;left:14px;background:var(--accent-d);border:1px solid var(--border);color:var(--t2);width:34px;height:34px;border-radius:var(--radius-sm);font-size:18px;display:flex;align-items:center;justify-content:center;cursor:pointer;border:none;transition:all var(--transition)}
.modal-close:hover{background:var(--red-bg);color:var(--red-t)}
.modal-title{font-size:16px;font-weight:700;color:var(--t1);margin-bottom:18px;display:flex;align-items:center;gap:10px}
.modal-title i{color:var(--accent)}
.modal-v2{background:var(--bg-card);backdrop-filter:blur(24px);-webkit-backdrop-filter:blur(24px);border:1px solid var(--border);border-radius:var(--radius);padding:0;max-width:430px;width:calc(100% - 32px);max-height:92vh;overflow-y:auto;position:relative;animation:fadeSlide .3s ease;box-shadow:var(--shadow-hover),var(--shadow-inner)}
.modal-v2-head{background:linear-gradient(155deg,var(--purple-bg),transparent 65%);padding:18px 22px 14px;position:relative;overflow:hidden}
.modal-v2-head::before{content:'';position:absolute;top:-50px;left:-50px;width:160px;height:160px;background:radial-gradient(circle,rgba(139,92,246,0.12),transparent 72%);pointer-events:none}
.modal-v2-close{position:absolute;top:14px;left:14px;background:var(--accent-d);border:1px solid var(--border);color:var(--t2);width:34px;height:34px;border-radius:var(--radius-sm);font-size:17px;display:flex;align-items:center;justify-content:center;cursor:pointer;z-index:2;transition:all var(--transition)}
.modal-v2-close:hover{background:var(--red-bg);color:var(--red-t);border-color:rgba(239,68,68,0.25)}
.modal-v2-icon{width:44px;height:44px;border-radius:var(--radius-sm);background:linear-gradient(135deg,var(--purple),#6D48D6);display:flex;align-items:center;justify-content:center;color:#fff;font-size:20px;margin-bottom:10px;position:relative;z-index:1;box-shadow:0 8px 24px rgba(139,92,246,0.30)}
.modal-v2-title{font-size:15.5px;font-weight:800;color:var(--t1);position:relative;z-index:1;letter-spacing:-0.01em}
.modal-v2-sub{font-size:10.5px;color:var(--t3);margin-top:3px;position:relative;z-index:1;line-height:1.6}
.modal-v2-body{padding:16px 22px 20px;border-top:1px solid var(--border)}
.modal-v2-field{margin-bottom:12px}
.modal-v2-field label{display:flex;align-items:center;gap:5px;font-size:9.5px;font-weight:800;color:var(--t2);text-transform:uppercase;letter-spacing:.06em;margin-bottom:6px}
.modal-v2-field label i{color:var(--purple);font-size:13px}
.modal-v2-input-wrap{position:relative}
.modal-v2-input-wrap>i{position:absolute;right:13px;top:50%;transform:translateY(-50%);color:var(--t3);font-size:14px;pointer-events:none;transition:color var(--transition);z-index:1}
.modal-v2-input{width:100%;padding:10px 40px 10px 14px;border-radius:var(--radius-sm);border:1px solid var(--border);background:rgba(0,0,0,0.10);color:var(--t1);font-family:var(--font);font-size:12.5px;outline:none;transition:all var(--transition)}
[data-theme="light"] .modal-v2-input{background:rgba(255,255,255,0.30)}
.modal-v2-input::placeholder{color:var(--t3)}
.modal-v2-input:focus{border-color:rgba(139,92,246,0.45);box-shadow:0 0 0 4px rgba(139,92,246,0.08);background:rgba(0,0,0,0.16)}
.modal-v2-input:focus~i{color:var(--purple)}
.modal-v2-footer{display:flex;gap:8px;margin-top:16px}
.modal-v2-footer .btn{flex:1;justify-content:center;padding:10px}
.lmodal-head{background:linear-gradient(155deg,var(--accent-d),transparent 70%);padding:22px 24px 18px;position:relative;border-bottom:1px solid var(--border)}
.lmodal-icon-row{display:flex;align-items:center;gap:12px;position:relative;z-index:1}
.lmodal-icon{width:46px;height:46px;border-radius:var(--radius-sm);background:linear-gradient(135deg,var(--accent),var(--accent2));display:flex;align-items:center;justify-content:center;color:#fff;font-size:20px;flex-shrink:0;box-shadow:0 6px 24px var(--accent-glow)}
.lmodal-title{font-size:14.5px;font-weight:800;color:var(--t1)}
.lmodal-sub{font-size:10.5px;color:var(--t3);margin-top:2px}
.lmodal-search{margin-top:14px;position:relative}
.lmodal-search input{width:100%;padding:10px 40px 10px 14px;border-radius:var(--radius-sm);border:1px solid var(--border);background:rgba(0,0,0,0.10);color:var(--t1);font-family:var(--font);font-size:12px;outline:none;transition:all var(--transition)}
[data-theme="light"] .lmodal-search input{background:rgba(255,255,255,0.30)}
.lmodal-search input:focus{border-color:var(--accent2);box-shadow:0 0 0 4px var(--accent-d)}
.lmodal-search i{position:absolute;left:12px;top:50%;transform:translateY(-50%);color:var(--t3);font-size:15px}
.lmodal-quickbar{display:flex;gap:8px;margin-top:12px;position:relative;z-index:1}
.lmodal-qbtn{font-size:10px;font-weight:700;padding:5px 12px;border-radius:8px;background:var(--accent-d);color:var(--accent2);border:1px solid var(--border);cursor:pointer;transition:all var(--transition);font-family:var(--font)}
.lmodal-qbtn:hover{background:rgba(99,102,241,0.16)}
.lmodal-count{margin-right:auto;font-size:10.5px;color:var(--t3);display:flex;align-items:center}
.lmodal-list{padding:10px 14px;max-height:360px;overflow-y:auto}
.lrow{display:flex;align-items:center;gap:12px;padding:11px 12px;border-radius:var(--radius-sm);cursor:pointer;transition:all var(--transition);margin-bottom:4px;border:1px solid transparent}
.lrow:hover{background:var(--accent-d)}
.lrow-checked{background:rgba(99,102,241,0.06);border-color:rgba(99,102,241,0.18)}
.lrow-check{width:20px;height:20px;border-radius:6px;border:2px solid var(--border);flex-shrink:0;display:flex;align-items:center;justify-content:center;transition:all var(--transition);background:rgba(0,0,0,0.06)}
.lrow-checked .lrow-check{background:var(--accent);border-color:var(--accent)}
.lrow-check i{font-size:12px;color:#fff;opacity:0;transform:scale(.5);transition:all var(--transition)}
.lrow-checked .lrow-check i{opacity:1;transform:scale(1)}
.lrow-avatar{width:34px;height:34px;border-radius:var(--radius-sm);background:var(--accent-d);color:var(--accent);display:flex;align-items:center;justify-content:center;font-size:14px;flex-shrink:0}
.lrow-checked .lrow-avatar{background:var(--accent);color:#fff}
.lrow-info{flex:1;min-width:0}
.lrow-name{font-size:12.5px;font-weight:700;color:var(--t1);white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.lrow-meta{font-size:9.5px;color:var(--t3);margin-top:2px;display:flex;align-items:center;gap:6px}
.lrow-status{font-size:9px;font-weight:800;padding:3px 10px;border-radius:20px;flex-shrink:0;white-space:nowrap}
.lrow-status-on{background:var(--green-bg);color:var(--green-t)}
.lrow-status-off{background:var(--red-bg);color:var(--red-t)}
.lmodal-footer{display:flex;align-items:center;justify-content:space-between;gap:10px;padding:16px 24px;border-top:1px solid var(--border)}
.lmodal-footer-info{font-size:10.5px;color:var(--t3);display:flex;align-items:center;gap:6px}
.lmodal-footer-info i{color:var(--accent)}
.lmodal-footer-btns{display:flex;gap:8px}
.toast{position:fixed;bottom:24px;left:50%;transform:translateX(-50%)translateY(40px);background:var(--bg-card);backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px);border:1px solid var(--border);color:var(--t1);border-radius:var(--radius-sm);padding:12px 22px;font-size:12.5px;font-weight:600;opacity:0;transition:all .35s ease;z-index:999;pointer-events:none;display:flex;align-items:center;gap:8px;box-shadow:var(--shadow-hover),var(--shadow-inner);white-space:nowrap}
.toast.show{opacity:1;transform:translateX(-50%)translateY(0)}
.toast-success{border-color:rgba(16,185,129,0.25);background:var(--green-bg);color:var(--green-t)}
.toast-error{border-color:rgba(239,68,68,0.25);background:var(--red-bg);color:var(--red-t)}
@media(max-width:1050px){.sidebar{transform:translateX(100%)}.sidebar.open{transform:translateX(0);box-shadow:-12px 0 48px rgba(0,0,0,0.40)}.sb-close{display:flex}.main{margin-right:0;padding-top:74px}.mob-top{display:flex}.metrics{grid-template-columns:1fr 1fr}.grid-2,.grid-3{grid-template-columns:1fr}}
@media(max-width:500px){.metrics{grid-template-columns:1fr}.main{padding:68px 14px 50px}.sub-grid,.cfg-grid,.conn-grid{grid-template-columns:1fr}.modal{padding:24px 18px}.modal-v2-body{padding:14px 16px 18px}.vless-box{padding:18px}}
</style>
</head>
<body>
<div class="toast" id="toast"></div>
<div class="modal-bg" id="modal-links">...</div>
<div class="modal-bg" id="modal-create-sub">...</div>
<div class="modal-bg" id="modal-edit-link">...</div>
<div class="mob-top">...</div>
<div class="overlay" id="overlay"></div>
<aside class="sidebar" id="sb">...</aside>
<main class="main">...</main>
<script>
let isDark=localStorage.getItem('spacezone-theme')!=='light';
function applyTheme(dark){document.documentElement.setAttribute('data-theme',dark?'dark':'light');const icon=dark?'ti-sun':'ti-moon';const label=dark?'تم روشن':'تم تاریک';const el=document.getElementById('theme-icon');if(el)el.className='ti '+icon;const lbl=document.getElementById('theme-label');if(lbl)lbl.textContent=label;const mobIcon=document.getElementById('theme-mob-icon');if(mobIcon)mobIcon.className='ti '+icon}
function toggleTheme(){isDark=!isDark;localStorage.setItem('spacezone-theme',isDark?'dark':'light');applyTheme(isDark)}
applyTheme(isDark);
function toast(msg,type=''){const t=document.getElementById('toast');t.textContent=msg;t.className='toast show'+(type?' toast-'+type:'');clearTimeout(t._timer);t._timer=setTimeout(()=>t.classList.remove('show'),2400)}
function fmtBytes(b){if(!b||b===0)return'0 B';if(b<1024)return b+' B';if(b<1024**2)return(b/1024).toFixed(1)+' KB';if(b<1024**3)return(b/1024**2).toFixed(2)+' MB';return(b/1024**3).toFixed(2)+' GB'}
function toFa(n){return String(n).replace(/\d/g,d=>'۰۱۲۳۴۵۶۷۸۹'[d])}
function esc(s){return String(s||'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]))}
function daysLeft(exp){if(!exp)return null;return Math.ceil((new Date(exp)-Date.now())/86400000)}
function expChip(exp,expired){if(expired)return'<span class="exp-chip exp-exp"><i class="ti ti-calendar-x"></i> منقضی</span>';if(!exp)return'<span class="exp-chip exp-inf"><i class="ti ti-infinity"></i> نامحدود</span>';const d=daysLeft(exp);if(d<=0)return'<span class="exp-chip exp-exp"><i class="ti ti-calendar-x"></i> منقضی</span>';if(d<=3)return`<span class="exp-chip exp-warn"><i class="ti ti-alert-triangle"></i> ${toFa(d)} روز</span>`;return`<span class="exp-chip exp-ok"><i class="ti ti-calendar-check"></i> ${toFa(d)} روز</span>`}
function protoBadge(p){const map={'vless-ws':['VLESS · WS','proto-ws'],'xhttp-packet-up':['XHTTP · packet-up','proto-xhttp'],'xhttp-stream-up':['XHTTP · stream-up','proto-xhttp']};const v=map[p]||map['vless-ws'];return`<span class="proto-chip ${v[1]}">${v[0]}</span>`}
async function checkAuth(){try{const r=await fetch('/api/me');const d=await r.json();if(!d.authenticated)location.href='/login'}catch(e){location.href='/login'}}
async function logout(){try{await fetch('/api/logout',{method:'POST'})}catch(e){}location.href='/login'}
document.getElementById('logout-btn')?.addEventListener('click',logout);
async function authFetch(url,opts={}){const r=await fetch(url,opts);if(r.status===401){location.href='/login';throw new Error('unauthorized')}return r}
const sb=document.getElementById('sb');const overlay=document.getElementById('overlay');
function openSb(){sb.classList.add('open');overlay.classList.add('show')}
function closeSb(){sb.classList.remove('open');overlay.classList.remove('show')}
document.getElementById('open-sb')?.addEventListener('click',openSb);
document.getElementById('close-sb')?.addEventListener('click',closeSb);
overlay?.addEventListener('click',closeSb);
function navTo(name){document.querySelectorAll('.nav-item').forEach(n=>n.classList.toggle('active',n.dataset.pg===name));document.querySelectorAll('.page').forEach(p=>p.classList.toggle('active',p.id==='pg-'+name));const loaders={links:loadLinks,connections:loadConns,errors:loadErrs,subscriptions:loadSubsPage,subgroups:loadSubs,logs:loadActivity};if(loaders[name])loaders[name]();closeSb();window.scrollTo({top:0,behavior:'smooth'})}
document.querySelectorAll('.nav-item').forEach(el=>el.addEventListener('click',()=>navTo(el.dataset.pg)));
function openModal(id){document.getElementById(id)?.classList.add('open')}
function closeModal(id){document.getElementById(id)?.classList.remove('open')}
let ch1,ch2,ch3,prevTraf=0;
function makeGradient(ctx,color1,color2){const g=ctx.createLinearGradient(0,0,0,260);g.addColorStop(0,color1);g.addColorStop(1,color2);return g}
function initCharts(){const c1=document.getElementById('ch1').getContext('2d');const grad1=makeGradient(c1,'rgba(99,102,241,0.38)','rgba(99,102,241,0)');ch1=new Chart(c1,{type:'line',data:{labels:[],datasets:[{label:'MB',data:[],borderColor:'#6366F1',backgroundColor:grad1,fill:true,tension:.42,pointRadius:0,pointHoverRadius:6,pointHoverBackgroundColor:'#6366F1',pointHoverBorderColor:'#fff',pointHoverBorderWidth:2,borderWidth:2.5}]},options:{responsive:true,maintainAspectRatio:false,interaction:{mode:'index',intersect:false},plugins:{legend:{display:false},tooltip:{backgroundColor:'rgba(15,22,42,0.96)',borderColor:'rgba(99,102,241,0.30)',borderWidth:1,titleColor:'#E8F0FE',bodyColor:'#94A3B8',padding:11,cornerRadius:10,displayColors:false,titleFont:{family:'Vazirmatn',size:11,weight:'700'},bodyFont:{family:'Vazirmatn',size:11},callbacks:{label:v=>`${v.parsed.y.toFixed(2)} مگابایت`}}},scales:{x:{grid:{display:false},border:{display:false},ticks:{color:'#475569',font:{size:9,family:'Vazirmatn'}}},y:{grid:{color:'rgba(99,102,241,0.06)'},border:{display:false},ticks:{color:'#475569',font:{size:9,family:'Vazirmatn'},callback:v=>v+' MB'}}},elements:{line:{capBezierPoints:true}}}});ch2=new Chart(document.getElementById('ch2'),{type:'doughnut',data:{labels:['VLESS/WS','XHTTP Ultra','HTTP Proxy'],datasets:[{data:[55,35,10],backgroundColor:['#6366F1','#10B981','#8B5CF6'],borderColor:getComputedStyle(document.documentElement).getPropertyValue('--bg-card')||'#0c1430',borderWidth:4,hoverOffset:10,borderRadius:6,spacing:3}]},options:{responsive:true,maintainAspectRatio:false,cutout:'72%',plugins:{legend:{position:'bottom',labels:{color:'var(--t2)',font:{size:10,family:'Vazirmatn'},padding:12,usePointStyle:true,pointStyle:'circle'}},tooltip:{backgroundColor:'rgba(15,22,42,0.96)',borderColor:'rgba(99,102,241,0.30)',borderWidth:1,padding:10,cornerRadius:10,bodyFont:{family:'Vazirmatn'},titleFont:{family:'Vazirmatn'}}}}});const c3=document.getElementById('ch3').getContext('2d');const grad3=(()=>{const g=c3.createLinearGradient(0,0,0,320);g.addColorStop(0,'rgba(99,102,241,0.45)');g.addColorStop(.6,'rgba(99,102,241,0.08)');g.addColorStop(1,'rgba(99,102,241,0)');return g})();ch3=new Chart(c3,{type:'line',data:{labels:[],datasets:[{label:'مصرف',data:[],borderColor:'#6366F1',backgroundColor:grad3,fill:true,tension:.45,pointRadius:0,pointHoverRadius:7,pointHoverBackgroundColor:'#fff',pointHoverBorderColor:'#6366F1',pointHoverBorderWidth:3,borderWidth:3,order:2},{label:'میانگین',data:[],borderColor:'#F59E0B',borderDash:[6,5],borderWidth:1.6,pointRadius:0,fill:false,tension:0,order:1}]},options:{responsive:true,maintainAspectRatio:false,interaction:{mode:'index',intersect:false},plugins:{legend:{display:false},tooltip:{backgroundColor:'rgba(15,22,42,0.97)',borderColor:'rgba(99,102,241,0.35)',borderWidth:1,titleColor:'#E8F0FE',bodyColor:'#94A3B8',padding:13,cornerRadius:12,displayColors:true,boxPadding:4,titleFont:{family:'Vazirmatn',size:11.5,weight:'700'},bodyFont:{family:'Vazirmatn',size:11},callbacks:{label:v=>` ${v.dataset.label}: ${v.parsed.y.toFixed(2)} MB`}}},scales:{x:{grid:{display:false},border:{display:false},ticks:{color:'#475569',font:{size:9.5,family:'Vazirmatn'},maxRotation:0}},y:{grid:{color:'rgba(99,102,241,0.05)'},border:{display:false},ticks:{color:'#475569',font:{size:9.5,family:'Vazirmatn'},callback:v=>v+' MB'}}}}})}
async function fetchStats(){try{const r=await authFetch('/stats');const d=await r.json();document.getElementById('m-conns').textContent=d.active_connections;document.getElementById('conns-nb').textContent=d.active_connections;document.getElementById('m-traffic').innerHTML=d.total_traffic_mb.toFixed(1)+'<span class="m-unit">MB</span>';document.getElementById('m-alinks').textContent=d.active_links??'—';document.getElementById('m-lsub').textContent='از '+d.links_count+' کانفیگ';document.getElementById('m-subs').textContent=d.subs_count??'—';document.getElementById('errs-badge').textContent=d.total_errors+' خطا';document.getElementById('uptime-inline').textContent=d.uptime;document.getElementById('uptime-badge').textContent='Railway · '+d.uptime;document.getElementById('last-upd').textContent='آخرین بروزرسانی: '+new Date().toLocaleTimeString('fa-IR');document.getElementById('conns-live').innerHTML='<span class="dot dot-green pulse"></span> '+d.active_connections+' اتصال';document.getElementById('t-traffic').innerHTML=d.total_traffic_mb.toFixed(1)+'<span class="m-unit">MB</span>';const delta=d.total_traffic_mb-prevTraf;const pct=Math.min(100,Math.round((delta/50)*100));document.getElementById('bw-pct').textContent=pct+'%';document.getElementById('bw-bar').style.width=pct+'%';prevTraf=d.total_traffic_mb;if(d.hourly){const labels=Object.keys(d.hourly).sort();const vals=labels.map(k=>+(d.hourly[k]/1024**2).toFixed(2));[ch1,ch3].forEach(c=>{if(!c)return;c.data.labels=labels;c.data.datasets[0].data=vals;c.update()});if(vals.length){const avg=vals.reduce((a,b)=>a+b,0)/vals.length;const peak=Math.max(...vals);document.getElementById('t-avg').innerHTML=avg.toFixed(2)+'<span class="m-unit">MB</span>';document.getElementById('t-peak').innerHTML=peak.toFixed(2)+'<span class="m-unit">MB</span>'}}renderErrs(d.recent_errors||[])}catch(e){console.error(e)}}
function renderErrs(errs){const el=document.getElementById('errs-full');if(!el)return;if(!errs.length){el.innerHTML='<div style="color:var(--green-t);padding:10px;font-size:12px;display:flex;align-items:center;gap:5px"><i class="ti ti-circle-check"></i> هیچ خطایی نیست</div>';return}el.innerHTML=errs.slice().reverse().map(e=>`<div class="erow"><div class="etime"><i class="ti ti-clock"></i>${new Date(e.time).toLocaleString('fa-IR')}</div><div class="emsg">${esc(e.error)}${e.url?' — '+esc(e.url):''}</div></div>`).join('')}
async function loadActivity(){try{const r=await authFetch('/api/activity');const d=await r.json();const logs=(d.logs||[]).slice().reverse();const el=document.getElementById('logs-list');const em=document.getElementById('logs-empty');if(!logs.length){el.innerHTML='';em.style.display='block';return}em.style.display='none';const icMap={ok:'ti-circle-check',err:'ti-circle-x',warn:'ti-alert-triangle',info:'ti-info-circle'};const kindFa={link:'کانفیگ',sub:'گروه',auth:'ورود',connection:'اتصال',system:'سیستم'};el.innerHTML=logs.map(l=>`<div class="log-item"><div class="log-ic ${l.level}"><i class="ti ${icMap[l.level]||'ti-info-circle'}"></i></div><div class="log-body"><div class="log-msg">${esc(l.message)}</div><div class="log-time"><i class="ti ti-clock"></i> ${new Date(l.time).toLocaleString('fa-IR')} <span class="log-kind">${kindFa[l.kind]||l.kind}</span></div></div></div>`).join('')}catch(e){console.error(e)}}
let allSubsList=[],allLinksList=[];
async function loadLinks(){try{const[lr,sr]=await Promise.all([authFetch('/api/links'),authFetch('/api/subs')]);const{links=[]}=await lr.json();const{subs=[]}=await sr.json();allSubsList=subs;allLinksList=links;const nlSub=document.getElementById('nl-sub');if(nlSub){nlSub.innerHTML='<option value="">— بدون گروه —</option>'+subs.map(s=>`<option value="${esc(s.sub_id)}">${esc(s.name)}</option>`).join('')}document.getElementById('links-nb').textContent=links.length;document.getElementById('links-pg-cnt').textContent=toFa(links.length)+' کانفیگ';document.getElementById('lsummary-badge').textContent=toFa(links.length);const grid=document.getElementById('links-grid');const empty=document.getElementById('links-empty');if(!links.length){grid.innerHTML='';empty.style.display='block';document.getElementById('lsummary').innerHTML='<div class="empty-state"><i class="ti ti-link-off"></i><p>کانفیگی وجود ندارد</p></div>';return}empty.style.display='none';grid.innerHTML=links.map(l=>{const lim=l.limit_bytes===0?'∞':fmtBytes(l.limit_bytes);const pct=l.limit_bytes===0?0:Math.min(100,l.used_bytes/l.limit_bytes*100);const bc=pct>90?'var(--red)':pct>70?'var(--amber)':'var(--accent)';const allowed=l.active&&!l.expired;const cardCls=!l.active?'cfg-card-inactive':(l.expired?'cfg-card-expired':'');return`<div class="cfg-card ${cardCls}"><div class="cfg-row"><span class="cfg-status-dot ${allowed?'pulse':''}"></span><div class="cfg-identity"><div class="cfg-label">${esc(l.label)}</div><div class="cfg-meta"><span class="cfg-uuid-mini" onclick="navigator.clipboard.writeText('${l.uuid}').then(()=>toast('UUID کپی شد','success'))" title="${l.uuid}"><i class="ti ti-fingerprint"></i> ${l.uuid.slice(0,10)}…</span><span>${new Date(l.created_at).toLocaleDateString('fa-IR')}</span></div></div><div class="cfg-divider"></div><div class="cfg-usage"><div class="usage-bar"><div class="usage-fill" style="width:${pct}%;background:${bc}"></div></div><div class="usage-text"><span>${fmtBytes(l.used_bytes)}</span><span>از ${lim}</span></div></div><div class="cfg-divider"></div><div class="cfg-expiry">${expChip(l.expires_at,l.expired)}</div><div class="cfg-divider"></div><div class="cfg-badges">${protoBadge(l.protocol)}<span class="cfg-tag" title="پورت"><i class="ti ti-route"></i> :${l.port||443}</span><span class="cfg-tag" title="Fingerprint"><i class="ti ti-fingerprint"></i> ${esc(l.fingerprint||'chrome')}</span><span class="cfg-tag" title="آی‌پی"><i class="ti ti-users"></i> ${l.connected_ips||0}${l.ip_limit?'/'+l.ip_limit:' (∞)'}</span><span class="cfg-tag" title="سرعت"><i class="ti ti-gauge"></i> ${l.speed_limit_bytes?(l.speed_limit_bytes*8/1024/1024).toFixed(1)+' Mbps':'نامحدود'}</span>${l.sub_id&&allSubsList.find(s=>s.sub_id===l.sub_id)?`<span class="cfg-tag"><i class="ti ti-folder"></i> ${esc(allSubsList.find(s=>s.sub_id===l.sub_id).name)}</span>`:''}</div><div class="cfg-divider"></div><div class="cfg-actions"><button class="toggle${allowed?' on':''}" onclick="toggleActive('${l.uuid}',${!l.active})" title="فعال/غیرفعال"></button><button class="btn btn-ghost btn-sm btn-icon" onclick="navigator.clipboard.writeText('${esc(l.vless_link)}').then(()=>toast('لینک کپی شد','success'))" title="کپی لینک"><i class="ti ti-copy"></i></button><button class="btn btn-ghost btn-sm btn-icon" onclick="navigator.clipboard.writeText('${esc(l.sub_url)}').then(()=>toast('Sub کپی شد','success'))" title="Sub URL"><i class="ti ti-rss"></i></button><button class="btn btn-ghost btn-sm btn-icon" onclick="showQR('${esc(l.vless_link)}')" title="QR"><i class="ti ti-qrcode"></i></button><button class="btn btn-amber btn-sm btn-icon" onclick="openEditLink('${l.uuid}')" title="ویرایش"><i class="ti ti-edit"></i></button><button class="btn btn-ghost btn-sm btn-icon" onclick="resetUsage('${l.uuid}')" title="ریست مصرف"><i class="ti ti-rotate"></i></button><button class="btn btn-danger btn-sm btn-icon" onclick="deleteLink('${l.uuid}')" title="حذف"><i class="ti ti-trash"></i></button></div></div></div>`}).join('');document.getElementById('lsummary').innerHTML=links.slice(0,6).map(l=>`<div class="stat-row"><span class="stat-key" style="gap:5px"><i class="ti ${l.expired?'ti-calendar-x':l.active?'ti-circle-check':'ti-circle-x'}" style="color:${l.expired?'var(--amber)':l.active?'var(--green)':'var(--red)'}"></i>${esc(l.label)}</span><span class="stat-value" style="font-size:10px">${fmtBytes(l.used_bytes)} / ${l.limit_bytes===0?'∞':fmtBytes(l.limit_bytes)}</span></div>`).join('')}catch(e){console.error(e)}}
async function createLink(){const label=document.getElementById('nl-label').value.trim()||'کانفیگ جدید';const val=document.getElementById('nl-val').value;const unit=document.getElementById('nl-unit').value;const exp=document.getElementById('nl-exp').value;const note=document.getElementById('nl-note').value.trim();const sub_id=document.getElementById('nl-sub').value||null;const protocol=document.getElementById('nl-proto').value||'vless-ws';const fingerprint=document.getElementById('nl-fp').value||'chrome';const alpn=document.getElementById('nl-alpn').value.trim();const port=Number(document.getElementById('nl-port').value)||443;const ip_limit=Number(document.getElementById('nl-iplimit').value)||0;const speed_limit_value=Number(document.getElementById('nl-speed').value)||0;const speed_limit_unit=document.getElementById('nl-speed-unit').value;try{const r=await authFetch('/api/links',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({label,limit_value:val||0,limit_unit:unit,expires_days:exp||0,note,sub_id,protocol,fingerprint,alpn,port,ip_limit,speed_limit_value,speed_limit_unit})});if(!r.ok)throw new Error('failed');['nl-label','nl-val','nl-exp','nl-note','nl-alpn'].forEach(id=>document.getElementById(id).value='');document.getElementById('nl-port').value='443';document.getElementById('nl-iplimit').value='0';document.getElementById('nl-speed').value='0';document.getElementById('nl-alpn-preset').value='';document.getElementById('nl-alpn').style.display='none';toast('کانفیگ ساخته شد ✓','success');loadLinks()}catch(e){toast('خطا در ساخت','error')}}
function openEditLink(uuid){const l=allLinksList.find(x=>x.uuid===uuid);if(!l)return;document.getElementById('el-uuid').value=uuid;document.getElementById('el-label').value=l.label;document.getElementById('el-note').value=l.note||'';if(l.limit_bytes===0){document.getElementById('el-val').value='';document.getElementById('el-unit').value='GB'}else{document.getElementById('el-val').value=(l.limit_bytes/1024/1024).toFixed(0);document.getElementById('el-unit').value='MB'}document.getElementById('el-exp').value='';document.getElementById('el-fp').value=l.fingerprint||'chrome';document.getElementById('el-alpn').value=l.alpn||'';document.getElementById('el-port').value=l.port||443;document.getElementById('el-iplimit').value=l.ip_limit||0;if(!l.speed_limit_bytes){document.getElementById('el-speed').value='0';document.getElementById('el-speed-unit').value='MBIT'}else{document.getElementById('el-speed').value=(l.speed_limit_bytes*8/1024/1024).toFixed(2);document.getElementById('el-speed-unit').value='MBIT'}openModal('modal-edit-link')}
async function saveEditLink(){const uuid=document.getElementById('el-uuid').value;const label=document.getElementById('el-label').value.trim();const note=document.getElementById('el-note').value.trim();const val=document.getElementById('el-val').value;const unit=document.getElementById('el-unit').value;const exp=document.getElementById('el-exp').value;const fingerprint=document.getElementById('el-fp').value||'chrome';const alpn=document.getElementById('el-alpn').value.trim();const port=Number(document.getElementById('el-port').value)||443;const ip_limit=Number(document.getElementById('el-iplimit').value)||0;const speed_limit_value=Number(document.getElementById('el-speed').value)||0;const speed_limit_unit=document.getElementById('el-speed-unit').value;const body={label,note,limit_value:val||0,limit_unit:unit,fingerprint,alpn,port,ip_limit,speed_limit_value,speed_limit_unit};if(exp&&Number(exp)>0)body.expires_days=Number(exp);try{const r=await authFetch('/api/links/'+uuid,{method:'PATCH',headers:{'Content-Type':'application/json'},body:JSON.stringify(body)});if(!r.ok)throw new Error();closeModal('modal-edit-link');toast('کانفیگ ویرایش شد ✓','success');loadLinks()}catch(e){toast('خطا در ویرایش','error')}}
async function toggleActive(uuid,newState){try{const r=await authFetch('/api/links/'+uuid,{method:'PATCH',headers:{'Content-Type':'application/json'},body:JSON.stringify({active:newState})});if(!r.ok)throw new Error();toast(newState?'فعال شد ✓':'غیرفعال شد','success');loadLinks()}catch(e){toast('خطا','error')}}
async function resetUsage(uuid){try{const r=await authFetch('/api/links/'+uuid,{method:'PATCH',headers:{'Content-Type':'application/json'},body:JSON.stringify({reset_usage:true})});if(!r.ok)throw new Error();toast('مصرف ریست شد ✓','success');loadLinks()}catch(e){toast('خطا','error')}}
async function deleteLink(uuid){if(!confirm('حذف این کانفیگ؟'))return;try{const r=await authFetch('/api/links/'+uuid,{method:'DELETE'});if(!r.ok)throw new Error();toast('حذف شد ✓','success');loadLinks()}catch(e){toast('خطا','error')}}
function showQR(link){window.open('https://api.qrserver.com/v1/create-qr-code/?size=300x300&data='+encodeURIComponent(link),'_blank')}
let allSubsRaw=[];
async function loadSubs(){try{const r=await authFetch('/api/subs');const d=await r.json();const subs=d.subs||[];allSubsRaw=subs;document.getElementById('subs-nb').textContent=subs.length;document.getElementById('subs-pg-cnt').textContent=toFa(subs.length)+' گروه';renderSubsGrid(subs)}catch(e){console.error(e)}}
function renderSubsGrid(subs){const grid=document.getElementById('subs-grid');if(!subs.length){grid.innerHTML='<div class="subs-empty"><div class="subs-empty-icon"><i class="ti ti-folders"></i></div><div class="subs-empty-title">هنوز گروهی وجود ندارد</div><div class="subs-empty-sub">یک گروه جدید بسازید تا کانفیگ‌ها را دسته‌بندی کنید</div></div>';return}grid.innerHTML=subs.map(s=>`<div class="sub-card"><div class="sub-top"><div class="sub-head"><div class="sub-icon"><i class="ti ti-folder"></i></div><div class="sub-titles"><div class="sub-name">${esc(s.name)}</div>${s.desc?`<div class="sub-desc">${esc(s.desc)}</div>`:'<div class="sub-desc" style="opacity:.5">بدون توضیحات</div>'}</div><div class="sub-lock ${s.has_password?'sub-lock-locked':'sub-lock-open'}" title="${s.has_password?'رمزدار':'پابلیک'}"><i class="ti ${s.has_password?'ti-lock':'ti-lock-open'}"></i></div></div><div class="sub-stats"><div class="sub-stat"><div class="sub-stat-value">${toFa(s.links_count)}</div><div class="sub-stat-label">کانفیگ</div></div><div class="sub-stat"><div class="sub-stat-value" style="color:var(--green-t)">${toFa(s.active_count)}</div><div class="sub-stat-label">فعال</div></div><div class="sub-stat"><div class="sub-stat-value" style="font-size:12px">${esc(s.total_used_fmt)}</div><div class="sub-stat-label">مصرف</div></div></div></div><div class="sub-url-row"><span class="sub-url-text">${esc(s.public_url)}</span><button class="sub-url-copy" onclick="navigator.clipboard.writeText('${esc(s.public_url)}').then(()=>toast('لینک پابلیک کپی شد','success'))" title="کپی"><i class="ti ti-copy"></i></button><button class="sub-url-copy" onclick="window.open('${esc(s.public_url)}','_blank')" title="باز کردن"><i class="ti ti-external-link"></i></button></div><div class="sub-bottom"><button class="btn btn-ghost btn-sm" onclick="openSubLinks('${esc(s.sub_id)}','${esc(s.name)}')"><i class="ti ti-link-plus"></i> کانفیگ‌ها</button><button class="btn btn-outline btn-sm" onclick="navigator.clipboard.writeText('${esc(s.sub_url)}').then(()=>toast('لینک ساب کپی شد','success'))"><i class="ti ti-rss"></i> ساب</button><button class="btn btn-ghost btn-sm btn-icon" onclick="showQR('${esc(s.sub_url)}')" title="QR"><i class="ti ti-qrcode"></i></button><button class="btn btn-danger btn-sm btn-icon" onclick="deleteSub('${esc(s.sub_id)}')" title="حذف"><i class="ti ti-trash"></i></button></div></div>`).join('')}
function filterSubs(q){q=q.trim().toLowerCase();if(!q){renderSubsGrid(allSubsRaw);return}renderSubsGrid(allSubsRaw.filter(s=>s.name.toLowerCase().includes(q)||(s.desc||'').toLowerCase().includes(q)))}
async function createSub(){const name=document.getElementById('ns-name').value.trim()||'گروه جدید';const desc=document.getElementById('ns-desc').value.trim();const pw=document.getElementById('ns-pw').value;try{const r=await authFetch('/api/subs',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({name,desc,password:pw})});if(!r.ok)throw new Error('failed');['ns-name','ns-desc','ns-pw'].forEach(id=>document.getElementById(id).value='');closeModal('modal-create-sub');toast('گروه ساخته شد ✓','success');loadSubs()}catch(e){toast('خطا در ساخت گروه','error')}}
async function deleteSub(sub_id){if(!confirm('حذف این گروه؟ کانفیگ‌ها حذف نمی‌شوند.'))return;try{const r=await authFetch('/api/subs/'+sub_id,{method:'DELETE'});if(!r.ok)throw new Error();toast('گروه حذف شد ✓','success');loadSubs();loadLinks()}catch(e){toast('خطا','error')}}
let lmodalLinks=[],lmodalInSub=new Set(),currentSubId=null;
async function openSubLinks(sub_id,name){currentSubId=sub_id;document.getElementById('modal-sub-name').textContent=name;document.getElementById('modal-links-body').innerHTML='<div style="color:var(--t3);font-size:12px;padding:20px;text-align:center"><i class="ti ti-loader-2" style="animation:spin 1s linear infinite;font-size:20px"></i></div>';document.getElementById('lmodal-search-inp').value='';openModal('modal-links');try{const[lr,sr]=await Promise.all([authFetch('/api/links'),authFetch('/api/subs')]);const{links=[]}=await lr.json();const{subs=[]}=await sr.json();const thisSub=subs.find(s=>s.sub_id===sub_id);lmodalInSub=new Set(thisSub?.link_ids||[]);lmodalLinks=links;renderLmodalList(links)}catch(e){toast('خطا در بارگذاری','error')}}
function renderLmodalList(links){const body=document.getElementById('modal-links-body');if(!links.length){body.innerHTML='<div class="empty-state" style="padding:30px"><i class="ti ti-link-off"></i><p>هنوز کانفیگی وجود ندارد</p></div>';updateLmodalCount();return}body.innerHTML=links.map(l=>{const checked=lmodalInSub.has(l.uuid);const on=l.active&&!l.expired;return`<div class="lrow ${checked?'lrow-checked':''}" data-uuid="${l.uuid}" data-name="${esc(l.label).toLowerCase()}" onclick="toggleLrow('${l.uuid}',this)"><div class="lrow-check"><i class="ti ti-check"></i></div><div class="lrow-avatar"><i class="ti ti-key"></i></div><div class="lrow-info"><div class="lrow-name">${esc(l.label)}</div><div class="lrow-meta"><i class="ti ti-database" style="font-size:10px"></i> ${fmtBytes(l.used_bytes)}</div></div><span class="lrow-status ${on?'lrow-status-on':'lrow-status-off'}">${on?'فعال':'غیرفعال'}</span></div>`}).join('');updateLmodalCount()}
function toggleLrow(uuid,el){if(lmodalInSub.has(uuid)){lmodalInSub.delete(uuid);el.classList.remove('lrow-checked')}else{lmodalInSub.add(uuid);el.classList.add('lrow-checked')}updateLmodalCount()}
function lmodalSelectAll(state){lmodalLinks.forEach(l=>{if(state)lmodalInSub.add(l.uuid);else lmodalInSub.delete(l.uuid)});renderLmodalList(lmodalLinks)}
function updateLmodalCount(){const el=document.getElementById('lmodal-count');if(el)el.textContent=toFa(lmodalInSub.size)+' انتخاب شده'}
function filterLmodal(q){q=q.trim().toLowerCase();document.querySelectorAll('#modal-links-body .lrow').forEach(row=>{row.style.display=!q||row.dataset.name.includes(q)?'':'none'})}
async function saveSubLinks(){if(!currentSubId)return;const link_ids=[...lmodalInSub];try{const r=await authFetch('/api/subs/'+currentSubId,{method:'PATCH',headers:{'Content-Type':'application/json'},body:JSON.stringify({link_ids})});if(!r.ok)throw new Error();await Promise.all(lmodalLinks.map(l=>authFetch('/api/links/'+l.uuid,{method:'PATCH',headers:{'Content-Type':'application/json'},body:JSON.stringify({sub_id:lmodalInSub.has(l.uuid)?currentSubId:null})})));closeModal('modal-links');toast('کانفیگ‌های گروه ذخیره شدند ✓','success');loadSubs();loadLinks()}catch(e){toast('خطا در ذخیره','error')}}
async function loadSubsPage(){document.getElementById('sub-all-url').textContent=location.protocol+'//'+location.host+'/sub-all';try{const r=await authFetch('/api/subs');const d=await r.json();const subs=d.subs||[];const el=document.getElementById('sub-groups-list');if(!subs.length){el.innerHTML='<div class="empty-state"><i class="ti ti-rss-off"></i><p>هنوز گروهی ندارید</p></div>';return}el.innerHTML=subs.map(s=>`<div style="padding:13px 15px;background:var(--accent-d);border:1px solid var(--border);border-radius:var(--radius-sm);margin-bottom:8px;display:flex;align-items:center;justify-content:space-between;gap:10px;flex-wrap:wrap"><div><div style="font-weight:700;font-size:13px;margin-bottom:3px">${esc(s.name)}</div><div style="font-family:ui-monospace,monospace;font-size:10px;color:#A78BFA">${esc(s.sub_url)}</div><div style="font-size:10px;color:var(--t3);margin-top:3px">${toFa(s.links_count)} کانفیگ · ${esc(s.total_used_fmt)} مصرف ${s.has_password?'· 🔒 رمزدار':''}</div></div><div style="display:flex;gap:5px;flex-wrap:wrap"><button class="btn btn-purple btn-sm" onclick="navigator.clipboard.writeText('${esc(s.sub_url)}').then(()=>toast('کپی شد','success'))"><i class="ti ti-copy"></i> ساب</button><button class="btn btn-purple btn-sm" onclick="navigator.clipboard.writeText('${esc(s.public_url)}').then(()=>toast('کپی شد','success'))"><i class="ti ti-globe"></i> پابلیک</button><button class="btn btn-ghost btn-sm" onclick="showQR('${esc(s.sub_url)}')"><i class="ti ti-qrcode"></i></button></div></div>`).join('')}catch(e){console.error(e)}}
function cpSubAll(){navigator.clipboard.writeText(location.protocol+'//'+location.host+'/sub-all').then(()=>toast('کپی شد ✓','success'))}
function parseBytesFmt(s){if(!s)return 0;const m=String(s).match(/([\d.]+)\s*([A-Za-z]+)/);if(!m)return 0;const n=parseFloat(m[1]);const u=m[2].toUpperCase();const mult={B:1,KB:1024,MB:1024**2,GB:1024**3,TB:1024**4};return n*(mult[u]||1)}
async function loadConns(){try{const r=await authFetch('/api/connections');const d=await r.json();const grid=document.getElementById('conns-grid');const ce=document.getElementById('conns-empty');document.getElementById('conns-live').innerHTML='<span class="dot dot-green pulse"></span> '+d.count+' اتصال';document.getElementById('ch-count').textContent=toFa(d.count);const conns=d.connections||[];if(!d.count){grid.innerHTML='';ce.style.display='block';document.getElementById('ch-traffic').textContent='—';document.getElementById('ch-avgdur').textContent='—';document.getElementById('ch-uniq').textContent='—';return}ce.style.display='none';const totalBytes=conns.reduce((s,c)=>s+parseBytesFmt(c.bytes_fmt),0);document.getElementById('ch-traffic').textContent=fmtBytes(totalBytes);const uniqIps=new Set(conns.map(c=>c.ip)).size;document.getElementById('ch-uniq').textContent=toFa(uniqIps);const durs=conns.map(c=>c.connected_at?Math.max(0,Math.floor((Date.now()-new Date(c.connected_at).getTime())/1000)):0);const avgSec=durs.length?Math.floor(durs.reduce((a,b)=>a+b,0)/durs.length):0;document.getElementById('ch-avgdur').textContent=avgSec<60?avgSec+' ث':avgSec<3600?Math.floor(avgSec/60)+' د':Math.floor(avgSec/3600)+' س';const maxDur=Math.max(...durs,1);grid.innerHTML=conns.map(c=>{const secs=c.connected_at?Math.max(0,Math.floor((Date.now()-new Date(c.connected_at).getTime())/1000)):0;const dur=secs<60?secs+' ثانیه':secs<3600?Math.floor(secs/60)+' دقیقه':Math.floor(secs/3600)+' ساعت';const durPct=Math.min(100,Math.round((secs/maxDur)*100));const protoVal=c.transport==='vless-ws'?'vless-ws':(c.transport||'').replace('xhttp-','xhttp-');return`<div class="conn-card"><div class="conn-card-glow"></div><div class="conn-top"><div class="conn-avatar"><i class="ti ti-device-desktop"></i></div><div class="conn-id"><div class="conn-ip">${esc(c.ip)}<button class="conn-ip-copy" onclick="navigator.clipboard.writeText('${esc(c.ip)}').then(()=>toast('IP کپی شد','success'))" title="کپی IP"><i class="ti ti-copy"></i></button></div><div class="conn-label">${esc(c.label)}</div></div><span class="conn-pill"><span class="dot dot-green pulse"></span> زنده</span></div><div class="conn-divider"></div><div class="conn-body"><div class="conn-proto-row">${protoBadge(protoVal)}</div><div class="conn-stat-row"><div class="conn-stat"><div class="conn-stat-icon"><i class="ti ti-transfer"></i></div><div><div class="conn-stat-label">ترافیک</div><div class="conn-stat-value">${esc(c.bytes_fmt)}</div></div></div><div class="conn-stat"><div class="conn-stat-icon conn-stat-icon-time"><i class="ti ti-clock"></i></div><div><div class="conn-stat-label">مدت</div><div class="conn-stat-value">${dur}</div></div></div></div><div class="conn-duration-track"><div class="conn-duration-fill" style="width:${durPct}%"></div></div></div></div>`}).join('')}catch(e){console.error(e)}}
async function loadErrs(){try{const r=await authFetch('/stats');const d=await r.json();renderErrs(d.recent_errors||[])}catch(e){console.error(e)}}
async function fetchDefaultVless(){try{const r=await authFetch('/api/links');const d=await r.json();const links=d.links||[];const def=links.find(l=>l.limit_bytes===0&&l.active&&!l.expired)||links.find(l=>l.active&&!l.expired)||links[0];document.getElementById('vless-main').textContent=def?def.vless_link:'هنوز کانفیگی وجود ندارد'}catch(e){console.error(e)}}
function cpText(id){navigator.clipboard.writeText(document.getElementById(id).textContent).then(()=>toast('کپی شد ✓','success'))}
function qrFor(id){showQR(document.getElementById(id).textContent)}
function refreshAll(){fetchStats();fetchDefaultVless();loadLinks();if(document.getElementById('pg-subgroups').classList.contains('active'))loadSubs();if(document.getElementById('pg-subscriptions').classList.contains('active'))loadSubsPage();if(document.getElementById('pg-connections').classList.contains('active'))loadConns();if(document.getElementById('pg-logs').classList.contains('active'))loadActivity();toast('رفرش شد','success')}
async function changePw(){const cur=document.getElementById('cp-cur').value;const nw=document.getElementById('cp-new').value;const cf=document.getElementById('cp-cf').value;if(!cur||!nw||!cf){toast('همه فیلدها را پر کنید','error');return}if(nw.length<4){toast('حداقل ۴ کاراکتر','error');return}if(nw!==cf){toast('تکرار رمز اشتباه','error');return}try{const r=await authFetch('/api/change-password',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({current_password:cur,new_password:nw})});const d=await r.json().catch(()=>({}));if(!r.ok)throw new Error(d.detail||'خطا');toast('رمز تغییر کرد ✓','success');['cp-cur','cp-new','cp-cf'].forEach(id=>document.getElementById(id).value='')}catch(e){toast('✗ '+e.message,'error')}}
function togglePwField(id,btn){const inp=document.getElementById(id);const icon=btn.querySelector('i');const toText=inp.type==='password';inp.type=toText?'text':'password';icon.className='ti '+(toText?'ti-eye-off':'ti-eye')}
function checkPwStrength(val){const segs=document.querySelectorAll('#pw-strength-bar .pw-strength-seg');const label=document.getElementById('pw-strength-label');const reqLen=document.getElementById('req-len');const reqNum=document.getElementById('req-num');const reqCase=document.getElementById('req-case');const hasLen=val.length>=4;const hasNum=/\d/.test(val);const hasCase=/[a-z]/.test(val)&&/[A-Z]/.test(val);const hasLong=val.length>=8;reqLen.classList.toggle('met',hasLen);reqNum.classList.toggle('met',hasNum);reqCase.classList.toggle('met',hasCase);let score=0;if(hasLen)score++;if(hasNum)score++;if(hasCase)score++;if(hasLong)score++;const colors=['#EF4444','#F59E0B','#3B82F6','#10B981'];const labels=['خیلی ضعیف','ضعیف','متوسط','قوی'];segs.forEach((s,i)=>{s.style.background=i<score?colors[Math.max(0,score-1)]:'rgba(100,116,139,.2)'});if(val.length===0){label.innerHTML='<i class="ti ti-shield"></i> قدرت رمز';return}label.innerHTML=`<i class="ti ti-shield-check" style="color:${colors[Math.max(0,score-1)]}"></i> ${labels[Math.max(0,score-1)]}`}
let ws;
function wsLog(c,m){const l=document.getElementById('ws-log');const p=document.createElement('p');const colors={ok:'#34D399',err:'#F87171',info:'#94A3B8',sent:'#FCD34D'};p.style.color=colors[c]||'#fff';p.textContent='['+new Date().toLocaleTimeString('fa-IR')+'] '+m;l.appendChild(p);l.scrollTop=l.scrollHeight}
function wsConn(){const u=document.getElementById('ws-uuid').value.trim();if(!u){toast('UUID را وارد کنید','error');return}const url=(location.protocol==='https:'?'wss':'ws')+'://'+location.host+'/ws/'+u;wsLog('info','اتصال: '+url);ws=new WebSocket(url);ws.onopen=()=>wsLog('ok','✓ متصل - UUID معتبر');ws.onerror=()=>wsLog('err','✗ خطا - UUID نامعتبر یا غیرفعال');ws.onmessage=m=>wsLog('info','دریافت '+(m.data.size||m.data.length)+' byte');ws.onclose=e=>wsLog('err','قطع ('+e.code+')'+(e.code===1008?' - دسترسی رد شد':''))}
function wsSend(){const m=document.getElementById('ws-msg').value;if(!m||!ws||ws.readyState!==1)return;ws.send(m);wsLog('sent','ارسال: '+m);document.getElementById('ws-msg').value=''}
function wsDisc(){if(ws)ws.close()}
function setQuota(val,unit,el){document.getElementById('nl-val').value=val===0?'':val;document.getElementById('nl-unit').value=unit;document.querySelectorAll('#quota-chips .chip').forEach(c=>c.classList.remove('chip-active'));el.classList.add('chip-active')}
function setExpiry(days,el){document.getElementById('nl-exp').value=days===0?'':days;document.querySelectorAll('#exp-chips .chip').forEach(c=>c.classList.remove('chip-active'));el.classList.add('chip-active')}
function selectProto(val,el){document.getElementById('nl-proto').value=val;document.querySelectorAll('.proto-card').forEach(c=>c.classList.remove('proto-card-active'));el.classList.add('proto-card-active')}
function setIpLimit(n,el){document.getElementById('nl-iplimit').value=n;document.querySelectorAll('#iplimit-chips .chip').forEach(c=>c.classList.remove('chip-active'));el.classList.add('chip-active')}
function setSpeedLimit(n,el){document.getElementById('nl-speed').value=n;document.getElementById('nl-speed-unit').value='MBIT';document.querySelectorAll('#speed-chips .chip').forEach(c=>c.classList.remove('chip-active'));el.classList.add('chip-active')}
function onAlpnPresetChange(){const p=document.getElementById('nl-alpn-preset').value;const inp=document.getElementById('nl-alpn');if(p==='__custom__'){inp.style.display='block';inp.value='';inp.focus()}else{inp.style.display='none';inp.value=p}}
document.addEventListener('DOMContentLoaded',async()=>{await checkAuth();initCharts();document.getElementById('set-host').textContent=location.host;const subAll=document.getElementById('sub-all-url');if(subAll)subAll.textContent=location.protocol+'//'+location.host+'/sub-all';fetchStats();fetchDefaultVless();loadLinks();loadSubs();setInterval(fetchStats,5000);setInterval(()=>{if(document.getElementById('pg-links').classList.contains('active'))loadLinks();if(document.getElementById('pg-subgroups').classList.contains('active'))loadSubs();if(document.getElementById('pg-subscriptions').classList.contains('active'))loadSubsPage();if(document.getElementById('pg-connections').classList.contains('active'))loadConns();if(document.getElementById('pg-logs').classList.contains('active'))loadActivity()},8000)})
</script>
</body></html>"""


def get_public_page_html(uuid_key: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0">
<title>SpaceZone Sub</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@3.19.0/dist/tabler-icons.min.css">
<style>
*{{margin:0;padding:0;box-sizing:border-box;-webkit-tap-highlight-color:transparent}}
:root{{--bg:#080c1a;--bg2:#0c1430;--bg3:#101a3a;--card:rgba(12,20,44,0.60);--card-b:rgba(99,102,241,0.12);--card-bh:rgba(99,102,241,0.28);--accent:#6366F1;--accent2:#818CF8;--accent3:#A5B4FC;--accent-d:rgba(99,102,241,0.08);--green:#10B981;--green-bg:rgba(16,185,129,0.08);--green-t:#34D399;--red:#EF4444;--red-bg:rgba(239,68,68,0.08);--red-t:#F87171;--amber:#F59E0B;--amber-bg:rgba(245,158,11,0.08);--amber-t:#FCD34D;--purple:#8B5CF6;--purple-bg:rgba(139,92,246,0.08);--purple-t:#A78BFA;--t1:#E8F0FE;--t2:#94A3B8;--t3:#475569;--radius:20px;--shadow:0 16px 52px rgba(0,0,0,0.45);--shadow-inner:inset 0 2px 4px rgba(255,255,255,0.04),inset 0 -2px 4px rgba(0,0,0,0.20);--font:'Vazirmatn',sans-serif}}
[data-theme="light"]{{--bg:#E8EEF8;--bg2:#DCE4F2;--bg3:#CED8EC;--card:rgba(255,255,255,0.55);--card-b:rgba(79,70,229,0.10);--card-bh:rgba(79,70,229,0.22);--accent:#4F46E5;--accent2:#6366F1;--accent3:#818CF8;--accent-d:rgba(79,70,229,0.06);--green:#059669;--green-bg:rgba(5,150,105,0.06);--green-t:#065F46;--red:#DC2626;--red-bg:rgba(220,38,38,0.06);--red-t:#991B1B;--amber:#D97706;--amber-bg:rgba(217,119,6,0.06);--amber-t:#92400E;--purple:#7C3AED;--purple-bg:rgba(124,58,237,0.06);--purple-t:#7C3AED;--t1:#0F172A;--t2:#334155;--t3:#64748B;--shadow:0 16px 44px rgba(0,0,0,0.06);--shadow-inner:inset 0 2px 4px rgba(255,255,255,0.40),inset 0 -2px 4px rgba(0,0,0,0.04)}}
html,body{{min-height:100%;background:var(--bg);font-family:var(--font);color:var(--t1);font-size:14px;transition:background .35s,color .35s}}
.bg-fx{{position:fixed;inset:0;background:radial-gradient(ellipse 70% 45% at 50% -8%,rgba(99,102,241,0.10),transparent 62%),var(--bg);z-index:0;pointer-events:none;transition:background .35s}}
.wrap{{position:relative;z-index:10;max-width:800px;margin:0 auto;padding:24px 16px 64px}}
.top{{display:flex;align-items:center;justify-content:space-between;margin-bottom:26px;gap:10px}}
.brand{{display:flex;align-items:center;gap:11px;min-width:0}}
.brand-img{{width:40px;height:40px;border-radius:50%;overflow:hidden;border:2px solid var(--card-b);box-shadow:0 0 16px rgba(99,102,241,0.30);flex-shrink:0}}
.brand-img img{{width:100%;height:100%;object-fit:cover}}
.brand-name{{font-size:14.5px;font-weight:800;color:var(--t1);letter-spacing:-.01em}}
.brand-sub{{font-size:9.5px;color:var(--t3);font-weight:500}}
.top-actions{{display:flex;align-items:center;gap:6px;flex-shrink:0}}
.icon-btn{{width:36px;height:36px;border-radius:12px;background:var(--card);border:1px solid var(--card-b);color:var(--t2);display:flex;align-items:center;justify-content:center;font-size:16px;cursor:pointer;transition:.18s;backdrop-filter:blur(12px)}}
.icon-btn:hover{{background:var(--accent-d);color:var(--accent2);border-color:var(--card-bh)}}
.sub-info{{background:var(--card);backdrop-filter:blur(20px);border:1px solid var(--card-b);border-radius:var(--radius);padding:24px 24px 22px;margin-bottom:16px;box-shadow:var(--shadow),var(--shadow-inner);position:relative;overflow:hidden}}
.sub-info::before{{content:'';position:absolute;top:0;right:0;width:160px;height:160px;background:radial-gradient(circle at top right,rgba(99,102,241,0.06),transparent 72%);pointer-events:none}}
.sub-eyebrow{{font-size:10px;font-weight:700;color:var(--accent2);text-transform:uppercase;letter-spacing:.12em;margin-bottom:8px;display:flex;align-items:center;gap:6px}}
.sub-eyebrow i{{font-size:13px}}
.sub-name{{font-size:23px;font-weight:800;color:var(--t1);margin-bottom:6px;letter-spacing:-.02em}}
.sub-desc{{font-size:12.5px;color:var(--t2);line-height:1.8;margin-bottom:14px}}
.sub-meta-row{{font-size:10.5px;color:var(--t3);margin-bottom:14px;display:flex;align-items:center;gap:6px}}
.sub-sub-box{{background:var(--accent-d);border:1px solid var(--card-b);border-radius:12px;padding:12px 14px;display:flex;align-items:center;gap:9px;flex-wrap:wrap;backdrop-filter:blur(8px)}}
.sub-sub-url{{font-family:ui-monospace,monospace;font-size:10px;color:var(--accent2);word-break:break-all;flex:1;min-width:140px}}
.stats-bar{{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin-bottom:18px}}
.stat-card{{background:var(--card);backdrop-filter:blur(16px);border:1px solid var(--card-b);border-radius:12px;padding:16px 17px;transition:.2s;box-shadow:var(--shadow-inner)}}
.stat-card:hover{{border-color:var(--card-bh);transform:translateY(-2px)}}
.stat-label{{font-size:9px;color:var(--t3);font-weight:700;text-transform:uppercase;letter-spacing:.07em;margin-bottom:7px}}
.stat-val{{font-size:22px;font-weight:800;color:var(--t1);line-height:1;letter-spacing:-.01em}}
.stat-sub{{font-size:9.5px;color:var(--t3);margin-top:6px}}
.copy-all-bar{{display:flex;align-items:center;gap:12px;background:linear-gradient(135deg,var(--accent),var(--accent2));border-radius:var(--radius);padding:16px 19px;margin-bottom:18px;box-shadow:0 8px 32px var(--accent-glow),var(--shadow-inner);flex-wrap:wrap}}
.copy-all-text{{flex:1;min-width:160px}}
.copy-all-title{{font-size:13.5px;font-weight:800;color:#fff;display:flex;align-items:center;gap:6px}}
.copy-all-sub{{font-size:10px;color:rgba(255,255,255,.78);margin-top:3px}}
.copy-all-btn{{background:#fff;color:var(--accent);border:none;border-radius:12px;padding:10px 19px;font-family:var(--font);font-size:12.5px;font-weight:800;cursor:pointer;display:flex;align-items:center;gap:6px;transition:.18s;white-space:nowrap}}
.copy-all-btn:hover{{transform:translateY(-2px);box-shadow:0 6px 20px rgba(0,0,0,.20)}}
.copy-all-btn:active{{transform:translateY(0)scale(.97)}}
.cfg-title{{font-size:12px;font-weight:800;color:var(--t2);margin-bottom:13px;display:flex;align-items:center;gap:6px;text-transform:uppercase;letter-spacing:.07em}}
.cfg-title i{{color:var(--accent);font-size:15px}}
.cfg-grid{{display:grid;gap:13px}}
.cfg-card{{background:var(--card);backdrop-filter:blur(16px);border:1px solid var(--card-b);border-radius:var(--radius);transition:all .2s;position:relative;overflow:hidden;box-shadow:var(--shadow-inner)}}
.cfg-card:hover{{border-color:var(--card-bh);box-shadow:var(--shadow),var(--shadow-inner)}}
.cfg-top{{padding:17px 19px 15px;position:relative}}
.cfg-top::after{{content:'';position:absolute;top:0;right:0;width:3px;height:100%;background:var(--green)}}
.cfg-card.inactive .cfg-top::after{{background:var(--red)}}
.cfg-head{{display:flex;align-items:flex-start;justify-content:space-between;gap:8px;margin-bottom:12px;flex-wrap:wrap}}
.cfg-label{{font-size:14.5px;font-weight:700;color:var(--t1)}}
.cfg-badges{{display:flex;gap:5px;flex-wrap:wrap;margin-top:6px}}
.proto-chip{{font-size:9px;padding:3px 8px;border-radius:7px;font-weight:800;letter-spacing:.02em}}
.pc-ws{{background:var(--accent-d);color:var(--accent2)}}
.pc-xhttp{{background:var(--purple-bg);color:var(--purple-t)}}
.pc-ultra{{background:var(--green-bg);color:var(--green-t)}}
.cfg-status{{display:flex;align-items:center;gap:5px;font-size:10px;font-weight:700;padding:4px 10px;border-radius:20px;white-space:nowrap}}
.cfg-status.ok{{background:var(--green-bg);color:var(--green-t)}}
.cfg-status.no{{background:var(--red-bg);color:var(--red-t)}}
.cfg-usage{{margin-bottom:4px}}
.ubar{{height:6px;border-radius:4px;background:rgba(99,102,241,0.06);overflow:hidden;margin-bottom:5px}}
.ubar-f{{height:100%;border-radius:4px;transition:width .5s ease}}
.utxt{{font-size:10px;color:var(--t3);display:flex;justify-content:space-between}}
.cfg-tear{{position:relative;height:0;border-top:1.5px dashed var(--card-b);margin:0 19px}}
.cfg-tear::before,.cfg-tear::after{{content:'';position:absolute;top:50%;width:18px;height:18px;border-radius:50%;background:var(--bg);transform:translateY(-50%);border:1px solid var(--card-b)}}
.cfg-tear::before{{right:-28px}}
.cfg-tear::after{{left:-28px}}
.cfg-bottom{{padding:15px 19px 18px}}
.cfg-link-toggle{{width:100%;display:flex;align-items:center;justify-content:space-between;gap:10px;background:transparent;border:1px dashed var(--card-b);border-radius:12px;padding:10px 13px;cursor:pointer;font-family:var(--font);color:var(--t2);font-size:11.5px;font-weight:600;transition:.15s}}
.cfg-link-toggle:hover{{background:var(--accent-d);border-color:var(--card-bh);color:var(--accent2)}}
.cfg-link-toggle .ltl{{display:flex;align-items:center;gap:7px}}
.cfg-link-toggle i.ti-chevron-down{{transition:transform .2s}}
.cfg-link-toggle.open i.ti-chevron-down{{transform:rotate(180deg)}}
.cfg-vless-wrap{{display:grid;grid-template-rows:0fr;transition:grid-template-rows .25s ease}}
.cfg-vless-wrap.open{{grid-template-rows:1fr}}
.cfg-vless-inner{{overflow:hidden}}
.cfg-vless{{background:rgba(0,0,0,.18);border:1px solid var(--card-b);border-radius:10px;padding:11px 13px;font-size:9.8px;font-family:ui-monospace,monospace;color:var(--accent2);word-break:break-all;line-height:1.7;margin-top:9px;max-height:90px;overflow-y:auto}}
[data-theme="light"] .cfg-vless{{background:rgba(0,0,0,.04)}}
.cfg-actions{{display:flex;gap:7px;flex-wrap:wrap;margin-top:11px}}
.btn{{font-family:var(--font);font-size:11.5px;font-weight:700;border-radius:10px;padding:8px 15px;cursor:pointer;display:inline-flex;align-items:center;gap:5px;border:none;transition:all .15s;white-space:nowrap}}
.btn i{{font-size:13px}}
.btn-p{{background:linear-gradient(135deg,#6366F1,#818CF8);color:#fff;box-shadow:0 4px 16px rgba(99,102,241,.30)}}
.btn-p:hover{{transform:translateY(-2px)}}
.btn-g{{background:var(--accent-d);color:var(--accent2);border:1px solid rgba(99,102,241,.14)}}
.btn-g:hover{{background:rgba(99,102,241,.18)}}
.btn-pur{{background:var(--purple-bg);color:var(--purple-t);border:1px solid rgba(139,92,246,.14)}}
.btn-pur:hover{{background:rgba(139,92,246,.18)}}
.conn-chip{{display:inline-flex;align-items:center;gap:4px;font-size:9.5px;padding:3px 8px;border-radius:20px;background:var(--green-bg);color:var(--green-t);font-weight:700}}
.dot{{width:5px;height:5px;border-radius:50%;background:var(--green);display:inline-block;animation:pulse 2s infinite}}
@keyframes pulse{{0%,100%{{opacity:1}}50%{{opacity:.25}}}}
.lock-stage{{display:flex;align-items:center;justify-content:center;min-height:78vh;padding:20px 0}}
.lock-card{{background:var(--card);backdrop-filter:blur(24px);border:1px solid var(--card-b);border-radius:var(--radius);padding:0;text-align:center;max-width:380px;width:100%;box-shadow:var(--shadow),var(--shadow-inner);overflow:hidden;position:relative}}
.lock-banner{{background:linear-gradient(150deg,rgba(99,102,241,.12),rgba(99,102,241,.02)70%);padding:38px 30px 26px;position:relative}}
.lock-shield{{width:64px;height:64px;border-radius:12px;background:var(--accent-d);border:1px solid var(--card-bh);display:flex;align-items:center;justify-content:center;margin:0 auto 18px;position:relative}}
.lock-shield::after{{content:'';position:absolute;inset:-7px;border-radius:16px;border:1px solid var(--card-b);animation:breathe 2.6s ease-in-out infinite}}
@keyframes breathe{{0%,100%{{transform:scale(1);opacity:.5}}50%{{transform:scale(1.08);opacity:0}}}}
.lock-shield i{{font-size:28px;color:var(--accent2)}}
.lock-title{{font-size:18px;font-weight:800;margin-bottom:6px;color:var(--t1);letter-spacing:-.01em}}
.lock-sub{{font-size:12px;color:var(--t3);line-height:1.7}}
.lock-form{{padding:24px 30px 30px}}
.lock-field{{position:relative;margin-bottom:13px}}
.lock-inp{{width:100%;padding:13px 44px 13px 44px;border-radius:12px;border:1px solid var(--card-b);background:rgba(0,0,0,.14);color:var(--t1);font-family:var(--font);font-size:14px;outline:none;text-align:center;letter-spacing:.14em;transition:.18s}}
[data-theme="light"] .lock-inp{{background:rgba(255,255,255,.30)}}
.lock-inp:focus{{border-color:var(--accent);box-shadow:0 0 0 4px var(--accent-d)}}
.lock-eye{{position:absolute;left:13px;top:50%;transform:translateY(-50%);background:none;border:none;color:var(--t3);cursor:pointer;font-size:16px;padding:4px;display:flex}}
.lock-eye:hover{{color:var(--accent2)}}
.lock-lockicon{{position:absolute;right:14px;top:50%;transform:translateY(-50%);color:var(--t3);font-size:15px;pointer-events:none}}
.lock-err{{color:var(--red-t);font-size:11.5px;margin-bottom:10px;min-height:16px;display:flex;align-items:center;justify-content:center;gap:5px}}
.lock-btn{{width:100%;justify-content:center;padding:13px;font-size:13px;border-radius:12px}}
.lock-footer{{padding:14px 30px;border-top:1px solid var(--card-b);font-size:10px;color:var(--t3);display:flex;align-items:center;justify-content:center;gap:6px}}
.empty-state{{text-align:center;padding:80px 20px;color:var(--t3)}}
.empty-state i{{font-size:38px;display:block;margin-bottom:14px}}
.toast{{position:fixed;bottom:22px;left:50%;transform:translateX(-50%)translateY(40px);background:var(--card);backdrop-filter:blur(20px);border:1px solid var(--card-b);color:var(--t1);border-radius:12px;padding:10px 20px;font-size:12.5px;font-weight:600;opacity:0;transition:all .25s;z-index:999;pointer-events:none;display:flex;align-items:center;gap:7px;box-shadow:var(--shadow),var(--shadow-inner);white-space:nowrap}}
.toast.show{{opacity:1;transform:translateX(-50%)translateY(0)}}
.toast.ok{{border-color:rgba(16,185,129,.25);background:var(--green-bg);color:var(--green-t)}}
.qr-modal{{display:none;position:fixed;inset:0;background:rgba(0,0,0,.70);z-index:600;align-items:center;justify-content:center;backdrop-filter:blur(6px);padding:20px}}
.qr-modal.open{{display:flex}}
.qr-box{{background:var(--card);backdrop-filter:blur(24px);border:1px solid var(--card-b);border-radius:var(--radius);padding:26px;text-align:center;max-width:340px;width:100%;box-shadow:var(--shadow),var(--shadow-inner)}}
.qr-title{{font-size:13.5px;font-weight:800;margin-bottom:16px;color:var(--t1)}}
.qr-img{{border-radius:12px;overflow:hidden;margin-bottom:15px}}
.qr-img img{{width:100%;display:block;background:#fff;padding:10px;border-radius:12px}}
.footer{{text-align:center;padding-top:28px;font-size:10.5px;color:var(--t3)}}
@media(max-width:520px){{.stats-bar{{grid-template-columns:1fr 1fr}}.stats-bar .stat-card:nth-child(3){{grid-column:1/-1}}.sub-name{{font-size:19px}}.copy-all-bar{{flex-direction:column;align-items:stretch}}.copy-all-btn{{justify-content:center}}.wrap{{padding:16px 12px 50px}}.lock-banner{{padding:32px 22px 22px}}.lock-form{{padding:20px 22px 26px}}}}
@keyframes spin{{to{{transform:rotate(360deg)}}}}
@keyframes fadeSlide{{from{{opacity:0;transform:translateY(12px)}}to{{opacity:1;transform:translateY(0)}}}}
.card{{animation:fadeSlide .5s ease}}
</style>
</head>
<body>
<div class="bg-fx"></div>
<div class="toast" id="toast"></div>
<div class="qr-modal" id="qr-modal" onclick="this.classList.remove('open')">
<div class="qr-box" onclick="event.stopPropagation()">
<div class="qr-title" id="qr-label">QR Code</div>
<div class="qr-img"><img id="qr-img" src="" alt="QR"></div>
<button class="btn btn-g" style="width:100%;justify-content:center" onclick="document.getElementById('qr-modal').classList.remove('open')"><i class="ti ti-x"></i> بستن</button>
</div>
</div>
<div class="wrap">
<div class="top">
<div class="brand">
<div class="brand-img"><img src="https://uploadkon.ir/uploads/7e7c16_26InShot-20260628-102209067.jpg" alt="SpaceZone"></div>
<div><div class="brand-name">SpaceZone</div><div class="brand-sub">v10.3</div></div>
</div>
<div class="top-actions">
<button class="icon-btn" id="theme-toggle" onclick="toggleTheme()" title="تغییر تم"><i class="ti ti-sun" id="theme-icon"></i></button>
</div>
</div>
<div id="root">
<div class="empty-state"><i class="ti ti-loader-2" style="animation:spin 1s linear infinite"></i>در حال بارگذاری...</div>
</div>
<div class="footer">SpaceZone v10.3</div>
</div>
<script>
const UUID_KEY='{uuid_key}';
let savedPw='';
let isDark=localStorage.getItem('x4g-pub-theme')!=='light';
function applyTheme(dark){{document.documentElement.setAttribute('data-theme',dark?'dark':'light');document.getElementById('theme-icon').className='ti '+(dark?'ti-sun':'ti-moon');}}
function toggleTheme(){{isDark=!isDark;localStorage.setItem('x4g-pub-theme',isDark?'dark':'light');applyTheme(isDark);}}
applyTheme(isDark);
function toast(msg,type=''){{const t=document.getElementById('toast');t.textContent=msg;t.className='toast show'+(type?' '+type:'');setTimeout(()=>t.classList.remove('show'),2400);}}
function esc(s){{return String(s||'').replace(/[&<>"']/g,c=>({{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}}[c]));}}
function fmtB(b){{if(!b||b===0)return'0 B';if(b<1024)return b+' B';if(b<1024**2)return(b/1024).toFixed(1)+' KB';if(b<1024**3)return(b/1024**2).toFixed(2)+' MB';return(b/1024**3).toFixed(2)+' GB';}}
function toFa(n){{return String(n).replace(/\\d/g,d=>'۰۱۲۳۴۵۶۷۸۹'[d]);}}
function protoChip(p){{if(p==='xhttp-stream-one')return'<span class="proto-chip pc-ultra"><i class="ti ti-bolt"></i> XHTTP ULTRA</span>';if(p&&p.startsWith('xhttp'))return'<span class="proto-chip pc-xhttp">'+esc(p)+'</span>';return'<span class="proto-chip pc-ws">VLESS · WS</span>';}}
function showQR(label,link){{document.getElementById('qr-label').textContent=label;document.getElementById('qr-img').src='https://api.qrserver.com/v1/create-qr-code/?size=260x260&data='+encodeURIComponent(link);document.getElementById('qr-modal').classList.add('open');}}
function toggleLink(i){{const wrap=document.getElementById('vw-'+i);const btn=document.getElementById('vt-'+i);const open=wrap.classList.toggle('open');btn.classList.toggle('open',open);btn.querySelector('.ltl span').textContent=open?'پنهان کردن لینک':'نمایش لینک کانفیگ';}}
async function loadData(pw=''){{const url='/api/public/sub/'+UUID_KEY+(pw?'?pw='+encodeURIComponent(pw):'');const r=await fetch(url);return r.json();}}
function renderLock(name,errMsg=''){{document.getElementById('root').innerHTML=`<div class="lock-stage"><div class="lock-card"><div class="lock-banner"><div class="lock-shield"><i class="ti ti-shield-lock"></i></div><div class="lock-title">${{esc(name)}}</div><div class="lock-sub">این گروه با رمز محافظت شده. برای دیدن کانفیگ‌ها رمز رو وارد کنید.</div></div><div class="lock-form"><div class="lock-err" id="lock-err">${{errMsg?'<i class="ti ti-alert-circle"></i> '+esc(errMsg):''}}</div><div class="lock-field"><i class="ti ti-lock lock-lockicon"></i><input class="lock-inp" type="password" id="lock-pw" placeholder="••••••••" autofocus><button class="lock-eye" type="button" onclick="togglePwVis()"><i class="ti ti-eye" id="lock-eye-icon"></i></button></div><button class="btn btn-p lock-btn" onclick="submitLock()"><i class="ti ti-lock-open"></i> ورود به گروه</button></div><div class="lock-footer"><i class="ti ti-shield-check"></i> اتصال شما رمزنگاری‌شده است</div></div></div>`;const inp=document.getElementById('lock-pw');inp.addEventListener('keydown',e=>{{if(e.key==='Enter')submitLock();}});}}
function togglePwVis(){{const inp=document.getElementById('lock-pw');const icon=document.getElementById('lock-eye-icon');const toText=inp.type==='password';inp.type=toText?'text':'password';icon.className='ti '+(toText?'ti-eye-off':'ti-eye');}}
async function submitLock(){{const pw=document.getElementById('lock-pw').value;const data=await loadData(pw);if(data.locked){{renderLock(data.name,'رمز اشتباه است');return;}}savedPw=pw;renderContent(data);}}
function renderContent(d){{const activeCount=d.links.filter(l=>l.active).length;const baseSubUrl=d.sub_url||(window.location.protocol+'//'+window.location.host+'/sub-group/'+UUID_KEY);const subUrl=baseSubUrl+(savedPw?'?pw='+encodeURIComponent(savedPw):'');window._x4gSubUrl=subUrl;window._x4gSubName=d.name;window._x4gLinks=d.links.map(l=>({{vless:l.vless_link,sub:l.sub_url+(savedPw?'?pw='+encodeURIComponent(savedPw):''),label:l.label}}));document.getElementById('root').innerHTML=`<div class="sub-info"><div class="sub-eyebrow"><i class="ti ti-folders"></i> گروه دسترسی</div><div class="sub-name">${{esc(d.name)}}</div>${{d.desc?`<div class="sub-desc">${{esc(d.desc)}}</div>`:''}}<div class="sub-meta-row"><i class="ti ti-clock"></i> آخرین بروزرسانی: ${{new Date().toLocaleTimeString('fa-IR')}}</div><div class="sub-sub-box"><span class="sub-sub-url">${{esc(subUrl)}}</span><button class="btn btn-pur" style="padding:7px 12px;font-size:10.5px" onclick="navigator.clipboard.writeText(window._x4gSubUrl).then(()=>toast('لینک ساب کپی شد ✓','ok'))"><i class="ti ti-copy"></i> کپی لینک ساب</button><button class="btn btn-g" style="padding:7px 12px;font-size:10.5px" onclick="showQR(window._x4gSubName+' — کل گروه',window._x4gSubUrl)"><i class="ti ti-qrcode"></i> QR کل</button></div></div><div class="copy-all-bar"><div class="copy-all-text"><div class="copy-all-title"><i class="ti ti-copy"></i> کپی همه‌ی کانفیگ‌ها</div><div class="copy-all-sub">تمام لینک‌های فعال این گروه را یک‌جا کپی کن</div></div><button class="copy-all-btn" onclick="copyAllConfigs()"><i class="ti ti-clipboard-copy"></i> کپی همه (${{toFa(activeCount)}})</button></div><div class="stats-bar"><div class="stat-card"><div class="stat-label">کانفیگ‌های فعال</div><div class="stat-val">${{toFa(activeCount)}}</div><div class="stat-sub">از ${{toFa(d.links.length)}} کانفیگ</div></div><div class="stat-card"><div class="stat-label">اتصالات زنده</div><div class="stat-val">${{toFa(d.active_connections)}}</div><div class="stat-sub" style="color:var(--green-t);display:flex;align-items:center;gap:4px"><span class="dot"></span> آنلاین</div></div><div class="stat-card"><div class="stat-label">کل مصرف</div><div class="stat-val" style="font-size:17px;margin-top:3px">${{esc(d.total_used_fmt)}}</div><div class="stat-sub">همه کانفیگ‌ها</div></div></div><div class="cfg-title"><i class="ti ti-link"></i> کانفیگ‌ها (${{toFa(d.links.length)}} عدد)</div><div class="cfg-grid">${{d.links.map((l,i)=>{{const pct=l.limit_bytes===0?0:Math.min(100,l.used_bytes/l.limit_bytes*100);const bc=pct>90?'var(--red)':pct>70?'var(--amber)':'var(--green)';const lim=l.limit_bytes===0?'∞':fmtB(l.limit_bytes);return`<div class="cfg-card${{l.active?'':' inactive'}}"><div class="cfg-top"><div class="cfg-head"><div><div class="cfg-label">${{esc(l.label)}}</div><div class="cfg-badges">${{protoChip(l.protocol)}}${{l.connections>0?`<span class="conn-chip"><span class="dot"></span> ${{toFa(l.connections)}} اتصال</span>`:''}}</div></div><span class="cfg-status ${{l.active?'ok':'no'}}">${{l.active?'<i class="ti ti-circle-check"></i> فعال':'<i class="ti ti-circle-x"></i> غیرفعال'}}</span></div><div class="cfg-usage"><div class="ubar"><div class="ubar-f" style="width:${{pct}}%;background:${{bc}}"></div></div><div class="utxt"><span>${{esc(l.used_fmt)}} مصرف شده</span><span>سهمیه: ${{lim}}</span></div></div></div><div class="cfg-tear"></div><div class="cfg-bottom"><button class="cfg-link-toggle" id="vt-${{i}}" onclick="toggleLink(${{i}})"><span class="ltl"><i class="ti ti-eye"></i> <span>نمایش لینک کانفیگ</span></span><i class="ti ti-chevron-down"></i></button><div class="cfg-vless-wrap" id="vw-${{i}}"><div class="cfg-vless-inner"><div class="cfg-vless">${{esc(l.vless_link)}}</div></div></div><div class="cfg-actions"><button class="btn btn-p" onclick="navigator.clipboard.writeText(window._x4gLinks[${{i}}].vless).then(()=>toast('لینک کپی شد ✓','ok'))"><i class="ti ti-copy"></i> کپی لینک</button><button class="btn btn-g" onclick="showQR(window._x4gLinks[${{i}}].label,window._x4gLinks[${{i}}].vless)"><i class="ti ti-qrcode"></i> QR</button></div></div></div>`;}}).join('')}}</div>`;setTimeout(()=>autoRefresh(),30000);}}
function copyAllConfigs(){{const links=window._x4gLinks||[];if(!links.length){{toast('کانفیگی برای کپی نیست','');return;}}const text=links.map(l=>l.vless).join('\\n');navigator.clipboard.writeText(text).then(()=>toast('همه‌ی '+toFa(links.length)+' کانفیگ کپی شد ✓','ok'));}}
async function autoRefresh(){{try{{const data=await loadData(savedPw);if(!data.locked)renderContent(data);}}catch(e){{}}}}
async function init(){{try{{const data=await loadData();if(data.locked){{renderLock(data.name);return;}}renderContent(data);}}catch(e){{document.getElementById('root').innerHTML='<div class="empty-state" style="color:var(--red-t)"><i class="ti ti-alert-circle"></i>خطا در بارگذاری</div>';}}}}
init();
</script>
</body></html>"""
