import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "tools"))
from lib import *

ACCOUNT = 'dollartrail'
TRAIL = '018'
FOLLOWING = 'a year of college'
SOURCES = ['https://nces.ed.gov/fastfacts/display.asp?id=76',
           'https://nces.ed.gov/programs/coe/indicator/cue']

CAPTION = """A year at a public four-year college, living on campus, cost $27,100 in 2022-23. Tuition and fees were $9,800 of it; books, room, board and other expenses were the other $17,300.

Data: National Center for Education Statistics (NCES), Fast Facts and Condition of Education, 2022-23 school year in constant 2022-23 dollars; college spending per student, 2020-21.

Did the cost of living there surprise you more than tuition?

#college #tuition #studentloans #highereducation #personalfinance #dollartrail"""

SLIDES = [
    '<div class=tag>Trail No. 018</div>\n<div class=hook style="font-size:104px">A year at a public 4&#8209;year college, living on campus: <em>$27,100.</em></div>\n<div class=hook2>Tuition and fees: only $9,800 of it.</div>\n<div class=mini style="margin-top:60px">Source: National Center for Education Statistics (NCES), Fast Facts: Tuition costs of colleges and universities. Public 4-year institutions, total cost of attendance living on campus, 2022-23, in constant 2022-23 dollars.</div>',
    stack([(36, R, "TUITION 36%"), (64, G, "EVERYTHING ELSE 64%")],
          [("Tuition and fees", "$9,800", R), ("Room, board, other", "$17,300", G)],
          "Public 4-year, living on campus, 2022-23 (NCES). &ldquo;Room, board, other&rdquo; includes books and supplies. Shares and $17,300: our math.",
          "Follow $27,100", height=700),
    stop(1, 4, "Tuition and fees", "$9,800", "PUBLIC 4-YEAR, 2022-23",
         ["Tuition and required fees for first-time, full-time undergraduates at public four-year schools."],
         "About 36% of the on-campus cost (our math).", R),
    stop(2, 4, "Everything else", "$17,300", "BOOKS, SUPPLIES, ROOM, BOARD AND OTHER",
         ["Most of the bill is living there, plus books and supplies."],
         "About 64% of the $27,100 at a public 4-year school (our math).", Y),
    stop(3, 4, "Where the college spends", "$13,540", "INSTRUCTION, PER STUDENT, PUBLIC 4-YEAR, 2020-21",
         ["That&rsquo;s <b>34%</b> of core expenses of <b>$39,330</b> per full-time-equivalent student. Different year and measure from the prices."],
         "Research and public service: $8,650 per student, or 22% of core.", BL),
    stop(4, 4, "At a private nonprofit", "$58,600", "ON-CAMPUS COST, PRIVATE NONPROFIT 4-YEAR, 2022-23",
         ["Tuition and fees: <b>$40,700</b>, about 69% of the bill (our math)."],
         "The non-tuition part is close to a public school&rsquo;s: $17,900 vs. $17,300 (our math).", P),
    '<div class=tag>Detour</div>\n<h2>Tuition and fees,<br>one year</h2>\n' + cmp([(4000, "$4,000", False), (9800, "$9,800", True), (19500, "$19,500", False), (40700, "$40,700", False)],
        ["Public<br>2-year", "Public<br>4-year", "Private<br>2-year", "Private<br>4-year"]) + '\n<div class=mini style="margin-top:24px">NCES, tuition and required fees, first-time full-time undergraduates, 2022-23, constant 2022-23 dollars. Private = private nonprofit.</div>',
    '<div class=tag>End of the trail</div>\n<div class=hook style="font-size:92px">$27,100 a year.<br><em>About 64% of it isn&rsquo;t tuition or fees.</em></div>\n<div class=cta>Send this to someone<br>picking a <em>college.</em></div>\n<div class=src>' + DT_FOLLOW + '<br><br>Source: NCES, Fast Facts: Tuition costs of colleges and universities (2022-23, constant 2022-23 dollars) and Condition of Education: Postsecondary Institution Expenses (per student, 2020-21). Shares: our math.</div>',
]
