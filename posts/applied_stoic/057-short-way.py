import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "tools"))
from lib import *

ACCOUNT = 'applied_stoic'
SOURCES = ['https://classics.mit.edu/Antoninus/meditations.4.four.html']

CAPTION = """Most of the stress in a hard conversation comes from the angles we work: the spin, the hints, the excuse built in advance. Marcus Aurelius's advice was to take the short way. Say the true thing plainly and skip the performance.

Source: Marcus Aurelius, Meditations 4.51, tr. George Long.

#stoicism #marcusaurelius #simplicity #honesty #mindset #stoic"""

SLIDES = [
    ('I', '<div class=kick>Applied Stoicism</div><div class=rule></div>\n<div class=hook style="font-size:104px">Stop working the angles. <em>Take the short way.</em></div>\n<div class=sub>An emperor&rsquo;s advice<br><em>for every hard conversation.</em></div>'),
    ('II', "<div class=kick>Who&rsquo;s talking</div><div class=rule></div>\n<h2>An emperor writing to himself.</h2>\n<p>Marcus Aurelius ruled the Roman Empire from AD 161 to 180.</p>\n<p class=strong>He closed Book Four of his private notebook, the <i>Meditations</i>, with a note to himself about the simplest route.</p>"),
    ('III', '<div class=kick>The short way</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:64px">Always run to the short way; and the short way is the natural: accordingly say and do everything in conformity with the soundest reason. For such a purpose frees a man from trouble, and warfare, and all artifice and ostentatious display.</div>\n<div class=cite>Marcus Aurelius &middot; Meditations 4.51 &middot; tr. George Long</div>'),
    ('IV', '<div class=kick>Your version</div><div class=rule></div>\n<h2>The message you&rsquo;ve drafted five times.</h2>\n<p>You need to tell a client the project is late. So you soften it, bury it in paragraph three, and add an excuse just in case.</p>\n<p class=strong>The short way: &ldquo;It&rsquo;s late. Here&rsquo;s the new date. Here&rsquo;s what I&rsquo;m doing about it.&rdquo;</p>'),
    ('V', '<div class=kick>What it frees you from</div><div class=rule></div>\n<h2>Three things you can drop.</h2>\n<ul class=steps>\n<li><span class=n>1</span><span class=t><b>Trouble:</b> no story to keep straight later.</span></li>\n<li><span class=n>2</span><span class=t><b>Warfare:</b> no hidden moves for the other side to fight.</span></li>\n<li><span class=n>3</span><span class=t><b>Display:</b> no image to protect.</span></li>\n</ul>\n<p class=strong style="margin-top:36px">The long way feels safer. It&rsquo;s usually just more work.</p>'),
    ('VI', '<div class=kick>Try it today</div><div class=rule></div>\n<h2>Cut to the short way.</h2>\n<ul class=steps>\n<li><span class=n>1</span><span class=t><b>Write</b> the hard message the way you&rsquo;d say it to a friend.</span></li>\n<li><span class=n>2</span><span class=t><b>Delete</b> every line that exists only to protect your image.</span></li>\n<li><span class=n>3</span><span class=t><b>Send</b> what&rsquo;s left: true, clear and kind.</span></li>\n</ul>'),
    ('VII', '<div class=kick>Remember</div><div class=rule></div>\n<div class=big style="font-size:96px">Say it plainly.<br><em>Skip the performance.</em></div>\n<div class=cta>Send this to someone<br>who&rsquo;s <em>overthinking a message.</em></div>\n' + STOIC_FOLLOW),
]
