import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "tools"))
from lib import *

ACCOUNT = 'applied_stoic'
THEME = 'parchment'
SOURCES = ['https://classics.mit.edu/Antoninus/meditations.7.seven.html']

CAPTION = """Marcus Aurelius told himself not to be troubled by what hasn't happened yet: when it comes, he will meet it with the same reason he uses today. Tonight, deal with today and let tomorrow wait for you.

Source: Marcus Aurelius, Meditations 7.8, tr. George Long.

#stoicism #marcusaurelius #anxiety #overthinking #mindset #stoic"""

SLIDES = [
    ('I', '<div class=kick>Applied Stoicism</div><div class=rule></div>\n<div class=hook style="font-size:104px">2 a.m. You are already living <em>next week.</em></div>\n<div class=sub>A Roman emperor had a one-line answer.<br><em>He wrote it to himself.</em></div>'),
    ('II', "<div class=kick>Who&rsquo;s talking</div><div class=rule></div>\n<h2>A man with real futures to fear.</h2>\n<p>Marcus Aurelius ruled the Roman Empire from AD 161 to 180, through war and plague.</p>\n<p class=strong>In his private notebook, the <i>Meditations</i>, he kept reminding himself how to face what was coming.</p>"),
    ('III', '<div class=kick>The line</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:74px">Let not future things disturb thee, for thou wilt come to them, if it shall be necessary, having with thee the same reason which now thou usest for present things.</div>\n<div class=cite>Marcus Aurelius &middot; Meditations 7.8 &middot; tr. George Long</div>'),
    ('IV', '<div class=kick>Your version</div><div class=rule></div>\n<h2>The meeting that hasn&rsquo;t happened.</h2>\n<p>You rehearse the hard conversation ten times. You lose the argument in the shower. You read the bad news before it arrives.</p>\n<p class=strong>The future isn&rsquo;t here yet. Only the worry is.</p>'),
    ('V', '<div class=kick>What he means</div><div class=rule></div>\n<h2>You bring the same tools.</h2>\n<p>The mind that handles today&rsquo;s problems will be the one that shows up for next week&rsquo;s.</p>\n<p class=strong>&ldquo;If it shall be necessary&rdquo;: some of what you fear will never need facing at all.</p>'),
    ('VI', '<div class=kick>Try it tonight</div><div class=rule></div>\n<h2>Park the future.</h2>\n<ul class=steps>\n<li><span class=n>1</span><span class=t><b>Write the worry down</b> in one line, with the date it could happen.</span></li>\n<li><span class=n>2</span><span class=t><b>Write one thing</b> you can do about it today. Do it, or plan when.</span></li>\n<li><span class=n>3</span><span class=t><b>Close the notebook.</b> You will meet the rest when you get there.</span></li>\n</ul>'),
    ('VII', '<div class=kick>Remember</div><div class=rule></div>\n<div class=big style="font-size:86px">You don&rsquo;t have to face next week tonight.<br><em>You&rsquo;ll get there.</em></div>\n<div class=cta>Send this to someone<br>who <em>can&rsquo;t switch off at night.</em></div>\n' + STOIC_FOLLOW),
]
