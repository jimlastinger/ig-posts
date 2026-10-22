import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "tools"))
from lib import *

ACCOUNT = 'applied_stoic'
THEME = 'parchment'
SOURCES = ['https://classics.mit.edu/Antoninus/meditations.4.four.html']

CAPTION = """A Roman emperor wrote himself a note: everyone who remembers you will die too. And praise doesn't make a good thing any better.

Do one good thing today that you don't post or mention to anyone.

Source: Marcus Aurelius, Meditations 4.19 and 4.20, tr. George Long.

#stoicism #marcusaurelius #meditations #socialmedia #mindset #stoic"""

SLIDES = [
    ('I', '<div class=kick>Applied Stoicism</div><div class=rule></div>\n<div class=hook style="font-size:118px">You want to be remembered. <em>By whom?</em></div>\n<div class=sub>An emperor&rsquo;s note<br><em>on chasing fame.</em></div>'),
    ('II', "<div class=kick>Who&rsquo;s talking</div><div class=rule></div>\n<h2>The man at the top of Rome.</h2>\n<p>Marcus Aurelius ruled the Roman Empire from AD 161 to 180.</p>\n<p class=strong>In his private notebook, the <i>Meditations</i>, he kept talking himself out of caring about fame.</p>"),
    ('III', '<div class=kick>The math of fame</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:70px">He who has a vehement desire for posthumous fame does not consider that every one of those who remember him will himself also die very soon; then again also they who have succeeded them, until the whole remembrance shall have been extinguished&hellip;</div>\n<div class=cite>Marcus Aurelius &middot; Meditations 4.19 &middot; tr. George Long</div>'),
    ('IV', '<div class=kick>Even if it lasted</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:84px">&hellip; what then is this to thee? &hellip; What is praise except indeed so far as it has a certain utility?</div>\n<div class=cite>Marcus Aurelius &middot; Meditations 4.19 &middot; tr. George Long</div>\n<div class=note>Praise is worth only what it&rsquo;s useful for. The rest is noise.</div>'),
    ('V', '<div class=kick>Your version</div><div class=rule></div>\n<h2>Likes, views, followers.</h2>\n<p>We check the count an hour after posting, then again before bed. A post that does well feels like it proved something.</p>\n<p class=strong>Marcus would ask: who will remember it in a year? And did the likes change what it was?</p>'),
    ('VI', '<div class=kick>The emerald test</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:88px">Is such a thing as an emerald made worse than it was, if it is not praised?</div>\n<div class=cite>Marcus Aurelius &middot; Meditations 4.20 &middot; tr. George Long</div>\n<div class=note>&ldquo;Neither worse then nor better is a thing made by being praised.&rdquo;</div>'),
    ('VII', '<div class=kick>Try it today</div><div class=rule></div>\n<h2>Do one thing unseen.</h2>\n<ul class=steps>\n<li><span class=n>1</span><span class=t><b>Do something good</b> and tell no one: no post, no story, no mention.</span></li>\n<li><span class=n>2</span><span class=t><b>Before you post,</b> ask: would I still do this with zero likes?</span></li>\n<li><span class=n>3</span><span class=t><b>Sort the praise.</b> Keep what&rsquo;s useful. Let the applause go.</span></li>\n</ul>'),
    ('VIII', '<div class=kick>Remember</div><div class=rule></div>\n<div class=big style="font-size:88px">An emerald with no likes<br><em>is still an emerald.</em></div>\n<div class=cta>Send this to someone<br>who <em>checks the count.</em></div>\n' + STOIC_FOLLOW),
]
