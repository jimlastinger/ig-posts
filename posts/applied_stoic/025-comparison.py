import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "tools"))
from lib import *

ACCOUNT = 'applied_stoic'
THEME = 'parchment'
SOURCES = ['https://classics.mit.edu/Epictetus/epicench.html']

CAPTION = """"I am richer than you, therefore I am better." Epictetus called that reasoning unconnected: richer only means more property. And you, he said, are neither property nor style.

Next time you scroll past someone's big news, fix the sentence.

Source: Epictetus, Enchiridion 44 and 25, tr. Elizabeth Carter (MIT Internet Classics Archive).

#stoicism #epictetus #comparison #selfworth #mindset #stoic"""

SLIDES = [
    ('I', '<div class=kick>Applied Stoicism</div><div class=rule></div>\n<div class=hook style="font-size:114px">They got the promotion. <em>You got the comparison.</em></div>\n<div class=sub>Epictetus found<br><em>the flaw in the logic.</em></div>'),
    ('II', "<div class=kick>Who&rsquo;s talking</div><div class=rule></div>\n<h2>Epictetus, the teacher.</h2>\n<p>Born a slave in the Roman Empire and later freed, he became one of the best-known Stoic teachers of his time.</p>\n<p class=strong>His student Arrian wrote down his teaching. The <i>Enchiridion</i>, or handbook, is the short version.</p>"),
    ('III', '<div class=kick>The bad math</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:72px">These reasonings are unconnected: &ldquo;I am richer than you, therefore I am better&rdquo;; &ldquo;I am more eloquent than you, therefore I am better.&rdquo; The connection is rather this: &ldquo;I am richer than you, therefore my property is greater than yours;&rdquo; &hellip;</div>\n<div class=cite>Epictetus &middot; Enchiridion 44 &middot; tr. Elizabeth Carter</div>'),
    ('IV', '<div class=kick>The punchline</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:104px">But you, after all, are neither property nor style.</div>\n<div class=cite>Epictetus &middot; Enchiridion 44 &middot; tr. Elizabeth Carter</div>\n<div class=note>Their house is bigger. That says something about the house, not about them, and not about you.</div>'),
    ('V', '<div class=kick>Your version</div><div class=rule></div>\n<h2>The scroll that ruins your evening.</h2>\n<p>A former classmate&rsquo;s new title. A friend&rsquo;s salary. The neighbor&rsquo;s new car.</p>\n<p class=strong>Your brain skips a step: &ldquo;They have more, so they are more.&rdquo; Epictetus says that step doesn&rsquo;t follow.</p>'),
    ('VI', '<div class=kick>When someone is picked first</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:72px">Is anyone preferred before you at an entertainment, or in a compliment, or in being admitted to a consultation? If these things are good, you ought to be glad that he has gotten them; and if they are evil, don&rsquo;t be grieved that you have not gotten them.</div>\n<div class=cite>Epictetus &middot; Enchiridion 25 &middot; tr. Elizabeth Carter</div>'),
    ('VII', '<div class=kick>Try it today</div><div class=rule></div>\n<h2>Fix the sentence.</h2>\n<ul class=steps>\n<li><span class=n>1</span><span class=t><b>Catch it.</b> Notice the moment you compare.</span></li>\n<li><span class=n>2</span><span class=t><b>Rewrite it.</b> Not &ldquo;they&rsquo;re better than me.&rdquo; Just &ldquo;their car is nicer than mine.&rdquo;</span></li>\n<li><span class=n>3</span><span class=t><b>Be glad for them.</b> If it&rsquo;s good, they got something good.</span></li>\n</ul>'),
    ('VIII', '<div class=kick>Remember</div><div class=rule></div>\n<div class=big style="font-size:88px">More stuff is just more stuff.<br><em>It doesn&rsquo;t make anyone more.</em></div>\n<div class=cta>Send this to someone<br>who <em>can&rsquo;t stop scrolling.</em></div>\n' + STOIC_FOLLOW),
]
