#!/usr/bin/env python3
from pathlib import Path
import sys
root=Path(sys.argv[1] if len(sys.argv)>1 else '.')
p=root/'index.html'
s=p.read_text(encoding='utf-8')
css=r"""
/* Listing cards and interaction states — intentionally separate from page structure. */
.card.ad2{display:flex;flex-direction:column;overflow:hidden;min-width:0;border-radius:22px;background:var(--c);border:1px solid var(--bd);cursor:pointer;box-shadow:none;transition:transform .2s,border-color .2s,box-shadow .2s}
.card.ad2:hover{transform:translateY(-3px);border-color:color-mix(in srgb,var(--ac2) 48%,var(--bd));box-shadow:var(--sh)}
.card.ad2 .cth{position:relative;height:176px;display:grid;place-items:center;overflow:hidden;background:var(--bg2);color:var(--ac2)}
.card.ad2 .cth>.ic{width:44px;height:44px;opacity:.8}
.card.ad2 .cth img{display:block;width:100%;height:100%;object-fit:cover;transition:transform .35s}
.card.ad2:hover .cth img{transform:scale(1.035)}
.card.ad2 .cth .cn{position:absolute;right:10px;bottom:10px;display:flex;align-items:center;gap:5px;padding:6px 9px;border-radius:9px;background:rgba(23,37,31,.82);color:white;font-size:11px;font-weight:800}
.card.ad2 .cbd{display:flex;flex:1;flex-direction:column;align-items:stretch;gap:9px;padding:19px}
.card.ad2 .chd{display:flex;align-items:flex-start;justify-content:space-between;gap:10px}
.card.ad2 .ctg{display:flex;flex-wrap:wrap;gap:6px;min-width:0}
.card.ad2 h4{margin:2px 0 0;font-size:17px;line-height:1.32;letter-spacing:-.035em;font-weight:850}
.card.ad2 .pay{font-size:22px;line-height:1.2;font-weight:900;letter-spacing:-.05em;color:var(--ac2)}
.card.ad2 .cmeta{display:flex;flex-wrap:wrap;align-items:center;gap:5px;font-size:10.5px;line-height:1.5;color:var(--mu)}
.card.ad2 p{display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden;margin:0;color:var(--mu);font-size:12px;line-height:1.55}
.card.ad2 .fv{flex:none}
.fv.on{animation:deHeartPop .24s ease-out}@keyframes deHeartPop{50%{transform:scale(1.16)}}
.de-modal,.psh,.mnu{animation:deOverlayIn .18s ease-out}@keyframes deOverlayIn{from{opacity:0;transform:translateY(6px) scale(.99)}to{opacity:1;transform:translateY(0) scale(1)}}
@media(max-width:760px){.card.ad2{display:grid;grid-template-columns:108px minmax(0,1fr);align-items:stretch;border-radius:18px}.card.ad2 .cth{height:100%;min-height:148px}.card.ad2 .cbd{padding:13px;gap:7px}.card.ad2 h4{font-size:14px}.card.ad2 .pay{font-size:18px}.card.ad2 p{font-size:11px}.card.ad2 .ctg .tag{font-size:9px;padding:5px 7px}.card.ad2 .fv{width:32px;height:32px;border-radius:10px}.gr.one{grid-template-columns:1fr;gap:10px}}
@media(max-width:380px){.card.ad2{grid-template-columns:88px minmax(0,1fr)}.card.ad2 .cth{min-height:142px}.card.ad2 .cbd{padding:11px}.card.ad2 .cmeta{font-size:9.5px}}
"""
style='<style id="delo-est-cardfix">\n'+css+'\n</style>'
if 'id="delo-est-cardfix"' in s:
 import re
 s=re.sub(r'<style id="delo-est-cardfix">.*?</style>',lambda _:style,s,count=1,flags=re.S)
else:s=s.replace('</head>',style+'\n</head>',1)
p.write_text(s,encoding='utf-8')
print('Added listing-card and modal motion styles')
