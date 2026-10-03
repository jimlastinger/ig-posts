import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "tools"))
from lib import *

ACCOUNT = 'applied_stoic'
SOURCES = ['https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Diogenes_Laertius/Lives_of_the_Eminent_Philosophers/7/Zeno*.html']

CAPTION = """Stoicism started with a shipwreck. Zeno lost his cargo, wandered into a bookshop in Athens, and found the life he actually wanted.

If something just sank for you, it might be the start, not the end.

Source: Diogenes Laertius, Lives of the Eminent Philosophers VII.2-5, tr. R. D. Hicks (1925).

#stoicism #stoic #zeno #resilience #philosophy #mindset"""

SLIDES = [
    ('I', '<div class=kick>Applied Stoicism</div><div class=rule></div>\n<div class=hook style="font-size:120px">Stoicism began with <em>losing everything.</em></div>\n<div class=sub>The founder\'s first lesson<br><em>was a shipwreck.</em></div>'),
    ('II', "<div class=kick>Who's talking</div><div class=rule></div>\n<h2>Zeno of Citium was a merchant, not a philosopher.</h2>\n<p>He came from Citium, on Cyprus. The ancient biographer Diogenes Laertius says he was sailing to Athens with a cargo of purple dye, one of the most valuable goods in the ancient world.</p>\n<p>The ship went down. The cargo was gone.</p>"),
    ('III', "<div class=kick>What happened next</div><div class=rule></div>\n<h2>He walked into a bookshop.</h2>\n<p>Stranded in Athens, Zeno sat in a bookseller's shop reading Xenophon's book about Socrates. He asked where men like that could be found.</p>\n<p>Just then the philosopher Crates walked past. The bookseller pointed: <b>follow that man.</b></p>\n<p>He did. Years later he was teaching on his own, at the Painted Stoa. His students were named after the porch: Stoics.</p>"),
    ('IV', '<div class=kick>How he saw it later</div>\n<span class=qm>&ldquo;</span>\n<div class=q>I made a prosperous voyage when I suffered shipwreck.</div>\n<div class=cite>Zeno, in Diogenes Laertius &middot; Lives VII.4 &middot; tr. R. D. Hicks</div>\n<div class=note>The voyage he planned failed. The one he didn\'t plan made him.</div>'),
    ('V', '<div class=kick>Apply it</div><div class=rule></div>\n<h2>Your cargo sank. Now what?</h2>\n<div class=pair><div class=lab>The event</div><div class=val>The job, the deal, the plan is gone.</div>\n<div class=lab>The story you tell</div><div class=val>&ldquo;My life is ruined.&rdquo;</div>\n<div class=lab>Zeno\'s question</div><div class=val style="margin-bottom:0">&ldquo;What can I build from here?&rdquo;</div></div>'),
    ('VI', '<div class=kick>Another version</div><div class=rule></div>\n<h2>The ancient sources disagree on the details.</h2>\n<p>One version says Zeno was already in Athens when he heard the news, and answered:</p>\n<div class=q style="font-size:76px;margin-top:10px">&ldquo;It is well done of thee, Fortune, thus to drive me to philosophy.&rdquo;</div>\n<p style="margin-top:30px">Every version ends the same way: he stopped mourning the cargo and started walking.</p>'),
    ('VII', "<div class=kick>Try this today</div><div class=rule></div>\n<h2>The shipwreck audit:</h2>\n<ul class=steps>\n<li><span class=n>1</span><span class=t><b>Name what sank.</b> One sentence. No adjectives.</span></li>\n<li><span class=n>2</span><span class=t><b>List what survived.</b> Skills, people, time, health.</span></li>\n<li><span class=n>3</span><span class=t><b>Find your bookshop.</b> One door the loss just opened. Walk through it this week.</span></li>\n</ul>"),
    ('VIII', '<div class=kick>Remember</div><div class=rule></div>\n<div class=big>The cargo was never the point.<br><em>The voyage was.</em></div>\n<div class=cta>Send this to someone<br>whose ship <em>just sank.</em></div>\n' + STOIC_FOLLOW),
]
