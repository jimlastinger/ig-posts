"""Archived example post. Slides are pre-rendered HTML strings; new posts should use the helpers in tools/lib.py."""
import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "tools"))
from lib import *

ACCOUNT = 'applied_stoic'
SOURCES = ['https://www.politifact.com/factchecks/2019/sep/26/viral-image/no-marcus-aurelius-didnt-say-about-opinions-and-fa/', 'https://en.wikiquote.org/wiki/Marcus_Aurelius']

CAPTION = "Half the Marcus Aurelius quotes online aren't his. ..."

SLIDES = [
    ('I', '<div class=kick>Applied Stoicism</div><div class=rule></div>\n<div class=hook style="font-size:116px">That Marcus Aurelius quote you saved?</div>\n<div class=sub><em>He never wrote it.</em><br>Four fakes, and what he really said.</div>'),
    ('II', '<div class="fake">Fake</div>\n<div class=viral>&ldquo;Everything we hear is an opinion, not a fact. Everything we see is a perspective, not the truth.&rdquo;</div>\n<div class=verdict>Not in the <i>Meditations</i>. PolitiFact rated the attribution false. Marcus believed in facts; his point was that our <b>judgments</b> about them disturb us.</div>\n<div class=real><div class=lab>What he actually wrote &middot; Meditations 2.15</div><div class=t>&ldquo;Remember that all is opinion.&rdquo;</div></div>'),
    ('III', '<div class="fake">Fake</div>\n<div class=viral>&ldquo;You have power over your mind, not outside events. Realize this, and you will find strength.&rdquo;</div>\n<div class=verdict>No passage says this. It\'s an anonymous modern paraphrase. The real line is sharper:</div>\n<div class=real><div class=lab>Meditations 8.47 &middot; tr. George Long</div><div class=t>&ldquo;If thou art pained by any external thing, it is not this thing that disturbs thee, but thy own judgement about it.&rdquo;</div></div>'),
    ('IV', '<div class="fake">Fake</div>\n<div class=viral>&ldquo;When you arise in the morning, think of what a precious privilege it is to be alive.&rdquo;</div>\n<div class=verdict>Written by American author Elbert Hubbard in 1914, who credited it to Marcus. The real morning passage is less cozy:</div>\n<div class=real><div class=lab>Meditations 5.1 &middot; tr. George Long</div><div class=t>&ldquo;In the morning when thou risest unwillingly, let this thought be present: I am rising to the work of a human being.&rdquo;</div></div>'),
    ('V', '<div class="fake para">Stretched</div>\n<div class=viral>&ldquo;The happiness of your life depends upon the quality of your thoughts.&rdquo;</div>\n<div class=verdict>From Jeremy Collier\'s very loose 1701 translation. A faithful translation of the same passage reads:</div>\n<div class=real><div class=lab>Meditations 3.9 &middot; tr. George Long</div><div class=t>&ldquo;Reverence the faculty which produces opinion.&rdquo;</div></div>'),
    ('VI', '<div class=kick>Why it matters</div><div class=rule></div>\n<h2>The real Marcus is tougher than the poster version.</h2>\n<p>The fakes comfort you. The originals ask something of you: get up and work, question your own judgments, expect difficult people.</p>\n<p class=strong>How to check: real quotes have a book and section, like 8.47. No reference? Search the exact words before you share.</p>'),
    ('VII', '<div class=kick>Remember</div><div class=rule></div>\n<div class=big>Quote the man,<br><em>not the meme.</em></div>\n<div class=cta>Send this to the friend<br>with a fake one as <em>their wallpaper.</em></div>\n<p style="margin-top:40px;font-size:44px;color:#a99f8c">Follow @applied_stoic: one ancient idea, applied to real life, every day.</p>'),
]
