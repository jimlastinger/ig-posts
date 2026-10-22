import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "tools"))
from lib import *

ACCOUNT = 'applied_stoic'
SOURCES = ['https://classics.mit.edu/Antoninus/meditations.7.seven.html',
           'https://classics.mit.edu/Antoninus/meditations.2.two.html']

CAPTION = """"Live every day like it's your last" usually means go big. Marcus Aurelius meant the opposite: no frenzy, no drifting, no pretending.

Check yourself once today: frantic, numb, or performing? Then do the next thing plainly.

Source: Marcus Aurelius, Meditations 7.69 and 2.11, tr. George Long.

#stoicism #marcusaurelius #meditations #mindfulness #mindset #stoic"""

SLIDES = [
    ('I', '<div class=kick>Applied Stoicism</div><div class=rule></div>\n<div class=hook style="font-size:112px">&ldquo;Live every day like it&rsquo;s <em>your last.&rdquo;</em></div>\n<div class=sub>Marcus Aurelius wrote a version.<br><em>He didn&rsquo;t mean YOLO.</em></div>'),
    ('II', "<div class=kick>Who&rsquo;s talking</div><div class=rule></div>\n<h2>An emperor writing notes to himself.</h2>\n<p>Marcus Aurelius ruled Rome from AD 161 to 180. His <i>Meditations</i> was a private notebook, not a book for readers.</p>\n<p class=strong>In it, &ldquo;every day as the last&rdquo; comes with three warnings attached.</p>"),
    ('III', '<div class=kick>The full line</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:82px">The perfection of moral character consists in this, in passing every day as the last, and in being neither violently excited nor torpid nor playing the hypocrite.</div>\n<div class=cite>Marcus Aurelius &middot; Meditations 7.69 &middot; tr. George Long</div>'),
    ('IV', '<div class=kick>Three ways to get it wrong</div><div class=rule></div>\n<h2>Not the bucket-list binge.</h2>\n<div class=pair><div class=lab>&ldquo;Violently excited&rdquo;</div><div class=val>Cramming every thrill in, because tomorrow might not come.</div>\n<div class=lab>&ldquo;Torpid&rdquo;</div><div class=val>Going numb, because nothing matters anyway.</div>\n<div class=lab>&ldquo;Playing the hypocrite&rdquo;</div><div class=val style="margin-bottom:0">Performing a life instead of living it.</div></div>'),
    ('V', '<div class=kick>Earlier in the notebook</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:90px">Since it is possible that thou mayest depart from life this very moment, regulate every act and thought accordingly.</div>\n<div class=cite>Marcus Aurelius &middot; Meditations 2.11 &middot; tr. George Long</div>\n<div class=note>Not &ldquo;do more.&rdquo; Do each thing as if it counts.</div>'),
    ('VI', '<div class=kick>Your version</div><div class=rule></div>\n<h2>Your last day probably looks like a Tuesday.</h2>\n<p>Email, errands, a meeting, dinner. Marcus isn&rsquo;t asking you to skip them for skydiving.</p>\n<p class=strong>He&rsquo;s asking how you&rsquo;d do them if this one were the last: calm, awake, and honest.</p>'),
    ('VII', '<div class=kick>Try it today</div><div class=rule></div>\n<h2>The midday check.</h2>\n<ul class=steps>\n<li><span class=n>1</span><span class=t><b>Frantic?</b> Rushing to squeeze more in. Slow down.</span></li>\n<li><span class=n>2</span><span class=t><b>Numb?</b> Scrolling the hours away. Wake up.</span></li>\n<li><span class=n>3</span><span class=t><b>Performing?</b> Acting for an audience. Drop it.</span></li>\n</ul>'),
    ('VIII', '<div class=kick>Remember</div><div class=rule></div>\n<div class=big style="font-size:88px">Not louder.<br><em>Just awake, and honest.</em></div>\n<div class=cta>Send this to someone<br>who says <em>&ldquo;YOLO.&rdquo;</em></div>\n' + STOIC_FOLLOW),
]
