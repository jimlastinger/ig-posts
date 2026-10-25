import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "tools"))
from lib import *

ACCOUNT = 'applied_stoic'
THEME = 'parchment'
SOURCES = ['https://classics.mit.edu/Antoninus/meditations.5.five.html',
           'https://classics.mit.edu/Antoninus/meditations.3.three.html']

CAPTION = """Marcus Aurelius wrote that "the soul is dyed by the thoughts." Whatever you think about most is what your mind turns into, so choose what you let it soak in, starting with tonight's scroll.

Source: Marcus Aurelius, Meditations 5.16 and 3.4, tr. George Long.

#stoicism #marcusaurelius #mindset #focus #digitalwellbeing #stoic"""

SLIDES = [
    ('I', '<div class=kick>Applied Stoicism</div><div class=rule></div>\n<div class=hook style="font-size:108px">Your mind takes the color of <em>what you feed it.</em></div>\n<div class=sub>Marcus Aurelius said it long ago.<br><em>Your feed shows it.</em></div>'),
    ('II', "<div class=kick>Who&rsquo;s talking</div><div class=rule></div>\n<h2>An emperor who watched his own thoughts.</h2>\n<p>Marcus Aurelius ruled the Roman Empire from AD 161 to 180.</p>\n<p class=strong>In his private notebook, the <i>Meditations</i>, he kept reminding himself that his thoughts were shaping him.</p>"),
    ('III', '<div class=kick>The line</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:86px">Such as are thy habitual thoughts, such also will be the character of thy mind; for the soul is dyed by the thoughts.</div>\n<div class=cite>Marcus Aurelius &middot; Meditations 5.16 &middot; tr. George Long</div>\n<div class=note>Dyed: like cloth left in color until it takes it.</div>'),
    ('IV', '<div class=kick>Your version</div><div class=rule></div>\n<h2>The hour before bed.</h2>\n<p>Someone else&rsquo;s fight. Someone else&rsquo;s vacation. Someone else&rsquo;s bad news, again and again.</p>\n<p class=strong>Do that every night and it stops being what you watch. It becomes how you think.</p>'),
    ('V', '<div class=kick>The trap he named</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:72px">Do not waste the remainder of thy life in thoughts about others, when thou dost not refer thy thoughts to some object of common utility.</div>\n<div class=cite>Marcus Aurelius &middot; Meditations 3.4 &middot; tr. George Long</div>\n<div class=note>His list: what is such a person doing, and why, and what is he saying.</div>'),
    ('VI', '<div class=kick>His test</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:82px">What hast thou now in thy thoughts?</div>\n<div class=cite>Marcus Aurelius &middot; Meditations 3.4 &middot; tr. George Long</div>\n<div class=note>He wanted to be able to answer openly, with nothing he would blush to say.</div>'),
    ('VII', '<div class=kick>Try it tonight</div><div class=rule></div>\n<h2>Check the dye.</h2>\n<ul class=steps>\n<li><span class=n>1</span><span class=t><b>Ask his question</b> after ten minutes of scrolling: what&rsquo;s in my thoughts now?</span></li>\n<li><span class=n>2</span><span class=t><b>Say the answer out loud.</b> Would you be glad to say it to a friend?</span></li>\n<li><span class=n>3</span><span class=t><b>Swap ten minutes of feed</b> for one thought you&rsquo;d choose on purpose.</span></li>\n</ul>'),
    ('VIII', '<div class=kick>Remember</div><div class=rule></div>\n<div class=big style="font-size:86px">You become what you dwell on.<br><em>Choose the color.</em></div>\n<div class=cta>Send this to someone<br>who <em>scrolls before bed.</em></div>\n' + STOIC_FOLLOW),
]
