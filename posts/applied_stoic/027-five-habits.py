import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "tools"))
from lib import *

ACCOUNT = 'applied_stoic'
SOURCES = ['https://monadnock.net/seneca/18.html',
           'https://en.wikisource.org/wiki/Moral_letters_to_Lucilius/Letter_18',
           'https://classics.mit.edu/Antoninus/meditations.1.one.html',
           'https://classics.mit.edu/Antoninus/meditations.5.five.html',
           'https://classics.mit.edu/Antoninus/meditations.8.eight.html',
           'https://classics.mit.edu/Antoninus/meditations.10.ten.html']

CAPTION = """Two weeks of Stoicism, boiled down to five habits: practice the worst, get up for the work, keep a thank-you list, shrink it to the next hour, and stop talking about being good and just be it.

Pick one and try it this weekend.

Sources: Seneca, Letter 18, tr. Richard M. Gummere; Marcus Aurelius, Meditations 5.1, 1.1, 8.36 and 10.16, tr. George Long.

#stoicism #marcusaurelius #seneca #habits #selfimprovement #stoic"""

SLIDES = [
    ('I', '<div class=kick>Applied Stoicism</div><div class=rule></div>\n<div class=hook style="font-size:118px">Two weeks. <em>Five Stoic habits.</em></div>\n<div class=sub>The ones worth keeping.<br><em>Save this one.</em></div>'),
    ('II', '<div class=kick>Habit 1 &middot; Practice the worst</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:66px">Set aside a certain number of days, during which you shall be content with the scantiest and cheapest fare, with coarse and rough dress, saying to yourself the while: &ldquo;Is this the condition that I feared?&rdquo;</div>\n<div class=cite>Seneca &middot; Letter 18.5 &middot; tr. Richard M. Gummere</div>\n<div class=note>Try the thing you dread, on purpose, while it&rsquo;s safe.</div>'),
    ('III', '<div class=kick>Habit 2 &middot; Get up for the work</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:84px">In the morning when thou risest unwillingly, let this thought be present&mdash;I am rising to the work of a human being.</div>\n<div class=cite>Marcus Aurelius &middot; Meditations 5.1 &middot; tr. George Long</div>\n<div class=note>The snooze button is an argument. Answer it.</div>'),
    ('IV', '<div class=kick>Habit 3 &middot; Keep a thank-you list</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:88px">From my grandfather Verus I learned good morals and the government of my temper.</div>\n<div class=cite>Marcus Aurelius &middot; Meditations 1.1 &middot; tr. George Long</div>\n<div class=note>Who taught you something good? Name one person tonight.</div>'),
    ('V', '<div class=kick>Habit 4 &middot; Shrink it to the next hour</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:90px">Do not disturb thyself by thinking of the whole of thy life.</div>\n<div class=cite>Marcus Aurelius &middot; Meditations 8.36 &middot; tr. George Long</div>\n<div class=note>When it all piles up, ask what you have to handle in the next hour.</div>'),
    ('VI', '<div class=kick>Habit 5 &middot; Stop talking. Be it.</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:88px">No longer talk at all about the kind of man that a good man ought to be, but be such.</div>\n<div class=cite>Marcus Aurelius &middot; Meditations 10.16 &middot; tr. George Long</div>\n<div class=note>Less theory. More practice.</div>'),
    ('VII', '<div class=kick>This weekend</div><div class=rule></div>\n<h2>Pick one. Just one.</h2>\n<ul class=steps>\n<li><span class=n>1</span><span class=t><b>Choose a habit.</b> The one that stung a little.</span></li>\n<li><span class=n>2</span><span class=t><b>Do it once.</b> Saturday or Sunday, no more planning.</span></li>\n<li><span class=n>3</span><span class=t><b>Write one line.</b> What happened, and whether you&rsquo;ll repeat it.</span></li>\n</ul>'),
    ('VIII', '<div class=kick>Remember</div><div class=rule></div>\n<div class=big style="font-size:88px">Reading about Stoicism is easy.<br><em>Practice is the point.</em></div>\n<div class=cta>Send this to someone<br>who&rsquo;d <em>actually try one.</em></div>\n' + STOIC_FOLLOW),
]
