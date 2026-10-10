"""Text check for a post: catches typos and broken markup before anything is rendered or posted.

usage: python tools/lint.py posts/<account>/<NNN>-<slug>.py [more files...]
       (render.py runs this automatically and refuses to render a post that fails)

Checks the visible text of every slide plus the caption for:
  - leftover HTML entities or tags (e.g. "rsquo;", "&amp", "<b")
  - doubled words ("the the") and glued doubles ("HereHere")
  - a word jammed onto a sentence end ("2025.rsquo")
  - words not in the dictionary (tools/words.txt.gz + tools/allow.txt)
  - account rules: no post numbers on @applied_stoic; @dollartrail source on hook, final slide and caption
Also writes _build/<account>-<NNN>-text.txt: the plain text of every slide, for a word-by-word read.

False positive? If it's a real word or name, add it (lowercase) to tools/allow.txt.
"""
import sys, re, gzip, pathlib, html.parser, importlib.util, unicodedata

TOOLS = pathlib.Path(__file__).resolve().parent
REPO = TOOLS.parent
sys.path.insert(0, str(TOOLS))

_words = None
def words():
    global _words
    if _words is None:
        _words = set(gzip.open(TOOLS / "words.txt.gz", "rt").read().split())
        allow = TOOLS / "allow.txt"
        if allow.exists():
            _words |= {w.strip().lower() for w in allow.read_text().splitlines() if w.strip() and not w.startswith("#")}
    return _words

class _Text(html.parser.HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True); self.out = []; self._skip = 0
    def handle_starttag(self, tag, attrs):
        if tag in ("style", "script"): self._skip += 1
        if tag in ("br", "p", "div", "li", "h2"): self.out.append("\n")
        if tag in ("span", "td", "th"): self.out.append(" ")
    def handle_endtag(self, tag):
        if tag in ("style", "script"): self._skip -= 1
        if tag in ("p", "div", "li", "h2"): self.out.append("\n")
        if tag in ("span", "td", "th"): self.out.append(" ")
    def handle_data(self, d):
        if not self._skip: self.out.append(d)

def visible(html_str):
    p = _Text(); p.feed(html_str); p.close()
    t = unicodedata.normalize("NFC", "".join(p.out)).replace(" ", " ").replace("‑", "-")
    return re.sub(r"[ \t]+", " ", re.sub(r"\n\s*\n+", "\n", t)).strip()

ENTITY = re.compile(r"&[#a-zA-Z0-9]+;|&(?:amp|nbsp|quot|rsquo|lsquo|ldquo|rdquo|hellip|middot|mdash|ndash|rarr|larr|minus|bull)\b|(?<![A-Za-z])(?:rsquo|lsquo|ldquo|rdquo|hellip|middot|nbsp|mdash|ndash|rarr|larr)\b;?")
TAG = re.compile(r"</?[a-zA-Z][^ ]*")
DOUBLE = re.compile(r"\b(\w+)[ \t]+\1\b", re.I)
GLUED = re.compile(r"\b([A-Za-z]{3,})\1\b")
JAM = re.compile(r"\b([a-z]{2,})[.;:]([a-z]{2,})\b", re.I)
DOMAIN_TLD = {"gov", "com", "org", "edu", "net", "html", "htm", "io", "uk"}
WORD = re.compile(r"[^\W\d_]+(?:['\u2019][^\W\d_]+)*")
SKIP = re.compile(r"[#@]\w+|https?://\S+|\S+\.(?:gov|com|org|edu|net|html?)\S*")
SUFFIX = {"s", "t", "re", "ve", "ll", "d", "m"}

def check_text(label, text):
    errs = []
    for m in ENTITY.finditer(text): errs.append(f"{label}: leftover HTML entity {m.group(0)!r}")
    for m in TAG.finditer(text): errs.append(f"{label}: leftover HTML tag {m.group(0)!r}")
    for m in DOUBLE.finditer(text):
        if not m.group(1).isdigit(): errs.append(f"{label}: doubled word {m.group(0)!r}")
    W = words()
    for m in GLUED.finditer(text):
        if m.group(0).lower() not in W: errs.append(f"{label}: glued double word {m.group(0)!r}")
    text = SKIP.sub(" ", text)  # hashtags, @handles, URLs and domains aren't spell-checked
    for m in JAM.finditer(text):
        if m.group(2).lower() not in DOMAIN_TLD: errs.append(f"{label}: text jammed after punctuation {m.group(0)!r}")
    for m in WORD.finditer(text):
        tok = m.group(0).replace("’", "'")
        parts = tok.split("'")
        base = parts[0] if len(parts) == 2 and parts[1].lower() in SUFFIX else tok.replace("'", "")
        if len(parts) == 2 and parts[1].lower() == "t" and base.lower().endswith("n") and base.lower()[:-1] in W:
            continue
        if base.lower() in W or (base.isupper() and len(base) <= 6):
            continue
        if base.lower().rstrip("s") in W:  # simple plurals
            continue
        errs.append(f"{label}: unknown word {tok!r} (typo? if real, add to tools/allow.txt)")
    return errs

def load(path):
    spec = importlib.util.spec_from_file_location("post", path)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m

def slide_texts(m):
    from render import htmls  # same HTML that gets rendered
    _, slides = htmls(m)
    return [visible(h) for h in slides]

# Oct 1-4 posts whose file keeps only the start of the caption that was posted.
LEGACY_STUB_CAPTIONS = {("applied_stoic", n) for n in ("001", "002", "003", "004")} | {("dollartrail", n) for n in ("001", "002", "003", "004")}

def lint(path, write_text=True):
    path = pathlib.Path(path).resolve(); m = load(path)
    num = path.stem.split("-", 1)[0]
    texts = slide_texts(m); cap = getattr(m, "CAPTION", "")
    errs = []
    for i, t in enumerate(texts, 1): errs += check_text(f"slide {i}", t)
    stub = cap.rstrip().endswith("...")
    if stub and (m.ACCOUNT, num) not in LEGACY_STUB_CAPTIONS: errs.append("caption: looks like a placeholder (ends with '...')")
    errs += check_text("caption", unicodedata.normalize("NFC", cap))
    if not getattr(m, "SOURCES", None): errs.append("SOURCES is empty")
    if m.ACCOUNT == "applied_stoic":
        for i, t in enumerate(texts, 1):
            if re.search(r"\bNo\.\s*\d|(?<![\d,.])\b0\d\d\b|#\d{2,}", t): errs.append(f"slide {i}: looks like a post number (not allowed on @applied_stoic)")
    else:
        if "source" not in texts[0].lower(): errs.append("slide 1: no source line on the hook slide")
        if "source" not in texts[-1].lower(): errs.append("last slide: no source line")
        if not stub and "Data:" not in cap: errs.append("caption: no 'Data:' source line")
    if write_text:
        (REPO / "_build").mkdir(exist_ok=True)
        out = REPO / "_build" / f"{m.ACCOUNT}-{num}-text.txt"
        out.write_text("".join(f"--- Slide {i} ---\n{t}\n\n" for i, t in enumerate(texts, 1)) + f"--- Caption ---\n{cap}\n")
    return errs

if __name__ == "__main__":
    bad = 0
    for f in sys.argv[1:]:
        e = lint(f)
        print(("FAIL " if e else "ok   ") + f)
        for x in e: print("     " + x)
        bad += bool(e)
    sys.exit(1 if bad else 0)
