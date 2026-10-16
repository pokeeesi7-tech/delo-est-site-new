#!/usr/bin/env python3
"""Apply the DeloEst clean, unified UI adjustments to the website archive during deploy."""
from pathlib import Path
import re, sys

root = Path(sys.argv[1] if len(sys.argv) > 1 else ".")
html_path = root / "index.html"
if not html_path.exists():
    raise SystemExit(f"index.html not found under {root}")
s = html_path.read_text(encoding="utf-8")

# Page metadata must match the new GitHub Pages project URL, not the old live domain.
old = "https://mchipta.github.io/delo-est/"
new = "https://pokeeesi7-tech.github.io/delo-est-site-new/"
s = s.replace(old, new)

# Cabinet contact details are available in Profile settings; keep the dashboard header compact.

# A new cache name forces installed PWA users to retrieve the updated interface.
sw_path = root / "sw.js"
if sw_path.exists():
    sw = sw_path.read_text(encoding="utf-8")
    sw = re.sub(r"const C='[^']+';", "const C='delo-est-v3-clean-unified';", sw, count=1)
    sw_path.write_text(sw, encoding="utf-8")

css = r'''<style id="delo-clean-unified-v3">
/* One design system across the website: fewer competing borders, tighter hierarchy, responsive spacing. */
:root{--de-content:1200px;--de-r-sm:12px;--de-r-md:16px;--de-r-lg:22px;--de-focus:0 0 0 3px color-mix(in srgb,var(--ac) 24%,transparent)}
html{scroll-padding-top:82px}body{min-width:320px;letter-spacing:-.006em;background:var(--bg);-webkit-font-smoothing:antialiased}
.in{max-width:var(--de-content);padding-inline:24px}
header{background:color-mix(in srgb,var(--bg) 91%,transparent);border-bottom-color:color-mix(in srgb,var(--bd) 82%,transparent);box-shadow:0 3px 18px color-mix(in srgb,var(--tx) 3%,transparent)}
.hd{min-height:66px;height:66px;gap:16px}.logo{font-size:21px;letter-spacing:-.04em}.logo .ic{width:29px;height:29px}
.lk{gap:20px;font-size:14px}.ac{gap:8px}.hd .btn.ib{width:44px;min-width:44px;min-height:44px;border-radius:15px;padding:0;background:var(--c);border-color:var(--bd);box-shadow:none}.hd .btn.ib:hover{border-color:var(--ac);color:var(--ac);transform:translateY(-1px)}
button,a,input,select,textarea{-webkit-tap-highlight-color:transparent}button:focus-visible,a:focus-visible,input:focus-visible,select:focus-visible,textarea:focus-visible{outline:0;box-shadow:var(--de-focus)}
main.page{max-width:var(--de-content);padding:30px 24px 32px;min-height:62vh}main.page h2{margin-bottom:18px;line-height:1.12}main.page.cab{max-width:900px;padding-top:26px}
.hero{padding:76px 0 64px}.hero::before{opacity:.19;filter:blur(36px)}.hero p{line-height:1.6}.sb{max-width:800px;border-radius:20px;padding:7px;box-shadow:0 14px 40px color-mix(in srgb,var(--tx) 6%,transparent)}
.card,.cat,.box,.step,.rev,.it{border-radius:20px;border-color:var(--bd);box-shadow:none;transition:border-color .18s,background .18s,transform .18s}
.card:hover,.cat:hover{transform:translateY(-2px);box-shadow:0 12px 28px color-mix(in srgb,var(--tx) 7%,transparent);border-color:color-mix(in srgb,var(--ac) 48%,var(--bd))}
.btn{min-height:44px;border-radius:14px;padding:10px 16px;font-weight:750;box-shadow:none}.btn:hover{transform:translateY(-1px);box-shadow:0 7px 18px color-mix(in srgb,var(--tx) 6%,transparent)}.btn.sm{min-height:38px;border-radius:12px;padding:7px 12px}.btn.pri{box-shadow:0 5px 14px color-mix(in srgb,var(--ac) 15%,transparent)}
input,select,textarea{border-radius:14px;background:var(--c)}input:focus,select:focus,textarea:focus{box-shadow:var(--de-focus)}
.prof{padding:18px 20px;border-radius:24px;margin-bottom:14px;box-shadow:0 12px 26px color-mix(in srgb,var(--ac) 12%,transparent)}.prof .pn{letter-spacing:-.035em}.prof .pchips{gap:6px}.prof .pc{padding:5px 10px;border-radius:12px;max-width:100%;font-size:13px;backdrop-filter:blur(4px)}.prof .acts{gap:8px}.prof .acts .btn{min-height:40px}
/* Profile contact details live in the settings rows; don't repeat them in the dashboard summary. */
.cab>.prof .pchips{display:none!important}.cab>.prof{align-items:center}.cab>.prof .pm{min-width:120px}
/* Counts remain on the destination tabs/navigation; remove banner cards that repeat those counts. */
.cab .alerts{display:none!important}
.ctabs{padding:4px;gap:5px;border-radius:18px;margin-bottom:14px}.ctabs button{min-height:58px;border-radius:14px;padding:9px 5px}.ctabs button.on{box-shadow:0 3px 10px color-mix(in srgb,var(--tx) 5%,transparent)}
.cab .it{padding:16px 18px;margin-bottom:12px;gap:6px}.cab .it> b:first-child{display:block;font-size:18px;letter-spacing:-.02em;margin-bottom:5px}.cab .it{gap:0}.cab .prow{min-height:58px;padding:10px 6px}.cab .prow+.prow{border-top:1px solid var(--bd);border-radius:0}.cab .prow:hover{background:color-mix(in srgb,var(--bg2) 70%,transparent)}.cab .prl{gap:12px}.cab .prl>.ic{width:21px;height:21px}.cab .prl small{font-size:12px;margin-bottom:2px}.cab .prl b{font-size:15px;line-height:1.35}
.fav-intro{gap:18px}.fav-switch{max-width:560px}.fav-search-grid{gap:14px}.fav-search-card{border-radius:18px}
.psh{padding:22px;background:rgba(4,8,23,.58);backdrop-filter:blur(5px)}.psc{border-radius:22px;border-color:var(--bd);box-shadow:0 22px 70px rgba(0,0,0,.24);gap:10px}.psc>b{letter-spacing:-.02em}.psc button{min-height:46px;border-radius:14px}
#tabs{background:color-mix(in srgb,var(--c) 94%,transparent);backdrop-filter:blur(18px);border-top-color:var(--bd);padding-top:7px;box-shadow:0 -8px 28px color-mix(in srgb,var(--tx) 4%,transparent)}#tabs a{min-height:45px;font-size:11px;gap:3px}#tabs a.on{font-weight:800}#tabs .ic{width:21px;height:21px}
#toast{box-shadow:0 12px 32px rgba(0,0,0,.18)}
@media(min-width:1000px){main.page{padding-top:36px}.page.cab{padding-top:32px}.cab .prof{padding:22px 24px}}
@media(max-width:640px){.in{padding-inline:16px}.hd{height:60px;min-height:60px;gap:8px}.logo{font-size:19px;gap:6px}.logo .ic{width:27px;height:27px}.ac{gap:6px}.hd .btn.ib{width:40px;min-width:40px;min-height:40px;border-radius:13px}main.page{padding:22px 14px 26px}.hero{padding:50px 0 42px}.hero p{font-size:16px}.sb{border-radius:18px}.prof{padding:15px 14px;gap:11px;border-radius:20px}.prof .pn{font-size:20px}.prof .av.xl{width:58px;height:58px;border-radius:18px}.prof .pc{font-size:12px;padding:4px 8px}.prof .acts{gap:7px}.prof .acts .btn{flex:1;min-width:0;padding-inline:8px}.cab>.prof{align-items:center}.cab>.prof .acts{width:auto;flex:1}.ctabs{gap:3px;padding:3px}.ctabs button{min-height:56px;padding:8px 2px;font-size:11.5px}.cab .it{padding:14px 14px;border-radius:18px}.cab .prow{min-height:54px}.fav-intro h2{font-size:30px}.psh{align-items:flex-end;padding:0}.psc{width:100%;border-radius:24px 24px 0 0;padding:20px 16px max(18px,env(safe-area-inset-bottom));max-height:88dvh}.de-modal-backdrop{align-items:end;padding:0}.de-modal-card{width:100%;border-radius:24px 24px 0 0;padding:24px 18px max(20px,env(safe-area-inset-bottom))}}
@media(prefers-reduced-motion:reduce){.btn,.card,.cat,.prof{transition:none!important}}
</style>
'''
if 'id="delo-clean-unified-v3"' not in s:
    s = s.replace('</head>', css + '\n</head>', 1)
html_path.write_text(s, encoding="utf-8")
print(f"Patched {html_path} ({len(s)} chars)")
