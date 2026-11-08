import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "tools"))
from lib import *

ACCOUNT = 'applied_stoic'
THEME = 'parchment'
SOURCES = ['https://classics.mit.edu/Antoninus/meditations.mb.txt']

CAPTION = """A bad review, and you replay one line of it all weekend. Marcus Aurelius split it in two: what they think of you is their business. Whether you earned it is yours.

Source: Marcus Aurelius, Meditations 11.13, tr. George Long.

#stoicism #marcusaurelius #criticism #work #mindset #stoic"""

SLIDES = [
    ('I', '<div class=kick>Applied Stoicism</div><div class=rule></div>\n<div class=hook style="font-size:104px">Bad review on Friday. <em>Still replaying it Sunday.</em></div>\n<div class=sub>There are two questions in it.<br><em>Only one of them is yours.</em></div>'),
    ('II', "<div class=kick>Who&rsquo;s talking</div><div class=rule></div>\n<h2>An emperor talking to himself.</h2>\n<p>Marcus Aurelius ruled the Roman Empire from AD 161 to 180.</p>\n<p class=strong>In his private notebook, the <i>Meditations</i>, he wrote down what to do when someone thinks little of you.</p>"),
    ('III', '<div class=kick>The rule</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:70px">Suppose any man shall despise me. Let him look to that himself. But I will look to this, that I be not discovered doing or saying anything deserving of contempt.</div>\n<div class=cite>Marcus Aurelius &middot; Meditations 11.13 &middot; tr. George Long</div>'),
    ('IV', '<div class=kick>Your version</div><div class=rule></div>\n<h2>&ldquo;Needs improvement.&rdquo;</h2>\n<p>Two questions are tangled together. What does my manager think of me? And is the feedback true?</p>\n<p class=strong>The first one lives in their head, so you can&rsquo;t fix it from yours. The second is the only part you can work on.</p>'),
    ('V', '<div class=kick>When it&rsquo;s unfair</div><div class=rule></div>\n<h2>Some of it won&rsquo;t be true.</h2>\n<p>Marcus covers that too. In the same passage he says to stay mild with that person, and be ready to show them their mistake, without scolding or showing off.</p>\n<p class=strong>So if the criticism misses, say so calmly, once. Then get back to work.</p>'),
    ('VI', '<div class=kick>Try it today</div><div class=rule></div>\n<h2>Split the review in two.</h2>\n<ul class=steps>\n<li><span class=n>1</span><span class=t><b>Write</b> down each criticism in one plain line.</span></li>\n<li><span class=n>2</span><span class=t><b>Mark</b> each one: true, partly true, or not true.</span></li>\n<li><span class=n>3</span><span class=t><b>Pick</b> the true line that matters most and start on it this week. Let the untrue ones go.</span></li>\n</ul>'),
    ('VII', '<div class=kick>Remember</div><div class=rule></div>\n<div class=big style="font-size:92px">Their opinion is theirs.<br><em>Your work is yours.</em></div>\n<div class=cta>Send this to someone<br>who&rsquo;s <em>replaying a review.</em></div>\n' + STOIC_FOLLOW),
]
