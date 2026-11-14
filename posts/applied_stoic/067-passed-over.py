import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "tools"))
from lib import *

ACCOUNT = 'applied_stoic'
THEME = 'fresco'
SOURCES = ['https://gutenberg.org/files/10661/10661-h/10661-h.htm']

CAPTION = """Someone else got the promotion, and you keep replaying the meeting where it was announced. Epictetus would ask what the job cost the person who got it. That person paid a price you didn't, so decide whether it's worth paying next time. Wanting the prize without paying is the one option Epictetus calls silly.

Source: Epictetus, Encheiridion 25, tr. George Long.

#stoicism #epictetus #promotion #career #mindset #stoic"""

SLIDES = [
    ('I', '<div class=kick>Applied Stoicism</div><div class=rule></div>\n<div class=hook>The promotion went to him. <em>Again.</em></div>\n<div class=sub>You did the work.<br><em>He got the title.</em></div>'),
    ('II', "<div class=kick>Who&rsquo;s talking</div><div class=rule></div>\n<h2>Epictetus, the former slave.</h2>\n<p>He was born a slave, won his freedom and became a teacher. His student Arrian wrote his lessons down, including a short handbook called the <i>Encheiridion</i>.</p>\n<p class=strong>Chapter 25 is about watching someone else get picked.</p>"),
    ('III', '<div class=kick>The question</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:84px">Has any man been preferred before you at a banquet, or in being saluted, or in being invited to a consultation?</div>\n<div class=cite>Epictetus &middot; Encheiridion 25 &middot; tr. George Long</div>'),
    ('IV', '<div class=kick>The lettuce</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:58px">Well, what is the price of lettuces? An obolus perhaps. If then a man gives up the obolus, and receives the lettuces, and if you do not give up the obolus and do not obtain the lettuces, do not suppose that you receive less than he who has got the lettuces; for as he has the lettuces, so you have the obolus which you did not give.</div>\n<div class=cite>Epictetus &middot; Encheiridion 25 &middot; tr. George Long</div>\n<div class=note>An obolus was a small Greek coin.</div>'),
    ('V', '<div class=kick>Your version</div><div class=rule></div>\n<h2>The job had a price.</h2>\n<p>Maybe it was the late nights, or the golf with the boss, or saying yes to every project nobody wanted. He paid it. You didn&rsquo;t.</p>\n<p class=strong>So you didn&rsquo;t come away with less. You still have what you didn&rsquo;t spend.</p>'),
    ('VI', '<div class=kick>The choice</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:70px">Give then the price, if it is for your interest, for which it is sold. But if you wish both not to give the price and to obtain the things, you are insatiable and silly.</div>\n<div class=cite>Epictetus &middot; Encheiridion 25 &middot; tr. George Long</div>'),
    ('VII', '<div class=kick>Try it this week</div><div class=rule></div>\n<h2>Before you sulk.</h2>\n<ul class=steps>\n<li><span class=n>1</span><span class=t><b>Name</b> the price. What did the job actually cost the person who got it?</span></li>\n<li><span class=n>2</span><span class=t><b>Decide</b> if you&rsquo;d pay it. If yes, start paying it, and pay it honestly.</span></li>\n<li><span class=n>3</span><span class=t><b>If not</b>, stop wanting the job for free. Keep what you saved.</span></li>\n</ul>'),
    ('VIII', '<div class=kick>Remember</div><div class=rule></div>\n<div class=big style="font-size:84px">He has the lettuce.<br>You kept the coin.<br><em>Pick your price.</em></div>\n<div class=cta>Send this to someone<br>who <em>just got passed over.</em></div>\n' + STOIC_FOLLOW),
]
