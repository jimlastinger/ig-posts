import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "tools"))
from lib import *

ACCOUNT = 'applied_stoic'
SOURCES = ['https://classics.mit.edu/Antoninus/meditations.6.six.html']

CAPTION = """Marcus Aurelius had the biggest promotion in the world, and he wrote himself a warning: "Take care that thou art not made into a Caesar…" The title can change you quietly unless you watch for it.

New role? Write down who you were before it.

Source: Marcus Aurelius, Meditations 6.30, tr. George Long (MIT Internet Classics Archive).

#stoicism #marcusaurelius #meditations #leadership #promotion #stoic"""

SLIDES = [
    ('I', '<div class=kick>Applied Stoicism</div><div class=rule></div>\n<div class=hook style="font-size:118px">You got the promotion. <em>Don&rsquo;t let it get you.</em></div>\n<div class=sub>An emperor wrote himself<br><em>the same warning.</em></div>'),
    ('II', "<div class=kick>Who&rsquo;s talking</div><div class=rule></div>\n<h2>Marcus Aurelius, writing to himself.</h2>\n<p>He ruled Rome from AD 161 to 180. <i>Meditations</i> was his private notebook, never meant for us.</p>\n<p class=strong>He had the top job in the world. In Book 6, he worries about what it could do to him.</p>"),
    ('III', '<div class=kick>The warning</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:92px">Take care that thou art not made into a Caesar, that thou art not dyed with this dye; for such things happen.</div>\n<div class=cite>Marcus Aurelius &middot; Meditations 6.30 &middot; tr. George Long</div>\n<div class=note>Like cloth in a vat: soak in the role long enough and it colors you.</div>'),
    ('IV', '<div class=kick>Who to be instead</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:80px">Keep thyself then simple, good, pure, serious, free from affectation, a friend of justice, a worshipper of the gods, kind, affectionate, strenuous in all proper acts.</div>\n<div class=cite>Marcus Aurelius &middot; Meditations 6.30 &middot; tr. George Long</div>'),
    ('V', '<div class=kick>Your version</div><div class=rule></div>\n<h2>New title.<br>Same you?</h2>\n<p>The bigger office, the full calendar, people who laugh a little harder at your jokes.</p>\n<p class=strong>Nobody decides to change. It happens a little at a time. Marcus&rsquo;s point: &ldquo;such things happen,&rdquo; so watch for it.</p>'),
    ('VI', '<div class=kick>His model</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:96px">Do everything as a disciple of Antoninus.</div>\n<div class=cite>Marcus Aurelius &middot; Meditations 6.30 &middot; tr. George Long</div>\n<div class=note>Antoninus Pius: his adoptive father and the emperor before him. Marcus held him up as a model of steadiness and modesty.</div>'),
    ('VII', '<div class=kick>Try it this week</div><div class=rule></div>\n<h2>A check before the title sinks in.</h2>\n<ul class=steps>\n<li><span class=n>1</span><span class=t><b>Write it down.</b> Who were you before the new role?</span></li>\n<li><span class=n>2</span><span class=t><b>Ask a peer.</b> Someone honest: &ldquo;Have I changed?&rdquo;</span></li>\n<li><span class=n>3</span><span class=t><b>Pick your Antoninus.</b> Someone who held power and stayed decent.</span></li>\n</ul>'),
    ('VIII', '<div class=kick>Remember</div><div class=rule></div>\n<div class=big style="font-size:88px">Short is life.<br><em>Keep the title. Don&rsquo;t become it.</em></div>\n<div class=cta>Send this to someone<br>who <em>just got promoted.</em></div>\n' + STOIC_FOLLOW),
]
