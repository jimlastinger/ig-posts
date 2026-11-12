import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "tools"))
from lib import *

ACCOUNT = 'applied_stoic'
THEME = 'journal'
SOURCES = ['https://classics.mit.edu/Antoninus/meditations.6.six.html']

CAPTION = """A customer snaps at you over something that isn't your fault, and you replay it for the rest of your shift. Marcus Aurelius had a trick for this from the gym: when a sparring partner hits you too hard, you don't hold a grudge. You keep your guard up and step out of the way.

Bust photo: Pierre-Selim, CC BY-SA 3.0 (cropped and toned).
Source: Marcus Aurelius, Meditations 6.20, tr. George Long.

#stoicism #marcusaurelius #customerservice #retail #work #stoic"""

SLIDES = [
    ('I', '<div class=kick>Applied Stoicism</div><div class=rule></div>\n<div class=hook>A customer yells at you. <em>It wasn&rsquo;t your fault.</em></div>\n<div class=sub>Six hours later you&rsquo;re still<br><em>arguing with him in your head.</em></div>' + portrait('marcus-1')),
    ('II', "<div class=kick>Who&rsquo;s talking</div><div class=rule></div>\n<h2>Marcus Aurelius, the emperor.</h2>\n<p>He ruled Rome and kept a private notebook of reminders to himself. We call it the <i>Meditations</i>.</p>\n<p class=strong>In Book 6 he borrows a lesson from the wrestling floor.</p>"),
    ('III', '<div class=kick>The gym</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:70px">In the gymnastic exercises suppose that a man has torn thee with his nails, and by dashing against thy head has inflicted a wound.</div>\n<div class=cite>Marcus Aurelius &middot; Meditations 6.20 &middot; tr. George Long</div>'),
    ('IV', '<div class=kick>What we do next</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:58px">Well, we neither show any signs of vexation, nor are we offended, nor do we suspect him afterwards as a treacherous fellow; and yet we are on our guard against him, not however as an enemy, nor yet with suspicion, but we quietly get out of his way.</div>\n<div class=cite>Marcus Aurelius &middot; Meditations 6.20 &middot; tr. George Long</div>'),
    ('V', '<div class=kick>Your version</div><div class=rule></div>\n<h2>Register three, 4:45 p.m.</h2>\n<p>He took a swing, and it stung. In a sparring match you&rsquo;d keep your hands up and finish the round. You wouldn&rsquo;t follow him home.</p>\n<p class=strong>Keep your guard up with him. You don&rsquo;t have to carry him into the next six customers.</p>'),
    ('VI', '<div class=kick>The rule for everywhere else</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:62px">Something like this let thy behaviour be in all the other parts of life; let us overlook many things in those who are like antagonists in the gymnasium.</div>\n<div class=cite>Marcus Aurelius &middot; Meditations 6.20 &middot; tr. George Long</div>'),
    ('VII', '<div class=kick>Try it next shift</div><div class=rule></div>\n<h2>Step out of the way.</h2>\n<ul class=steps>\n<li><span class=n>1</span><span class=t><b>Name</b> it to yourself: &ldquo;That one hit hard. Shake it off.&rdquo;</span></li>\n<li><span class=n>2</span><span class=t><b>Do</b> the one thing the job needs: fix it, refund it, or call a manager.</span></li>\n<li><span class=n>3</span><span class=t><b>Greet</b> the next person the way you would have if he&rsquo;d never shown up.</span></li>\n</ul>'),
    ('VIII', '<div class=kick>Remember</div><div class=rule></div>\n<div class=q style="font-size:66px">For it is in our power, as I said, to get out of the way, and to have no suspicion nor hatred.</div>\n<div class=cite>Marcus Aurelius &middot; Meditations 6.20 &middot; tr. George Long</div>\n<div class=cta>Send this to someone<br>who <em>works the front counter.</em></div>\n' + STOIC_FOLLOW),
]
