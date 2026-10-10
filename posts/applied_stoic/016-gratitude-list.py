import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "tools"))
from lib import *

ACCOUNT = 'applied_stoic'
THEME = 'parchment'
SOURCES = ['https://classics.mit.edu/Antoninus/meditations.1.one.html']

CAPTION = """Marcus Aurelius ruled Rome, and he opened his private notebook with a list of people and what each one taught him. Not "I'm self-made." A list of names.

Write three lines tonight: "From ___, I learned ___."

Source: Marcus Aurelius, Meditations Book 1, tr. George Long.

#stoicism #marcusaurelius #gratitude #meditations #journaling #stoic"""

SLIDES = [
    ('I', '<div class=kick>Applied Stoicism</div><div class=rule></div>\n<div class=hook style="font-size:118px">The emperor of Rome kept a <em>thank-you list.</em></div>\n<div class=sub>It&rsquo;s the first page of his<br>private notebook. <em>Write yours.</em></div>'),
    ('II', "<div class=kick>Who's talking</div><div class=rule></div>\n<h2>Marcus Aurelius, writing to himself.</h2>\n<p>He ruled Rome from AD 161 to 180. <i>Meditations</i> was his private notebook, never meant for us.</p>\n<p class=strong>Book 1 is a list: the people in his life, and what he learned from each.</p>"),
    ('III', '<div class=kick>Line one</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:84px">From my grandfather Verus I learned good morals and the government of my temper.</div>\n<div class=cite>Marcus Aurelius &middot; Meditations 1.1 &middot; tr. George Long</div>\n<div class=note>Not money. Not status. A temper he learned to govern.</div>'),
    ('IV', '<div class=kick>From his tutor</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:70px">From my governor, to be neither of the green nor of the blue party at the games in the Circus &hellip; and to want little, and to work with my own hands.</div>\n<div class=cite>Meditations 1.5 &middot; tr. George Long</div>\n<div class=note>Green and Blue were chariot-racing teams. His tutor taught him not to be a sports fanatic.</div>'),
    ('V', '<div class=kick>From a teacher</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:66px">From Rusticus I received the impression that my character required improvement and discipline; &hellip; and I am indebted to him for being acquainted with the discourses of Epictetus.</div>\n<div class=cite>Meditations 1.7 &middot; tr. George Long</div>\n<div class=note>Rusticus shared Epictetus &ldquo;out of his own collection.&rdquo;</div>'),
    ('VI', '<div class=kick>How the list ends</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:72px">To the gods I am indebted for having good grandfathers, good parents, a good sister, good teachers, good associates, good kinsmen and friends, nearly everything good.</div>\n<div class=cite>Meditations 1.17 &middot; tr. George Long</div>'),
    ('VII', '<div class=kick>Write yours tonight</div><div class=rule></div>\n<h2>From ___, I learned ___.</h2>\n<ul class=steps>\n<li><span class=n>1</span><span class=t><b>Someone in your family.</b> One habit, not a general &ldquo;everything.&rdquo;</span></li>\n<li><span class=n>2</span><span class=t><b>A teacher, coach or boss.</b> What did they show you by doing it?</span></li>\n<li><span class=n>3</span><span class=t><b>A friend.</b> Then tell one of them.</span></li>\n</ul>'),
    ('VIII', '<div class=kick>Remember</div><div class=rule></div>\n<div class=big style="font-size:84px">He never wrote &ldquo;self&#8209;made.&rdquo;<br><em>He wrote a list of names.</em></div>\n<div class=cta>Send this to someone<br>who&rsquo;s on <em>your list.</em></div>\n' + STOIC_FOLLOW),
]
