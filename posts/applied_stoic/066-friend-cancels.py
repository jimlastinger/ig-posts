import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "tools"))
from lib import *

ACCOUNT = 'applied_stoic'
THEME = 'marble'
SOURCES = ['https://classics.mit.edu/Antoninus/meditations.mb.txt']

CAPTION = """He cancels again at the last minute, and you start drafting the speech you'll give him. Marcus Aurelius had a short test for moments like this: fix the cause if you can, fix the night if you can't, and skip the blaming either way.

Bust photo: Pierre-Selim, CC BY-SA 3.0 (cropped and toned).
Source: Marcus Aurelius, Meditations 8.17 and 7.27, tr. George Long.

#stoicism #marcusaurelius #friendship #flakyfriends #mindset #stoic"""

SLIDES = [
    ('I', '<div class=kick>Applied Stoicism</div><div class=rule></div>\n<div class=hook>&ldquo;Hey, so sorry, can we do another night?&rdquo; <em>Third time.</em></div>\n<div class=sub>You&rsquo;re already dressed.<br><em>Now what?</em></div>' + portrait('marcus-1')),
    ('II', "<div class=kick>Who&rsquo;s talking</div><div class=rule></div>\n<h2>Marcus Aurelius, the emperor.</h2>\n<p>He ruled Rome and kept private notes to himself. We call them the <i>Meditations</i>.</p>\n<p class=strong>One note in Book 8 is a test for anything that annoys you.</p>"),
    ('III', '<div class=kick>The test</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:62px">If a thing is in thy own power, why dost thou do it? But if it is in the power of another, whom dost thou blame? The atoms (chance) or the gods? Both are foolish. Thou must blame nobody.</div>\n<div class=cite>Marcus Aurelius &middot; Meditations 8.17 &middot; tr. George Long</div>'),
    ('IV', '<div class=kick>What to do instead</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:58px">For if thou canst, correct that which is the cause; but if thou canst not do this, correct at least the thing itself; but if thou canst not do even this, of what use is it to thee to find fault? For nothing should be done without a purpose.</div>\n<div class=cite>Marcus Aurelius &middot; Meditations 8.17 &middot; tr. George Long</div>'),
    ('V', '<div class=kick>Your version</div><div class=rule></div>\n<h2>Fix the cause, or fix the night.</h2>\n<p><b>The cause</b> is between you and him. Tell him once, calmly: &ldquo;When you cancel last minute, I lose the night.&rdquo;</p>\n<p><b>The night</b> is still yours. Call someone else, or go without him.</p>\n<p class=strong>The speech in your head fixes neither one.</p>'),
    ('VI', '<div class=kick>The free evening</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:64px">Think not so much of what thou hast not as of what thou hast: but of the things which thou hast select the best, and then reflect how eagerly they would have been sought, if thou hadst them not.</div>\n<div class=cite>Marcus Aurelius &middot; Meditations 7.27 &middot; tr. George Long</div>\n<div class=note>A free night is still a night.</div>'),
    ('VII', '<div class=kick>Try it tonight</div><div class=rule></div>\n<h2>Before you reply.</h2>\n<ul class=steps>\n<li><span class=n>1</span><span class=t><b>Ask</b>: can I change why this keeps happening? If yes, say it once, plainly.</span></li>\n<li><span class=n>2</span><span class=t><b>Fix</b> the evening: pick the best thing you can still do with it.</span></li>\n<li><span class=n>3</span><span class=t><b>Drop</b> the rest. Blaming him tonight gets you nothing.</span></li>\n</ul>'),
    ('VIII', '<div class=kick>Remember</div><div class=rule></div>\n<div class=big style="font-size:88px">Fix the cause<br>or fix the night.<br><em>Then let it go.</em></div>\n<div class=cta>Send this to the friend<br>who <em>always shows up.</em></div>\n' + STOIC_FOLLOW),
]
