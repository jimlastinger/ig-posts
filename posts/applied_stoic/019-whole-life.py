import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "tools"))
from lib import *

ACCOUNT = 'applied_stoic'
THEME = 'parchment'
SOURCES = ['https://classics.mit.edu/Antoninus/meditations.8.eight.html']

CAPTION = """At 2 a.m. your mind stacks every future problem into one weight. Marcus Aurelius told himself not to think of the whole of his life at once, and to ask what in this moment is actually past bearing.

Next time it all piles up, shrink it to the next hour.

Source: Marcus Aurelius, Meditations 8.36, tr. George Long.

#stoicism #marcusaurelius #overwhelm #anxiety #meditations #stoic"""

SLIDES = [
    ('I', '<div class=kick>Applied Stoicism</div><div class=rule></div>\n<div class=hook style="font-size:118px">It&rsquo;s 2 a.m. and your <em>whole life</em> is on the ceiling.</div>\n<div class=sub>Marcus Aurelius had a fix for that.<br><em>Make it smaller.</em></div>'),
    ('II', "<div class=kick>Who&rsquo;s talking</div><div class=rule></div>\n<h2>Marcus Aurelius, writing to himself.</h2>\n<p>He ruled Rome from AD 161 to 180. <i>Meditations</i> was his private notebook, never meant for us.</p>\n<p class=strong>In Book 8 he gave himself a rule for when everything piles up at once.</p>"),
    ('III', '<div class=kick>The rule</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:76px">Do not disturb thyself by thinking of the whole of thy life. Let not thy thoughts at once embrace all the various troubles which thou mayest expect to befall thee.</div>\n<div class=cite>Marcus Aurelius &middot; Meditations 8.36 &middot; tr. George Long</div>\n<div class=note>In plain English: don&rsquo;t load every future problem onto tonight.</div>'),
    ('IV', '<div class=kick>The 2 a.m. spiral</div><div class=rule></div>\n<h2>Money. Kids. Career. All at once.</h2>\n<p>Rent next month. The review next quarter. Retirement in thirty years. Your mind stacks them into one weight.</p>\n<p class=strong>None of it is happening right now. Only the lying awake is.</p>'),
    ('V', '<div class=kick>The question he asked</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:80px">On every occasion ask thyself, What is there in this which is intolerable and past bearing? For thou wilt be ashamed to confess.</div>\n<div class=cite>Marcus Aurelius &middot; Meditations 8.36 &middot; tr. George Long</div>\n<div class=note>Look at this hour on its own. You&rsquo;ll find you can bear it.</div>'),
    ('VI', '<div class=kick>Only the present</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:76px">Remember that neither the future nor the past pains thee, but only the present. But this is reduced to a very little, if thou only circumscribest it &hellip;</div>\n<div class=cite>Marcus Aurelius &middot; Meditations 8.36 &middot; tr. George Long</div>\n<div class=note>Circumscribe: draw a line around it. Make the present small enough to hold.</div>'),
    ('VII', '<div class=kick>Tonight, try this</div><div class=rule></div>\n<h2>Shrink it to the next hour.</h2>\n<ul class=steps>\n<li><span class=n>1</span><span class=t><b>Write it all down.</b> Every worry on one list. Then close the notebook.</span></li>\n<li><span class=n>2</span><span class=t><b>Draw the line.</b> What do I have to handle in the next hour? Usually: sleep.</span></li>\n<li><span class=n>3</span><span class=t><b>Ask his question.</b> Is this hour past bearing? Answer honestly.</span></li>\n</ul>'),
    ('VIII', '<div class=kick>Remember</div><div class=rule></div>\n<div class=big style="font-size:84px">You don&rsquo;t have to carry your whole life tonight.<br><em>Just the next hour.</em></div>\n<div class=cta>Send this to a friend<br>who&rsquo;s <em>up at 2 a.m.</em></div>\n' + STOIC_FOLLOW),
]
