"""Render a post file to Instagram-ready JPEGs (+ a preview sheet), optionally a silent Reel.

usage: python tools/render.py posts/<account>/<NNN>-<slug>.py [--reel]
Writes:  <account>/<NNN>/<slug>_01.jpg ...   (the hosted slides; commit + push these)
         _build/<account>-<NNN>-preview.png   (contact sheet, for checking; not committed)
         _build/<account>-<NNN>-reel.mp4      (with --reel: silent 9:16 video, no swipe/page footer)
"""
import sys, pathlib, importlib.util, subprocess, os
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from lib import FONT_CSS, STOIC_CSS, MONEY_CSS, stoic, money
from playwright.sync_api import sync_playwright
from PIL import Image

REPO = pathlib.Path(__file__).resolve().parent.parent
BUILD = REPO / "_build"; BUILD.mkdir(exist_ok=True)
HIDE_FOOT = ".foot span:nth-child(2),.foot .sw{visibility:hidden}"

def load(path):
    spec = importlib.util.spec_from_file_location("post", path)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m

def htmls(m):
    n = len(m.SLIDES)
    if m.ACCOUNT == "applied_stoic":
        return STOIC_CSS, [stoic(i + 1, n, b, num) for i, (num, b) in enumerate(m.SLIDES)]
    return MONEY_CSS, [money(m.TRAIL, m.FOLLOWING, i + 1, n, b) for i, b in enumerate(m.SLIDES)]

def shoot(css, slides, prefix):
    out = []
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page(viewport={"width": 1080, "height": 1350})
        for k, h in enumerate(slides, 1):
            pg.set_content(f"<!doctype html><html><head><meta charset=utf-8><style>{FONT_CSS}{css}</style></head><body>{h}</body></html>")
            pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(150)
            f = f"{prefix}_{k:02d}.png"; pg.screenshot(path=f); out.append(f)
        b.close()
    return out

def main():
    post = pathlib.Path(sys.argv[1]).resolve(); m = load(post)
    num, slug = post.stem.split("-", 1)
    assert 2 <= len(m.SLIDES) <= 10, "Instagram API carousels need 2-10 slides"
    css, slides = htmls(m)
    tmp = BUILD / f"{m.ACCOUNT}-{num}"; tmp.mkdir(exist_ok=True)
    pngs = shoot(css, slides, str(tmp / slug))
    dest = REPO / m.ACCOUNT / num; dest.mkdir(parents=True, exist_ok=True)
    for f in pngs:
        Image.open(f).convert("RGB").save(dest / (pathlib.Path(f).stem + ".jpg"), quality=92, optimize=True)
    w, h, cols = 300, 375, 5; rows = (len(pngs) + cols - 1) // cols
    sheet = Image.new("RGB", (cols * w + (cols + 1) * 10, rows * h + (rows + 1) * 10), (30, 30, 30))
    for i, f in enumerate(pngs):
        sheet.paste(Image.open(f).convert("RGB").resize((w, h), Image.LANCZOS), (10 + (i % cols) * (w + 10), 10 + (i // cols) * (h + 10)))
    prev = BUILD / f"{m.ACCOUNT}-{num}-preview.png"; sheet.save(prev)
    print("slides:", dest); print("preview:", prev)
    if "--reel" in sys.argv:
        rp = shoot(css + HIDE_FOOT, slides, str(tmp / ("reel_" + slug)))
        bg = "#0c0b09" if m.ACCOUNT == "applied_stoic" else "#101214"
        d = [3.0] + [4.5] * (len(rp) - 1)
        clips = []
        for i, (s, t) in enumerate(zip(rp, d)):
            c = str(tmp / f"c{i:02d}.mp4"); fr = int(t * 30)
            vf = (f"scale=1080:1350,zoompan=z='1+0.035*on/{fr}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={fr}:s=1080x1350:fps=30,"
                  f"pad=1080:1920:0:285:color={bg},format=yuv420p")
            subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-loop", "1", "-i", s, "-vf", vf, "-t", str(t), "-r", "30", "-c:v", "libx264", "-crf", "20", c], check=True)
            clips.append(c)
        xf, fc, last, off = 0.35, [], "[0:v]", 0.0
        for i in range(1, len(clips)):
            off += d[i - 1] - xf; fc.append(f"{last}[{i}:v]xfade=transition=fade:duration={xf}:offset={off:.3f}[v{i}]"); last = f"[v{i}]"
        out = str(BUILD / f"{m.ACCOUNT}-{num}-reel.mp4")
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", *sum([["-i", c] for c in clips], []), "-filter_complex", ";".join(fc),
                        "-map", last, "-an", "-c:v", "libx264", "-crf", "21", "-pix_fmt", "yuv420p", "-movflags", "+faststart", out], check=True)
        print("reel:", out)

if __name__ == "__main__":
    main()
