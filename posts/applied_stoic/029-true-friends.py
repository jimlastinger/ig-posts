import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "tools"))
from lib import *

ACCOUNT = 'applied_stoic'
THEME = 'bronze'
SOURCES = ['https://monadnock.net/seneca/3.html']

CAPTION = """Seneca's rule for friendship comes in two steps: judge carefully before you let someone in, then trust them fully once you have. "It is equally faulty to trust everyone and to trust no one."

Think of one friend you've kept at arm's length, and tell them something real this week.

Source: Seneca, Moral Letters to Lucilius, Letter 3, tr. Richard Mott Gummere.

#stoicism #seneca #friendship #trust #relationships #stoic"""

SLIDES = [
    ('I', '<div class=kick>Applied Stoicism</div><div class=rule></div>\n<div class=hook style="font-size:112px">&ldquo;He&rsquo;s a friend. <em>Just don&rsquo;t tell him everything.&rdquo;</em></div>\n<div class=sub>Seneca&rsquo;s friend<br><em>said almost this.</em></div>'),
    ('II', "<div class=kick>Who&rsquo;s talking</div><div class=rule></div>\n<h2>Seneca, writing to a friend.</h2>\n<p>In Letter 3, Lucilius calls a man his &ldquo;friend&rdquo;, then in the next sentence warns Seneca not to discuss everything with him.</p>\n<p class=strong>Seneca&rsquo;s reply: &ldquo;you have in the same letter affirmed and denied that he is your friend.&rdquo;</p>"),
    ('III', '<div class=kick>The rule</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:86px">When friendship is settled, you must trust; before friendship is formed, you must pass judgment.</div>\n<div class=cite>Seneca &middot; Letter 3 &middot; tr. Richard M. Gummere</div>\n<div class=note>Judge first. Then trust.</div>'),
    ('IV', '<div class=kick>Slow in, then all in</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:74px">Ponder for a long time whether you shall admit a given person to your friendship; but when you have decided to admit him, welcome him with all your heart and soul. Speak as boldly with him as with yourself.</div>\n<div class=cite>Seneca &middot; Letter 3 &middot; tr. Richard M. Gummere</div>'),
    ('V', '<div class=kick>Your version</div><div class=rule></div>\n<h2>Hundreds of &ldquo;friends.&rdquo;<br>Few you&rsquo;d call at 2 a.m.</h2>\n<p>We add people fast and open up slowly, or tell strangers too much and hold back from the people who&rsquo;ve earned it.</p>\n<p class=strong>Seneca flips it: be slow to call someone a friend, and generous once you do.</p>'),
    ('VI', '<div class=kick>Both mistakes</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:90px">It is equally faulty to trust everyone and to trust no one.</div>\n<div class=cite>Seneca &middot; Letter 3 &middot; tr. Richard M. Gummere</div>\n<div class=note>&ldquo;Regard him as loyal, and you will make him loyal.&rdquo;</div>'),
    ('VII', '<div class=kick>Try it this week</div><div class=rule></div>\n<h2>Sort your trust.</h2>\n<ul class=steps>\n<li><span class=n>1</span><span class=t><b>Name one.</b> A real friend you still keep at arm&rsquo;s length.</span></li>\n<li><span class=n>2</span><span class=t><b>Tell them something true.</b> A worry, a plan, a mistake.</span></li>\n<li><span class=n>3</span><span class=t><b>Notice the rest.</b> Who gets your secrets without having earned them?</span></li>\n</ul>'),
    ('VIII', '<div class=kick>Remember</div><div class=rule></div>\n<div class=big style="font-size:86px">Judge slowly.<br><em>Then trust completely.</em></div>\n<div class=cta>Send this to the friend<br>you <em>tell everything.</em></div>\n' + STOIC_FOLLOW),
]
