import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "tools"))
from lib import *

ACCOUNT = 'applied_stoic'
SOURCES = ['https://monadnock.net/seneca/91.html']

CAPTION = """Seneca's Sunday-night move: send your mind ahead to the week and meet its problems on paper first.

Worry replays the fear. A premortem ends with a plan.

Source: Seneca, Moral Letters to Lucilius, Letter 91, tr. Richard M. Gummere.

#stoicism #seneca #premortem #sundayreset #mindset #stoic"""

SLIDES = [
    ('I', '<div class=kick>Applied Stoicism</div><div class=rule></div>\n<div class=hook style="font-size:120px">Sunday night. Run your week\'s <em>worst case.</em></div>\n<div class=sub>Seneca called it sending<br><em>the mind ahead.</em></div>'),
    ('II', "<div class=kick>Who's talking</div><div class=rule></div>\n<h2>A whole city burned in one night.</h2>\n<p>Seneca's friend Liberalis was shaken: fire had wiped out Lyons, a Roman colony in Gaul. Seneca wrote to steady him.</p>\n<div class=q style=\"font-size:64px;margin-top:10px\">&ldquo;So many beautiful buildings, any single one of which would make a single town famous, were wrecked in one night.&rdquo;</div>\n<div class=cite>Seneca &middot; Letter 91 &middot; tr. Richard M. Gummere</div>"),
    ('III', '<div class=kick>Why it hit so hard</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:84px">It is the unexpected that puts the heaviest load upon us.</div>\n<div class=cite>Seneca &middot; Letter 91 &middot; tr. Richard M. Gummere</div>\n<div class=note>Bad news is heavy. Bad news you never saw coming is heavier.</div>'),
    ('IV', '<div class=kick>His answer</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:72px">Our minds should be sent forward in advance to meet all problems, and we should consider, not what is wont to happen, but what can happen.</div>\n<div class=cite>Seneca &middot; Letter 91 &middot; tr. Richard M. Gummere</div>'),
    ('V', '<div class=kick>Apply it</div><div class=rule></div>\n<h2>Look at the week before it looks at you.</h2>\n<div class=pair><div class=lab>The big meeting</div><div class=val>What if they say no?</div>\n<div class=lab>The deadline</div><div class=val>What if Thursday slips?</div>\n<div class=lab>The commute, the kids, the car</div><div class=val style="margin-bottom:0">What if one of them breaks?</div></div>\n<div class=note>Business teams call this a premortem. Seneca was doing it 2,000 years earlier.</div>'),
    ('VI', "<div class=kick>The Sunday premortem</div><div class=rule></div>\n<h2>Ten minutes, one page:</h2>\n<ul class=steps>\n<li><span class=n>1</span><span class=t><b>List the week's three big things.</b></span></li>\n<li><span class=n>2</span><span class=t><b>For each, write what could go wrong.</b> Not the likely version. The one that would rattle you.</span></li>\n<li><span class=n>3</span><span class=t><b>Write one move now:</b> a backup, an email, an earlier start. Then close the page.</span></li>\n</ul>\n<div class=note>Worry replays the fear. A premortem ends with a plan.</div>"),
    ('VII', '<div class=kick>Remember</div><div class=rule></div>\n<div class=big>Meet Monday\'s problems on Sunday.<br><em>On paper. Then go to bed.</em></div>\n<div class=cta>Send this to the friend<br>with a <em>big week ahead.</em></div>\n' + STOIC_FOLLOW),
]
