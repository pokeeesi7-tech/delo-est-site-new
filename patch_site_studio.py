#!/usr/bin/env python3
"""Apply Studio v5 responsive styling/theme behavior to the existing one-file web app."""
from pathlib import Path
import json, re, sys
root=Path(sys.argv[1] if len(sys.argv)>1 else '.')
html=root/'index.html'
if not html.exists(): raise SystemExit(f'index.html not found: {html}')
s=html.read_text(encoding='utf-8')
s=s.replace('https://mchipta.github.io/delo-est/','https://pokeeesi7-tech.github.io/delo-est-site-new/')
font_link='<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&display=swap" rel="stylesheet">'
if 'family=Manrope' not in s: s=s.replace('<link rel="manifest" href="manifest.webmanifest">',font_link+'<link rel="manifest" href="manifest.webmanifest">',1)
new_theme='''let TH_AUTO=false;
function theme(t,save=true){const d=document.documentElement;if(t==='auto'){TH_AUTO=true;t=matchMedia('(prefers-color-scheme:dark)').matches?'dark':'light';save=false}else if(typeof t!=='string'){TH_AUTO=false;t=d.dataset.theme==='dark'?'light':'dark';save=true}else{TH_AUTO=false}d.dataset.theme=t;const mt=document.querySelector('meta[name=theme-color]');if(mt)mt.content=t==='dark'?'#0A1120':'#F4F7FC';try{if(save)localStorage.setItem('gig_t',t)}catch(e){}const b=$('#th');if(b)b.innerHTML=ico(t==='dark'?'sun':'moon')}
(()=>{let t;try{t=localStorage.getItem('gig_t')}catch(e){}if(t)theme(t,false);else theme('auto',false);const media=matchMedia('(prefers-color-scheme:dark)');const change=()=>{if(TH_AUTO)theme('auto',false)};if(media.addEventListener)media.addEventListener('change',change);else if(media.addListener)media.addListener(change)})();'''
if 'let TH_AUTO=false' not in s:
    start=s.find('function theme(t){')
    end=s.find('// Интерфейс адаптируется',start)
    if start<0 or end<0: raise SystemExit('Could not locate original theme controller safely')
    s=s[:start]+new_theme+'\n'+s[end:]
css_path=Path(__file__).resolve().with_name('studio-v5.css')
if not css_path.exists(): raise SystemExit(f'Missing design stylesheet {css_path}')
css=css_path.read_text(encoding='utf-8')
style='<style id="delo-est-studio-v5">\n'+css+'\n</style>'
if 'id="delo-est-studio-v5"' in s:
    s=re.sub(r'<style id="delo-est-studio-v5">.*?</style>',lambda _:style,s,count=1,flags=re.S)
else: s=s.replace('</head>',style+'\n</head>',1)
s=re.sub(r'<meta name="theme-color" content="[^"]+">','<meta name="theme-color" content="#F4F7FC">',s,count=1)
html.write_text(s,encoding='utf-8')
manifest=root/'manifest.webmanifest'
if manifest.exists():
    data=json.loads(manifest.read_text(encoding='utf-8'));data['background_color']='#F4F7FC';data['theme_color']='#F4F7FC'
    manifest.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
sw=root/'sw.js'
if sw.exists():
    t=sw.read_text(encoding='utf-8');t=re.sub(r"const C='[^']+';","const C='delo-est-studio-v5';",t,count=1);sw.write_text(t,encoding='utf-8')
print(f'Applied Studio v5 to {html} ({len(s):,} characters)')
