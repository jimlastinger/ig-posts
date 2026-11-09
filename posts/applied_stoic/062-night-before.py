import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "tools"))
from lib import *

ACCOUNT = 'applied_stoic'
THEME = 'bronze'
SOURCES = ['https://gutenberg.org/cache/epub/10661/pg10661-images.html', 'https://classics.mit.edu/Epictetus/discourses.2.two.html']

CAPTION = """Wide awake the night before a big presentation? Epictetus noticed that a singer who's calm singing alone gets nervous on stage because now he wants applause, and the applause isn't up to him. Get ready for the part that is, then go to sleep.

Source: Epictetus, Discourses 2.13, tr. George Long.

#stoicism #epictetus #anxiety #publicspeaking #work #stoic"""

SLIDES = [
    ('I', '<div class=kick>Applied Stoicism</div><div class=rule></div>\n<div class=hook style="font-size:104px">Big presentation tomorrow. <em>Wide awake at 1 a.m.</em></div>\n<div class=sub>The slides are done.<br><em>So what are you actually worried about?</em></div>'),
    ('II', "<div class=kick>Who&rsquo;s talking</div><div class=rule></div>\n<h2>Epictetus, the teacher.</h2>\n<p>Born a slave in the Roman Empire and later freed, he went on to teach Stoic philosophy.</p>\n<p class=strong>His student Arrian wrote down his talks, the <i>Discourses</i>. One of them is about the feeling you have tonight.</p>"),
    ('III', '<div class=kick>The question</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:72px">When I see a man anxious, I say, What does this man want? If he did not want something which is not in his power, how could he be anxious?</div>\n<div class=cite>Epictetus &middot; Discourses 2.13 &middot; tr. George Long</div>'),
    ('IV', '<div class=kick>The singer</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:60px">&hellip; a lute player when he is singing by himself has no anxiety, but when he enters the theatre, he is anxious, even if he has a good voice and plays well on the lute; for he not only wishes to sing well, but also to obtain applause: but this is not in his power.</div>\n<div class=cite>Epictetus &middot; Discourses 2.13 &middot; tr. George Long</div>'),
    ('V', '<div class=kick>Your version</div><div class=rule></div>\n<h2>It went fine in the kitchen.</h2>\n<p>You ran the talk alone and it was fine. Tomorrow you want something extra: the room&rsquo;s nods and your boss&rsquo;s approval.</p>\n<p class=strong>That extra part is what keeps you up. It was never yours to control.</p>'),
    ('VI', '<div class=kick>Where calm comes from</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:96px">Accordingly, where he has skill, there he has confidence.</div>\n<div class=cite>Epictetus &middot; Discourses 2.13 &middot; tr. George Long</div>\n<div class=note>So spend tonight on the skill, not the room.</div>'),
    ('VII', '<div class=kick>Try it tonight</div><div class=rule></div>\n<h2>Sort tomorrow in two.</h2>\n<ul class=steps>\n<li><span class=n>1</span><span class=t><b>Write</b> down what you want from tomorrow, all of it.</span></li>\n<li><span class=n>2</span><span class=t><b>Mark</b> each line: up to me, or up to them.</span></li>\n<li><span class=n>3</span><span class=t><b>Do</b> one thing on an &ldquo;up to me&rdquo; line, like saying your opening out loud twice. Then go to bed.</span></li>\n</ul>'),
    ('VIII', '<div class=kick>Remember</div><div class=rule></div>\n<div class=big style="font-size:92px">Prepare the talk.<br><em>Let go of the applause.</em></div>\n<div class=cta>Send this to someone<br>with a <em>big day tomorrow.</em></div>\n' + STOIC_FOLLOW),
]
