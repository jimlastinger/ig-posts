"""Slide templates for @applied_stoic and @dollartrail.

A post file (posts/<account>/<NNN>-<slug>.py) imports from here and defines:
  ACCOUNT  = "applied_stoic" | "dollartrail"
  SLIDES   = list of slide HTML bodies (for stoic: list of (numeral, body) tuples)
  TRAIL    = "005" etc.  (dollartrail only; shown in the header bar)
  FOLLOWING= "$1 of food spending"   (dollartrail only)
  CAPTION  = full Instagram caption (with source line and hashtags)
  SOURCES  = list of source URLs actually used (for the log; not shown)
Then:  python tools/render.py posts/<account>/<file>.py
"""
import base64, pathlib
from _css import STOIC_CSS, MONEY_CSS

ROOT = pathlib.Path(__file__).resolve().parent
_F = ROOT / "fonts"

def _font(face, fn, weight, style="normal"):
    data = base64.b64encode((_F / fn).read_bytes()).decode()
    return f"@font-face{{font-family:'{face}';src:url(data:font/woff2;base64,{data}) format('woff2');font-weight:{weight};font-style:{style};}}"

FONT_CSS = "".join([
    _font("Cormorant", "cormorant-garamond-latin-500-normal.woff2", 500),
    _font("Cormorant", "cormorant-garamond-latin-600-normal.woff2", 600),
    _font("Cormorant", "cormorant-garamond-latin-700-normal.woff2", 700),
    _font("Cormorant", "cormorant-garamond-latin-500-italic.woff2", 500, "italic"),
    _font("Cormorant", "cormorant-garamond-latin-600-italic.woff2", 600, "italic"),
    _font("Oswald", "oswald-latin-500-normal.woff2", 500),
    _font("Oswald", "oswald-latin-600-normal.woff2", 600),
    _font("Oswald", "oswald-latin-700-normal.woff2", 700),
    _font("Mono", "jetbrains-mono-latin-400-normal.woff2", 400),
    _font("Mono", "jetbrains-mono-latin-700-normal.woff2", 700),
    _font("Anton", "anton-latin-400-normal.woff2", 400),
])

# ============================================================ APPLIED STOIC
# Classes available in a stoic slide body:
#  .kick (small bronze label; NO post numbers)   .rule (short bronze line)
#  .hook (huge Oswald caps; <em> = bronze)       .sub (Oswald caps subhead)
#  h2 (serif headline)  p  p.strong
#  .qm (big quote mark) .q (italic quote)  .cite (attribution: Author · Work ref · tr. Translator)
#  .note (italic aside)  .pair>.lab+.val (event/opinion pairs)
#  ul.steps>li>(span.n + span.t)   .cols>.col.not / .col.yours (two-column sort)
#  .big (closing serif line; <em> bronze)  .cta (Oswald CTA; <em> bronze)
#  .fake / .fake.para + .viral + .verdict + .real>.lab+.t   (myth-busting slides; use fake())

def stoic(i, n, body, numeral=""):
    sw = "Swipe &rarr;" if i < n else "Save &bull; Share"
    num = f"<div class=numeral>{numeral}</div>" if numeral else ""
    return f"""<div class=s>{num}{body}
<div class=foot><span>@applied_stoic</span><span>{i} / {n}</span><span class=sw>{sw}</span></div></div>"""

def fake(kind, viral, verdict, real_lab, real):
    k, cls = ("Fake", "fake") if kind == "fake" else ("Stretched", "fake para")
    return f"""<div class="{cls}">{k}</div>
<div class=viral>&ldquo;{viral}&rdquo;</div>
<div class=verdict>{verdict}</div>
<div class=real><div class=lab>{real_lab}</div><div class=t>&ldquo;{real}&rdquo;</div></div>"""

STOIC_FOLLOW = '<p style="margin-top:40px;font-size:44px;color:#a99f8c">Follow @applied_stoic: one ancient idea, applied to real life, every day.</p>'

# ============================================================ DOLLAR TRAIL
# Palette for segments/stops (use in this order of importance)
R, Y, G, BL, P, T, W = "#ff5a4e", "#f2b84b", "#c9c5ba", "#6aa9ff", "#b98cff", "#4fd1a5", "#8c9097"
# Classes: .tag / .tag.ghost  .hook (<em> red) .hook2  h2  .amt  .pct  p (<b>)  .mini  .src
#  .finding>.lab+.t (use note())   .taxrow>.tx>(.l .n .d)  two side-by-side figures
#  .cta (<em> red)   .big2

def money(trail, following, i, n, body):
    sw = "Swipe &rarr;" if i < n else "Save + Send"
    return f"""<div class=s><div class=bar><span><b>Trail No. {trail}</b> &nbsp;/&nbsp; Following: {following}</span><span></span></div>
<div class=body>{body}</div>
<div class=foot><span>@dollartrail</span><span>{i} / {n}</span><span class=sw>{sw}</span></div></div>"""

def note(t, lab="Trail note"):
    return f"<div class=finding><div class=lab>{lab}</div><div class=t>{t}</div></div>"

def stop(k, n, title, amt, sub, paras, finding, color):
    """One 'stop' on the trail: title, big amount, small sub-label, 1-2 short paragraphs, a trail note."""
    ps = "".join(f"<p>{x}</p>" for x in paras)
    return f"""<div class="tag ghost" style="color:{color};border-color:{color}">Stop {k} of {n}</div>
<h2>{title}</h2><div class=amt style="color:{color}">{amt}</div><div class=pct>{sub}</div>{ps}{note(finding)}"""

def stack(segs, legend_rows, foot, title, tag="The trail map", height=760):
    """Stacked bar + legend. segs=[(pct, color, label_in_bar)] top to bottom; legend_rows=[(name, value, color)].
    Keep legend names short (<= ~20 chars) or they wrap. Lower height (e.g. 640) if the foot text is long."""
    bar = "".join(f'<div class=seg style="height:{round(height*p/100)}px;background:{c};font-size:{30 if p>=8 else 22}px">{lbl if p>=5 else ""}</div>' for p, c, lbl in segs)
    leg = "".join(f'<div class=lg><span class=k><i style="background:{c}"></i>{k}</span><span class=v>{v}</span></div>' for k, v, c in legend_rows)
    return f"""<div class=tag>{tag}</div><h2 style="font-size:70px">{title}</h2>
<div class=wrap><div class=gallon style="height:{height}px">{bar}</div><div class=legend>{leg}<div class=mini>{foot}</div></div></div>"""

def cmp(bars, labels):
    """Vertical bar comparison. bars=[(value, label_on_top, highlight_bool)]. Only compare like with like."""
    mx = max(v for v, _, _ in bars)
    cols = "".join(f'<div class="cb{" hot" if hot else ""}"><div class=lbl>{lbl}</div><div class=col style="height:{round(100*v/mx)}%"></div></div>' for v, lbl, hot in bars)
    ax = "".join(f"<span>{l}</span>" for l in labels)
    return f'<div class=cmp>{cols}</div><div class=xax>{ax}</div>'

DT_FOLLOW = "Follow @dollartrail: we follow one price to the end, every day."
