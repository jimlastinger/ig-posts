import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "tools"))
from lib import *

ACCOUNT = 'applied_stoic'
SOURCES = ['https://monadnock.net/seneca/13.html']

CAPTION = """Dreading Monday already? Seneca wrote to a friend about exactly this: most of what scares us never arrives.

Spend the weekend you actually have, not the Monday you're imagining.

Source: Seneca, Moral Letters to Lucilius, Letter 13, tr. Richard M. Gummere.

#stoicism #seneca #anxiety #sundayscaries #mindset #stoic"""

SLIDES = [
    ('I', '<div class=kick>Applied Stoicism</div><div class=rule></div>\n<div class=hook style="font-size:126px">It\'s Saturday. You\'re already dreading <em>Monday.</em></div>\n<div class=sub>Seneca has a note<br><em>for that feeling.</em></div>'),
    ('II', "<div class=kick>Who's talking</div><div class=rule></div>\n<h2>124 of Seneca's letters to one friend survive.</h2>\n<p>Late in life, the Roman statesman wrote to his friend Lucilius about how to actually live: time, money, friendship, death and fear.</p>\n<p>Letter 13 is about fear of things that haven't happened yet.</p>"),
    ('III', '<div class=kick>The line</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:76px">There are more things, Lucilius, likely to frighten us than there are to crush us; we suffer more often in imagination than in reality.</div>\n<div class=cite>Seneca &middot; Letter 13.4 &middot; tr. Richard M. Gummere</div>'),
    ('IV', '<div class=kick>Apply it</div><div class=rule></div>\n<h2>Count how many times you\'ll live Monday.</h2>\n<div class=pair><div class=lab>Saturday night</div><div class=val>You rehearse the meeting.</div>\n<div class=lab>Sunday afternoon</div><div class=val>You rehearse it again.</div>\n<div class=lab>Monday morning</div><div class=val style="margin-bottom:0">You finally live it. Once.</div></div>\n<div class=note>Three Mondays of stress for one Monday of work.</div>'),
    ('V', '<div class=kick>His advice</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:80px">What I advise you to do is, not to be unhappy before the crisis comes.</div>\n<div class=cite>Seneca &middot; Letter 13 &middot; tr. Richard M. Gummere</div>\n<div class=note>The thing you dread may never come. If it does, you will face it then, with Monday\'s energy, not Saturday\'s.</div>'),
    ('VI', "<div class=kick>The weekend test</div><div class=rule></div>\n<h2>When the dread shows up:</h2>\n<ul class=steps>\n<li><span class=n>1</span><span class=t><b>Write the fear down.</b> One line. What exactly do you think will happen?</span></li>\n<li><span class=n>2</span><span class=t><b>Ask: is it here yet?</b> If not, it's a forecast, not a fact.</span></li>\n<li><span class=n>3</span><span class=t><b>Pick one prep step</b> for Monday morning. Then close the note and go back to your weekend.</span></li>\n</ul>"),
    ('VII', '<div class=kick>Remember</div><div class=rule></div>\n<div class=big>Monday only gets one day.<br><em>Don\'t give it your weekend.</em></div>\n<div class=cta>Send this to the friend<br>with the <em>Sunday scaries.</em></div>\n' + STOIC_FOLLOW),
]
