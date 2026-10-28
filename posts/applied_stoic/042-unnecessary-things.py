import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "tools"))
from lib import *

ACCOUNT = 'applied_stoic'
SOURCES = ['https://classics.mit.edu/Antoninus/meditations.4.four.html']

CAPTION = """Marcus Aurelius thought most of what we say and do is unnecessary, and that cutting it gives "more leisure and less uneasiness." Before today's to-do list runs you, ask his one question of each item.

Source: Marcus Aurelius, Meditations 4.24, tr. George Long.

#stoicism #marcusaurelius #productivity #focus #mindset #stoic"""

SLIDES = [
    ('I', '<div class=kick>Applied Stoicism</div><div class=rule></div>\n<div class=hook style="font-size:104px">Twenty things on the list. <em>How many matter?</em></div>\n<div class=sub>A Roman emperor had one question<br><em>for every task.</em></div>'),
    ('II', "<div class=kick>Who&rsquo;s talking</div><div class=rule></div>\n<h2>A man who never ran out of work.</h2>\n<p>Marcus Aurelius was a Roman emperor.</p>\n<p class=strong>In his private notebook, the <i>Meditations</i>, he wrote down how to get through a crowded day.</p>"),
    ('III', '<div class=kick>The line</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:70px">For the greatest part of what we say and do being unnecessary, if a man takes this away, he will have more leisure and less uneasiness.</div>\n<div class=cite>Marcus Aurelius &middot; Meditations 4.24 &middot; tr. George Long</div>'),
    ('IV', '<div class=kick>The question</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:80px">Accordingly on every occasion a man should ask himself, Is this one of the unnecessary things?</div>\n<div class=cite>Marcus Aurelius &middot; Meditations 4.24 &middot; tr. George Long</div>'),
    ('V', '<div class=kick>Your version</div><div class=rule></div>\n<h2>Busy is not the same as useful.</h2>\n<p>The meeting that could be an email. The reply-all. The third rewrite of a message nobody will reread.</p>\n<p class=strong>Marcus didn&rsquo;t say do less. He said do what is necessary.</p>'),
    ('VI', '<div class=kick>The second cut</div><div class=rule></div>\n<h2>Start with the thoughts.</h2>\n<p>Marcus says to take away not only unnecessary acts, &ldquo;but also, unnecessary thoughts.&rdquo;</p>\n<p class=strong>His reason: then &ldquo;superfluous acts will not follow after.&rdquo; Stop the worry and you skip the busywork it starts.</p>'),
    ('VII', '<div class=kick>Try it this morning</div><div class=rule></div>\n<h2>Ask it of everything.</h2>\n<ul class=steps>\n<li><span class=n>1</span><span class=t><b>Write today&rsquo;s list.</b> All of it.</span></li>\n<li><span class=n>2</span><span class=t><b>Ask of each item:</b> is this one of the unnecessary things?</span></li>\n<li><span class=n>3</span><span class=t><b>Cross out one.</b> Use the time it frees for what is left.</span></li>\n</ul>'),
    ('VIII', '<div class=kick>Remember</div><div class=rule></div>\n<div class=big style="font-size:88px">Do what is necessary.<br><em>Then stop.</em></div>\n<div class=cta>Send this to someone<br>who <em>is busy all day and done with nothing.</em></div>\n' + STOIC_FOLLOW),
]
