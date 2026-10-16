#!/usr/bin/env python3
from pathlib import Path
import json,re,sys
root=Path(sys.argv[1] if len(sys.argv)>1 else '.')
p=root/'index.html'
if not p.exists(): raise SystemExit('index.html missing')
s=p.read_text(encoding='utf-8')
s=s.replace('https://mchipta.github.io/delo-est/','https://pokeeesi7-tech.github.io/delo-est-site-new/')
font='<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&display=swap" rel="stylesheet">'
if 'family=Manrope' not in s: s=s.replace('<link rel="manifest" href="manifest.webmanifest">',font+'<link rel="manifest" href="manifest.webmanifest">',1)
s=re.sub(r'<div class="chips">\$\{CATS\.slice\(0,5\).*?</div></div></section>','</div></section>',s,count=1,flags=re.S)
a=s.find('function theme(t){');b=s.find('// Интерфейс адаптируется',a)
if a<0 or b<0: raise SystemExit('theme function boundaries not found')
controller="""let DE_THEME_AUTO=true;
function theme(t){const d=document.documentElement;if(typeof t==='string')DE_THEME_AUTO=false;else{t=d.dataset.theme==='dark'?'light':'dark';DE_THEME_AUTO=false}d.dataset.theme=t;const mt=document.querySelector('meta[name="theme-color"]');if(mt)mt.content=t==='dark'?'#101914':'#f4f5ef';try{localStorage.setItem('gig_t',t)}catch(e){}const b=$('#th');if(b)b.innerHTML=ico(t==='dark'?'sun':'moon')}
(()=>{let saved='';try{saved=localStorage.getItem('gig_t')||''}catch(e){}DE_THEME_AUTO=!saved;const apply=dark=>{if(!DE_THEME_AUTO)return;document.documentElement.dataset.theme=dark?'dark':'light';const mt=document.querySelector('meta[name="theme-color"]');if(mt)mt.content=dark?'#101914':'#f4f5ef';const b=document.querySelector('#th');if(b)b.innerHTML=ico(dark?'sun':'moon')};if(saved)theme(saved);else{apply(matchMedia('(prefers-color-scheme: dark)').matches);const mq=matchMedia('(prefers-color-scheme: dark)');if(mq.addEventListener)mq.addEventListener('change',e=>apply(e.matches));else if(mq.addListener)mq.addListener(e=>apply(e.matches))}})();
"""
s=s[:a]+controller+s[b:]
style='<style id="delo-est-relaunch">\n'+Path(__file__).with_name('studio-relaunch.css').read_text(encoding='utf-8')+'\n</style>'
if 'id="delo-est-relaunch"' in s:s=re.sub(r'<style id="delo-est-relaunch">.*?</style>',lambda _:style,s,count=1,flags=re.S)
else:s=s.replace('</head>',style+'\n</head>',1)
s=re.sub(r'<meta name="theme-color" content="[^"]+">','<meta name="theme-color" content="#f4f5ef">',s,count=1)
p.write_text(s,encoding='utf-8')
m=root/'manifest.webmanifest'
if m.exists():
 d=json.loads(m.read_text(encoding='utf-8'));d['background_color']='#f4f5ef';d['theme_color']='#b6e64c';m.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
sw=root/'sw.js'
if sw.exists(): sw.write_text(re.sub(r"const C='[^']+';","const C='delo-est-field-notes-1';",sw.read_text(encoding='utf-8'),count=1),encoding='utf-8')
print('Applied Field Notes web design; retained the existing API and account flows.')
