import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "tools"))
from lib import *

ACCOUNT = 'applied_stoic'
THEME = 'parchment'
SOURCES = ['http://classics.mit.edu/Epictetus/discourses.2.two.html']

CAPTION = """Epictetus started one of his lessons with four words: "Consider who you are." Son, brother, citizen, young or old: he said each of these names, examined, marks out what you owe.

Write down your names today, and ask what each one asks of you.

Source: Epictetus, Discourses 2.10, tr. George Long.

#stoicism #epictetus #identity #family #mindset #stoic"""

SLIDES = [
    ('I', '<div class=kick>Applied Stoicism</div><div class=rule></div>\n<div class=hook style="font-size:112px">Not sure what to do? <em>Start with who you are.</em></div>\n<div class=sub>A four-word lesson<br><em>from a freed slave.</em></div>'),
    ('II', "<div class=kick>Who&rsquo;s talking</div><div class=rule></div>\n<h2>Epictetus, the teacher.</h2>\n<p>Born a slave in the Roman Empire and later freed, he became one of the best-known Stoic teachers of his time.</p>\n<p class=strong>His student Arrian wrote down his lessons as the <i>Discourses</i>. One chapter is titled &ldquo;How we may discover the duties of life from names.&rdquo;</p>"),
    ('III', '<div class=kick>Where it starts</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:150px">Consider who you are.</div>\n<div class=cite>Epictetus &middot; Discourses 2.10 &middot; tr. George Long</div>\n<div class=note>His first answer: a human being, with the power to choose.</div>'),
    ('IV', '<div class=kick>Your names</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:76px">&hellip; if a youth, that you are a youth: if an old man, that you are an old man; for each of such names, if it comes to be examined, marks out the proper duties.</div>\n<div class=cite>Epictetus &middot; Discourses 2.10 &middot; tr. George Long</div>\n<div class=note>His list also includes son, brother and senator.</div>'),
    ('V', '<div class=kick>Your version</div><div class=rule></div>\n<h2>The Saturday with no plan.</h2>\n<p>You could scroll, sleep in, or catch up on work. Nothing tells you which.</p>\n<p class=strong>Epictetus would ask: who are you today? A parent, a friend, a sibling, a neighbor? Each name already has a few jobs attached.</p>'),
    ('VI', '<div class=kick>When you forget</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:96px">You have forgotten who you are and what is your name.</div>\n<div class=cite>Epictetus &middot; Discourses 2.10 &middot; tr. George Long</div>\n<div class=note>What he tells the man who goes and blames his brother.</div>'),
    ('VII', '<div class=kick>Try it today</div><div class=rule></div>\n<h2>Read your own names.</h2>\n<ul class=steps>\n<li><span class=n>1</span><span class=t><b>List three names</b> you carry: daughter, father, partner, friend, boss.</span></li>\n<li><span class=n>2</span><span class=t><b>Write one duty</b> each name marks out for you.</span></li>\n<li><span class=n>3</span><span class=t><b>Do one of them</b> before tonight.</span></li>\n</ul>'),
    ('VIII', '<div class=kick>Remember</div><div class=rule></div>\n<div class=big style="font-size:86px">Your names are a job description.<br><em>Read them.</em></div>\n<div class=cta>Send this to someone<br>who <em>wears a lot of names.</em></div>\n' + STOIC_FOLLOW),
]
