import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "tools"))
from lib import *

ACCOUNT = 'applied_stoic'
THEME = 'parchment'
SOURCES = ['https://classics.mit.edu/Epictetus/epicench.html']

CAPTION = """A stranger's comment can ruin your evening, but only if you agree with it. Epictetus said the sting comes from your own judgment, not the words.

Next time, wait before you reply, and try: "It seemed so to him."

Source: Epictetus, Enchiridion 20, 33 and 42, tr. Elizabeth Carter (MIT Internet Classics Archive).

#stoicism #epictetus #mindset #criticism #selfcontrol #stoic"""

SLIDES = [
    ('I', '<div class=kick>Applied Stoicism</div><div class=rule></div>\n<div class=hook style="font-size:124px">Someone in the comments <em>came for you.</em></div>\n<div class=sub>A former slave wrote the<br>best reply <em>2,000 years ago.</em></div>'),
    ('II', "<div class=kick>Who's talking</div><div class=rule></div>\n<h2>Epictetus knew real insults.</h2>\n<p>He was born a slave in the Roman Empire, later freed, and became one of the most famous teachers of his time.</p>\n<p class=strong>His student Arrian wrote down his teaching. The <i>Enchiridion</i>, or handbook, is the short version.</p>"),
    ('III', '<div class=kick>The line</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:78px">Remember, that not he who gives ill language or a blow insults, but the principle which represents these things as insulting.</div>\n<div class=cite>Epictetus &middot; Enchiridion 20 &middot; tr. Elizabeth Carter</div>\n<div class=note>The words land. Your judgment decides if they wound.</div>'),
    ('IV', '<div class=kick>His first instruction</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:84px">For if you once gain time and respite, you will more easily command yourself.</div>\n<div class=cite>Enchiridion 20</div>\n<div class=note>Translation for 2026: don\'t reply in the first five minutes.</div>'),
    ('V', '<div class=kick>Two replies he recommended</div><div class=rule></div>\n<div class=pair><div class=lab>When they\'re wrong about you</div><div class=val>&ldquo;It seemed so to him.&rdquo; <span style="font-size:34px;color:#a99f8c">(Enchiridion 42)</span></div>\n<div class=lab>When they\'re right about you</div><div class=val style="margin-bottom:0">&ldquo;He does not know my other faults, else he would not have mentioned only these.&rdquo; <span style="font-size:34px;color:#a99f8c">(Enchiridion 33)</span></div></div>'),
    ('VI', '<div class=kick>Next time it happens</div><div class=rule></div>\n<h2>Before you type a word:</h2>\n<ul class=steps>\n<li><span class=n>1</span><span class=t><b>Wait.</b> Close the app. Gain time, as Epictetus said.</span></li>\n<li><span class=n>2</span><span class=t><b>Ask:</b> is it true? If yes, learn. If no, &ldquo;it seemed so to him.&rdquo;</span></li>\n<li><span class=n>3</span><span class=t><b>Then decide</b> if a reply helps anyone. Usually it doesn\'t.</span></li>\n</ul>'),
    ('VII', '<div class=kick>Remember</div><div class=rule></div>\n<div class=big style="font-size:84px">They wrote the comment.<br><em>You decide if it\'s an insult.</em></div>\n<div class=cta>Send this to someone<br>stuck in a <em>comment war.</em></div>\n' + STOIC_FOLLOW),
]
