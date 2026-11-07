import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "tools"))
from lib import *

ACCOUNT = 'applied_stoic'
SOURCES = ['https://classics.mit.edu/Antoninus/meditations.mb.txt']

CAPTION = """They read your message and didn't answer. Within minutes you've decided they're upset with you. Marcus Aurelius had a rule for this: say nothing more to yourself than what you actually saw.

Source: Marcus Aurelius, Meditations 8.49, tr. George Long.

#stoicism #marcusaurelius #overthinking #anxiety #mindset #stoic"""

SLIDES = [
    ('I', '<div class=kick>Applied Stoicism</div><div class=rule></div>\n<div class=hook style="font-size:110px">They left you on read. <em>That&rsquo;s all you know.</em></div>\n<div class=sub>Everything else is a story<br><em>you wrote yourself.</em></div>'),
    ('II', "<div class=kick>Who&rsquo;s talking</div><div class=rule></div>\n<h2>An emperor who caught himself guessing.</h2>\n<p>Marcus Aurelius ruled the Roman Empire from AD 161 to 180.</p>\n<p class=strong>In his private notebook, the <i>Meditations</i>, he kept a rule for the moment the mind starts filling in blanks.</p>"),
    ('III', '<div class=kick>The rule</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:64px">Say nothing more to thyself than what the first appearances report. Suppose that it has been reported to thee that a certain person speaks ill of thee. This has been reported; but that thou hast been injured, that has not been reported.</div>\n<div class=cite>Marcus Aurelius &middot; Meditations 8.49 &middot; tr. George Long</div>'),
    ('IV', '<div class=kick>Your version</div><div class=rule></div>\n<h2>Read 9:14 p.m. No reply.</h2>\n<p>By 9:25 you&rsquo;ve decided they&rsquo;re annoyed and started drafting an apology.</p>\n<p class=strong>What was reported? A message got read. Marcus would stop there. The rest you added yourself.</p>'),
    ('V', '<div class=kick>Waiting on news</div><div class=rule></div>\n<h2>It works on scary news too.</h2>\n<p>Marcus&rsquo;s own example: &ldquo;I see that my child is sick. I do see; but that he is in danger, I do not see.&rdquo;</p>\n<p class=strong>The test results. The email that just says &ldquo;quick chat?&rdquo; Deal with what you know now, and let the rest show up on its own.</p>'),
    ('VI', '<div class=kick>Try it today</div><div class=rule></div>\n<h2>Split the fact from the story.</h2>\n<ul class=steps>\n<li><span class=n>1</span><span class=t><b>Write</b> what you think happened, in one plain sentence.</span></li>\n<li><span class=n>2</span><span class=t><b>Underline</b> every word you can&rsquo;t actually prove.</span></li>\n<li><span class=n>3</span><span class=t><b>Cross it out</b> and act only on what&rsquo;s left.</span></li>\n</ul>'),
    ('VII', '<div class=kick>Remember</div><div class=rule></div>\n<div class=big style="font-size:96px">Keep the fact.<br><em>Drop the sequel.</em></div>\n<div class=cta>Send this to someone<br>who&rsquo;s <em>overthinking a text.</em></div>\n' + STOIC_FOLLOW),
]
