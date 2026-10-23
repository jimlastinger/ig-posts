import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "tools"))
from lib import *

ACCOUNT = 'applied_stoic'
THEME = 'bronze'
SOURCES = ['https://classics.mit.edu/Epictetus/epicench.html']

CAPTION = """You can't make your partner, your kids or your friends think or act the way you want. Epictetus said that wish is a wish for "things that belong to others to be your own."

Pick one person who frustrates you and find the other handle.

Source: Epictetus, Enchiridion 1, 14 and 43, tr. Elizabeth Carter.

#stoicism #epictetus #relationships #family #mindset #stoic"""

SLIDES = [
    ('I', '<div class=kick>Applied Stoicism</div><div class=rule></div>\n<div class=hook style="font-size:112px">You can&rsquo;t control the people <em>you love.</em></div>\n<div class=sub>A former slave&rsquo;s rule<br><em>for family, friends and partners.</em></div>'),
    ('II', "<div class=kick>Who&rsquo;s talking</div><div class=rule></div>\n<h2>Epictetus, the teacher.</h2>\n<p>Born a slave in the Roman Empire and later freed, he became one of the best-known Stoic teachers of his time.</p>\n<p class=strong>His student Arrian wrote down his teaching. The <i>Enchiridion</i>, or handbook, opens with one dividing line.</p>"),
    ('III', '<div class=kick>The dividing line</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:76px">Things in our control are opinion, pursuit, desire, aversion, and, in a word, whatever are our own actions.</div>\n<div class=cite>Epictetus &middot; Enchiridion 1 &middot; tr. Elizabeth Carter</div>\n<div class=note>Your actions are on the list. Theirs are not.</div>'),
    ('IV', '<div class=kick>The trap</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:66px">If you wish your children, and your wife, and your friends to live for ever, you are stupid; for you wish to be in control of things which you cannot, you wish for things that belong to others to be your own.</div>\n<div class=cite>Epictetus &middot; Enchiridion 14 &middot; tr. Elizabeth Carter</div>\n<div class=note>Their lives, and their choices, belong to them.</div>'),
    ('V', '<div class=kick>Your version</div><div class=rule></div>\n<h2>The argument you keep having.</h2>\n<p>Your partner is late again. Your brother won&rsquo;t call back. Your teenager won&rsquo;t listen. You replay it, rehearse the speech, and wait for them to change.</p>\n<p class=strong>Epictetus would say: their choices were never on your list. Your response is.</p>'),
    ('VI', '<div class=kick>The other handle</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:72px">Everything has two handles, the one by which it may be carried, the other by which it cannot.</div>\n<div class=cite>Epictetus &middot; Enchiridion 43 &middot; tr. Elizabeth Carter</div>\n<div class=note>His example: if your brother acts unjustly, don&rsquo;t grab his action by &ldquo;the handle of his injustice&rdquo; but by the other one, &ldquo;that he is your brother.&rdquo;</div>'),
    ('VII', '<div class=kick>Try it today</div><div class=rule></div>\n<h2>Sort one relationship.</h2>\n<ul class=steps>\n<li><span class=n>1</span><span class=t><b>Name the person</b> and the thing you keep wanting them to do.</span></li>\n<li><span class=n>2</span><span class=t><b>Split it:</b> what is their choice, and what is yours?</span></li>\n<li><span class=n>3</span><span class=t><b>Find the other handle:</b> what is still true about them that you value?</span></li>\n</ul>'),
    ('VIII', '<div class=kick>Remember</div><div class=rule></div>\n<div class=big style="font-size:86px">Their choices are theirs.<br><em>Your response is yours.</em></div>\n<div class=cta>Send this to someone<br>who <em>keeps waiting for them to change.</em></div>\n' + STOIC_FOLLOW),
]
