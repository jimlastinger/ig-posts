import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "tools"))
from lib import *

ACCOUNT = 'applied_stoic'
THEME = 'parchment'
SOURCES = ['https://classics.mit.edu/Antoninus/meditations.5.five.html']

CAPTION = """Broke the streak? Marcus Aurelius wrote himself a note for exactly this: don't be disgusted or discouraged, just come back. Return to your practice like a remedy, not a punishment.

Source: Marcus Aurelius, Meditations 5.9, tr. George Long.

#stoicism #marcusaurelius #habits #selfcompassion #discipline #stoic"""

SLIDES = [
    ('I', '<div class=kick>Applied Stoicism</div><div class=rule></div>\n<div class=hook style="font-size:104px">You broke the streak. <em>Now what?</em></div>\n<div class=sub>An emperor&rsquo;s advice<br><em>for the day after you slip.</em></div>'),
    ('II', "<div class=kick>Who&rsquo;s talking</div><div class=rule></div>\n<h2>An emperor with a plan for falling short.</h2>\n<p>Marcus Aurelius ruled the Roman Empire from AD 161 to 180.</p>\n<p class=strong>In his private notebook, the <i>Meditations</i>, he didn&rsquo;t pretend he always lived up to his own rules. He wrote himself instructions for when he didn&rsquo;t.</p>"),
    ('III', '<div class=kick>When you fail</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:62px">Be not disgusted, nor discouraged, nor dissatisfied, if thou dost not succeed in doing everything according to right principles; but when thou [hast] failed, return back again, and be content if the greater part of what thou doest is consistent with man&rsquo;s nature&hellip;</div>\n<div class=cite>Marcus Aurelius &middot; Meditations 5.9 &middot; tr. George Long</div>'),
    ('IV', '<div class=kick>Your version</div><div class=rule></div>\n<h2>Day 12 of the new habit. Then you miss one.</h2>\n<p>The gym, the journal, the no-phone mornings. One bad day, and the voice says: &ldquo;See? You always quit.&rdquo;</p>\n<p class=strong>Marcus&rsquo;s answer: the miss isn&rsquo;t the problem. Not coming back is.</p>'),
    ('V', '<div class=kick>A remedy, not a master</div><div class=rule></div>\n<h2>Come back like you&rsquo;re treating a sore eye.</h2>\n<p>In the same passage he says not to return to philosophy &ldquo;as if she were a master,&rdquo; but the way someone with sore eyes reaches for a sponge and egg, a plaster, or water.</p>\n<p class=strong>You don&rsquo;t punish yourself for needing a remedy. You just use it.</p>'),
    ('VI', '<div class=kick>Try it today</div><div class=rule></div>\n<h2>The no-drama restart.</h2>\n<ul class=steps>\n<li><span class=n>1</span><span class=t><b>Name</b> the slip in one plain sentence. No adjectives.</span></li>\n<li><span class=n>2</span><span class=t><b>Count</b> the days you did show up. That&rsquo;s &ldquo;the greater part.&rdquo;</span></li>\n<li><span class=n>3</span><span class=t><b>Do</b> the smallest version of the habit today.</span></li>\n</ul>'),
    ('VII', '<div class=kick>Remember</div><div class=rule></div>\n<div class=big style="font-size:96px">You slipped.<br><em>Return back again.</em></div>\n<div class=cta>Send this to someone<br>who&rsquo;s <em>starting over.</em></div>\n' + STOIC_FOLLOW),
]
