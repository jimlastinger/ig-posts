import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "tools"))
from lib import *

ACCOUNT = 'applied_stoic'
THEME = 'fresco'
SOURCES = ['https://gutenberg.org/files/10661/10661-h/10661-h.htm']

CAPTION = """Moving day. The rooms are empty and you're about to hand back the keys to a place you loved. Epictetus had one sentence for this: "Never say about anything, I have lost it, but say I have restored it." Six years in that place. You're giving it back.

Source: Epictetus, Encheiridion 11, tr. George Long.

#stoicism #epictetus #movingday #lettinggo #dailystoic #stoic"""

SLIDES = [
    ('I', '<div class=kick>Applied Stoicism</div><div class=rule></div>\n<div class=hook>The rooms are empty. You&rsquo;re holding <em>the keys.</em></div>\n<div class=sub>Six years in this place.<br><em>Today you hand them back.</em></div>'),
    ('II', "<div class=kick>Who&rsquo;s talking</div><div class=rule></div>\n<h2>Epictetus, the former slave.</h2>\n<p>He was born a slave, won his freedom and became a teacher. His student Arrian wrote his lessons down, including a short handbook called the <i>Encheiridion</i>.</p>\n<p class=strong>Chapter 11 opens with one line about loss.</p>"),
    ('III', '<div class=kick>One sentence</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:92px">Never say about anything, I have lost it, but say I have restored it.</div>\n<div class=cite>Epictetus &middot; Encheiridion 11 &middot; tr. George Long</div>\n<div class=note>To restore something is to give it back to where it came from.</div>'),
    ('IV', '<div class=kick>Your version</div><div class=rule></div>\n<h2>You didn&rsquo;t lose the apartment.</h2>\n<p>It was never yours for good. You had it for a stretch, and the stretch is over.</p>\n<p class=strong>&ldquo;I lost it&rdquo; sounds like something was taken. &ldquo;I gave it back&rdquo; sounds like a deal that ended on time.</p>'),
    ('V', '<div class=kick>The same move</div><div class=rule></div>\n<h2>It works on more than keys.</h2>\n<p>The job you left last spring, or the old car you finally sold to the neighbor&rsquo;s kid.</p>\n<p class=strong>Each one ended. Calling it given back doesn&rsquo;t make you miss it less. It just stops the sense that you were robbed.</p>'),
    ('VI', '<div class=kick>Try it today</div><div class=rule></div>\n<h2>Change one word.</h2>\n<ul class=steps>\n<li><span class=n>1</span><span class=t><b>Notice</b> the next time you say &ldquo;I lost&rdquo; about something that ended.</span></li>\n<li><span class=n>2</span><span class=t><b>Say</b> it again as &ldquo;I gave it back.&rdquo;</span></li>\n<li><span class=n>3</span><span class=t><b>Name</b> one good thing you got while you had it. Then lock the door behind you.</span></li>\n</ul>'),
    ('VII', '<div class=kick>Remember</div><div class=rule></div>\n<div class=big style="font-size:84px">Not lost.<br><em>Given back.</em></div>\n<div class=cta>Send this to someone<br>who <em>just moved out.</em></div>\n' + STOIC_FOLLOW),
]
