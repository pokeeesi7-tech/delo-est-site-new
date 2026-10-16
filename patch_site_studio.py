#!/usr/bin/env python3
from pathlib import Path
import json,re,sys
root=Path(sys.argv[1] if len(sys.argv)>1 else ".")
p=root/"index.html"
if not p.exists(): raise SystemExit("index.html missing")
s=p.read_text(encoding="utf-8")
s=s.replace('<meta name="theme-color" content="#fff">','<meta name="theme-color" content="#F4F7FC">')
s=s.replace('<link rel="manifest" href="manifest.webmanifest">','<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&display=swap" rel="stylesheet"><link rel="manifest" href="manifest.webmanifest">')
css=r"""
<style id="delo-est-studio">
:root{color-scheme:light;--bg:#F4F7FC;--bg2:#EAF0F8;--c:#fff;--tx:#152039;--mu:#65738B;--bd:#DCE4F0;--ac:#405CF5;--ac2:#19B99A;--sh:0 14px 44px rgba(22,43,88,.09);--ease:cubic-bezier(.2,.75,.25,1)}
:root[data-theme=dark]{color-scheme:dark;--bg:#0A1120;--bg2:#111D30;--c:#142138;--tx:#F2F6FC;--mu:#A1B0C6;--bd:#283850;--ac:#8EA2FF;--ac2:#4AD8BD;--sh:0 18px 55px rgba(0,0,0,.25)}
*{box-sizing:border-box}html{scroll-behavior:smooth;scroll-padding-top:90px}body{background:var(--bg);color:var(--tx);font-family:Manrope,Inter,system-ui,-apple-system,sans-serif;letter-spacing:-.012em;-webkit-font-smoothing:antialiased;transition:background .25s,color .25s}h1,h2,h3,h4{font-family:Manrope,Inter,system-ui,sans-serif;letter-spacing:-.045em}h1{font-size:clamp(34px,4vw,60px);font-weight:800;line-height:1.07}h2{font-size:clamp(26px,3vw,38px);font-weight:800}a{transition:color .18s}button,input,select,textarea{font:inherit}button:focus-visible,a:focus-visible,input:focus-visible,select:focus-visible,textarea:focus-visible{outline:0;box-shadow:0 0 0 4px color-mix(in srgb,var(--ac) 22%,transparent)!important}
header{background:color-mix(in srgb,var(--bg) 88%,transparent);backdrop-filter:blur(18px) saturate(1.3);-webkit-backdrop-filter:blur(18px) saturate(1.3);border-bottom:1px solid var(--bd)}.hd{min-height:72px;gap:22px}.logo{font-weight:850;letter-spacing:-.055em}.logo .ic{color:var(--ac)}.lk{gap:clamp(12px,2vw,26px);font-weight:750}.lk a:hover{color:var(--ac)}
.btn{border-radius:13px;border-color:var(--bd);background:var(--c);color:var(--tx);font-weight:800;transition:transform .18s var(--ease),box-shadow .18s,border-color .18s,background .18s}.btn:hover{transform:translateY(-2px);border-color:color-mix(in srgb,var(--ac) 50%,var(--bd));box-shadow:0 9px 24px color-mix(in srgb,var(--tx) 8%,transparent)}.btn:active{transform:scale(.975)}.btn.pri{background:var(--ac);border-color:var(--ac);color:#fff;box-shadow:0 7px 18px color-mix(in srgb,var(--ac) 22%,transparent)}[data-theme=dark] .btn.pri{color:#0a1120}
input,select,textarea{border-radius:13px;border-color:var(--bd);background:var(--c);color:var(--tx);transition:border-color .18s,box-shadow .18s}input:focus,select:focus,textarea:focus{border-color:var(--ac);box-shadow:0 0 0 4px color-mix(in srgb,var(--ac) 15%,transparent)}
.hero{background:linear-gradient(145deg,color-mix(in srgb,var(--ac) 7%,var(--bg)),var(--bg) 62%);padding:clamp(34px,5vw,70px) 0 38px;overflow:hidden}.hero:before{content:"";position:absolute;right:-110px;top:-190px;width:560px;height:560px;border-radius:50%;background:radial-gradient(closest-side,color-mix(in srgb,var(--ac) 13%,transparent),transparent);pointer-events:none}.hero .in{position:relative}.hero p{line-height:1.8;color:var(--mu)}.hero .pill{border:1px solid color-mix(in srgb,var(--ac) 22%,var(--bd));border-radius:9px;background:var(--c);color:var(--ac);font-weight:800;letter-spacing:.04em}
.sb,.searchbox,.search-panel,.filters,.filterbox{border:1px solid var(--bd);border-radius:20px;background:var(--c);box-shadow:var(--sh)}.card,.ad,.ad-card,.cat,.category,.panel,.box,.modal,.dialog{border-color:var(--bd);border-radius:18px}.card,.ad,.ad-card,.cat,.category{background:var(--c);transition:transform .2s var(--ease),border-color .2s,box-shadow .2s}.card:hover,.ad:hover,.ad-card:hover,.cat:hover,.category:hover{transform:translateY(-3px);border-color:color-mix(in srgb,var(--ac) 35%,var(--bd));box-shadow:var(--sh)}
#app{min-height:52vh;animation:page-in .28s var(--ease)}.page{animation:page-in .25s var(--ease)}@keyframes page-in{from{opacity:.45;transform:translateY(7px)}to{opacity:1;transform:none}}
#tabs{background:color-mix(in srgb,var(--c) 94%,transparent);backdrop-filter:blur(18px);border-top:1px solid var(--bd)}#tabs a{border-radius:13px;transition:background .18s,color .18s}#tabs a.on{background:color-mix(in srgb,var(--ac) 10%,var(--c));color:var(--ac)}
footer#contacts{border-top:1px solid var(--bd);background:var(--bg2)}.fg{gap:34px}.fh{font-weight:800}.ct{color:var(--mu)}.ct:hover{color:var(--ac)}
#toast{border:1px solid var(--bd);border-radius:14px;box-shadow:var(--sh);backdrop-filter:blur(14px)}
.modal,.dialog,.pop,.sheet{box-shadow:0 25px 80px rgba(0,0,0,.2);animation:modal-in .22s var(--ease)}@keyframes modal-in{from{opacity:0;transform:translateY(10px) scale(.985)}to{opacity:1;transform:none}}
.skeleton,.skel{background:linear-gradient(100deg,var(--bg2) 25%,color-mix(in srgb,var(--bd) 75%,var(--c)) 38%,var(--bg2) 52%);background-size:220% 100%;animation:shine 1.35s ease infinite}@keyframes shine{to{background-position-x:-220%}}
@media(min-width:900px){.in{max-width:1320px}.lk{white-space:nowrap}.hero .in{gap:clamp(32px,5vw,76px)}}
@media(max-width:760px){.in{padding-inline:16px}.hd{min-height:62px;height:62px;gap:8px}.lk{display:none}.hero{padding:30px 0 24px}.hero h1{font-size:clamp(32px,9vw,44px)}.hero p{font-size:14px}.btn{min-height:44px}.btn.sm{min-height:38px}.card,.ad,.ad-card{border-radius:16px}#tabs{padding-bottom:max(7px,env(safe-area-inset-bottom))}footer#contacts{padding-bottom:22px}}
@media(max-width:390px){.in{padding-inline:12px}.logo{font-size:17px}.ac{gap:1px}.btn.ib{width:36px;min-width:36px}}
@media(prefers-reduced-motion:reduce){*,*:before,*:after{animation-duration:.01ms!important;animation-iteration-count:1!important;transition-duration:.01ms!important;scroll-behavior:auto!important}}
</style>"""
if 'id="delo-est-studio"' in s:s=re.sub(r'<style id="delo-est-studio">.*?</style>',css,s,count=1,flags=re.S)
else:s=s.replace('</head>',css+'\n</head>',1)
# Respect explicit choice; otherwise track the operating-system preference.
theme_fn = r"""let DELO_AUTO_THEME=false;
function theme(t,save=true){
 const d=document.documentElement;
 if(t===undefined){DELO_AUTO_THEME=false;t=d.dataset.theme==='dark'?'light':'dark';save=true}
 else if(t==='auto'){DELO_AUTO_THEME=true;t=matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light';save=false}
 else{DELO_AUTO_THEME=false}
 d.dataset.theme=t;
 const mt=document.querySelector('meta[name=theme-color]');if(mt)mt.content=t==='dark'?'#0A1120':'#F4F7FC';
 try{if(save)localStorage.setItem('gig_t',t)}catch(e){}
 const btn=document.querySelector('#th');if(btn)btn.innerHTML=ico(t==='dark'?'sun':'moon')
}
"""
if "let DELO_AUTO_THEME=false" not in s:
  s=re.sub(r'function theme\([^\n]*\n',theme_fn,s,count=1)
  boot=r"""(()=>{const media=matchMedia('(prefers-color-scheme: dark)');const follow=()=>{if(DELO_AUTO_THEME)theme('auto',false)};if(media.addEventListener)media.addEventListener('change',follow);else if(media.addListener)media.addListener(follow);let saved=null;try{saved=localStorage.getItem('gig_t')}catch(e){}theme(saved||'auto',false)})();"""
  s=re.sub(r'\(\(\)=>\{let t;try\{t=localStorage\.getItem\([\s\S]*?\}\)\(\);',boot,s,count=1)
p.write_text(s,encoding="utf-8")
m=root/"manifest.webmanifest"
if m.exists():
 try:
  d=json.loads(m.read_text(encoding="utf-8"));d["background_color"]="#F4F7FC";d["theme_color"]="#F4F7FC";m.write_text(json.dumps(d,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 except Exception: pass
sw=root/"sw.js"
if sw.exists():sw.write_text(re.sub(r'delo-est-v\d+-unified','delo-est-studio',sw.read_text(encoding="utf-8")),encoding="utf-8")
print("Applied Studio responsive redesign:",p)
