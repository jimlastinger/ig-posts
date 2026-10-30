import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "tools"))
from lib import *

ACCOUNT = 'applied_stoic'
THEME = 'bronze'
SOURCES = ['https://classics.mit.edu/Antoninus/meditations.6.six.html']

CAPTION = """Marcus Aurelius told himself it should make no difference whether he was cold or warm, drowsy or rested, ill-spoken of or praised, as long as he was doing his duty. Tired, ignored, still showing up: that counts. Before the weekend, name one thing you did well this week that nobody noticed.

Source: Marcus Aurelius, Meditations 6.2, tr. George Long.

#stoicism #marcusaurelius #discipline #work #mindset #stoic"""

SLIDES = [
    ('I', '<div class=kick>Applied Stoicism</div><div class=rule></div>\n<div class=hook style="font-size:100px">Tired. Cold. Ignored. <em>Did it anyway.</em></div>\n<div class=sub>The long week is over.<br><em>Marcus would call that a good one.</em></div>'),
    ('II', "<div class=kick>Who&rsquo;s talking</div><div class=rule></div>\n<h2>A ruler who worked through it.</h2>\n<p>Marcus Aurelius ruled the Roman Empire from AD 161 to 180.</p>\n<p class=strong>In his private notebook, the <i>Meditations</i>, he reminded himself how little his comfort, or other people&rsquo;s opinions, should matter to the work.</p>"),
    ('III', '<div class=kick>The line</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:70px">Let it make no difference to thee whether thou art cold or warm, if thou art doing thy duty; and whether thou art drowsy or satisfied with sleep; and whether ill-spoken of or praised&hellip;</div>\n<div class=cite>Marcus Aurelius &middot; Meditations 6.2 &middot; tr. George Long</div>'),
    ('IV', '<div class=kick>Your version</div><div class=rule></div>\n<h2>The conditions were never perfect.</h2>\n<p>You worked on five hours of sleep. The office was freezing. The thing you fixed got no thank-you.</p>\n<p class=strong>Marcus would say: the duty got done. The rest is weather.</p>'),
    ('V', '<div class=kick>The hard part</div><div class=rule></div>\n<h2>Praise is weather too.</h2>\n<p>He puts &ldquo;ill-spoken of or praised&rdquo; in the same list as cold and warm.</p>\n<p class=strong>If a compliment can make your week, a complaint can ruin it. Marcus wanted neither to decide.</p>'),
    ('VI', '<div class=kick>Try it tonight</div><div class=rule></div>\n<h2>The unnoticed list.</h2>\n<ul class=steps>\n<li><span class=n>1</span><span class=t><b>Write one:</b> a thing you did well this week that nobody saw.</span></li>\n<li><span class=n>2</span><span class=t><b>Note the conditions:</b> tired, cold, criticized, ignored.</span></li>\n<li><span class=n>3</span><span class=t><b>Count it anyway:</b> the duty got done.</span></li>\n</ul>'),
    ('VII', '<div class=kick>Remember</div><div class=rule></div>\n<div class=big style="font-size:92px">Cold or warm,<br><em>do the duty.</em></div>\n<div class=cta>Send this to someone<br>who <em>showed up all week.</em></div>\n' + STOIC_FOLLOW),
]
