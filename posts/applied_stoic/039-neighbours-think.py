import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "tools"))
from lib import *

ACCOUNT = 'applied_stoic'
SOURCES = ['https://classics.mit.edu/Antoninus/meditations.12.twelve.html']

CAPTION = """Marcus Aurelius wondered why we love ourselves most, yet value other people's opinion of us more than our own. Before you post, buy or say something tomorrow, ask whose opinion you are working for.

Source: Marcus Aurelius, Meditations 12.4, tr. George Long.

#stoicism #marcusaurelius #selfworth #mindset #confidence #stoic"""

SLIDES = [
    ('I', '<div class=kick>Applied Stoicism</div><div class=rule></div>\n<div class=hook style="font-size:104px">You love yourself most. <em>So why do their opinions win?</em></div>\n<div class=sub>A Roman emperor wondered the same thing.<br><em>He wrote it down.</em></div>'),
    ('II', "<div class=kick>Who&rsquo;s talking</div><div class=rule></div>\n<h2>A man everyone watched.</h2>\n<p>Marcus Aurelius ruled the Roman Empire from AD 161 to 180. Everyone had an opinion of him.</p>\n<p class=strong>In his private notebook, the <i>Meditations</i>, he asked why other people&rsquo;s opinions matter so much to us.</p>"),
    ('III', '<div class=kick>The puzzle</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:72px">I have often wondered how it is that every man loves himself more than all the rest of men, but yet sets less value on his own opinion of himself than on the opinion of others.</div>\n<div class=cite>Marcus Aurelius &middot; Meditations 12.4 &middot; tr. George Long</div>'),
    ('IV', '<div class=kick>Your version</div><div class=rule></div>\n<h2>Three likes, and the day is ruined.</h2>\n<p>You liked the photo when you took it. You liked the idea before you shared it.</p>\n<p class=strong>Then the numbers came in, and suddenly their opinion counted more than yours.</p>'),
    ('V', '<div class=kick>His test</div><div class=rule></div>\n<h2>Could you say every thought out loud?</h2>\n<p>Marcus imagined a god or a wise teacher telling a man to think nothing he would not say aloud the moment he thought it.</p>\n<p class=strong>His verdict: the man &ldquo;could not endure it even for a single day.&rdquo; We hide our thoughts because we fear what others would think.</p>'),
    ('VI', '<div class=kick>The line</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:76px">So much more respect have we to what our neighbours shall think of us than to what we shall think of ourselves.</div>\n<div class=cite>Marcus Aurelius &middot; Meditations 12.4 &middot; tr. George Long</div>'),
    ('VII', '<div class=kick>Try it tomorrow</div><div class=rule></div>\n<h2>Whose opinion is this for?</h2>\n<ul class=steps>\n<li><span class=n>1</span><span class=t><b>Before you post, buy or speak up,</b> pause for one breath.</span></li>\n<li><span class=n>2</span><span class=t><b>Ask:</b> would I still do this if no one ever saw it?</span></li>\n<li><span class=n>3</span><span class=t><b>If yes, do it</b> and stop checking. If no, you have learned who you were doing it for.</span></li>\n</ul>'),
    ('VIII', '<div class=kick>Remember</div><div class=rule></div>\n<div class=big style="font-size:86px">You are the one who has to live with you.<br><em>Your opinion counts.</em></div>\n<div class=cta>Send this to someone<br>who <em>refreshes for likes.</em></div>\n' + STOIC_FOLLOW),
]
