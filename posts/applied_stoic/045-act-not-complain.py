import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "tools"))
from lib import *

ACCOUNT = 'applied_stoic'
SOURCES = ['https://classics.mit.edu/Antoninus/meditations.8.eight.html']

CAPTION = """Marcus Aurelius wrote that when an outside thing pains you, it is your own judgement about it that disturbs you, and you can wipe that judgement out now. And if you're pained because you aren't doing something you think is right: "why dost thou not rather act than complain?" Pick the one complaint you repeat most and do one thing about it tonight.

Source: Marcus Aurelius, Meditations 8.47, tr. George Long.

#stoicism #marcusaurelius #mindset #selfimprovement #discipline #stoic"""

SLIDES = [
    ('I', '<div class=kick>Applied Stoicism</div><div class=rule></div>\n<div class=hook style="font-size:104px">Same complaint, third time this week. <em>Still not fixed.</em></div>\n<div class=sub>The messy garage. The job you hate. The call you keep avoiding.<br><em>Marcus asked himself one blunt question.</em></div>'),
    ('II', "<div class=kick>Who&rsquo;s talking</div><div class=rule></div>\n<h2>A notebook nobody was meant to read.</h2>\n<p>Marcus Aurelius ruled the Roman Empire from AD 161 to 180.</p>\n<p class=strong>The <i>Meditations</i> were notes to himself. This one starts with where the pain really comes from.</p>"),
    ('III', '<div class=kick>Part one</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:70px">If thou art pained by any external thing, it is not this thing that disturbs thee, but thy own judgement about it. And it is in thy power to wipe out this judgement now.</div>\n<div class=cite>Marcus Aurelius &middot; Meditations 8.47 &middot; tr. George Long</div>'),
    ('IV', '<div class=kick>Part two</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:70px">And even if thou art pained because thou art not doing some particular thing which seems to thee to be right, why dost thou not rather act than complain?</div>\n<div class=cite>Marcus Aurelius &middot; Meditations 8.47 &middot; tr. George Long</div>'),
    ('V', '<div class=kick>Your version</div><div class=rule></div>\n<h2>The complaint is the easy part.</h2>\n<p>You tell a friend the garage is a disaster. You tell your partner you need to exercise. You tell yourself you&rsquo;ll call your dad.</p>\n<p class=strong>Each retelling feels like progress. None of it moves a box.</p>'),
    ('VI', '<div class=kick>The fine print</div><div class=rule></div>\n<h2>And if you truly can&rsquo;t?</h2>\n<p>Marcus covers that too. If something really is blocking you, he says not to grieve, &ldquo;for the cause of its not being done depends not on thee.&rdquo;</p>\n<p class=strong>Either act, or let it go. Complaining is neither.</p>'),
    ('VII', '<div class=kick>Try it tonight</div><div class=rule></div>\n<h2>Trade a complaint for a move.</h2>\n<ul class=steps>\n<li><span class=n>1</span><span class=t><b>Name it:</b> the complaint you&rsquo;ve said out loud most this week.</span></li>\n<li><span class=n>2</span><span class=t><b>Sort it:</b> can you act on it, or is it out of your hands?</span></li>\n<li><span class=n>3</span><span class=t><b>Act or drop it:</b> do one ten-minute step, or stop retelling it.</span></li>\n</ul>'),
    ('VIII', '<div class=kick>Remember</div><div class=rule></div>\n<div class=big style="font-size:92px">Why not rather act<br><em>than complain?</em></div>\n<div class=cta>Send this to someone<br>who <em>keeps saying &ldquo;I should really&hellip;&rdquo;</em></div>\n' + STOIC_FOLLOW),
]
