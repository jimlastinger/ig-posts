"""Archived example post. Slides are pre-rendered HTML strings; new posts should use the helpers in tools/lib.py."""
import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "tools"))
from lib import *

ACCOUNT = 'applied_stoic'
SOURCES = ['https://archive.org/details/moralessayswithe01seneuoft']

CAPTION = "Seneca's advice for the text you're about to send: wait. ..."

SLIDES = [
    ('I', '<div class=kick>Applied Stoicism</div><div class=rule></div>\n<div class=hook style="font-size:126px">You\'re about to send the angry text.</div>\n<div class=sub>Seneca wrote three books<br><em>for this exact moment.</em></div>'),
    ('II', "<div class=kick>Who's talking</div><div class=rule></div>\n<h2>Seneca spent his life close to dangerous tempers.</h2>\n<p>He lived at the center of Roman power and later served as an advisor to Nero, one of Rome's most volatile emperors.</p>\n<p>He also wrote <i>On Anger</i>: three books on how rage takes over a mind, and how to stop it before it acts.</p>"),
    ('III', '<div class=kick>His main remedy</div>\n<span class=qm>&ldquo;</span>\n<div class=q>The greatest corrective of anger lies in delay.</div>\n<div class=cite>Seneca &middot; On Anger II.29 &middot; tr. John W. Basore</div>\n<div class=note>Not bottling it up. Not letting it rip. Just waiting.</div>'),
    ('IV', '<div class=kick>Why waiting works</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:88px">The best cure for anger is waiting, to allow the first ardour to abate.</div>\n<div class=cite>Seneca &middot; On Anger III.12</div>\n<div class=pair><div class=lab>The text you write at 9 p.m.</div><div class=val>Is not the one</div>\n<div class=lab>you\'d send at 9 a.m.</div><div class=val style="margin-bottom:0">Wait for 9 a.m.</div></div>'),
    ('V', '<div class=kick>A story Seneca tells</div><div class=rule></div>\n<h2>Plato caught himself mid-swing.</h2>\n<p>Angry at a slave, Plato raised his hand to strike, then froze and held it there. A friend asked what he was doing.</p>\n<div class=q style="font-size:76px;margin-top:10px">&ldquo;I am exacting punishment from an angry man.&rdquo;</div>\n<p style="margin-top:30px">He was punishing himself, for being angry.</p>'),
    ('VI', "<div class=kick>The ten-minute rule</div><div class=rule></div>\n<h2>Before you hit send:</h2>\n<ul class=steps>\n<li><span class=n>1</span><span class=t><b>Write it. Don't send it.</b> Get it out of your head and onto the screen.</span></li>\n<li><span class=n>2</span><span class=t><b>Wait ten minutes.</b> Then reread it. Is this judgment, or anger?</span></li>\n<li><span class=n>3</span><span class=t><b>If it still needs saying,</b> say it in half the words.</span></li>\n</ul>"),
    ('VII', '<div class=kick>Remember</div><div class=rule></div>\n<div class=big>Anger wants it now.<br><em>Wisdom can wait.</em></div>\n<div class=cta>Send this to the friend<br>who replies <em>too fast.</em></div>\n<p style="margin-top:40px;font-size:44px;color:#a99f8c">Follow @applied_stoic: one ancient idea, applied to real life, every day.</p>'),
]
