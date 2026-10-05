import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "tools"))
from lib import *

ACCOUNT = 'applied_stoic'
SOURCES = ['https://classics.mit.edu/Antoninus/meditations.5.five.html']

CAPTION = """Book 5 of the Meditations opens with an emperor arguing with his own bed. His answer: you're rising to do the work of a human being.

Decide tonight what that work is, and the alarm is easier to answer.

Source: Marcus Aurelius, Meditations 5.1, tr. George Long.

#stoicism #marcusaurelius #morningroutine #discipline #mindset #stoic"""

SLIDES = [
    ('I', '<div class=kick>Applied Stoicism</div><div class=rule></div>\n<div class=hook style="font-size:124px">Tomorrow\'s alarm is coming. <em>Decide tonight.</em></div>\n<div class=sub>Marcus Aurelius had to<br><em>argue with his bed,</em> too.</div>'),
    ('II', "<div class=kick>Who's talking</div><div class=rule></div>\n<h2>Even an emperor didn't want to get up.</h2>\n<p>Marcus Aurelius ruled the Roman Empire. He wrote the <i>Meditations</i> as private notes to himself.</p>\n<p class=strong>Book 5 opens with him talking himself out of bed.</p>"),
    ('III', '<div class=kick>His morning line</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:84px">In the morning when thou risest unwillingly, let this thought be present&mdash;I am rising to the work of a human being.</div>\n<div class=cite>Marcus Aurelius &middot; Meditations 5.1 &middot; tr. George Long</div>'),
    ('IV', '<div class=kick>The argument</div><div class=rule></div>\n<div class=q style="font-size:66px">&ldquo;Or have I been made for this, to lie in the bed-clothes and keep myself warm?&rdquo;</div>\n<div class=q style="font-size:66px;margin-top:34px">&ldquo;But this is more pleasant.&mdash; Dost thou exist then to take thy pleasure, and not at all for action or exertion?&rdquo;</div>\n<div class=cite>Meditations 5.1</div>\n<div class=note>He is arguing with himself, the same way you do at 6:45.</div>'),
    ('V', '<div class=kick>He wasn\'t against sleep</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:80px">But it is necessary to take rest also.&mdash; It is necessary: however nature has fixed bounds to this too&hellip;</div>\n<div class=cite>Meditations 5.1</div>\n<div class=note>Rest has a limit. Past it, staying in bed is just avoiding the day.</div>'),
    ('VI', '<div class=kick>Tonight, before bed</div><div class=rule></div>\n<h2>Win the argument in advance.</h2>\n<ul class=steps>\n<li><span class=n>1</span><span class=t><b>Write tomorrow\'s first task.</b> That\'s the work you\'re rising to.</span></li>\n<li><span class=n>2</span><span class=t><b>Put the alarm across the room.</b> Make the bed harder to negotiate with.</span></li>\n<li><span class=n>3</span><span class=t><b>When it rings,</b> say his line and put your feet on the floor.</span></li>\n</ul>'),
    ('VII', '<div class=kick>Remember</div><div class=rule></div>\n<div class=big style="font-size:84px">You aren\'t getting up to suffer.<br><em>You\'re getting up to work.</em></div>\n<div class=cta>Send this to the friend<br>who hits <em>snooze five times.</em></div>\n' + STOIC_FOLLOW),
]
