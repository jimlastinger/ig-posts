import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "tools"))
from lib import *

ACCOUNT = 'applied_stoic'
THEME = 'bronze'
SOURCES = ['https://monadnock.net/seneca/28.html']

CAPTION = """Lucilius traveled far and still couldn't shake his gloom. Seneca told him why: "You need a change of soul rather than a change of climate."

Before your next escape, name the thing you're trying to leave behind.

Source: Seneca, Moral Letters to Lucilius, Letter 28, tr. Richard Mott Gummere.

#stoicism #seneca #burnout #travel #mindset #stoic"""

SLIDES = [
    ('I', '<div class=kick>Applied Stoicism</div><div class=rule></div>\n<div class=hook style="font-size:112px">The vacation ended. <em>The restlessness didn&rsquo;t.</em></div>\n<div class=sub>Seneca knew why<br><em>the trip didn&rsquo;t fix it.</em></div>'),
    ('II', "<div class=kick>Who&rsquo;s talking</div><div class=rule></div>\n<h2>Seneca, writing to a friend.</h2>\n<p>In his <i>Moral Letters to Lucilius</i>, the Stoic Seneca gives his friend advice, one letter at a time.</p>\n<p class=strong>In Letter 28, Lucilius has traveled a lot and still feels gloomy. Seneca tells him the problem is coming along for the ride.</p>"),
    ('III', '<div class=kick>The diagnosis</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:70px">Are you surprised, as if it were a novelty, that after such long travel and so many changes of scene you have not been able to shake off the gloom and heaviness of your mind? You need a change of soul rather than a change of climate.</div>\n<div class=cite>Seneca &middot; Letter 28 &middot; tr. Richard M. Gummere</div>'),
    ('IV', '<div class=kick>The luggage you forgot</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:86px">Why do you wonder that globe-trotting does not help you, seeing that you always take yourself with you?</div>\n<div class=cite>Seneca, quoting Socrates &middot; Letter 28 &middot; tr. Richard M. Gummere</div>\n<div class=note>Seneca adds: &ldquo;&hellip; your faults will follow you whithersoever you travel.&rdquo;</div>'),
    ('V', '<div class=kick>Your version</div><div class=rule></div>\n<h2>New city. New job.<br>Same feeling by month three.</h2>\n<p>The trip that didn&rsquo;t cure the burnout. The move that was supposed to be a fresh start.</p>\n<p class=strong>A change of scene can be good. But if the restlessness is inside you, it gets a window seat.</p>'),
    ('VI', '<div class=kick>Where the fix starts</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:94px">The knowledge of sin is the beginning of salvation.</div>\n<div class=cite>Seneca, quoting Epicurus &middot; Letter 28 &middot; tr. Richard M. Gummere</div>\n<div class=note>Seneca called it &ldquo;a noble one.&rdquo; You can&rsquo;t fix what you won&rsquo;t name.</div>'),
    ('VII', '<div class=kick>Before your next escape</div><div class=rule></div>\n<h2>Name what you&rsquo;re leaving.</h2>\n<ul class=steps>\n<li><span class=n>1</span><span class=t><b>Write one sentence.</b> &ldquo;I want to get away from ___.&rdquo;</span></li>\n<li><span class=n>2</span><span class=t><b>Ask where it lives.</b> In the place, or in you?</span></li>\n<li><span class=n>3</span><span class=t><b>Work on that part.</b> Then go, and enjoy the trip for what it is.</span></li>\n</ul>'),
    ('VIII', '<div class=kick>Remember</div><div class=rule></div>\n<div class=big style="font-size:86px">You always take yourself with you.<br><em>Change that first.</em></div>\n<div class=cta>Send this to someone<br>who&rsquo;s <em>planning an escape.</em></div>\n' + STOIC_FOLLOW),
]
