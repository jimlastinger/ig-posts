import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "tools"))
from lib import *

ACCOUNT = 'applied_stoic'
SOURCES = ['https://classics.mit.edu/Antoninus/meditations.11.eleven.html']

CAPTION = """The myth: Stoics just bottle up their anger. Marcus Aurelius didn't tell himself to swallow it. He wrote out a list of things to think through so the anger had less to feed on.

Next time someone sets you off, run his questions before you reply.

Source: Marcus Aurelius, Meditations 11.18, tr. George Long.

#stoicism #marcusaurelius #anger #emotions #mindset #stoic"""

SLIDES = [
    ('I', '<div class=kick>Stoic myths</div><div class=rule></div>\n<div class=hook style="font-size:112px">&ldquo;Stoics just bottle up their <em>anger.&rdquo;</em></div>\n<div class=sub>That&rsquo;s not what<br><em>the emperor wrote.</em></div>'),
    ('II', "<div class=kick>Who&rsquo;s talking</div><div class=rule></div>\n<h2>A man with a lot to be angry about.</h2>\n<p>Marcus Aurelius ruled the Roman Empire from AD 161 to 180.</p>\n<p class=strong>In his private notebook, the <i>Meditations</i>, he wrote himself a checklist for the moment someone offends him.</p>"),
    ('III', '<div class=kick>Where it starts</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:82px">If any have offended against thee, consider first: What is my relation to men, and that we are made for one another&hellip;</div>\n<div class=cite>Marcus Aurelius &middot; Meditations 11.18 &middot; tr. George Long</div>\n<div class=note>Not &ldquo;hold it in.&rdquo; Think it through.</div>'),
    ('IV', '<div class=kick>The real cost</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:76px">Eighth, consider how much more pain is brought on us by the anger and vexation caused by such acts than by the acts themselves&hellip;</div>\n<div class=cite>Marcus Aurelius &middot; Meditations 11.18 &middot; tr. George Long</div>'),
    ('V', '<div class=kick>Your version</div><div class=rule></div>\n<h2>The coworker who took credit.</h2>\n<p>It took them ten seconds. You spent the evening replaying it, drafting replies, and telling three people.</p>\n<p class=strong>Marcus&rsquo;s point: the anger hurt more than the act.</p>'),
    ('VI', '<div class=kick>Calm is not weak</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:70px">&hellip; mildness and gentleness, as they are more agreeable to human nature, so also are they more manly; and he who possesses these qualities possesses strength, nerves and courage&hellip;</div>\n<div class=cite>Marcus Aurelius &middot; Meditations 11.18 &middot; tr. George Long</div>'),
    ('VII', '<div class=kick>Try it today</div><div class=rule></div>\n<h2>Before you fire back.</h2>\n<ul class=steps>\n<li><span class=n>1</span><span class=t><b>Remember your relation:</b> Marcus&rsquo;s first point is that we are made for one another.</span></li>\n<li><span class=n>2</span><span class=t><b>Weigh the cost:</b> what is hurting more right now, what they did or your anger about it?</span></li>\n<li><span class=n>3</span><span class=t><b>Choose the calm reply.</b> Marcus counted it as strength.</span></li>\n</ul>'),
    ('VIII', '<div class=kick>Remember</div><div class=rule></div>\n<div class=big style="font-size:86px">Stoics don&rsquo;t bury anger.<br><em>They question it.</em></div>\n<div class=cta>Send this to someone<br>who <em>is still mad about it.</em></div>\n' + STOIC_FOLLOW),
]
