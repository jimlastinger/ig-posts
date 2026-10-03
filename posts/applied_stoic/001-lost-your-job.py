"""Archived example post. Slides are pre-rendered HTML strings; new posts should use the helpers in tools/lib.py."""
import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "tools"))
from lib import *

ACCOUNT = 'applied_stoic'
SOURCES = ['https://classics.mit.edu/Epictetus/epicench.html']

CAPTION = "Epictetus was born a slave, won his freedom, then lost his city to an emperor's decree. ..."

SLIDES = [
    ('I', '<div class=kick>Applied Stoicism</div><div class=rule></div>\n<div class=hook>You just<br>lost your job.</div>\n<div class=sub>A man who was <em>born a slave</em><br>has advice for you.</div>'),
    ('II', "<div class=kick>Who's talking</div><div class=rule></div>\n<h2>Epictetus didn't write about hardship from a comfortable chair.</h2>\n<p>He was born enslaved in what is now Turkey. He won his freedom. Then the emperor Domitian banished the philosophers from Rome, and he lost his city too.</p>\n<p>He rebuilt in exile, teaching in a small town in Greece.</p>\n<p class=strong>He knew something about losing what you thought was yours.</p>"),
    ('III', '<div class=kick>His first lesson</div>\n<span class=qm>&ldquo;</span>\n<div class=q>Of things some are in our power, and others are not.</div>\n<div class=cite>Epictetus &middot; Enchiridion 1 &middot; tr. George Long</div>\n<div class=note>The opening line of his handbook. Everything else he taught follows from it.</div>'),
    ('IV', '<div class=kick>Now apply it</div><div class=rule></div>\n<h2>Sort your situation into two piles.</h2>\n<div class=cols>\n <div class="col not"><h3>Not in your power</h3><ul><li>Their decision</li><li>The economy</li><li>Their reasons</li><li>What people say</li></ul></div>\n <div class="col yours"><h3>In your power</h3><ul><li>Tomorrow at 8 a.m.</li><li>Who you call this week</li><li>How you tell the story</li><li>Keeping your routine</li></ul></div>\n</div>'),
    ('V', '<div class=kick>The second lesson</div>\n<span class=qm>&ldquo;</span>\n<div class=q style="font-size:92px">Men are disturbed not by the things which happen, but by the opinions about the things.</div>\n<div class=cite>Epictetus &middot; Enchiridion 5</div>\n<div class=pair><div class=lab>The event</div><div class=val>&ldquo;My position was cut.&rdquo;</div>\n<div class=lab>The opinion</div><div class=val style="margin-bottom:0">&ldquo;I\'m finished.&rdquo;</div></div>'),
    ('VI', "<div class=kick>Do this tonight</div><div class=rule></div>\n<h2>Three lines on paper.</h2>\n<ul class=steps>\n<li><span class=n>1</span><span class=t><b>What happened.</b> One plain sentence. No adjectives.</span></li>\n<li><span class=n>2</span><span class=t><b>What you've been telling yourself.</b> Is it a fact, or an opinion about a fact?</span></li>\n<li><span class=n>3</span><span class=t><b>One thing in your power before noon tomorrow.</b> Then go do it.</span></li>\n</ul>"),
    ('VII', '<div class=kick>Remember</div><div class=rule></div>\n<div class=big>The job was never yours.<br><em>Your next move always is.</em></div>\n<div class=cta>Send this to someone<br>who just got <em>the call.</em></div>\n<p style="margin-top:40px;font-size:44px;color:#a99f8c">Follow @applied_stoic: one ancient idea, applied to real life, every day.</p>'),
]
