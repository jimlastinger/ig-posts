"""Archived example post. Slides are pre-rendered HTML strings; new posts should use the helpers in tools/lib.py."""
import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "tools"))
from lib import *

ACCOUNT = 'applied_stoic'
SOURCES = ['https://classics.mit.edu/Antoninus/meditations.2.two.html']

CAPTION = 'Marcus Aurelius started his mornings by expecting difficult people. ...'

SLIDES = [
    ('I', '<div class=kick>Applied Stoicism</div><div class=rule></div>\n<div class=hook style="font-size:130px">Someone will be difficult today.</div>\n<div class=sub>Marcus Aurelius<br><em>planned for it</em> every morning.</div>'),
    ('II', "<div class=kick>Who's talking</div><div class=rule></div>\n<h2>The most powerful man in the world did this before breakfast.</h2>\n<p>Marcus Aurelius ruled the Roman Empire from AD 161 to 180. His notebook, the <i>Meditations</i>, was written for himself, not for readers.</p>\n<p class=strong>Book 2 opens with a morning exercise.</p>"),
    ('III', '<div class=kick>The exercise</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:92px">Begin the morning by saying to thyself, I shall meet with the busy-body, the ungrateful, arrogant, deceitful, envious, unsocial.</div>\n<div class=cite>Marcus Aurelius &middot; Meditations 2.1 &middot; tr. George Long</div>'),
    ('IV', '<div class=kick>Translate it to your Tuesday</div><div class=rule></div>\n<h2>Today you may meet:</h2>\n<ul class=steps style="margin-top:10px">\n<li><span class=n>&middot;</span><span class=t><b>The coworker</b> who takes credit</span></li>\n<li><span class=n>&middot;</span><span class=t><b>The customer</b> who\'s rude to you</span></li>\n<li><span class=n>&middot;</span><span class=t><b>The driver</b> who cuts you off</span></li>\n<li><span class=n>&middot;</span><span class=t><b>The relative</b> with an opinion on everything</span></li>\n</ul>\n<p class=strong>Name them first, and none of them can surprise you.</p>'),
    ('V', '<div class=kick>Why he didn\'t hate them</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:84px">Nor can I be angry with my kinsman, nor hate him. For we are made for co-operation, like feet, like hands, like eyelids&hellip;</div>\n<div class=cite>Meditations 2.1</div>\n<div class=note>Difficult people are still on your team. You need them anyway.</div>'),
    ('VI', '<div class=kick>Do this tomorrow morning</div><div class=rule></div>\n<h2>Sixty seconds, before your phone.</h2>\n<ul class=steps>\n<li><span class=n>1</span><span class=t><b>Name one person</b> likely to test you today.</span></li>\n<li><span class=n>2</span><span class=t><b>Decide your response now:</b> calm, brief, fair.</span></li>\n<li><span class=n>3</span><span class=t><b>When it happens,</b> notice it: you saw this coming.</span></li>\n</ul>'),
    ('VII', '<div class=kick>Remember</div><div class=rule></div>\n<div class=big>You can\'t choose who shows up.<br><em>You can be ready.</em></div>\n<div class=cta>Send this to someone<br>with a <em>hard day</em> ahead.</div>\n<p style="margin-top:40px;font-size:44px;color:#a99f8c">Follow @applied_stoic: one ancient idea, applied to real life, every day.</p>'),
]
