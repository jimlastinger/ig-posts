import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "tools"))
from lib import *

ACCOUNT = 'applied_stoic'
THEME = 'parchment'
SOURCES = ['https://classics.mit.edu/Antoninus/meditations.4.four.html']

CAPTION = """Marcus Aurelius wanted the country house and the seashore too. Then he reminded himself that the quietest retreat is into your own mind, and you can go there whenever you choose.

Today, take five minutes for it. No booking required.

Source: Marcus Aurelius, Meditations 4.3, tr. George Long (MIT Internet Classics Archive).

#stoicism #marcusaurelius #meditations #mindfulness #calm #stoic"""

SLIDES = [
    ('I', '<div class=kick>Applied Stoicism</div><div class=rule></div>\n<div class=hook style="font-size:118px">You don&rsquo;t need a vacation. <em>You need five minutes.</em></div>\n<div class=sub>Marcus had a retreat<br><em>that goes where you go.</em></div>'),
    ('II', "<div class=kick>Who&rsquo;s talking</div><div class=rule></div>\n<h2>Marcus Aurelius, the emperor.</h2>\n<p>He ruled Rome and wrote the <i>Meditations</i> as private notes to himself.</p>\n<p class=strong>In Book 4, he takes on a wish we all know: to get away from it all.</p>"),
    ('III', '<div class=kick>The wish</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:84px">Men seek retreats for themselves, houses in the country, sea-shores, and mountains; and thou too art wont to desire such things very much.</div>\n<div class=cite>Marcus Aurelius &middot; Meditations 4.3 &middot; tr. George Long</div>\n<div class=note>The emperor wanted the beach house too.</div>'),
    ('IV', '<div class=kick>His answer</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:80px">&hellip; it is in thy power whenever thou shalt choose to retire into thyself. For nowhere either with more quiet or more freedom from trouble does a man retire than into his own soul &hellip;</div>\n<div class=cite>Marcus Aurelius &middot; Meditations 4.3 &middot; tr. George Long</div>'),
    ('V', '<div class=kick>What calm is</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:84px">&hellip; I affirm that tranquility is nothing else than the good ordering of the mind. Constantly then give to thyself this retreat, and renew thyself &hellip;</div>\n<div class=cite>Marcus Aurelius &middot; Meditations 4.3 &middot; tr. George Long</div>\n<div class=note>Calm isn&rsquo;t a place. It&rsquo;s a mind in order.</div>'),
    ('VI', '<div class=kick>Your version</div><div class=rule></div>\n<h2>The trip is in March.<br>The stress is today.</h2>\n<p>We save rest for the vacation and push through everything until then.</p>\n<p class=strong>Marcus&rsquo;s retreat needs no booking. You can take it between meetings, and he says to take it often.</p>'),
    ('VII', '<div class=kick>Try it today</div><div class=rule></div>\n<h2>A five-minute retreat.</h2>\n<ul class=steps>\n<li><span class=n>1</span><span class=t><b>Step away.</b> Close the door, or just close your eyes.</span></li>\n<li><span class=n>2</span><span class=t><b>Sort your thoughts.</b> Name what&rsquo;s bothering you, one thing at a time.</span></li>\n<li><span class=n>3</span><span class=t><b>Come back renewed.</b> Repeat tomorrow.</span></li>\n</ul>'),
    ('VIII', '<div class=kick>Remember</div><div class=rule></div>\n<div class=big style="font-size:84px">No beach required.<br><em>Just a few minutes with your own mind.</em></div>\n<div class=cta>Send this to someone<br>who <em>needs a vacation.</em></div>\n' + STOIC_FOLLOW),
]
