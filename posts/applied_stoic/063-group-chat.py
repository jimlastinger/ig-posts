import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "tools"))
from lib import *

ACCOUNT = 'applied_stoic'
THEME = 'marble'
SOURCES = ['https://classics.mit.edu/Antoninus/meditations.10.ten.html']

CAPTION = """Someone in the group chat said something that made your jaw tighten, and you're halfway through a reply. Marcus Aurelius kept a note for that moment: first find where you make the same kind of mistake. It's hard to stay furious after that.

Bust photo: Pierre-Selim, CC BY-SA 3.0 (cropped and toned).
Source: Marcus Aurelius, Meditations 10.30, tr. George Long.

#stoicism #marcusaurelius #anger #friendship #mindset #stoic"""

SLIDES = [
    ('I', '<div class=kick>Applied Stoicism</div><div class=rule></div>\n<div class=hook>The group chat. <em>He said it again.</em></div>\n<div class=sub>Your reply is half typed.<br><em>Give it one minute.</em></div>' + portrait('marcus-1')),
    ('II', "<div class=kick>Who&rsquo;s talking</div><div class=rule></div>\n<h2>Marcus Aurelius, the emperor.</h2>\n<p>He ruled Rome from AD 161 to 180 and kept private notes to himself, now called the <i>Meditations</i>.</p>\n<p class=strong>In the tenth book there&rsquo;s a note for the moment right before you hit send.</p>"),
    ('III', '<div class=kick>The note</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:64px">When thou art offended at any man&rsquo;s fault, forthwith turn to thyself and reflect in what like manner thou dost err thyself; for example, in thinking that money is a good thing, or pleasure, or a bit of reputation, and the like.</div>\n<div class=cite>Marcus Aurelius &middot; Meditations 10.30 &middot; tr. George Long</div>'),
    ('IV', '<div class=kick>Your version</div><div class=rule></div>\n<h2>Look at your own messages first.</h2>\n<p>He&rsquo;s wrong about this one. You&rsquo;ve been wrong in the same way: you posted too fast, or argued to win instead of to understand.</p>\n<p class=strong>Once you find your own version of his mistake, the reply you were typing loses its heat.</p>'),
    ('V', '<div class=kick>Why it works</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:62px">For by attending to this thou wilt quickly forget thy anger, if this consideration also is added, that the man is compelled: for what else could he do? or, if thou art able, take away from him the compulsion.</div>\n<div class=cite>Marcus Aurelius &middot; Meditations 10.30 &middot; tr. George Long</div>\n<div class=note>He&rsquo;s acting on what he believes. If you can, change what he believes.</div>'),
    ('VI', '<div class=kick>Try it next time</div><div class=rule></div>\n<h2>Before you reply.</h2>\n<ul class=steps>\n<li><span class=n>1</span><span class=t><b>Put</b> the phone face down for one minute.</span></li>\n<li><span class=n>2</span><span class=t><b>Name</b> one time you made the same kind of mistake.</span></li>\n<li><span class=n>3</span><span class=t><b>Decide</b>: reply to help him see it, or let it go.</span></li>\n</ul>'),
    ('VII', '<div class=kick>Remember</div><div class=rule></div>\n<div class=big style="font-size:92px">Find your version<br><em>of his mistake.</em></div>\n<div class=cta>Send this to someone<br>in a <em>heated group chat.</em></div>\n' + STOIC_FOLLOW),
]
