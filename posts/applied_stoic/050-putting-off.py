import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "tools"))
from lib import *

ACCOUNT = 'applied_stoic'
THEME = 'bronze'
SOURCES = ['https://classics.mit.edu/Antoninus/meditations.2.two.html']

CAPTION = """The clocks fell back last night, so today has one extra hour. Marcus Aurelius would ask what you plan to do with it, because the thing you keep putting off won't wait forever. Spend the hour on it.

Source: Marcus Aurelius, Meditations 2.4, tr. George Long.

#stoicism #marcusaurelius #procrastination #timemanagement #mindset #stoic"""

SLIDES = [
    ('I', '<div class=kick>Applied Stoicism</div><div class=rule></div>\n<div class=hook style="font-size:104px">You got <em>an hour back</em> last night.</div>\n<div class=sub>The clocks fell back.<br><em>A Roman emperor would ask what it&rsquo;s for.</em></div>'),
    ('II', "<div class=kick>Who&rsquo;s talking</div><div class=rule></div>\n<h2>A ruler who wrote to himself.</h2>\n<p>Marcus Aurelius ruled the Roman Empire from AD 161 to 180.</p>\n<p class=strong>Early in Book Two of his private notebook, the <i>Meditations</i>, he scolds himself for delaying.</p>"),
    ('III', '<div class=kick>The line</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:68px">Remember how long thou hast been putting off these things, and how often thou hast received an opportunity from the gods, and yet dost not use it.</div>\n<div class=cite>Marcus Aurelius &middot; Meditations 2.4 &middot; tr. George Long</div>'),
    ('IV', '<div class=kick>Your version</div><div class=rule></div>\n<h2>The call. The form. The first page.</h2>\n<p>The appointment you keep meaning to book. The email you keep meaning to answer. The project you keep saying you&rsquo;ll start next week.</p>\n<p class=strong>Every free hour is another chance to do it. Most of them go somewhere else.</p>'),
    ('V', '<div class=kick>The deadline</div><div class=rule></div>\n<h2>The time is not unlimited.</h2>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:56px">&hellip;a limit of time is fixed for thee, which if thou dost not use for clearing away the clouds from thy mind, it will go and thou wilt go, and it will never return.</div>\n<div class=cite>Meditations 2.4 &middot; tr. George Long</div>'),
    ('VI', '<div class=kick>Try it today</div><div class=rule></div>\n<h2>Spend the extra hour.</h2>\n<ul class=steps>\n<li><span class=n>1</span><span class=t><b>Name it:</b> the one thing you have put off the longest.</span></li>\n<li><span class=n>2</span><span class=t><b>Shrink it:</b> what part of it fits in one hour?</span></li>\n<li><span class=n>3</span><span class=t><b>Start now:</b> before the hour goes where the others went.</span></li>\n</ul>'),
    ('VII', '<div class=kick>Remember</div><div class=rule></div>\n<div class=big style="font-size:92px">It will go,<br><em>and it will never return.</em></div>\n<div class=cta>Send this to someone<br>who <em>keeps saying &ldquo;next week.&rdquo;</em></div>\n' + STOIC_FOLLOW),
]
