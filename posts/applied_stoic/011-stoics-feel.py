import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "tools"))
from lib import *

ACCOUNT = 'applied_stoic'
SOURCES = ['https://monadnock.net/seneca/63.html',
           'https://classics.mit.edu/Antoninus/meditations.1.one.html']

CAPTION = """The Stoics weren't trying to feel nothing. Seneca told a grieving friend to let the tears come, just not to let them take over.

Feel it. Then decide what to do with it.

Sources: Seneca, Letter 63.1, tr. Richard M. Gummere; Marcus Aurelius, Meditations 1.9, tr. George Long.

#stoicism #seneca #emotions #grief #mindset #stoic"""

SLIDES = [
    ('I', '<div class=kick>Applied Stoicism</div><div class=rule></div>\n<div class=hook style="font-size:118px">&ldquo;Stoics don\'t feel <em>emotions.&rdquo;</em></div>\n<div class=sub>A common myth about Stoicism.<br><em>Here\'s what they wrote.</em></div>'),
    ('II', fake("para", "A real Stoic feels nothing. No tears, no grief, no warmth.",
                "Not what they taught. When his friend Lucilius lost a friend, Seneca didn't tell him to feel nothing:",
                "Seneca &middot; Letter 63.1 &middot; tr. Richard M. Gummere",
                "Let not the eyes be dry when we have lost a friend, nor let them overflow.")),
    ('III', '<div class=kick>The rule</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:100px">We may weep, but we must not wail.</div>\n<div class=cite>Seneca &middot; Letter 63.1 &middot; tr. Richard M. Gummere</div>\n<div class=note>Tears are allowed. Being swept away is the problem.</div>'),
    ('IV', '<div class=kick>To be fair</div><div class=rule></div>\n<h2>He still set a high bar.</h2>\n<div class=q style="font-size:62px">&ldquo;That you should not mourn at all I shall hardly dare to insist; and yet I know that it is the better way.&rdquo;</div>\n<div class=cite>Letter 63.1</div>\n<p>Seneca thought less grief was the ideal. But he didn\'t pretend it away, and he didn\'t demand it of a friend.</p>'),
    ('V', '<div class=kick>What Marcus admired in Sextus</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:76px">&hellip;entirely free from passion, and also most affectionate&hellip;</div>\n<div class=cite>Marcus Aurelius on Sextus &middot; Meditations 1.9 &middot; tr. George Long</div>\n<div class=note>Calm and warm, in the same man. That was the goal.</div>'),
    ('VI', '<div class=kick>Next time it hits</div><div class=rule></div>\n<h2>Feel it. Then steer.</h2>\n<ul class=steps>\n<li><span class=n>1</span><span class=t><b>Let it land.</b> Don\'t argue with the feeling. Weeping is allowed.</span></li>\n<li><span class=n>2</span><span class=t><b>Name it.</b> &ldquo;This is grief.&rdquo; &ldquo;This is anger.&rdquo; One word.</span></li>\n<li><span class=n>3</span><span class=t><b>Then ask:</b> what will I do next? That part is yours.</span></li>\n</ul>'),
    ('VII', '<div class=kick>Remember</div><div class=rule></div>\n<div class=big style="font-size:84px">Stoics felt it.<br><em>They just didn\'t let it drive.</em></div>\n<div class=cta>Send this to the friend<br>who thinks Stoic means <em>cold.</em></div>\n' + STOIC_FOLLOW),
]
