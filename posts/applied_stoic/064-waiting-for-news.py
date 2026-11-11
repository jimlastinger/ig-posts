import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "tools"))
from lib import *

ACCOUNT = 'applied_stoic'
THEME = 'fresco'
SOURCES = ['https://monadnock.net/seneca/5.html']

CAPTION = """Waiting to hear back is its own kind of tired. You refresh the inbox and replay every way it could go. Seneca put his finger on it: the waiting mind swings between hope and fear, and both live in a future that hasn't happened yet.

Bust photo: Marcus Cyron, CC BY-SA 3.0 (cropped and toned).
Source: Seneca, Moral Letters to Lucilius, Letter 5, tr. Richard Mott Gummere.

#stoicism #seneca #anxiety #waiting #mindset #stoic"""

SLIDES = [
    ('I', '<div class=kick>Applied Stoicism</div><div class=rule></div>\n<div class=hook>Waiting to hear back. <em>Refreshing again.</em></div>\n<div class=sub>The test results. The job offer.<br><em>Neither is up to you now.</em></div>' + portrait('seneca-1')),
    ('II', "<div class=kick>Who&rsquo;s talking</div><div class=rule></div>\n<h2>Seneca, writing to a friend.</h2>\n<p>In his <i>Moral Letters to Lucilius</i>, the Stoic Seneca gives his friend advice, one letter at a time.</p>\n<p class=strong>In Letter 5 he passes on a line from another Stoic writer, Hecato, about the mind that&rsquo;s stuck waiting.</p>"),
    ('III', '<div class=kick>The line</div>\n<div class=q style="font-size:90px">&ldquo;Cease to hope,&rdquo; he says, &ldquo;and you will cease to fear.&rdquo;</div>\n<div class=cite>Hecato, quoted by Seneca &middot; Letter 5 &middot; tr. Richard Mott Gummere</div>\n<div class=note>Seneca&rsquo;s point: hope and fear are the same habit pointed in two directions.</div>'),
    ('IV', '<div class=kick>Why they travel together</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:72px">&hellip; each alike belongs to a mind that is in suspense, a mind that is fretted by looking forward to the future.</div>\n<div class=cite>Seneca &middot; Letter 5 &middot; tr. Richard Mott Gummere</div>'),
    ('V', '<div class=kick>Your version</div><div class=rule></div>\n<h2>You&rsquo;ve checked your inbox fifty times.</h2>\n<p>In the good version you celebrate. In the bad one you start planning for the worst. Both are scenes you made up, and you&rsquo;re living in both.</p>\n<p class=strong>Today, nothing has happened yet, and today is the only part you can do anything with.</p>'),
    ('VI', '<div class=kick>The way out</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:66px">Many of our blessings bring bane to us; for memory recalls the tortures of fear, while foresight anticipates them. The present alone can make no man wretched.</div>\n<div class=cite>Seneca &middot; Letter 5 &middot; tr. Richard Mott Gummere</div>'),
    ('VII', '<div class=kick>Try it while you wait</div><div class=rule></div>\n<h2>Come back to today.</h2>\n<ul class=steps>\n<li><span class=n>1</span><span class=t><b>Pick</b> two set times a day to check for news. Then close the tab.</span></li>\n<li><span class=n>2</span><span class=t><b>Write</b> one thing you&rsquo;d do in each outcome. Then stop planning.</span></li>\n<li><span class=n>3</span><span class=t><b>Ask</b> what today needs from you, and do that.</span></li>\n</ul>'),
    ('VIII', '<div class=kick>Remember</div><div class=rule></div>\n<div class=big style="font-size:92px">The news isn&rsquo;t here yet.<br><em>Today is.</em></div>\n<div class=cta>Send this to someone<br>who&rsquo;s <em>waiting to hear back.</em></div>\n' + STOIC_FOLLOW),
]
