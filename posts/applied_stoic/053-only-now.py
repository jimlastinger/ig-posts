import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "tools"))
from lib import *

ACCOUNT = 'applied_stoic'
THEME = 'bronze'
SOURCES = ['https://classics.mit.edu/Antoninus/meditations.3.three.html']

CAPTION = """Tonight your mind will want to replay today and rehearse tomorrow. Marcus Aurelius reminded himself that the only time anyone lives is this present moment; the rest is either past or uncertain.

Source: Marcus Aurelius, Meditations 3.10, tr. George Long.

#stoicism #marcusaurelius #presentmoment #overthinking #mindset #stoic"""

SLIDES = [
    ('I', '<div class=kick>Applied Stoicism</div><div class=rule></div>\n<div class=hook style="font-size:104px">Replaying today? <em>Dreading tomorrow?</em></div>\n<div class=sub>A Roman emperor on the<br><em>only time you actually have.</em></div>'),
    ('II', "<div class=kick>Who&rsquo;s talking</div><div class=rule></div>\n<h2>An emperor writing to himself.</h2>\n<p>Marcus Aurelius ruled the Roman Empire from AD 161 to 180.</p>\n<p class=strong>His private notebook, the <i>Meditations</i>, was never meant for us. In Book Three he pins down where a life actually happens.</p>"),
    ('III', '<div class=kick>The point</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:66px">&hellip;bear in mind that every man lives only this present time, which is an indivisible point, and that all the rest of his life is either past or it is uncertain.</div>\n<div class=cite>Marcus Aurelius &middot; Meditations 3.10 &middot; tr. George Long</div>'),
    ('IV', '<div class=kick>Your version</div><div class=rule></div>\n<h2>The 11 p.m. spiral.</h2>\n<p>You lie in bed going over what you said in the meeting, then jump ahead to everything that could go wrong next week.</p>\n<p class=strong>One of those is past. The other is uncertain. Neither is the moment you are actually living.</p>'),
    ('V', '<div class=kick>Keep it small</div><div class=rule></div>\n<h2>Hold on to a few things.</h2>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:70px">Throwing away then all things, hold to these only which are few&hellip;</div>\n<div class=cite>Marcus Aurelius &middot; Meditations 3.10 &middot; tr. George Long</div>\n<p class=strong style="margin-top:36px">Drop the replay and the forecast. Keep the few things that matter, here, now.</p>'),
    ('VI', '<div class=kick>Try it tonight</div><div class=rule></div>\n<h2>Come back to the point.</h2>\n<ul class=steps>\n<li><span class=n>1</span><span class=t><b>Catch it:</b> notice when your mind is in the past or the future.</span></li>\n<li><span class=n>2</span><span class=t><b>Label it:</b> say &ldquo;past&rdquo; or &ldquo;uncertain,&rdquo; and set it down.</span></li>\n<li><span class=n>3</span><span class=t><b>Return:</b> ask what this moment needs from you. Often it&rsquo;s just sleep.</span></li>\n</ul>'),
    ('VII', '<div class=kick>Remember</div><div class=rule></div>\n<div class=big style="font-size:96px">Past, or uncertain.<br><em>You live now.</em></div>\n<div class=cta>Send this to someone<br>who <em>can&rsquo;t switch off at night.</em></div>\n' + STOIC_FOLLOW),
]
