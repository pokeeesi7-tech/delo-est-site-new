#!/usr/bin/env python3
"""V4 cleanup: remove duplicated category chips and low-value feed counters."""
from pathlib import Path
import re, sys

root = Path(sys.argv[1] if len(sys.argv) > 1 else ".")
path = root / "index.html"
if not path.exists():
    raise SystemExit(f"index.html not found under {root}")
s = path.read_text(encoding="utf-8")

# View counts remain on the listing detail page, not on every compact feed preview.
d = chr(36)
s = s.replace(" · " + d + "{ico('eye')}" + d + "{x.opens||0}", "")
# Categories already appear in a dedicated section below fresh listings.
s = re.sub(r'<div class="chips">.*?</div>', '', s, count=1, flags=re.S)

css = r'''<style id="delo-clean-unified-v4">
.card.ad2{padding:12px;border-radius:18px;gap:12px}
.card.ad2:hover{transform:translateY(-2px)}
.card.ad2 .cth{border-radius:14px}
.card.ad2 .tag{font-size:11px;padding:3px 8px}
.card.ad2 h4{font-size:16px;line-height:1.25;letter-spacing:-.02em;margin:7px 0 3px}
.card.ad2 .pay{font-size:16px;line-height:1.25;letter-spacing:-.02em}
.card.ad2 .cmeta{display:flex;align-items:center;gap:4px;flex-wrap:wrap;line-height:1.35;font-size:12px}
.card.ad2 .cmeta .ic{width:14px;height:14px;flex:none}
.card.ad2 p{font-size:13px;line-height:1.4;margin-top:5px}
.bar,.bar2{gap:10px}.bar input,.bar select,.bar2 input,.bar2 select{min-height:46px}
.tabs{gap:8px}.tabs .btn{border-radius:99px}
.fav-toolbar{gap:10px}.fav-search-wrap,.fav-sort{border-radius:14px}
.sc,.it,.emp,.rvf{border-radius:18px}
.ad-h{border-radius:22px;overflow:hidden}.ad-s{gap:12px}
@media(min-width:900px){.card.ad2 .cth{width:104px;height:104px}.card.ad2{padding:14px;gap:14px}}
@media(max-width:640px){.card.ad2 .cth{width:78px;height:78px}.card.ad2{padding:11px;gap:10px}.card.ad2 h4{font-size:15.5px}.card.ad2 .cmeta{font-size:11.5px}.card.ad2 p{font-size:12.5px;-webkit-line-clamp:1}.hero .sb{margin-top:20px}}
</style>'''
if 'id="delo-clean-unified-v4"' not in s:
    s = s.replace("</head>", css + "\n</head>", 1)
path.write_text(s, encoding="utf-8")
print(f"Applied V4 website cleanup to {path}")
