import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "tools"))
from lib import *

ACCOUNT = 'applied_stoic'
SOURCES = ['https://classics.mit.edu/Antoninus/meditations.4.four.html']

CAPTION = """Marcus Aurelius told himself to be like a rock the sea keeps hitting: "Be like the promontory against which the waves continually break, but it stands firm and tames the fury of the water around it." His point wasn't that bad things won't happen. It was that bearing them well is its own good fortune.

Source: Marcus Aurelius, Meditations 4.49, tr. George Long.

#stoicism #marcusaurelius #resilience #hardtimes #mindset #stoic"""

SLIDES = [
    ('I', '<div class=kick>Applied Stoicism</div><div class=rule></div>\n<div class=hook style="font-size:112px">Rough week? <em>Be the rock, not the wave.</em></div>\n<div class=sub>An emperor&rsquo;s note<br><em>for when it keeps coming.</em></div>'),
    ('II', "<div class=kick>Who&rsquo;s talking</div><div class=rule></div>\n<h2>A man who didn&rsquo;t get easy years.</h2>\n<p>Marcus Aurelius ruled the Roman Empire from AD 161 to 180.</p>\n<p class=strong>In his private notebook, the <i>Meditations</i>, he wrote down what he wanted to be when trouble kept hitting.</p>"),
    ('III', '<div class=kick>The image</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:84px">Be like the promontory against which the waves continually break, but it stands firm and tames the fury of the water around it.</div>\n<div class=cite>Marcus Aurelius &middot; Meditations 4.49 &middot; tr. George Long</div>\n<div class=note>The waves don&rsquo;t stop. The rock doesn&rsquo;t move.</div>'),
    ('IV', '<div class=kick>Your version</div><div class=rule></div>\n<h2>The week where everything lands at once.</h2>\n<p>The car needs work. A deadline moves up. Someone you count on cancels.</p>\n<p class=strong>You can&rsquo;t stop the waves. You can decide not to be knocked over by each one.</p>'),
    ('V', '<div class=kick>The switch</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:76px">Unhappy am I because this has happened to me.&mdash;Not so, but happy am I, though this has happened to me, because I continue free from pain, neither crushed by the present nor fearing the future.</div>\n<div class=cite>Marcus Aurelius &middot; Meditations 4.49 &middot; tr. George Long</div>'),
    ('VI', '<div class=kick>The rule he kept</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:80px">Not that this is a misfortune, but that to bear it nobly is good fortune.</div>\n<div class=cite>Marcus Aurelius &middot; Meditations 4.49 &middot; tr. George Long</div>\n<div class=note>He told himself to apply it &ldquo;on every occasion which leads thee to vexation.&rdquo;</div>'),
    ('VII', '<div class=kick>Try it today</div><div class=rule></div>\n<h2>When the next wave hits.</h2>\n<ul class=steps>\n<li><span class=n>1</span><span class=t><b>Name it plainly:</b> &ldquo;This happened.&rdquo; Leave off &ldquo;to me, again.&rdquo;</span></li>\n<li><span class=n>2</span><span class=t><b>Check the present:</b> are you crushed right now, or bracing for what comes next?</span></li>\n<li><span class=n>3</span><span class=t><b>Pick one way to bear it well</b> today, and count that as the win.</span></li>\n</ul>'),
    ('VIII', '<div class=kick>Remember</div><div class=rule></div>\n<div class=big style="font-size:86px">The waves keep coming.<br><em>Stand firm anyway.</em></div>\n<div class=cta>Send this to someone<br>who <em>is having a week.</em></div>\n' + STOIC_FOLLOW),
]
