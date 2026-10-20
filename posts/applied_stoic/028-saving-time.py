import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "tools"))
from lib import *

ACCOUNT = 'applied_stoic'
THEME = 'parchment'
SOURCES = ['https://monadnock.net/seneca/1.html']

CAPTION = """Seneca's first letter to Lucilius carries a warning: "While we are postponing, life speeds by." Money can be earned back. The hour you just scrolled away can't.

Today, do the task you keep moving to tomorrow before anything else.

Source: Seneca, Moral Letters to Lucilius, Letter 1, tr. Richard Mott Gummere.

#stoicism #seneca #procrastination #time #productivity #stoic"""

SLIDES = [
    ('I', '<div class=kick>Applied Stoicism</div><div class=rule></div>\n<div class=hook style="font-size:116px">&ldquo;I&rsquo;ll start tomorrow.&rdquo; <em>Said again today.</em></div>\n<div class=sub>Seneca&rsquo;s first letter<br><em>was about exactly this.</em></div>'),
    ('II', "<div class=kick>Who&rsquo;s talking</div><div class=rule></div>\n<h2>Seneca, writing to a friend.</h2>\n<p>In his <i>Moral Letters to Lucilius</i>, the Stoic Seneca gives his friend advice, one letter at a time.</p>\n<p class=strong>The very first letter is about one thing: how we lose our time, and how to keep it.</p>"),
    ('III', '<div class=kick>The question</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:84px">What man can you show me who places any value on his time, who reckons the worth of each day, who understands that he is dying daily?</div>\n<div class=cite>Seneca &middot; Letter 1 &middot; tr. Richard M. Gummere</div>'),
    ('IV', '<div class=kick>Where it goes</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:90px">The most disgraceful kind of loss, however, is that due to carelessness.</div>\n<div class=cite>Seneca &middot; Letter 1 &middot; tr. Richard M. Gummere</div>\n<div class=note>Not stolen. Not taken. Just let slip.</div>'),
    ('V', '<div class=kick>Your version</div><div class=rule></div>\n<h2>The task that moves<br>to tomorrow, every day.</h2>\n<p>The email you&rsquo;ll answer later. The call you&rsquo;ll make next week. The project that waits for a better time.</p>\n<p class=strong>Each delay feels free. Seneca&rsquo;s point: it&rsquo;s paid for in the one thing you can&rsquo;t earn back.</p>'),
    ('VI', '<div class=kick>The fix</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:82px">Lay hold of to-day&rsquo;s task, and you will not need to depend so much upon to-morrow&rsquo;s. While we are postponing, life speeds by. Nothing, Lucilius, is ours, except time.</div>\n<div class=cite>Seneca &middot; Letter 1 &middot; tr. Richard M. Gummere</div>'),
    ('VII', '<div class=kick>Try it today</div><div class=rule></div>\n<h2>Take back one hour.</h2>\n<ul class=steps>\n<li><span class=n>1</span><span class=t><b>Name it.</b> The one task you keep moving to tomorrow.</span></li>\n<li><span class=n>2</span><span class=t><b>Do it first.</b> Before email, news or your phone.</span></li>\n<li><span class=n>3</span><span class=t><b>Count it.</b> Tonight, write down where today&rsquo;s hours went.</span></li>\n</ul>'),
    ('VIII', '<div class=kick>Remember</div><div class=rule></div>\n<div class=big style="font-size:88px">While we are postponing,<br><em>life speeds by.</em></div>\n<div class=cta>Send this to someone<br>who&rsquo;s <em>starting tomorrow.</em></div>\n' + STOIC_FOLLOW),
]
