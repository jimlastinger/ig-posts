import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "tools"))
from lib import *

ACCOUNT = 'applied_stoic'
THEME = 'marble'
SOURCES = ['https://classics.mit.edu/Antoninus/meditations.8.eight.html']

CAPTION = """The bookmark hasn't moved in a month, and you feel bad about it. Marcus Aurelius wrote himself a note about that exact excuse: maybe there's no time to read today, but there's still time to keep your ego in check and stay patient with ungrateful people. That part doesn't need a free evening.

Bust photo: Pierre-Selim, CC BY-SA 3.0 (cropped and toned).
Source: Marcus Aurelius, Meditations 8.8, tr. George Long.

#stoicism #marcusaurelius #reading #books #mindset #stoic"""

SLIDES = [
    ('I', '<div class=kick>Applied Stoicism</div><div class=rule></div>\n<div class=hook>The book on your nightstand. <em>Same page for a month.</em></div>\n<div class=sub>No time to read.<br><em>Again.</em></div>' + portrait('marcus-1')),
    ('II', "<div class=kick>Who&rsquo;s talking</div><div class=rule></div>\n<h2>Marcus Aurelius, the emperor.</h2>\n<p>He ruled Rome and kept private notes to himself. We call them the <i>Meditations</i>.</p>\n<p class=strong>In Book 8 he answers an excuse you&rsquo;ve probably made.</p>"),
    ('III', '<div class=kick>The excuse</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:62px">Thou hast not leisure or ability to read. But thou hast leisure or ability to check arrogance: thou hast leisure to be superior to pleasure and pain: thou hast leisure to be superior to love of fame, and not to be vexed at stupid and ungrateful people, nay even to care for them.</div>\n<div class=cite>Marcus Aurelius &middot; Meditations 8.8 &middot; tr. George Long</div>'),
    ('IV', '<div class=kick>Your version</div><div class=rule></div>\n<h2>The book can wait. The practice can&rsquo;t.</h2>\n<p>He doesn&rsquo;t call reading useless. He just won&rsquo;t let &ldquo;no time&rdquo; get him off the hook.</p>\n<p class=strong>What the books teach, you can practice anywhere: on the drive to work, or at the next family dinner.</p>'),
    ('V', '<div class=kick>The hard one</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:80px">not to be vexed at stupid and ungrateful people, nay even to care for them.</div>\n<div class=cite>Marcus Aurelius &middot; Meditations 8.8 &middot; tr. George Long</div>\n<div class=note>Vexed means annoyed. And he goes past putting up with them: he says care for them.</div>'),
    ('VI', '<div class=kick>Try it today</div><div class=rule></div>\n<h2>No book required.</h2>\n<ul class=steps>\n<li><span class=n>1</span><span class=t><b>Pick</b> one line from his list: check arrogance, or stay calm with someone ungrateful.</span></li>\n<li><span class=n>2</span><span class=t><b>Practice</b> it once. In the next meeting, let someone else be right.</span></li>\n<li><span class=n>3</span><span class=t><b>Tonight</b>, read one page anyway. One page still counts.</span></li>\n</ul>'),
    ('VII', '<div class=kick>Remember</div><div class=rule></div>\n<div class=big style="font-size:84px">No time to read?<br>There&rsquo;s time to practice.<br><em>Start there.</em></div>\n<div class=cta>Send this to someone<br>with <em>a stack of unread books.</em></div>\n' + STOIC_FOLLOW),
]
