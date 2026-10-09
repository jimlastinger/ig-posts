import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "tools"))
from lib import *

ACCOUNT = 'applied_stoic'
THEME = 'bronze'
SOURCES = ['https://classics.mit.edu/Antoninus/meditations.10.ten.html']

CAPTION = """It's easy to spend an evening arguing about what a good person, partner or boss should do. Marcus Aurelius told himself to skip the debate and just be one.

Today, trade one opinion about someone else for one small action of your own.

Source: Marcus Aurelius, Meditations 10.15 and 10.16, tr. George Long.

#stoicism #marcusaurelius #meditations #character #selfimprovement #stoic"""

SLIDES = [
    ('I', '<div class=kick>Applied Stoicism</div><div class=rule></div>\n<div class=hook style="font-size:118px">Stop arguing about what a good person <em>should do.</em></div>\n<div class=sub>Marcus Aurelius wrote himself a one-line <em>order.</em></div>'),
    ('II', "<div class=kick>Who's talking</div><div class=rule></div>\n<h2>An emperor taking notes for himself.</h2>\n<p>Marcus Aurelius ruled Rome from AD 161 to 180. His <i>Meditations</i> was a private notebook, not a book for readers.</p>\n<p class=strong>So when he wrote this line, he wasn't lecturing anyone. He was lecturing himself.</p>"),
    ('III', '<div class=kick>The line</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:96px">No longer talk at all about the kind of man that a good man ought to be, but be such.</div>\n<div class=cite>Marcus Aurelius &middot; Meditations 10.16 &middot; tr. George Long</div>\n<div class=note>Less theory. More practice.</div>'),
    ('IV', '<div class=kick>Where we do the talking</div><div class=rule></div>\n<h2>We\'re great at describing good people.</h2>\n<div class=pair><div class=lab>The thread about what a good partner does</div><div class=val>Did you do it today?</div>\n<div class=lab>The rant about what a good boss would say</div><div class=val>Did you say it to your team?</div>\n<div class=lab>The self-help book on kindness</div><div class=val style="margin-bottom:0">Who got the kindness this week?</div></div>'),
    ('V', '<div class=kick>Why he was in a hurry</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:96px">Short is the little which remains to thee of life.</div>\n<div class=cite>Marcus Aurelius &middot; Meditations 10.15 &middot; tr. George Long</div>\n<div class=note>Every hour spent defining goodness is an hour not spent doing it.</div>'),
    ('VI', '<div class=kick>Try this today</div><div class=rule></div>\n<h2>One opinion, one action.</h2>\n<ul class=steps>\n<li><span class=n>1</span><span class=t><b>Catch yourself</b> judging what someone else &ldquo;should&rdquo; do.</span></li>\n<li><span class=n>2</span><span class=t><b>Turn it around:</b> what would that look like from you, today?</span></li>\n<li><span class=n>3</span><span class=t><b>Do one small version</b> of it before you go to bed.</span></li>\n</ul>'),
    ('VII', '<div class=kick>Remember</div><div class=rule></div>\n<div class=big>Don\'t describe a good person.<br><em>Be one.</em></div>\n<div class=cta>Send this to the friend<br>who loves a <em>good debate.</em></div>\n' + STOIC_FOLLOW),
]
