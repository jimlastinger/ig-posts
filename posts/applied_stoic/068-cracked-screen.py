import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "tools"))
from lib import *

ACCOUNT = 'applied_stoic'
THEME = 'journal'
SOURCES = ['https://gutenberg.org/files/10661/10661-h/10661-h.htm']

CAPTION = """Your phone slips out of your hand and lands face down. Epictetus told his students to say plainly what a thing is while they still have it: a jug is a jug, so a broken one is no surprise. A phone is glass. Say so now, and the crack costs you less of your day.

Source: Epictetus, Encheiridion 3, tr. George Long.

#stoicism #epictetus #letgo #mindset #dailystoic #stoic"""

SLIDES = [
    ('I', '<div class=kick>Applied Stoicism</div><div class=rule></div>\n<div class=hook>Your phone hits the floor. <em>Face down.</em></div>\n<div class=sub>You turn it over slowly.<br><em>Cracked.</em></div>'),
    ('II', "<div class=kick>Who&rsquo;s talking</div><div class=rule></div>\n<h2>Epictetus, the former slave.</h2>\n<p>He was born a slave, won his freedom and became a teacher. His student Arrian wrote his lessons down, including a short handbook called the <i>Encheiridion</i>.</p>\n<p class=strong>Chapter 3 starts with a clay jug.</p>"),
    ('III', '<div class=kick>The jug</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:84px">If you love an earthen vessel, say it is an earthen vessel which you love; for when it has been broken you will not be disturbed.</div>\n<div class=cite>Epictetus &middot; Encheiridion 3 &middot; tr. George Long</div>\n<div class=note>An earthen vessel is a clay pot or jug.</div>'),
    ('IV', '<div class=kick>Your version</div><div class=rule></div>\n<h2>Say what it is.</h2>\n<p>A phone is a slab of glass you carry everywhere. Your favorite mug is fired clay, like his jug.</p>\n<p class=strong>If you say that while it&rsquo;s still in one piece, the crack is just news. It doesn&rsquo;t feel like betrayal.</p>'),
    ('V', '<div class=kick>He goes further</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:76px">If you are kissing your child or wife, say that it is a human being whom you are kissing, for when the wife or child dies you will not be disturbed.</div>\n<div class=cite>Epictetus &middot; Encheiridion 3 &middot; tr. George Long</div>\n<div class=note>Hard to read. He&rsquo;s saying the people you love are mortal, so you don&rsquo;t mistake them for permanent.</div>'),
    ('VI', '<div class=kick>Try it today</div><div class=rule></div>\n<h2>Before it breaks.</h2>\n<ul class=steps>\n<li><span class=n>1</span><span class=t><b>Pick</b> one thing you&rsquo;d hate to lose: your phone, or your favorite mug.</span></li>\n<li><span class=n>2</span><span class=t><b>Say</b> what it is, out loud. &ldquo;This is glass.&rdquo; &ldquo;This is clay.&rdquo;</span></li>\n<li><span class=n>3</span><span class=t><b>When</b> it breaks, repeat it. Then fix it or replace it, and get on with the day.</span></li>\n</ul>'),
    ('VII', '<div class=kick>Remember</div><div class=rule></div>\n<div class=big style="font-size:84px">A jug is a jug.<br>Glass is glass.<br><em>Say it first.</em></div>\n<div class=cta>Send this to someone<br>who <em>just cracked their screen.</em></div>\n' + STOIC_FOLLOW),
]
