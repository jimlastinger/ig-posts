import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "tools"))
from lib import *

ACCOUNT = 'applied_stoic'
SOURCES = ['https://classics.mit.edu/Antoninus/meditations.4.four.html']

CAPTION = """Marcus Aurelius ruled Rome, and he still had to remind himself that praise changes nothing. An emerald isn't worse for going unpraised, and neither is your work.

Do the thing well. Let the count be the count.

Source: Marcus Aurelius, Meditations 4.19 and 4.20, tr. George Long.

#stoicism #marcusaurelius #socialmedia #validation #mindset #stoic"""

SLIDES = [
    ('I', '<div class=kick>Applied Stoicism</div><div class=rule></div>\n<div class=hook style="font-size:120px">You keep checking <em>the likes.</em></div>\n<div class=sub>An emperor wrote a question<br><em>for you,</em> long before likes.</div>'),
    ('II', "<div class=kick>Who's talking</div><div class=rule></div>\n<h2>An emperor, writing only to himself.</h2>\n<p>Marcus Aurelius ruled Rome. Praise came with the job, every day.</p>\n<p class=strong>In his private notebook, he kept talking himself out of caring about any of it.</p>"),
    ('III', '<div class=kick>His test</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:88px">Is such a thing as an emerald made worse than it was, if it is not praised?</div>\n<div class=cite>Marcus Aurelius &middot; Meditations 4.20 &middot; tr. George Long</div>'),
    ('IV', '<div class=kick>Apply it</div><div class=rule></div>\n<h2>The post with 9 likes.</h2>\n<p>You worked on it. It went out. Almost nobody noticed.</p>\n<p>Was it worse than it was an hour ago? It\'s the same work. Only the number changed.</p>\n<div class=q style="font-size:66px;margin-top:20px">&ldquo;Neither worse then nor better is a thing made by being praised.&rdquo;</div>\n<div class=cite>Meditations 4.20</div>'),
    ('V', '<div class=kick>And the applause?</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:72px">He who has a vehement desire for posthumous fame does not consider that every one of those who remember him will himself also die very soon&hellip;</div>\n<div class=cite>Meditations 4.19</div>\n<div class=note>The people clapping are as temporary as you are.</div>'),
    ('VI', '<div class=kick>This week</div><div class=rule></div>\n<h2>Judge the emerald, not the crowd.</h2>\n<ul class=steps>\n<li><span class=n>1</span><span class=t><b>Before you post,</b> decide what &ldquo;good&rdquo; means for it. Write one line.</span></li>\n<li><span class=n>2</span><span class=t><b>After you post,</b> close the app. No checking for an hour.</span></li>\n<li><span class=n>3</span><span class=t><b>Next day,</b> grade it against your line, not the count.</span></li>\n</ul>'),
    ('VII', '<div class=kick>Remember</div><div class=rule></div>\n<div class=big style="font-size:84px">Praise doesn\'t make it better.<br><em>Silence doesn\'t make it worse.</em></div>\n<div class=cta>Send this to the friend<br>who <em>refreshes their post</em> every minute.</div>\n' + STOIC_FOLLOW),
]
