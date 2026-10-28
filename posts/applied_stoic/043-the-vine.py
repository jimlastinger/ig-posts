import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "tools"))
from lib import *

ACCOUNT = 'applied_stoic'
THEME = 'parchment'
SOURCES = ['https://classics.mit.edu/Antoninus/meditations.5.five.html']

CAPTION = """Marcus Aurelius described three kinds of people who do a favor: one sends the bill, one keeps a quiet tally, and one is like a vine that makes grapes and moves on to the next season. Tonight, notice which one you were today.

Source: Marcus Aurelius, Meditations 5.6, tr. George Long.

#stoicism #marcusaurelius #kindness #gratitude #mindset #stoic"""

SLIDES = [
    ('I', '<div class=kick>Applied Stoicism</div><div class=rule></div>\n<div class=hook style="font-size:100px">You did them a favor. <em>Are you still keeping score?</em></div>\n<div class=sub>Marcus Aurelius sorted helpers into three kinds.<br><em>Only one is at peace.</em></div>'),
    ('II', "<div class=kick>Who&rsquo;s talking</div><div class=rule></div>\n<h2>An emperor on doing favors.</h2>\n<p>Marcus Aurelius was a Roman emperor.</p>\n<p class=strong>In his private notebook, the <i>Meditations</i>, he wrote about what a good act should ask in return: nothing.</p>"),
    ('III', '<div class=kick>Kinds one and two</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:66px">One man, when he has done a service to another, is ready to set it down to his account as a favour conferred. Another &hellip; in his own mind he thinks of the man as his debtor.</div>\n<div class=cite>Marcus Aurelius &middot; Meditations 5.6 &middot; tr. George Long</div>'),
    ('IV', '<div class=kick>Kind three</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:70px">&hellip;he is like a vine which has produced grapes, and seeks for nothing more after it has once produced its proper fruit.</div>\n<div class=cite>Marcus Aurelius &middot; Meditations 5.6 &middot; tr. George Long</div>'),
    ('V', '<div class=kick>Your version</div><div class=rule></div>\n<h2>The silent invoice.</h2>\n<p>You covered their shift. You drove them to the airport. You never said a word about it.</p>\n<p class=strong>But you remember. And you&rsquo;re waiting. That&rsquo;s the second kind.</p>'),
    ('VI', '<div class=kick>His examples</div><div class=rule></div>\n<h2>A horse runs. A bee makes honey.</h2>\n<p>Marcus says a good person &ldquo;does not call out for others to come and see.&rdquo;</p>\n<p class=strong>He goes on to the next good act, &ldquo;as a vine goes on to produce again the grapes in season.&rdquo;</p>'),
    ('VII', '<div class=kick>Try it tonight</div><div class=rule></div>\n<h2>Close the tab.</h2>\n<ul class=steps>\n<li><span class=n>1</span><span class=t><b>Name one favor</b> you are still waiting to be thanked for.</span></li>\n<li><span class=n>2</span><span class=t><b>Write it down,</b> then cross it out. The debt is cancelled.</span></li>\n<li><span class=n>3</span><span class=t><b>Plan tomorrow&rsquo;s grapes:</b> one small good act, no audience.</span></li>\n</ul>'),
    ('VIII', '<div class=kick>Remember</div><div class=rule></div>\n<div class=big style="font-size:88px">Make the grapes.<br><em>Then make more.</em></div>\n<div class=cta>Send this to someone<br>who <em>helps everyone and never asks.</em></div>\n' + STOIC_FOLLOW),
]
