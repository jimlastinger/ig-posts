"""Optional design variations. A post opts in with  THEME = "<name>"  (default: the original look).
Each theme is a CSS override appended after the base brand CSS, so every helper in lib.py keeps working."""

# ------------------------------------------------------------------ @applied_stoic
PARCHMENT = """
body{background:#efe7d6;color:#221c14}
.s{background:#efe7d6;background-image:radial-gradient(ellipse 900px 700px at 50% 30%, #f7f1e4 0%, #e8dec9 75%)}
.s:before{border:2px solid #7a2e22;inset:44px}
.s:after{border:1px solid rgba(122,46,34,.35);inset:58px}
.kick,.cite,.foot .sw,.qm,.hook em,.sub em,.big em,.cta em,.steps .n{color:#7a2e22}
.rule{background:#7a2e22}
.sub,p,.steps .t{color:#3f362a}
p.strong,.steps .t b{color:#221c14}
.note{color:#6e6352}
.pair{border-left-color:#7a2e22}.pair .lab{color:#8a7d68}
.foot{color:#8a7d68}
.numeral{color:rgba(122,46,34,.07)}
p[style*="a99f8c"]{color:#6e6352 !important}
.q{color:#221c14}
.real{border-left-color:#7a2e22}.real .lab{color:#7a2e22}.real .t{color:#221c14}
"""

BRONZE = """
body{background:#c9a35a;color:#14110c}
.s{background:#c9a35a;background-image:linear-gradient(160deg,#d4b06a 0%,#c09650 60%,#a97f3d 100%)}
.s:before{border:3px solid #14110c;inset:40px}
.s:after{display:none}
.kick{color:#14110c;letter-spacing:.4em}
.rule{background:#14110c;height:4px;width:160px}
.hook{color:#14110c;font-size:150px}
.hook em,.sub em,.cta em{color:#5a1a10}
.sub{color:#2b2318}
h2,.q,.big{color:#14110c}
.big em{color:#5a1a10}
p[style*="a99f8c"]{color:#3d3121 !important}
.qm{color:#14110c}
p,.steps .t,.note{color:#2b2318}
p.strong,.steps .t b{color:#14110c}
.steps .n{color:#5a1a10}
.cite{color:#14110c}
.pair{border-left:4px solid #14110c}.pair .lab{color:#3d3121}.pair .val{color:#14110c}
.foot{color:#3d3121}.foot .sw{color:#14110c}
.numeral{color:rgba(20,17,12,.08)}
"""

# ------------------------------------------------------------------ @dollartrail
RECEIPT = """
body{background:#e9e5da;color:#17191c}
.s{background:#f4f1e8;background-image:none;
   box-shadow:inset 0 0 0 40px #e9e5da}
.s:before,.s:after{content:"";position:absolute;left:40px;right:40px;height:22px;
   background:radial-gradient(circle at 11px 0,#e9e5da 10px,transparent 11px) 0 0/22px 22px repeat-x}
.s:before{top:40px}
.s:after{bottom:40px;transform:rotate(180deg)}
.bar{top:62px;left:40px;right:40px;border-bottom:3px dashed #17191c;color:#5b5f66;padding:0 64px}
.bar b{color:#d8352a}
.body{padding:170px 40px 0}
.tag{background:#17191c;color:#f4f1e8}
.tag.ghost{background:transparent}
.hook,h2,.cta{color:#17191c}
.hook em,.cta em,.big2 em{color:#d8352a}
.hook2{color:#5b5f66}
.amt{color:#d8352a}
.pct,.mini,.src{color:#5b5f66}
p{color:#33363b}p b{color:#17191c}
.finding{border:none;border-top:3px dashed #17191c;border-bottom:3px dashed #17191c;background:transparent;padding:26px 0}
.finding .lab{color:#d8352a}.finding .t{color:#17191c}
.gallon{border-color:#17191c}
.lg{border-bottom:2px dashed #b5b0a3}
.tx{border:2px dashed #17191c}.tx .n{color:#17191c}.tx .d{color:#33363b}.tx .l{color:#5b5f66}
.cmp{border-bottom-color:#17191c}.cb .col{background:#b5b0a3}
.xax{color:#5b5f66}
.foot{bottom:92px;left:124px;right:124px;color:#5b5f66}.foot .sw{color:#d8352a}
"""

LEDGER = """
body{background:#0d1726;color:#eef1f5}
.s{background:#0d1726;
   background-image:linear-gradient(rgba(106,169,255,.10) 1px,transparent 1px),linear-gradient(90deg,transparent 150px,rgba(255,90,78,.35) 150px,rgba(255,90,78,.35) 152px,transparent 152px);
   background-size:100% 60px,100% 100%}
.bar{background:#ff5a4e;border-bottom:none;color:#0d1726}
.bar b{color:#0d1726}
.body{padding-left:110px}
.tag{background:#f2b84b;color:#0d1726}
.hook em,.cta em,.big2 em{color:#f2b84b}
.hook2{color:#a9b8cc}
.amt{color:#f2b84b}
.pct,.mini,.src,.xax,.tx .l{color:#8698b0}
p{color:#c6d0dc}p b{color:#eef1f5}
.finding{border:none;border-left:6px solid #f2b84b;background:rgba(242,184,75,.08)}
.finding .lab{color:#f2b84b}
.gallon{border-color:#eef1f5}
.lg{border-bottom-color:#22324a}
.tx{border-color:#22324a;background:rgba(13,23,38,.6)}
.cb .col{background:#2c3e57}.cb.hot .col{background:#f2b84b}.cb.hot .lbl{color:#f2b84b}
.foot{color:#8698b0}.foot .sw{color:#f2b84b}
"""

THEMES = {
    "applied_stoic": {"parchment": PARCHMENT, "bronze": BRONZE},
    "dollartrail": {"receipt": RECEIPT, "ledger": LEDGER},
}
