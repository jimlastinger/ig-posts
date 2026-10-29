import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "tools"))
from lib import *

ACCOUNT = 'applied_stoic'
THEME = 'bronze'
SOURCES = ['https://classics.mit.edu/Antoninus/meditations.7.seven.html']

CAPTION = """Marcus Aurelius said the art of life is more like wrestling than dancing: it has to stand ready and firm for onsets that are sudden and unexpected. Today, when the plan gets knocked over, plant your feet before you react.

Source: Marcus Aurelius, Meditations 7.61, tr. George Long.

#stoicism #marcusaurelius #resilience #mindset #discipline #stoic"""

SLIDES = [
    ('I', '<div class=kick>Applied Stoicism</div><div class=rule></div>\n<div class=hook style="font-size:104px">You planned the day like a dance. <em>Then it hit you.</em></div>\n<div class=sub>The 9 a.m. email. The sick kid. The flat tire.<br><em>Marcus had a better picture of life.</em></div>'),
    ('II', "<div class=kick>Who&rsquo;s talking</div><div class=rule></div>\n<h2>An emperor who rarely got the day he planned.</h2>\n<p>Marcus Aurelius ruled the Roman Empire from AD 161 to 180.</p>\n<p class=strong>In his private notebook, the <i>Meditations</i>, he compared living well to two very different arts.</p>"),
    ('III', '<div class=kick>The line</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:70px">The art of life is more like the wrestler&rsquo;s art than the dancer&rsquo;s, in respect of this, that it should stand ready and firm to meet onsets which are sudden and unexpected.</div>\n<div class=cite>Marcus Aurelius &middot; Meditations 7.61 &middot; tr. George Long</div>'),
    ('IV', '<div class=kick>The difference</div><div class=rule></div>\n<h2>A dancer knows the next step. A wrestler doesn&rsquo;t.</h2>\n<p>A dance is rehearsed. Every move is planned.</p>\n<p class=strong>A wrestler expects to be grabbed. The skill is staying on your feet when it happens.</p>'),
    ('V', '<div class=kick>Your version</div><div class=rule></div>\n<h2>The morning that goes sideways.</h2>\n<p>You had the day mapped out. Then a client cancels, a pipe leaks, or the school calls.</p>\n<p class=strong>If you only know the dance, you freeze or flail. A wrestler expected the grab and is already working.</p>'),
    ('VI', '<div class=kick>Try it today</div><div class=rule></div>\n<h2>Stand ready.</h2>\n<ul class=steps>\n<li><span class=n>1</span><span class=t><b>Expect one grab:</b> name one thing likely to go wrong before it does.</span></li>\n<li><span class=n>2</span><span class=t><b>Plant your feet:</b> when it hits, take one breath before you answer.</span></li>\n<li><span class=n>3</span><span class=t><b>Make the next move:</b> pick one action, not a complaint.</span></li>\n</ul>'),
    ('VII', '<div class=kick>Remember</div><div class=rule></div>\n<div class=big style="font-size:92px">Don&rsquo;t rehearse a dance.<br><em>Train to wrestle.</em></div>\n<div class=cta>Send this to someone<br>whose <em>week just went sideways.</em></div>\n' + STOIC_FOLLOW),
]
