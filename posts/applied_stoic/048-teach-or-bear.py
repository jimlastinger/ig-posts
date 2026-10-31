import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "tools"))
from lib import *

ACCOUNT = 'applied_stoic'
SOURCES = ['https://classics.mit.edu/Antoninus/meditations.8.eight.html']

CAPTION = """Marcus Aurelius gave himself two options for dealing with people who get it wrong: teach them, or bear with them. Resenting them was not on the list. Next time someone frustrates you this weekend, pick one of the two and let the third go.

Source: Marcus Aurelius, Meditations 8.59, tr. George Long.

#stoicism #marcusaurelius #patience #relationships #mindset #stoic"""

SLIDES = [
    ('I', '<div class=kick>Applied Stoicism</div><div class=rule></div>\n<div class=hook style="font-size:104px">Two options. <em>Not three.</em></div>\n<div class=sub>For the person who keeps getting it wrong.<br><em>From a Roman emperor&rsquo;s notebook.</em></div>'),
    ('II', "<div class=kick>Who&rsquo;s talking</div><div class=rule></div>\n<h2>A ruler surrounded by people.</h2>\n<p>Marcus Aurelius ruled the Roman Empire from AD 161 to 180.</p>\n<p class=strong>In his private notebook, the <i>Meditations</i>, he wrote down how he meant to deal with the people around him.</p>"),
    ('III', '<div class=kick>The line</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:88px">Men exist for the sake of one another. Teach them then or bear with them.</div>\n<div class=cite>Marcus Aurelius &middot; Meditations 8.59 &middot; tr. George Long</div>'),
    ('IV', '<div class=kick>Your version</div><div class=rule></div>\n<h2>The roommate. The coworker. The relative.</h2>\n<p>The dishes in the sink again. The same mistake in the same report. The same argument at the same table.</p>\n<p class=strong>Marcus would ask one thing: can you show them a better way? Then show them. If not, carry it.</p>'),
    ('V', '<div class=kick>The missing option</div><div class=rule></div>\n<h2>Resentment isn&rsquo;t on the list.</h2>\n<p>Teaching changes the situation. Bearing changes you. Stewing changes nothing.</p>\n<p class=strong>&ldquo;For the sake of one another&rdquo; means they are part of your work, not an interruption of it.</p>'),
    ('VI', '<div class=kick>Try it today</div><div class=rule></div>\n<h2>Teach or bear.</h2>\n<ul class=steps>\n<li><span class=n>1</span><span class=t><b>Notice it:</b> the next time someone irritates you, pause.</span></li>\n<li><span class=n>2</span><span class=t><b>Choose:</b> can you calmly show them, once? Then teach.</span></li>\n<li><span class=n>3</span><span class=t><b>If not:</b> bear with it, and drop the replay in your head.</span></li>\n</ul>'),
    ('VII', '<div class=kick>Remember</div><div class=rule></div>\n<div class=big style="font-size:96px">Teach them,<br><em>or bear with them.</em></div>\n<div class=cta>Send this to someone<br>who <em>is patient with you.</em></div>\n' + STOIC_FOLLOW),
]
