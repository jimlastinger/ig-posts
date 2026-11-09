"""Add a portrait to the @applied_stoic library (run once per image, in a session that can reach the image host).

  python tools/portraits/add.py <downloaded image> <name> "<who>" "<license>" "<author>" "<source page URL>"

Cuts the subject out of its background with rembg (pip install rembg onnxruntime --break-system-packages),
saves tools/portraits/<name>.png with transparency, and appends a line to CREDITS.md. Daily runs only read the PNG.
Only public-domain / CC0 images, or CC BY / BY-SA with the credit line added to the caption. Never AI-made faces.
"""
import sys, pathlib
from PIL import Image
from rembg import remove, new_session

src, name, who, lic, author, url = sys.argv[1:7]
here = pathlib.Path(__file__).resolve().parent
im = Image.open(src).convert("RGB")
if max(im.size) > 2000:
    im.thumbnail((2000, 2000), Image.LANCZOS)
out = remove(im, session=new_session("u2net"))
bbox = out.getchannel("A").point(lambda v: 255 if v > 24 else 0).getbbox()
if bbox:
    out = out.crop(bbox)
out.save(here / f"{name}.png", optimize=True)
with open(here / "CREDITS.md", "a") as f:
    f.write(f"| {name} | {who} | {lic} | {author} | {url} |\n")
print(f"saved tools/portraits/{name}.png {out.size}")
