import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "tools"))
from lib import *

ACCOUNT = 'applied_stoic'
THEME = 'parchment'
SOURCES = ['https://classics.mit.edu/Antoninus/meditations.9.nine.html']

CAPTION = """Somebody will take the whole candy bowl tonight. Marcus Aurelius had a question for moments like that: is it possible that shameless people should not be in the world? It isn't, so stop demanding it, and you may find yourself kinder to everyone else.

Source: Marcus Aurelius, Meditations 9.42, tr. George Long.

#stoicism #marcusaurelius #halloween #patience #mindset #stoic"""

SLIDES = [
    ('I', '<div class=kick>Applied Stoicism</div><div class=rule></div>\n<div class=hook style="font-size:100px">Someone will take <em>the whole bowl</em> tonight.</div>\n<div class=sub>A Roman emperor had a question<br><em>for exactly that moment.</em></div>'),
    ('II', "<div class=kick>Who&rsquo;s talking</div><div class=rule></div>\n<h2>A ruler who expected rudeness.</h2>\n<p>Marcus Aurelius ruled the Roman Empire from AD 161 to 180.</p>\n<p class=strong>He ends Book Nine of his private notebook, the <i>Meditations</i>, with advice for the moment someone behaves badly.</p>"),
    ('III', '<div class=kick>The question</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:66px">When thou art offended with any man&rsquo;s shameless conduct, immediately ask thyself, Is it possible, then, that shameless men should not be in the world? It is not possible. Do not, then, require what is impossible.</div>\n<div class=cite>Marcus Aurelius &middot; Meditations 9.42 &middot; tr. George Long</div>'),
    ('IV', '<div class=kick>Your version</div><div class=rule></div>\n<h2>The bowl. The line. The parking spot.</h2>\n<p>The kid who grabs five handfuls. The driver who cuts in. The person who takes the spot you were waiting for.</p>\n<p class=strong>You can be annoyed, or you can ask his question. A world with zero shameless people was never on offer.</p>'),
    ('V', '<div class=kick>The surprise</div><div class=rule></div>\n<h2>It makes you kinder.</h2>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:58px">&hellip;thou wilt become more kindly disposed towards every one individually.</div>\n<div class=cite>Meditations 9.42 &middot; tr. George Long</div>\n<p class=strong style="margin-top:40px">Stop expecting perfection from people, and each one stops feeling like a personal insult.</p>'),
    ('VI', '<div class=kick>Try it tonight</div><div class=rule></div>\n<h2>Ask the question.</h2>\n<ul class=steps>\n<li><span class=n>1</span><span class=t><b>Catch it:</b> the moment someone&rsquo;s behavior makes you bristle.</span></li>\n<li><span class=n>2</span><span class=t><b>Ask:</b> could a world exist without people like this?</span></li>\n<li><span class=n>3</span><span class=t><b>Answer honestly:</b> no. Then let it pass and stay kind.</span></li>\n</ul>'),
    ('VII', '<div class=kick>Remember</div><div class=rule></div>\n<div class=big style="font-size:92px">Don&rsquo;t require<br><em>what is impossible.</em></div>\n<div class=cta>Send this to someone<br>who <em>is handing out candy tonight.</em></div>\n' + STOIC_FOLLOW),
]
