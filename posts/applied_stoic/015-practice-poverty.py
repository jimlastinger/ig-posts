import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "tools"))
from lib import *

ACCOUNT = 'applied_stoic'
SOURCES = ['https://monadnock.net/seneca/18.html',
           'https://en.wikisource.org/wiki/Moral_letters_to_Lucilius/Letter_18']

CAPTION = """Seneca told a friend to spend a few days living on plain food and rough clothes, then ask: "Is this the condition that I feared?" Usually the fear of having less is worse than having less.

Try it this weekend, even for one day, and tell us how it went.

Source: Seneca, Moral Letters to Lucilius 18, tr. Richard M. Gummere.

#stoicism #seneca #minimalism #frugal #mindset #stoic"""

SLIDES = [
    ('I', '<div class=kick>Applied Stoicism</div><div class=rule></div>\n<div class=hook style="font-size:124px">This weekend, live poor <em>on purpose.</em></div>\n<div class=sub>A rich Roman&rsquo;s cure for the<br>fear of <em>losing it all.</em></div>'),
    ('II', "<div class=kick>Who's talking</div><div class=rule></div>\n<h2>Seneca had plenty to lose.</h2>\n<p>He was a wealthy Roman statesman and an adviser to the emperor Nero. Late in life he wrote letters of advice to his friend Lucilius.</p>\n<p class=strong>In Letter 18, he gave Lucilius a test, and he meant it literally.</p>"),
    ('III', '<div class=kick>The challenge</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:66px">Set aside a certain number of days, during which you shall be content with the scantiest and cheapest fare, with coarse and rough dress, saying to yourself the while: &ldquo;Is this the condition that I feared?&rdquo;</div>\n<div class=cite>Seneca &middot; Letter 18.5 &middot; tr. Richard M. Gummere</div>'),
    ('IV', '<div class=kick>Why do it when life is good</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:86px">If you would not have a man flinch when the crisis comes, train him before it comes.</div>\n<div class=cite>Seneca &middot; Letter 18.6 &middot; tr. Richard M. Gummere</div>\n<div class=note>Soldiers drill in peacetime. Seneca says your mind should too.</div>'),
    ('V', '<div class=kick>Not a costume</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:84px">Let the pallet be a real one, and the coarse cloak; let the bread be hard and grimy.</div>\n<div class=cite>Seneca &middot; Letter 18.7 &middot; tr. Richard M. Gummere</div>\n<div class=note>He wanted &ldquo;a test of yourself instead of a mere hobby.&rdquo;</div>'),
    ('VI', '<div class=kick>The weekend challenge</div><div class=rule></div>\n<h2>One or two days. Real ones.</h2>\n<ul class=steps>\n<li><span class=n>1</span><span class=t><b>Eat plain:</b> rice, beans, bread, water. No delivery.</span></li>\n<li><span class=n>2</span><span class=t><b>Spend nothing</b> beyond the essentials. Wear your oldest clothes.</span></li>\n<li><span class=n>3</span><span class=t><b>Then ask</b> Seneca&rsquo;s question: is this what I was afraid of?</span></li>\n</ul>'),
    ('VII', '<div class=kick>Remember</div><div class=rule></div>\n<div class=big style="font-size:84px">The fear of having less is often worse than <em>having less.</em></div>\n<div class=cta>Send this to the friend<br>who&rsquo;d take the <em>challenge.</em></div>\n' + STOIC_FOLLOW),
]
