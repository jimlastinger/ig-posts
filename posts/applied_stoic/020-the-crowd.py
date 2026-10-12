import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "tools"))
from lib import *

ACCOUNT = 'applied_stoic'
THEME = 'bronze'
SOURCES = ['https://monadnock.net/seneca/7.html']

CAPTION = """Seneca said the thing to avoid above all was crowds, because he came home from them "more greedy, more ambitious," even "more cruel." Today the crowd fits in your pocket.

This week, mute one chat that leaves you worse, and spend that time with someone who makes you better.

Source: Seneca, Moral Letters to Lucilius, Letter 7, tr. Richard Mott Gummere.

#stoicism #seneca #groupchat #digitalwellbeing #mindset #stoic"""

SLIDES = [
    ('I', '<div class=kick>Applied Stoicism</div><div class=rule></div>\n<div class=hook style="font-size:118px">Your group chat leaves you <em>angrier</em> than it found you.</div>\n<div class=sub>Seneca knew the feeling.<br><em>His word for it: the crowd.</em></div>'),
    ('II', "<div class=kick>Who&rsquo;s talking</div><div class=rule></div>\n<h2>Seneca, writing to a friend.</h2>\n<p>In his <i>Moral Letters to Lucilius</i>, the Stoic Seneca takes up a simple question: what should you avoid most?</p>\n<p class=strong>His answer is one word.</p>"),
    ('III', '<div class=kick>The answer</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:88px">Do you ask me what you should regard as especially to be avoided? I say, crowds.</div>\n<div class=cite>Seneca &middot; Letter 7 &middot; tr. Richard M. Gummere</div>\n<div class=note>His reason: what a crowd does to the person in it.</div>'),
    ('IV', '<div class=kick>What it did to him</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:84px">I come home more greedy, more ambitious, more voluptuous, and even more cruel and inhuman.</div>\n<div class=cite>Seneca &middot; Letter 7 &middot; tr. Richard M. Gummere</div>\n<div class=note>That&rsquo;s Seneca, coming home from the gladiator games.</div>'),
    ('V', '<div class=kick>Your crowd</div><div class=rule></div>\n<h2>The chat that sets your mood.</h2>\n<p>Someone&rsquo;s outraged. Then everyone is. You put the phone down an hour later, more irritated than when you picked it up.</p>\n<p class=strong>Seneca had no phone. He still knew what it&rsquo;s like to come home worse than you left.</p>'),
    ('VI', '<div class=kick>The better crowd</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:84px">Associate with those who will make a better man of you. &hellip; The process is mutual; for men learn while they teach.</div>\n<div class=cite>Seneca &middot; Letter 7 &middot; tr. Richard M. Gummere</div>\n<div class=note>Choose who gets your attention, and be that person for someone else.</div>'),
    ('VII', '<div class=kick>This week</div><div class=rule></div>\n<h2>Audit your crowds.</h2>\n<ul class=steps>\n<li><span class=n>1</span><span class=t><b>List them.</b> The chats and feeds you open most.</span></li>\n<li><span class=n>2</span><span class=t><b>Ask Seneca&rsquo;s question.</b> Do I come back from this better, or worse?</span></li>\n<li><span class=n>3</span><span class=t><b>Mute one.</b> Give that time to someone who makes you better.</span></li>\n</ul>'),
    ('VIII', '<div class=kick>Remember</div><div class=rule></div>\n<div class=big style="font-size:84px">Not every crowd is in a stadium.<br><em>Some fit in your pocket.</em></div>\n<div class=cta>Send this to someone<br>in <em>your group chat.</em></div>\n' + STOIC_FOLLOW),
]
