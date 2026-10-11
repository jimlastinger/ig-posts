import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "tools"))
from lib import *

ACCOUNT = 'applied_stoic'
THEME = 'bronze'
SOURCES = ['https://classics.mit.edu/Epictetus/epicench.html']

CAPTION = """A delayed flight, a rainy wedding day, a job offer that went to someone else. Epictetus said to stop demanding that it be different and start from what actually happened.

Next time plans break, say the plain fact out loud, then ask what your next good move is.

Source: Epictetus, Enchiridion 8, tr. Elizabeth Carter (MIT Internet Classics Archive).

#stoicism #epictetus #acceptance #mindset #resilience #stoic"""

SLIDES = [
    ('I', '<div class=kick>Applied Stoicism</div><div class=rule></div>\n<div class=hook style="font-size:124px">Your flight just got delayed. <em>Now what?</em></div>\n<div class=sub>One sentence for the day that<br><em>didn&rsquo;t go to plan.</em></div>'),
    ('II', "<div class=kick>Who's talking</div><div class=rule></div>\n<h2>Epictetus didn&rsquo;t get to choose much.</h2>\n<p>He was born a slave in the Roman Empire, later freed, and became one of the most famous teachers of his time.</p>\n<p class=strong>His student Arrian wrote down his teaching. The <i>Enchiridion</i>, or handbook, is the short version.</p>"),
    ('III', '<div class=kick>The line</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:84px">Don&rsquo;t demand that things happen as you wish, but wish that they happen as they do happen, and you will go on well.</div>\n<div class=cite>Epictetus &middot; Enchiridion 8 &middot; tr. Elizabeth Carter</div>\n<div class=note>Not &ldquo;like it.&rdquo; Not &ldquo;pretend.&rdquo; Stop arguing with what already happened.</div>'),
    ('IV', '<div class=kick>Gate 14, 6:40 p.m.</div><div class=rule></div>\n<h2>The board says: delayed three hours.</h2>\n<p>You can demand that it not be true: refresh the app, glare at the desk agent, replay the connection you&rsquo;ll miss.</p>\n<p class=strong>Or you can start from the fact. Rebook, eat, call home. The delay is the same either way. Your evening isn&rsquo;t.</p>'),
    ('V', '<div class=kick>Same rule, other days</div><div class=rule></div>\n<div class=pair><div class=lab>It rains on the wedding</div><div class=val>Demanding sun won&rsquo;t move a cloud. Wishing for the day you got lets you enjoy it.</div>\n<div class=lab>The offer goes to someone else</div><div class=val style="margin-bottom:0">The decision is made. Your next application isn&rsquo;t.</div></div>'),
    ('VI', '<div class=kick>Next time plans break</div><div class=rule></div>\n<h2>Three steps:</h2>\n<ul class=steps>\n<li><span class=n>1</span><span class=t><b>Say the fact</b> in one plain sentence. &ldquo;The flight leaves at 9:40.&rdquo;</span></li>\n<li><span class=n>2</span><span class=t><b>Catch the &ldquo;should.&rdquo;</b> &ldquo;It shouldn&rsquo;t be late.&rdquo; Drop it.</span></li>\n<li><span class=n>3</span><span class=t><b>Ask:</b> given what happened, what&rsquo;s my next good move?</span></li>\n</ul>'),
    ('VII', '<div class=kick>Remember</div><div class=rule></div>\n<div class=big style="font-size:84px">You can&rsquo;t edit what happened.<br><em>You can stop fighting it.</em></div>\n<div class=cta>Send this to someone<br>whose plans just <em>fell apart.</em></div>\n' + STOIC_FOLLOW),
]
