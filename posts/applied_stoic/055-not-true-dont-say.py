import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "tools"))
from lib import *

ACCOUNT = 'applied_stoic'
THEME = 'parchment'
SOURCES = ['https://classics.mit.edu/Antoninus/meditations.12.twelve.html']

CAPTION = """Before you hit share, forward or reply, Marcus Aurelius has a two-part test that fits in one line. "If it is not right, do not do it: if it is not true, do not say it."

Source: Marcus Aurelius, Meditations 12.17, tr. George Long.

#stoicism #marcusaurelius #honesty #integrity #mindset #stoic"""

SLIDES = [
    ('I', '<div class=kick>Applied Stoicism</div><div class=rule></div>\n<div class=hook style="font-size:104px">About to hit share? <em>One test first.</em></div>\n<div class=sub>A Roman emperor&rsquo;s<br><em>one-line filter.</em></div>'),
    ('II', "<div class=kick>Who&rsquo;s talking</div><div class=rule></div>\n<h2>An emperor writing to himself.</h2>\n<p>Marcus Aurelius ruled the Roman Empire from AD 161 to 180.</p>\n<p class=strong>Near the end of his private notebook, the <i>Meditations</i>, he sets himself a rule short enough to remember.</p>"),
    ('III', '<div class=kick>The test</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:80px">If it is not right, do not do it: if it is not true, do not say it.</div>\n<div class=cite>Marcus Aurelius &middot; Meditations 12.17 &middot; tr. George Long</div>'),
    ('IV', '<div class=kick>Your version</div><div class=rule></div>\n<h2>The screenshot in the group chat.</h2>\n<p>Someone posts a shocking claim. It confirms what you already think, and your thumb is already on &ldquo;forward.&rdquo;</p>\n<p class=strong>Do you know it&rsquo;s true? If not, passing it on is saying it. The test applies to you, not just whoever wrote it.</p>'),
    ('V', '<div class=kick>Two halves</div><div class=rule></div>\n<h2>One for hands, one for mouths.</h2>\n<ul class=steps>\n<li><span class=n>1</span><span class=t><b>&ldquo;Not right&rdquo;:</b> the shortcut, the little cheat, the thing you&rsquo;d hide from a friend.</span></li>\n<li><span class=n>2</span><span class=t><b>&ldquo;Not true&rdquo;:</b> the rumor, the exaggeration, the &ldquo;I heard that&hellip;&rdquo;</span></li>\n</ul>\n<p class=strong style="margin-top:36px">No debate about motives. Just two questions you can ask in a second.</p>'),
    ('VI', '<div class=kick>Try it today</div><div class=rule></div>\n<h2>Run the filter.</h2>\n<ul class=steps>\n<li><span class=n>1</span><span class=t><b>Pause:</b> before you send, share or repeat anything, wait three seconds.</span></li>\n<li><span class=n>2</span><span class=t><b>Ask:</b> is it true? Do I actually know?</span></li>\n<li><span class=n>3</span><span class=t><b>Ask:</b> is it right? If either answer is no, don&rsquo;t.</span></li>\n</ul>'),
    ('VII', '<div class=kick>Remember</div><div class=rule></div>\n<div class=big style="font-size:96px">Not right? Don&rsquo;t do it.<br><em>Not true? Don&rsquo;t say it.</em></div>\n<div class=cta>Send this to someone<br>who <em>checks before they share.</em></div>\n' + STOIC_FOLLOW),
]
