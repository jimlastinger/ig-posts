import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "tools"))
from lib import *

ACCOUNT = 'applied_stoic'
SOURCES = ['https://classics.mit.edu/Antoninus/meditations.5.five.html']

CAPTION = """When the plan collapses, Marcus Aurelius says the mind can turn the hindrance into an aid. The blocked road is still road.

Name what's blocked, find what it makes possible, and take the next step it allows.

Source: Marcus Aurelius, Meditations 5.20, tr. George Long.

#stoicism #marcusaurelius #meditations #resilience #mindset #stoic"""

SLIDES = [
    ('I', '<div class=kick>Applied Stoicism</div><div class=rule></div>\n<div class=hook style="font-size:124px">Your plan just fell apart. <em>Now what?</em></div>\n<div class=sub>Marcus Aurelius wrote:<br>the obstacle can <em>move you forward.</em></div>'),
    ('II', "<div class=kick>Who's talking</div><div class=rule></div>\n<h2>An emperor whose plans broke all the time.</h2>\n<p>Marcus Aurelius ruled Rome from AD 161 to 180. His reign brought plague, long wars on the northern frontier, and a general who rebelled against him.</p>\n<p class=strong>His private notebook, the <i>Meditations</i>, keeps coming back to one question: what do you do when things go wrong?</p>"),
    ('III', '<div class=kick>The line</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:76px">The mind converts and changes every hindrance to its activity into an aid&hellip; and that which is an obstacle on the road helps us on this road.</div>\n<div class=cite>Marcus Aurelius &middot; Meditations 5.20 &middot; tr. George Long</div>'),
    ('IV', '<div class=kick>What he means</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:80px">These may impede my action, but they are no impediments to my affects and disposition.</div>\n<div class=cite>Meditations 5.20</div>\n<div class=note>People and events can block what you do. They can\'t block how you respond.</div>'),
    ('V', '<div class=kick>Apply it</div><div class=rule></div>\n<h2>The block becomes the next step.</h2>\n<div class=pair><div class=lab>Flight cancelled</div><div class=val>Two quiet hours to finish the deck.</div>\n<div class=lab>The offer fell through</div><div class=val>Now you know what to fix in the next interview.</div>\n<div class=lab>Rain cancels the run</div><div class=val style="margin-bottom:0">Twenty minutes of push-ups at home.</div></div>'),
    ('VI', '<div class=kick>When the plan collapses</div><div class=rule></div>\n<h2>Three questions, in order:</h2>\n<ul class=steps>\n<li><span class=n>1</span><span class=t><b>What exactly is blocked?</b> Write it in one sentence.</span></li>\n<li><span class=n>2</span><span class=t><b>What does this make possible?</b> Or what does it train: patience, honesty, a better plan?</span></li>\n<li><span class=n>3</span><span class=t><b>What\'s the next step the obstacle allows?</b> Take it today.</span></li>\n</ul>'),
    ('VII', '<div class=kick>Remember</div><div class=rule></div>\n<div class=big>The block in the road is still road.<br><em>Walk on it.</em></div>\n<div class=cta>Send this to someone<br>whose <em>plan just fell apart.</em></div>\n' + STOIC_FOLLOW),
]
