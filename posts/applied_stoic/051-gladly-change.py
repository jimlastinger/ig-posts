import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "tools"))
from lib import *

ACCOUNT = 'applied_stoic'
SOURCES = ['https://classics.mit.edu/Antoninus/meditations.6.six.html']

CAPTION = """Marcus Aurelius promised himself that if anyone could show him he was wrong, he would gladly change his mind. The truth never hurt anyone, he wrote. Staying wrong does.

Source: Marcus Aurelius, Meditations 6.21, tr. George Long.

#stoicism #marcusaurelius #openmind #growthmindset #mindset #stoic"""

SLIDES = [
    ('I', '<div class=kick>Applied Stoicism</div><div class=rule></div>\n<div class=hook style="font-size:104px">When were you <em>last wrong?</em></div>\n<div class=sub>And did you admit it?<br><em>A Roman emperor promised he would.</em></div>'),
    ('II', "<div class=kick>Who&rsquo;s talking</div><div class=rule></div>\n<h2>An emperor who asked to be corrected.</h2>\n<p>Marcus Aurelius ruled the Roman Empire from AD 161 to 180.</p>\n<p class=strong>In his private notebook, the <i>Meditations</i>, even as emperor, he told himself to welcome correction.</p>"),
    ('III', '<div class=kick>The promise</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:70px">If any man is able to convince me and show me that I do not think or act right, I will gladly change; for I seek the truth by which no man was ever injured.</div>\n<div class=cite>Marcus Aurelius &middot; Meditations 6.21 &middot; tr. George Long</div>'),
    ('IV', '<div class=kick>Your version</div><div class=rule></div>\n<h2>The argument. The comment. The meeting.</h2>\n<p>Someone shows you a fact you missed. Your face gets hot, and you start looking for a way to win anyway.</p>\n<p class=strong>Marcus says the truth can&rsquo;t hurt you. What hurts is digging in to protect your pride.</p>'),
    ('V', '<div class=kick>The real harm</div><div class=rule></div>\n<h2>Staying wrong costs more.</h2>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:72px">But he is injured who abides in his error and ignorance.</div>\n<div class=cite>Meditations 6.21 &middot; tr. George Long</div>\n<p class=strong style="margin-top:40px">Losing an argument takes a minute. Keeping a wrong idea can cost you for years.</p>'),
    ('VI', '<div class=kick>Try it this week</div><div class=rule></div>\n<h2>Practice changing your mind.</h2>\n<ul class=steps>\n<li><span class=n>1</span><span class=t><b>Listen:</b> when someone disagrees, hear the whole point first.</span></li>\n<li><span class=n>2</span><span class=t><b>Check:</b> are they right? Look at the evidence, not your pride.</span></li>\n<li><span class=n>3</span><span class=t><b>Say it:</b> &ldquo;You&rsquo;re right, I was wrong.&rdquo; Out loud.</span></li>\n</ul>'),
    ('VII', '<div class=kick>Remember</div><div class=rule></div>\n<div class=big style="font-size:96px">Show me I&rsquo;m wrong,<br><em>and I will gladly change.</em></div>\n<div class=cta>Send this to someone<br>who <em>changed your mind.</em></div>\n' + STOIC_FOLLOW),
]
