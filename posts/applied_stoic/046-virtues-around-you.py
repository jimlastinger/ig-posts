import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "tools"))
from lib import *

ACCOUNT = 'applied_stoic'
THEME = 'parchment'
SOURCES = ['https://classics.mit.edu/Antoninus/meditations.6.six.html']

CAPTION = """Marcus Aurelius had a simple way to cheer himself up: think of the good qualities of the people he lived with, one at a time. "Wherefore we must keep them before us." Name one good trait in each person you'll see today, and tell one of them.

Source: Marcus Aurelius, Meditations 6.48, tr. George Long.

#stoicism #marcusaurelius #gratitude #relationships #mindset #stoic"""

SLIDES = [
    ('I', '<div class=kick>Applied Stoicism</div><div class=rule></div>\n<div class=hook style="font-size:100px">You can list their flaws in seconds. <em>Their virtues?</em></div>\n<div class=sub>The coworker, the roommate, the family at breakfast.<br><em>Marcus kept a different list.</em></div>'),
    ('II', "<div class=kick>Who&rsquo;s talking</div><div class=rule></div>\n<h2>An emperor surrounded by people.</h2>\n<p>Marcus Aurelius ruled the Roman Empire from AD 161 to 180.</p>\n<p class=strong>In his private notebook, the <i>Meditations</i>, he wrote down how he lifted his own mood. It wasn&rsquo;t a purchase. It was a habit of attention.</p>"),
    ('III', '<div class=kick>The method</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:68px">When thou wishest to delight thyself, think of the virtues of those who live with thee; for instance, the activity of one, and the modesty of another, and the liberality of a third, and some other good quality of a fourth.</div>\n<div class=cite>Marcus Aurelius &middot; Meditations 6.48 &middot; tr. George Long</div>'),
    ('IV', '<div class=kick>The reason</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:70px">For nothing delights so much as the examples of the virtues&hellip; Wherefore we must keep them before us.</div>\n<div class=cite>Marcus Aurelius &middot; Meditations 6.48 &middot; tr. George Long</div>'),
    ('V', '<div class=kick>Your version</div><div class=rule></div>\n<h2>One person, one good thing.</h2>\n<p>Your partner who never forgets the trash. The coworker who answers every question. The friend who always texts back.</p>\n<p class=strong>Marcus didn&rsquo;t ask for perfect people. He looked for one good quality in each.</p>'),
    ('VI', '<div class=kick>Why it works</div><div class=rule></div>\n<h2>You find what you look for.</h2>\n<p>Spend the morning cataloguing what annoys you, and the day fills with annoyance.</p>\n<p class=strong>Spend one minute on the virtues around you, and you walk in already on their side.</p>'),
    ('VII', '<div class=kick>Try it this morning</div><div class=rule></div>\n<h2>The four-person list.</h2>\n<ul class=steps>\n<li><span class=n>1</span><span class=t><b>Pick four:</b> people you&rsquo;ll see or talk to today.</span></li>\n<li><span class=n>2</span><span class=t><b>One word each:</b> patient, generous, funny, hardworking.</span></li>\n<li><span class=n>3</span><span class=t><b>Say one out loud:</b> tell one of them what you noticed.</span></li>\n</ul>'),
    ('VIII', '<div class=kick>Remember</div><div class=rule></div>\n<div class=big style="font-size:92px">Keep their virtues<br><em>before you.</em></div>\n<div class=cta>Send this to someone<br>whose <em>good quality you noticed.</em></div>\n' + STOIC_FOLLOW),
]
