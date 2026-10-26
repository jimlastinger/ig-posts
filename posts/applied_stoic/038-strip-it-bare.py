import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "tools"))
from lib import *

ACCOUNT = 'applied_stoic'
THEME = 'bronze'
SOURCES = ['https://classics.mit.edu/Antoninus/meditations.6.six.html']

CAPTION = """Marcus Aurelius looked at fine wine and saw "only a little grape juice." Before you buy the thing everyone wants, describe it in plain words and see what is left.

Source: Marcus Aurelius, Meditations 6.13, tr. George Long.

#stoicism #marcusaurelius #minimalism #mindset #money #stoic"""

SLIDES = [
    ('I', '<div class=kick>Applied Stoicism</div><div class=rule></div>\n<div class=hook style="font-size:108px">The thing in your cart is <em>less than it looks.</em></div>\n<div class=sub>An emperor had a trick for this.<br><em>It still works.</em></div>'),
    ('II', "<div class=kick>Who&rsquo;s talking</div><div class=rule></div>\n<h2>A man who owned the finest of everything.</h2>\n<p>Marcus Aurelius ruled the Roman Empire from AD 161 to 180. The best wine, the best clothes, the purple of an emperor.</p>\n<p class=strong>In his private notebook, he stripped those things down to what they really were.</p>"),
    ('III', '<div class=kick>The line</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:74px">This Falernian is only a little grape juice, and this purple robe some sheep&rsquo;s wool dyed with the blood of a shell-fish.</div>\n<div class=cite>Marcus Aurelius &middot; Meditations 6.13 &middot; tr. George Long</div>\n<div class=note>Falernian: one of the most prized Roman wines.</div>'),
    ('IV', '<div class=kick>The point</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:72px">We ought to lay them bare and look at their worthlessness and strip them of all the words by which they are exalted.</div>\n<div class=cite>Marcus Aurelius &middot; Meditations 6.13 &middot; tr. George Long</div>'),
    ('V', '<div class=kick>Your version</div><div class=rule></div>\n<h2>The ad already did the talking.</h2>\n<p>&ldquo;Iconic.&rdquo; &ldquo;Limited edition.&rdquo; &ldquo;Everyone&rsquo;s wearing it.&rdquo;</p>\n<p class=strong>Take the words away and a sneaker is rubber and cloth. A new phone is glass and metal: the phone you already have, slightly faster.</p>'),
    ('VI', '<div class=kick>His warning</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:76px">Outward show is a wonderful perverter of the reason.</div>\n<div class=cite>Marcus Aurelius &middot; Meditations 6.13 &middot; tr. George Long</div>\n<div class=note>He added that it fools you most when you feel surest the thing is worth it.</div>'),
    ('VII', '<div class=kick>Try it today</div><div class=rule></div>\n<h2>Strip it bare.</h2>\n<ul class=steps>\n<li><span class=n>1</span><span class=t><b>Pick one thing</b> you want to buy this week.</span></li>\n<li><span class=n>2</span><span class=t><b>Describe it in one plain sentence,</b> with no brand and no adjectives.</span></li>\n<li><span class=n>3</span><span class=t><b>Read it back.</b> If you still want it, fine. Now you are choosing the thing, not the words.</span></li>\n</ul>'),
    ('VIII', '<div class=kick>Remember</div><div class=rule></div>\n<div class=big style="font-size:86px">Wine is grape juice.<br><em>See things as they are.</em></div>\n<div class=cta>Send this to someone<br>with <em>a full shopping cart.</em></div>\n' + STOIC_FOLLOW),
]
