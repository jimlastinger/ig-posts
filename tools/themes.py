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


# ---- New looks added Nov 9, 2026 (Jim: "the feed is getting tired"; vary the typeface too) ----
import base64 as _b64
def _svg(svg):
    return "url(data:image/svg+xml;base64," + _b64.b64encode(svg.encode()).decode() + ")"
_MARBLE_VEINS = _svg('<svg xmlns="http://www.w3.org/2000/svg" width="1080" height="1350"><filter id="f" x="0" y="0" width="100%" height="100%"><feTurbulence type="turbulence" baseFrequency="0.0035 0.0016" numOctaves="6" seed="11"/><feColorMatrix type="matrix" values="0 0 0 0 0.42  0 0 0 0 0.44  0 0 0 0 0.5  -9 0 0 0 1.05"/></filter><rect width="100%" height="100%" filter="url(#f)" opacity=".42"/></svg>')
_GRAIN = _svg('<svg xmlns="http://www.w3.org/2000/svg" width="400" height="400"><filter id="g"><feTurbulence type="fractalNoise" baseFrequency="0.85" numOctaves="2" seed="3"/><feColorMatrix type="saturate" values="0"/></filter><rect width="100%" height="100%" filter="url(#g)" opacity=".16"/></svg>')

# MARBLE: white marble, lapis accent; Cinzel (Roman inscription capitals) + EB Garamond.
MARBLE = """
body{background:#efede8;color:#1b2230}
.s{background-color:#efede8;background-image:""" + _MARBLE_VEINS + """,radial-gradient(ellipse 900px 800px at 50% 35%,#f8f7f3 0%,#e6e3dc 80%);background-size:cover}
.s:before{border:1px solid #22407a;inset:44px}
.s:after{border:1px solid rgba(34,64,122,.35);inset:52px}
.kick,.cite,.foot,.pair .lab,.real .lab,.col h3{font-family:'Cinzel';font-weight:600}
.kick{color:#22407a;letter-spacing:.26em}
.rule{background:#22407a;height:1px;width:200px}
.hook{font-family:'Cinzel';font-weight:700;text-transform:none;font-size:92px !important;line-height:1.08;letter-spacing:.01em;color:#1b2230}
.hook em,.sub em,.big em,.cta em{color:#22407a;font-style:normal}
.sub{font-family:'Garamond';font-style:italic;font-weight:500;text-transform:none;font-size:58px !important;line-height:1.15;color:#3a4152}
.sub em{font-style:italic}
h2,.big{font-family:'Garamond';font-weight:700;color:#1b2230}
p,.steps .t,.note{font-family:'Garamond';color:#3a4152}
p.strong,.steps .t b{color:#1b2230}
.q{font-family:'Garamond';font-style:italic;font-weight:500;color:#1b2230}
.qm{font-family:'Garamond';color:#22407a}
.cite{color:#22407a;letter-spacing:.14em}
.steps .n{font-family:'Cinzel';color:#22407a}
.cta{font-family:'Cinzel';font-weight:700;letter-spacing:.02em;text-transform:none;color:#1b2230}
.foot{color:#6b7385;letter-spacing:.16em}.foot .sw{color:#22407a}
.numeral{font-family:'Cinzel';color:rgba(34,64,122,.06)}
.pair{border-left-color:#22407a}.real{border-left-color:#22407a}.real .lab{color:#22407a}.real .t{color:#1b2230;font-family:'Garamond'}
p[style*="a99f8c"]{color:#6b7385 !important}
.s:has(.portrait) .hook{font-size:72px !important}
.s:has(.portrait) .sub{font-size:48px !important}
"""

