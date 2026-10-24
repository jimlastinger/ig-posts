import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "tools"))
from lib import *

ACCOUNT = 'applied_stoic'
THEME = 'bronze'
SOURCES = ['https://classics.mit.edu/Antoninus/meditations.6.six.html',
           'https://classics.mit.edu/Antoninus/meditations.7.seven.html']

CAPTION = """Marcus Aurelius had a one-line answer for the urge to get even: "The best way of avenging thyself is not to become like the wrong doer." The next time someone wrongs you, ask what they thought was good before you decide what to do.

Source: Marcus Aurelius, Meditations 6.6 and 7.26, tr. George Long.

#stoicism #marcusaurelius #revenge #forgiveness #mindset #stoic"""

SLIDES = [
    ('I', '<div class=kick>Applied Stoicism</div><div class=rule></div>\n<div class=hook style="font-size:112px">Want to get even? <em>An emperor&rsquo;s version of revenge.</em></div>\n<div class=sub>It takes one line<br><em>and costs you nothing.</em></div>'),
    ('II', "<div class=kick>Who&rsquo;s talking</div><div class=rule></div>\n<h2>A man who could have had anyone punished.</h2>\n<p>Marcus Aurelius ruled the Roman Empire from AD 161 to 180.</p>\n<p class=strong>In his private notebook, the <i>Meditations</i>, he wrote down how he wanted to answer the people who wronged him.</p>"),
    ('III', '<div class=kick>The one line</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:96px">The best way of avenging thyself is not to become like the wrong doer.</div>\n<div class=cite>Marcus Aurelius &middot; Meditations 6.6 &middot; tr. George Long</div>\n<div class=note>That is the whole entry.</div>'),
    ('IV', '<div class=kick>Your version</div><div class=rule></div>\n<h2>The friend who talked behind your back.</h2>\n<p>You heard what they said. You know a few things about them too. One group chat, and you&rsquo;re even.</p>\n<p class=strong>Marcus&rsquo;s point: the moment you do it, you&rsquo;ve become what hurt you.</p>'),
    ('V', '<div class=kick>Before you react</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:78px">When a man has done thee any wrong, immediately consider with what opinion about good or evil he has done wrong.</div>\n<div class=cite>Marcus Aurelius &middot; Meditations 7.26 &middot; tr. George Long</div>'),
    ('VI', '<div class=kick>What it changes</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:82px">For when thou hast seen this, thou wilt pity him, and wilt neither wonder nor be angry.</div>\n<div class=cite>Marcus Aurelius &middot; Meditations 7.26 &middot; tr. George Long</div>\n<div class=note>His next thought: you may think the same thing, or something like it, is good.</div>'),
    ('VII', '<div class=kick>Try it today</div><div class=rule></div>\n<h2>Before you get even.</h2>\n<ul class=steps>\n<li><span class=n>1</span><span class=t><b>Name the wrong</b> in one plain sentence.</span></li>\n<li><span class=n>2</span><span class=t><b>Ask what they thought was good</b> when they did it: being liked, being right, being safe?</span></li>\n<li><span class=n>3</span><span class=t><b>Check your reply:</b> would it make you more like them, or less?</span></li>\n</ul>'),
    ('VIII', '<div class=kick>Remember</div><div class=rule></div>\n<div class=big style="font-size:86px">Don&rsquo;t get even.<br><em>Stay unlike them.</em></div>\n<div class=cta>Send this to someone<br>who <em>is planning a comeback.</em></div>\n' + STOIC_FOLLOW),
]
