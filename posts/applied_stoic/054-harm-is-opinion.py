import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "tools"))
from lib import *

ACCOUNT = 'applied_stoic'
SOURCES = ['https://classics.mit.edu/Antoninus/meditations.4.four.html']

CAPTION = """A curt email, a friend who didn't text back, a comment that stung. Marcus Aurelius noticed that the sentence "I have been harmed" is usually something we add ourselves, and that dropping it takes the harm away with it.

Source: Marcus Aurelius, Meditations 4.7, tr. George Long.

#stoicism #marcusaurelius #mindset #resilience #selfcontrol #stoic"""

SLIDES = [
    ('I', '<div class=kick>Applied Stoicism</div><div class=rule></div>\n<div class=hook style="font-size:104px">That email ruined your morning? <em>Read it again.</em></div>\n<div class=sub>A Roman emperor on the<br><em>sentence that does the damage.</em></div>'),
    ('II', "<div class=kick>Who&rsquo;s talking</div><div class=rule></div>\n<h2>An emperor writing to himself.</h2>\n<p>Marcus Aurelius ruled the Roman Empire from AD 161 to 180.</p>\n<p class=strong>His private notebook, the <i>Meditations</i>, was never meant for us. In Book Four he writes a two-sentence rule about being hurt.</p>"),
    ('III', '<div class=kick>The rule</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:64px">Take away thy opinion, and then there is taken away the complaint, &ldquo;I have been harmed.&rdquo; Take away the complaint, &ldquo;I have been harmed,&rdquo; and the harm is taken away.</div>\n<div class=cite>Marcus Aurelius &middot; Meditations 4.7 &middot; tr. George Long</div>'),
    ('IV', '<div class=kick>Your version</div><div class=rule></div>\n<h2>The two-line email.</h2>\n<p>Your manager replies &ldquo;Fine. Fix it by Friday.&rdquo; No thanks, no greeting.</p>\n<p class=strong>The words on the screen are short. &ldquo;She&rsquo;s annoyed with me, I&rsquo;m in trouble&rdquo; is the part you wrote yourself, and it&rsquo;s the part that hurts.</p>'),
    ('V', '<div class=kick>Two layers</div><div class=rule></div>\n<h2>What happened vs. what you added.</h2>\n<ul class=steps>\n<li><span class=n>1</span><span class=t><b>What happened:</b> a friend didn&rsquo;t text back for two days.</span></li>\n<li><span class=n>2</span><span class=t><b>What you added:</b> &ldquo;They don&rsquo;t care about me.&rdquo;</span></li>\n</ul>\n<p class=strong style="margin-top:36px">Marcus&rsquo;s point: the first is a fact. The second is an opinion, and you can take it back.</p>'),
    ('VI', '<div class=kick>Try it today</div><div class=rule></div>\n<h2>Strip out the complaint.</h2>\n<ul class=steps>\n<li><span class=n>1</span><span class=t><b>Write the fact:</b> only what a camera would have recorded.</span></li>\n<li><span class=n>2</span><span class=t><b>Spot the add-on:</b> find the words &ldquo;I have been harmed&rdquo; hiding in your head.</span></li>\n<li><span class=n>3</span><span class=t><b>Drop it:</b> then decide what, if anything, the fact asks you to do.</span></li>\n</ul>'),
    ('VII', '<div class=kick>Remember</div><div class=rule></div>\n<div class=big style="font-size:96px">Drop the complaint.<br><em>The harm goes with it.</em></div>\n<div class=cta>Send this to someone<br>who <em>rereads texts at midnight.</em></div>\n' + STOIC_FOLLOW),
]