# FRESCO: Pompeian red wall with a black frame band, ochre accent; Playfair Display + Source Serif.
FRESCO = """
body{background:#7a231b;color:#f4e8cf}
.s{background-color:#7a231b;background-image:""" + _GRAIN + """,radial-gradient(ellipse 900px 900px at 50% 40%,#8c2c22 0%,#6a1d16 85%)}
.s:before{border:26px solid #16100d;inset:30px}
.s:after{border:2px solid #e2a94a;inset:66px}
.kick,.cite,.foot,.pair .lab,.real .lab,.col h3{font-family:'SourceSerif';font-weight:600}
.kick{color:#e2a94a;letter-spacing:.3em}
.rule{background:#e2a94a}
.hook{font-family:'Playfair';font-weight:800;text-transform:none;font-size:104px !important;line-height:1.04;color:#f4e8cf}
.hook em,.big em{font-family:'Playfair';font-style:italic;font-weight:700;color:#e2a94a}
.sub{font-family:'SourceSerif';font-weight:600;text-transform:none;font-size:52px !important;line-height:1.2;color:#ecd9b8}
.sub em,.cta em{font-style:italic;color:#e2a94a}
h2,.big{font-family:'Playfair';font-weight:800;color:#f4e8cf}
p,.steps .t,.note{font-family:'SourceSerif';font-weight:400;color:#ecd9b8}
p.strong,.steps .t b{font-weight:700;color:#f4e8cf}
.q{font-family:'Playfair';font-style:italic;font-weight:600;color:#f4e8cf}
.qm{font-family:'Playfair';color:#e2a94a}
.cite{color:#e2a94a;letter-spacing:.16em}
.steps .n{font-family:'Playfair';color:#e2a94a}
.cta{font-family:'Playfair';font-weight:700;text-transform:none;letter-spacing:0;color:#f4e8cf}
.foot{color:#d9b88a;bottom:100px;left:112px;right:112px}.foot .sw{color:#e2a94a}
.numeral{font-family:'Playfair';color:rgba(226,169,74,.07);right:96px;top:70px}
.pair{border-left-color:#e2a94a}.real{border-left-color:#e2a94a}.real .lab{color:#e2a94a}.real .t{color:#f4e8cf}
p[style*="a99f8c"]{color:#d9b88a !important}
.s{padding:140px 124px 190px}
.s:has(.portrait) .hook{font-size:88px !important}
.s:has(.portrait) .sub{font-size:44px !important}
.s:has(.portrait) .portrait{bottom:150px}
"""

# JOURNAL: grainy notebook paper like an old print; typewriter labels + Libre Baskerville, forest-green accent.
JOURNAL = """
body{background:#e8dfcb;color:#262019}
.s{background-color:#e8dfcb;background-image:""" + _GRAIN + """,radial-gradient(ellipse 1000px 900px at 50% 30%,#f1eadb 0%,#ddd2ba 85%)}
.s:before{display:none}.s:after{display:none}
.kick,.cite,.foot,.pair .lab,.real .lab,.col h3{font-family:'Typewriter';font-weight:400}
.kick{color:#2e4b3c;letter-spacing:.12em;font-size:32px;text-transform:lowercase}
.rule{background:#262019;height:2px;width:90px}
.hook{font-family:'Baskerville';font-weight:700;text-transform:none;font-size:86px !important;line-height:1.14;letter-spacing:-.01em;color:#262019}
.hook em,.big em{font-style:italic;font-weight:400;color:#2e4b3c}
.sub{font-family:'Baskerville';font-weight:400;text-transform:none;font-size:44px !important;line-height:1.3;color:#4a4136}
.sub em,.cta em{font-style:italic;color:#2e4b3c}
h2,.big{font-family:'Baskerville';font-weight:700;color:#262019;font-size:76px}
p,.steps .t,.note{font-family:'Baskerville';font-size:40px;line-height:1.45;color:#4a4136}
p.strong,.steps .t b{font-weight:700;color:#262019}
.q{font-family:'Baskerville';font-style:italic;font-weight:400;color:#262019}
.qm{font-family:'Baskerville';color:#2e4b3c}
.cite{color:#2e4b3c;letter-spacing:.06em;font-size:26px}
.steps .n{font-family:'Baskerville';color:#2e4b3c}
.cta{font-family:'Typewriter';text-transform:none;letter-spacing:0;color:#262019}
.foot{color:#7d7262;letter-spacing:.06em;font-size:24px;text-transform:lowercase}.foot .sw{color:#2e4b3c}
.numeral{font-family:'Baskerville';color:rgba(46,75,60,.06)}
.pair{border-left-color:#2e4b3c}.real{border-left-color:#2e4b3c}.real .lab{color:#2e4b3c}.real .t{color:#262019;font-family:'Baskerville'}
p[style*="a99f8c"]{color:#7d7262 !important}
.s:has(.portrait) .hook{font-size:76px !important}
.s:has(.portrait) .sub{font-size:40px !important}
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
    "applied_stoic": {"parchment": PARCHMENT, "bronze": BRONZE, "marble": MARBLE, "fresco": FRESCO, "journal": JOURNAL},
    "dollartrail": {"receipt": RECEIPT, "ledger": LEDGER},
}
