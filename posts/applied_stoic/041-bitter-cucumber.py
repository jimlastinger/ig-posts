import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "tools"))
from lib import *

ACCOUNT = 'applied_stoic'
THEME = 'bronze'
SOURCES = ['https://classics.mit.edu/Antoninus/meditations.8.eight.html']

CAPTION = """A bitter cucumber? Throw it away. Briars on the road? Walk around them. Marcus Aurelius says that is enough, and warns against adding "And why were such things made in the world?" Tomorrow, handle the annoyance and skip the speech.

Source: Marcus Aurelius, Meditations 8.50, tr. George Long.

#stoicism #marcusaurelius #letitgo #mindset #resilience #stoic"""

SLIDES = [
    ('I', '<div class=kick>Applied Stoicism</div><div class=rule></div>\n<div class=hook style="font-size:104px">Flight delayed. <em>Then the real damage starts.</em></div>\n<div class=sub>The complaining, the retelling, the &ldquo;why me?&rdquo;<br><em>Marcus had a shorter answer.</em></div>'),
    ('II', "<div class=kick>Who&rsquo;s talking</div><div class=rule></div>\n<h2>An emperor with plenty to complain about.</h2>\n<p>Marcus Aurelius ruled the Roman Empire from AD 161 to 180.</p>\n<p class=strong>In his private notebook, the <i>Meditations</i>, he wrote this short reminder to himself.</p>"),
    ('III', '<div class=kick>The line</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:76px">A cucumber is bitter. &mdash; Throw it away. &mdash; There are briars in the road. &mdash; Turn aside from them. &mdash; This is enough.</div>\n<div class=cite>Marcus Aurelius &middot; Meditations 8.50 &middot; tr. George Long</div>'),
    ('IV', '<div class=kick>The part we skip</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:76px">Do not add, And why were such things made in the world?</div>\n<div class=cite>Marcus Aurelius &middot; Meditations 8.50 &middot; tr. George Long</div>'),
    ('V', '<div class=kick>Your version</div><div class=rule></div>\n<h2>The problem takes a minute. The speech takes all day.</h2>\n<p>The delay is the cucumber. Booking the next flight is turning aside.</p>\n<p class=strong>The rant to everyone at the gate, and again at dinner, is the part you added.</p>'),
    ('VI', '<div class=kick>His comparison</div><div class=rule></div>\n<h2>Nobody blames the carpenter for sawdust.</h2>\n<p>Marcus says a carpenter or a shoemaker would laugh at you for complaining about the shavings in their workshop.</p>\n<p class=strong>Scraps come with the work. Annoyances come with a life.</p>'),
    ('VII', '<div class=kick>Try it tomorrow</div><div class=rule></div>\n<h2>Handle it. Then stop.</h2>\n<ul class=steps>\n<li><span class=n>1</span><span class=t><b>Name the cucumber:</b> what exactly went wrong?</span></li>\n<li><span class=n>2</span><span class=t><b>Take one action:</b> throw it away or turn aside.</span></li>\n<li><span class=n>3</span><span class=t><b>Skip the &ldquo;why&rdquo;</b> speech. Notice how much of the day you get back.</span></li>\n</ul>'),
    ('VIII', '<div class=kick>Remember</div><div class=rule></div>\n<div class=big style="font-size:90px">Throw it away. Turn aside.<br><em>This is enough.</em></div>\n<div class=cta>Send this to someone<br>who <em>is still mad about Monday.</em></div>\n' + STOIC_FOLLOW),
]
