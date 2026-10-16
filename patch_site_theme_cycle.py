#!/usr/bin/env python3
from pathlib import Path
import sys
p=Path(sys.argv[1] if len(sys.argv)>1 else '.')/'index.html'
s=p.read_text(encoding='utf-8')
a=s.find('let DE_THEME_AUTO=true;');b=s.find('// Интерфейс адаптируется',a)
if a<0 or b<0:raise SystemExit('Theme controller not found')
controller="""let DE_THEME_AUTO=true;
function theme(t){const d=document.documentElement;if(t==='auto'){DE_THEME_AUTO=true;try{localStorage.removeItem('gig_t')}catch(e){}const dark=matchMedia('(prefers-color-scheme: dark)').matches;d.dataset.theme=dark?'dark':'light';const mt=document.querySelector('meta[name="theme-color"]');if(mt)mt.content=dark?'#101914':'#f4f5ef';const b=$('#th');if(b)b.innerHTML=ico('monitor');return}if(typeof t==='string')DE_THEME_AUTO=false;else if(DE_THEME_AUTO)t='light';else if(d.dataset.theme==='light')t='dark';else t='auto';if(t==='auto'){theme('auto');return}DE_THEME_AUTO=false;d.dataset.theme=t;const mt=document.querySelector('meta[name="theme-color"]');if(mt)mt.content=t==='dark'?'#101914':'#f4f5ef';try{localStorage.setItem('gig_t',t)}catch(e){}const b=$('#th');if(b)b.innerHTML=ico(t==='dark'?'sun':'moon')}
(()=>{let saved='';try{saved=localStorage.getItem('gig_t')||''}catch(e){}DE_THEME_AUTO=!saved;const apply=dark=>{if(!DE_THEME_AUTO)return;document.documentElement.dataset.theme=dark?'dark':'light';const mt=document.querySelector('meta[name="theme-color"]');if(mt)mt.content=dark?'#101914':'#f4f5ef';const b=document.querySelector('#th');if(b)b.innerHTML=ico('monitor')};if(saved)theme(saved);else{apply(matchMedia('(prefers-color-scheme: dark)').matches);const mq=matchMedia('(prefers-color-scheme: dark)');if(mq.addEventListener)mq.addEventListener('change',e=>apply(e.matches));else if(mq.addListener)mq.addListener(e=>apply(e.matches))}})();
"""
s=s[:a]+controller+s[b:]
p.write_text(s,encoding='utf-8')
print('Theme toggle now cycles light → dark → system')
