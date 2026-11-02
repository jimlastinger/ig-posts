import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "tools"))
from lib import *

ACCOUNT = 'applied_stoic'
THEME = 'parchment'
SOURCES = ['https://classics.mit.edu/Antoninus/meditations.2.two.html']

CAPTION = """Monday pulls your mind in ten directions at once. Marcus Aurelius told himself to do the one thing in front of him, and to do it as if it were his last. That, he wrote, is how you get relief from all the other thoughts.

Source: Marcus Aurelius, Meditations 2.5, tr. George Long.

#stoicism #marcusaurelius #focus #mondaymotivation #mindset #stoic"""

SLIDES = [
    ('I', '<div class=kick>Applied Stoicism</div><div class=rule></div>\n<div class=hook style="font-size:104px">Ten tabs open. <em>One brain.</em></div>\n<div class=sub>A Roman emperor&rsquo;s fix<br><em>for a scattered Monday.</em></div>'),
    ('II', "<div class=kick>Who&rsquo;s talking</div><div class=rule></div>\n<h2>An emperor with too much on his plate.</h2>\n<p>Marcus Aurelius ruled the Roman Empire from AD 161 to 180.</p>\n<p class=strong>In his private notebook, the <i>Meditations</i>, he reminded himself to deal with one thing at a time.</p>"),
    ('III', '<div class=kick>The instruction</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:66px">Every moment think steadily as a Roman and a man to do what thou hast in hand with perfect and simple dignity&hellip; and to give thyself relief from all other thoughts.</div>\n<div class=cite>Marcus Aurelius &middot; Meditations 2.5 &middot; tr. George Long</div>'),
    ('IV', '<div class=kick>Your version</div><div class=rule></div>\n<h2>The inbox. The chat. The list.</h2>\n<p>You start the report, check a message, open the calendar, remember a bill, and an hour later nothing is done.</p>\n<p class=strong>For Marcus, relief comes from giving yourself fully to the thing in your hands.</p>'),
    ('V', '<div class=kick>His rule</div><div class=rule></div>\n<h2>Treat this task like the last one.</h2>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:66px">And thou wilt give thyself relief, if thou doest every act of thy life as if it were the last&hellip;</div>\n<div class=cite>Marcus Aurelius &middot; Meditations 2.5 &middot; tr. George Long</div>\n<p class=strong style="margin-top:36px">If this were the last thing you did, you wouldn&rsquo;t do it half-distracted.</p>'),
    ('VI', '<div class=kick>Try it today</div><div class=rule></div>\n<h2>One thing, done well.</h2>\n<ul class=steps>\n<li><span class=n>1</span><span class=t><b>Pick:</b> name the one task that matters most right now.</span></li>\n<li><span class=n>2</span><span class=t><b>Close:</b> shut every tab and app that isn&rsquo;t that task.</span></li>\n<li><span class=n>3</span><span class=t><b>Finish:</b> do it with care before you touch the next thing.</span></li>\n</ul>'),
    ('VII', '<div class=kick>Remember</div><div class=rule></div>\n<div class=big style="font-size:92px">Do what you have in hand.<br><em>Let the rest wait.</em></div>\n<div class=cta>Send this to someone<br>with <em>too many tabs open.</em></div>\n' + STOIC_FOLLOW),
]
