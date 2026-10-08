import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "tools"))
from lib import *

ACCOUNT = 'applied_stoic'
SOURCES = ['https://classics.mit.edu/Antoninus/meditations.4.four.html']

CAPTION = """"Someday" assumes you have endless time. Marcus Aurelius reminded himself that he didn't, and neither do we.

Pick the thing you keep postponing and do the first ten minutes of it today.

Source: Marcus Aurelius, Meditations 4.17 and 4.37, tr. George Long.

#stoicism #marcusaurelius #procrastination #meditations #mindset #stoic"""

SLIDES = [
    ('I', '<div class=kick>Applied Stoicism</div><div class=rule></div>\n<div class=hook style="font-size:124px">&ldquo;I\'ll do it <em>someday.&rdquo;</em></div>\n<div class=sub>Marcus Aurelius had a<br>two-line answer to <em>that.</em></div>'),
    ('II', "<div class=kick>Who's talking</div><div class=rule></div>\n<h2>An emperor who wrote reminders to himself.</h2>\n<p>Marcus Aurelius ruled Rome from AD 161 to 180. His notebook, the <i>Meditations</i>, wasn't meant for readers. It's full of notes he needed to hear.</p>\n<p class=strong>One he kept returning to: time is shorter than you act like it is.</p>"),
    ('III', '<div class=kick>The line</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:88px">Do not act as if thou wert going to live ten thousand years. Death hangs over thee. While thou livest, while it is in thy power, be good.</div>\n<div class=cite>Marcus Aurelius &middot; Meditations 4.17 &middot; tr. George Long</div>'),
    ('IV', '<div class=kick>Translate it to your to-do list</div><div class=rule></div>\n<h2>&ldquo;Later&rdquo; is a bet on time you don\'t have.</h2>\n<div class=pair><div class=lab>The call you keep putting off</div><div class=val>Your parent won\'t always pick up.</div>\n<div class=lab>The project &ldquo;after things calm down&rdquo;</div><div class=val>Things rarely calm down.</div>\n<div class=lab>The apology</div><div class=val style="margin-bottom:0">It gets harder every week you wait.</div></div>'),
    ('V', '<div class=kick>He was hard on himself, too</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:84px">Thou wilt soon die, and thou art not yet simple, not free from perturbations&hellip;</div>\n<div class=cite>Marcus Aurelius &middot; Meditations 4.37 &middot; tr. George Long</div>\n<div class=note>Not a threat. A deadline, and a reason to start now.</div>'),
    ('VI', '<div class=kick>Do this today</div><div class=rule></div>\n<h2>The ten-minute start.</h2>\n<ul class=steps>\n<li><span class=n>1</span><span class=t><b>Name one thing</b> you\'ve been saving for &ldquo;someday.&rdquo;</span></li>\n<li><span class=n>2</span><span class=t><b>Shrink it</b> to a first step you can finish in ten minutes.</span></li>\n<li><span class=n>3</span><span class=t><b>Do it now,</b> while it is in your power.</span></li>\n</ul>'),
    ('VII', '<div class=kick>Remember</div><div class=rule></div>\n<div class=big>You don\'t have ten thousand years.<br><em>You have today.</em></div>\n<div class=cta>Send this to someone<br>who keeps saying <em>&ldquo;someday.&rdquo;</em></div>\n' + STOIC_FOLLOW),
]
