import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "tools"))
from lib import *

ACCOUNT = 'applied_stoic'
THEME = 'bronze'
SOURCES = ['https://monadnock.net/seneca/2.html']

CAPTION = """Seneca warned a friend that reading many authors in a hurried way can make you "discursive and unsteady." His fix: stay with a few master thinkers, and each day pick one idea to digest.

Today, close the extra tabs and reread one good book.

Source: Seneca, Moral Letters to Lucilius, Letter 2, tr. Richard Mott Gummere.

#stoicism #seneca #reading #books #focus #stoic"""

SLIDES = [
    ('I', '<div class=kick>Applied Stoicism</div><div class=rule></div>\n<div class=hook style="font-size:116px">40 open tabs. <em>Zero ideas that stuck.</em></div>\n<div class=sub>Seneca had a cure<br><em>for reading everything.</em></div>'),
    ('II', "<div class=kick>Who&rsquo;s talking</div><div class=rule></div>\n<h2>Seneca, writing to a friend.</h2>\n<p>In his <i>Moral Letters to Lucilius</i>, the Stoic Seneca gives his friend advice, one letter at a time.</p>\n<p class=strong>In Letter 2, he praises Lucilius for staying put, then warns him about his reading habits.</p>"),
    ('III', '<div class=kick>The warning</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:82px">You must linger among a limited number of master thinkers, and digest their works, if you would derive ideas which shall win firm hold in your mind. Everywhere means nowhere.</div>\n<div class=cite>Seneca &middot; Letter 2 &middot; tr. Richard M. Gummere</div>'),
    ('IV', '<div class=kick>Why skimming fails</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:80px">&hellip; a plant which is often moved can never grow strong. There is nothing so efficacious that it can be helpful while it is being shifted about. And in reading of many books is distraction.</div>\n<div class=cite>Seneca &middot; Letter 2 &middot; tr. Richard M. Gummere</div>\n<div class=note>An idea needs time to take root.</div>'),
    ('V', '<div class=kick>Your version</div><div class=rule></div>\n<h2>The pile keeps growing.<br>The ideas don&rsquo;t.</h2>\n<p>The unread stack, the podcast queue, the summaries we skim and forget.</p>\n<p class=strong>Seneca&rsquo;s point: taking in more is not the same as keeping more. Go back to the few that are worth it.</p>'),
    ('VI', '<div class=kick>One idea a day</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:80px">&hellip; after you have run over many thoughts, select one to be thoroughly digested that day. This is my own custom &hellip;</div>\n<div class=cite>Seneca &middot; Letter 2 &middot; tr. Richard M. Gummere</div>\n<div class=note>Skim if you must. Keep one thing.</div>'),
    ('VII', '<div class=kick>Try it today</div><div class=rule></div>\n<h2>Read less, keep more.</h2>\n<ul class=steps>\n<li><span class=n>1</span><span class=t><b>Pick one book.</b> One you already know is good. Reread it.</span></li>\n<li><span class=n>2</span><span class=t><b>Close the rest.</b> The extra tabs can wait.</span></li>\n<li><span class=n>3</span><span class=t><b>Write one line.</b> Each night, the one idea you&rsquo;re keeping.</span></li>\n</ul>'),
    ('VIII', '<div class=kick>Remember</div><div class=rule></div>\n<div class=big style="font-size:88px">Everywhere means nowhere.<br><em>Go deep on a few.</em></div>\n<div class=cta>Send this to someone<br>with <em>too many tabs open.</em></div>\n' + STOIC_FOLLOW),
]
