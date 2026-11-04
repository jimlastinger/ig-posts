import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "tools"))
from lib import *

ACCOUNT = 'applied_stoic'
THEME = 'bronze'
SOURCES = ['https://classics.mit.edu/Antoninus/meditations.mb.txt']

CAPTION = """Marcus Aurelius had a simple test for any deal, shortcut or secret: if it needs walls and curtains, it isn't worth what it costs you. Would you still do it with the curtains open?

Source: Marcus Aurelius, Meditations 3.7, tr. George Long.

#stoicism #marcusaurelius #integrity #character #mindset #stoic"""

SLIDES = [
    ('I', '<div class=kick>Applied Stoicism</div><div class=rule></div>\n<div class=hook style="font-size:104px">Would you do it <em>with the curtains open?</em></div>\n<div class=sub>An emperor&rsquo;s test<br><em>for anything you&rsquo;d hide.</em></div>'),
    ('II', "<div class=kick>Who&rsquo;s talking</div><div class=rule></div>\n<h2>An emperor writing to himself.</h2>\n<p>Marcus Aurelius ruled the Roman Empire from AD 161 to 180.</p>\n<p class=strong>In his private notebook, the <i>Meditations</i>, he wrote down what was never worth the price.</p>"),
    ('III', '<div class=kick>The test</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:58px">Never value anything as profitable to thyself which shall compel thee to break thy promise, to lose thy self-respect, to hate any man, to suspect, to curse, to act the hypocrite, to desire anything which needs walls and curtains&hellip;</div>\n<div class=cite>Marcus Aurelius &middot; Meditations 3.7 &middot; tr. George Long</div>'),
    ('IV', '<div class=kick>Your version</div><div class=rule></div>\n<h2>The &ldquo;great opportunity.&rdquo;</h2>\n<p>A side deal your boss can&rsquo;t know about. A purchase you&rsquo;d hide from your partner. A message you&rsquo;d delete before anyone saw it.</p>\n<p class=strong>If it only works behind closed doors, by Marcus&rsquo;s test it isn&rsquo;t profit. It&rsquo;s a cost you haven&rsquo;t paid yet.</p>'),
    ('V', '<div class=kick>Read the price tag</div><div class=rule></div>\n<h2>What it might cost you.</h2>\n<ul class=steps>\n<li><span class=n>1</span><span class=t><b>A promise</b> you have to break.</span></li>\n<li><span class=n>2</span><span class=t><b>Your self-respect</b>, the morning after.</span></li>\n<li><span class=n>3</span><span class=t><b>A mask</b>: acting one way in public, another in private.</span></li>\n</ul>\n<p class=strong style="margin-top:36px">Gain on one side, those losses on the other. Do the math honestly.</p>'),
    ('VI', '<div class=kick>Try it today</div><div class=rule></div>\n<h2>The curtain check.</h2>\n<ul class=steps>\n<li><span class=n>1</span><span class=t><b>Before you say yes</b> to anything, picture it on a screen in a crowded room.</span></li>\n<li><span class=n>2</span><span class=t><b>Ask:</b> would I need to hide this, or explain it away?</span></li>\n<li><span class=n>3</span><span class=t><b>If yes</b>, it needs walls and curtains. Walk away.</span></li>\n</ul>'),
    ('VII', '<div class=kick>Remember</div><div class=rule></div>\n<div class=big style="font-size:96px">If it needs walls and curtains,<br><em>it costs too much.</em></div>\n<div class=cta>Send this to someone<br>who <em>lives with the curtains open.</em></div>\n' + STOIC_FOLLOW),
]
