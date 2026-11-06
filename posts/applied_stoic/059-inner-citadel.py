import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "tools"))
from lib import *

ACCOUNT = 'applied_stoic'
THEME = 'bronze'
SOURCES = ['https://classics.mit.edu/Antoninus/meditations.8.eight.html']

CAPTION = """Marcus Aurelius called a mind free from passions a citadel. Think of it as a fortress where you decide what comes through the gate, and retreat there when the day gets loud.

Source: Marcus Aurelius, Meditations 8.48, tr. George Long.

#stoicism #marcusaurelius #innerpeace #mindset #resilience #stoic"""

SLIDES = [
    ('I', '<div class=kick>Applied Stoicism</div><div class=rule></div>\n<div class=hook style="font-size:104px">Everyone wants a piece of you. <em>Build a citadel.</em></div>\n<div class=sub>An emperor&rsquo;s fortress<br><em>no one enters without your say.</em></div>'),
    ('II', "<div class=kick>Who&rsquo;s talking</div><div class=rule></div>\n<h2>An emperor writing to himself.</h2>\n<p>Marcus Aurelius ruled the Roman Empire from AD 161 to 180.</p>\n<p class=strong>In his private notebook, the <i>Meditations</i>, he described the one place nothing outside could take.</p>"),
    ('III', '<div class=kick>The citadel</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:62px">Remember that the ruling faculty is invincible, when self-collected it is satisfied with itself, if it does nothing which it does not choose to do&hellip; Therefore the mind which is free from passions is a citadel&hellip;</div>\n<div class=cite>Marcus Aurelius &middot; Meditations 8.48 &middot; tr. George Long</div>'),
    ('IV', '<div class=kick>Your version</div><div class=rule></div>\n<h2>The inbox pings. Then the group chat.</h2>\n<p>Each one is knocking on the gate. It wants you upset or rushed, right now.</p>\n<p class=strong>Marcus&rsquo;s point: they can knock all day. Your mind is unbeatable when it does nothing it does not choose to do.</p>'),
    ('V', '<div class=kick>The gate</div><div class=rule></div>\n<h2>Walls don&rsquo;t fall. Gates get opened.</h2>\n<p>A citadel still gets visitors. You just decide who comes in.</p>\n<p class=strong>Marcus calls the part of you that judges and decides your &ldquo;ruling faculty.&rdquo; Keep it self-collected and the noise stays outside.</p>'),
    ('VI', '<div class=kick>Try it today</div><div class=rule></div>\n<h2>Close the gate for one minute.</h2>\n<ul class=steps>\n<li><span class=n>1</span><span class=t><b>Notice</b> the next thing that demands a reaction.</span></li>\n<li><span class=n>2</span><span class=t><b>Pause</b> and ask: &ldquo;Do I choose to let this in?&rdquo;</span></li>\n<li><span class=n>3</span><span class=t><b>Answer</b> from inside the walls, calm and on your own time.</span></li>\n</ul>'),
    ('VII', '<div class=kick>Remember</div><div class=rule></div>\n<div class=big style="font-size:96px">They can knock.<br><em>You hold the gate.</em></div>\n<div class=cta>Send this to someone<br>who&rsquo;s <em>stretched thin.</em></div>\n' + STOIC_FOLLOW),
]
