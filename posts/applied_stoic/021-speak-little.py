import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "tools"))
from lib import *

ACCOUNT = 'applied_stoic'
SOURCES = ['https://classics.mit.edu/Epictetus/epicench.html']

CAPTION = """Epictetus's advice on talking fits in one line: be mostly silent, or say what is necessary, in few words. And above all, don't make other people the topic.

Today, pick one meeting and speak only when it's needed.

Source: Epictetus, Enchiridion 33, tr. Elizabeth Carter (MIT Internet Classics Archive).

#stoicism #epictetus #mindset #communication #selfcontrol #stoic"""

SLIDES = [
    ('I', '<div class=kick>Applied Stoicism</div><div class=rule></div>\n<div class=hook style="font-size:124px">You said too much in the meeting. <em>Again.</em></div>\n<div class=sub>Epictetus had a rule.<br><em>It fits in one sentence.</em></div>'),
    ('II', "<div class=kick>Who&rsquo;s talking</div><div class=rule></div>\n<h2>Epictetus, the teacher.</h2>\n<p>Born a slave in the Roman Empire and later freed, he became one of the best-known Stoic teachers of his time.</p>\n<p class=strong>His student Arrian wrote down his teaching. The <i>Enchiridion</i>, or handbook, is the short version.</p>"),
    ('III', '<div class=kick>The rule</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:88px">Be for the most part silent, or speak merely what is necessary, and in few words.</div>\n<div class=cite>Epictetus &middot; Enchiridion 33 &middot; tr. Elizabeth Carter</div>\n<div class=note>Not &ldquo;never speak.&rdquo; Speak when it&rsquo;s needed.</div>'),
    ('IV', '<div class=kick>The topics he skipped</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:70px">&hellip; not on any of the common subjects, of gladiators, or horse races, or athletic champions, or feasts, the vulgar topics of conversation; but principally not of men, so as either to blame, or praise, or make comparisons.</div>\n<div class=cite>Epictetus &middot; Enchiridion 33 &middot; tr. Elizabeth Carter</div>'),
    ('V', '<div class=kick>The 2026 version</div><div class=rule></div>\n<h2>Same talk, new arena.</h2>\n<p>His &ldquo;common subjects&rdquo; were gladiators and horse races. Ours are last night&rsquo;s game, the latest drama, and whoever isn&rsquo;t in the room.</p>\n<p class=strong>The talk he warned against most: talk about people, to blame them, praise them or compare them.</p>'),
    ('VI', '<div class=kick>Try it today</div><div class=rule></div>\n<h2>One quiet meeting.</h2>\n<ul class=steps>\n<li><span class=n>1</span><span class=t><b>Pick one meeting</b> or group chat today.</span></li>\n<li><span class=n>2</span><span class=t><b>Before you speak, ask:</b> is this necessary?</span></li>\n<li><span class=n>3</span><span class=t><b>If yes,</b> say it in few words. <b>If no,</b> listen.</span></li>\n</ul>'),
    ('VII', '<div class=kick>Remember</div><div class=rule></div>\n<div class=big style="font-size:88px">Say what&rsquo;s needed.<br><em>Then stop.</em></div>\n<div class=cta>Send this to someone<br>who dreads <em>long meetings.</em></div>\n' + STOIC_FOLLOW),
]
