import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "tools"))
from lib import *

ACCOUNT = 'applied_stoic'
SOURCES = ['https://monadnock.net/seneca/2.html', 'https://monadnock.net/seneca/16.html']

CAPTION = """The raise comes, and so do the nicer car and the extra subscriptions. Seneca, building on Epicurus, said the one who craves more is the poor one, and that if you live according to opinion, you will never be rich.

Before your next upgrade, write down what "enough" looks like.

Source: Seneca, Moral Letters to Lucilius, Letters 2 and 16, tr. Richard Mott Gummere.

#stoicism #seneca #money #lifestylecreep #minimalism #stoic"""

SLIDES = [
    ('I', '<div class=kick>Applied Stoicism</div><div class=rule></div>\n<div class=hook style="font-size:118px">You got a raise. <em>Why don&rsquo;t you feel richer?</em></div>\n<div class=sub>Seneca described lifestyle creep<br><em>about 2,000 years ago.</em></div>'),
    ('II', "<div class=kick>Who's talking</div><div class=rule></div>\n<h2>Seneca, borrowing from a rival.</h2>\n<p>In his <i>Moral Letters to Lucilius</i>, the Stoic Seneca built these lines on sayings of Epicurus, founder of a competing school.</p>\n<p class=strong>He crossed into &ldquo;the enemy&rsquo;s camp,&rdquo; he wrote, &ldquo;not as a deserter, but as a scout.&rdquo;</p>"),
    ('III', '<div class=kick>The line</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:88px">It is not the man who has too little, but the man who craves more, that is poor.</div>\n<div class=cite>Seneca, on Epicurus &middot; Letter 2 &middot; tr. Richard Mott Gummere</div>\n<div class=note>Poor isn&rsquo;t a balance. It&rsquo;s a gap between what you have and what you want.</div>'),
    ('IV', '<div class=kick>The raise, one year later</div><div class=rule></div>\n<h2>Bigger paycheck. Still tight.</h2>\n<p>A nicer car. A bigger apartment. Three more subscriptions. Each one felt earned.</p>\n<p class=strong>Seneca named the trap: a man who &ldquo;reckons, not his past gains, but his hopes of gains to come.&rdquo;</p>'),
    ('V', '<div class=kick>Why it never stops</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:72px">If you live according to nature, you will never be poor; if you live according to opinion, you will never be rich. Nature&rsquo;s wants are slight; the demands of opinion are boundless.</div>\n<div class=cite>Seneca, quoting Epicurus &middot; Letter 16 &middot; tr. Richard Mott Gummere</div>\n<div class=note>&ldquo;Opinion&rdquo; is wanting what looks good to others. That part has no ceiling.</div>'),
    ('VI', '<div class=kick>So where&rsquo;s the limit?</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:80px">It is, first, to have what is necessary, and, second, to have what is enough.</div>\n<div class=cite>Seneca &middot; Letter 2 &middot; tr. Richard Mott Gummere</div>\n<div class=note>His answer to &ldquo;Do you ask what is the proper limit to wealth?&rdquo;</div>'),
    ('VII', '<div class=kick>Before the next upgrade</div><div class=rule></div>\n<h2>Ask three questions:</h2>\n<ul class=steps>\n<li><span class=n>1</span><span class=t><b>Nature or opinion?</b> Do I need it, or do I want to be seen with it?</span></li>\n<li><span class=n>2</span><span class=t><b>What is enough?</b> Write it down before the raise lands.</span></li>\n<li><span class=n>3</span><span class=t><b>Count past gains.</b> List three things you have that you once wanted.</span></li>\n</ul>'),
    ('VIII', '<div class=kick>Remember</div><div class=rule></div>\n<div class=big style="font-size:84px">More money won&rsquo;t cure wanting more.<br><em>Deciding what&rsquo;s enough will.</em></div>\n<div class=cta>Send this to a friend<br>who just got <em>a raise.</em></div>\n' + STOIC_FOLLOW),
]
