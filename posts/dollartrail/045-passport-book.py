import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "tools"))
from lib import *

ACCOUNT = 'dollartrail'
TRAIL = '045'
FOLLOWING = 'a first passport'
SOURCES = ['https://childabduction.state.gov/content/dam/passports/forms-fees/Passport_Fee_Chart_Feb_2026_English.pdf']

CAPTION = """A first-time adult passport book costs $165, paid in two separate payments: $130 to the State Department and $35 to the acceptance facility that takes your application. Need it fast? Add $60 to expedite and $22.05 for 1-3 day delivery.

Data: U.S. Department of State, passport fee chart (updated February 2026). Shares and totals: our math.

Where's the first trip you'd use it for?

#passport #travel #traveltips #money #personalfinance #dollartrail"""

SLIDES = [
    '<div class=tag>Trail No. 045</div>\n<div class=hook style="font-size:100px">A first passport: <em>$165.</em></div>\n<div class=hook2>Two separate payments. Two different places the money goes.</div>\n<div class=mini style="margin-top:60px">Source: U.S. Department of State, passport fee chart, updated February 2026. First-time adult passport book (age 16 and older), Form DS-11.</div>',
    stack([(79, R, "STATE DEPARTMENT 79%"), (21, Y, "ACCEPTANCE FACILITY 21%")],
          [("Application fee", "$130", R), ("Execution fee", "$35", Y)],
          "The application fee is paid to the U.S. Department of State. The execution (acceptance) fee is paid to the acceptance facility. Shares: our math.",
          "Where the $165 goes", height=680),
    stop(1, 4, "The application fee", "$130", "PAID TO THE U.S. DEPARTMENT OF STATE",
         ["Same fee for a first adult book or a renewal.", "Adult renewals pay only this <b>$130</b>, with no second fee."],
         "Book and card together: $160 application fee, plus the $35 execution fee.", R),
    stop(2, 4, "The execution fee", "$35", "PAID TO THE ACCEPTANCE FACILITY",
         ["First-time applications go through an acceptance facility.", "It is paid directly, as a separate <b>$35</b> payment."],
         "State says submitting the wrong fees could delay your application.", Y),
    stop(3, 4, "Need it fast?", "$60", "EXPEDITE FEE, PER APPLICATION",
         ["Paid to the State Department on top of the required fees.", "Add <b>$22.05</b> for 1-3 day delivery of the finished book."],
         "Rushed, delivered fast: $247.05 for a first adult book (our math).", BL),
    stop(4, 4, "Kids under 16", "$135", "$100 APPLICATION FEE + $35 EXECUTION FEE",
         ["Every minor applicant also pays the <b>$35</b> execution fee.", "A minor passport card alone: <b>$15</b> + $35."],
         "Two adults and two kids, first-time books: $600, with $140 of it in execution fees (our math).", P),
    '<div class=tag>Detour</div>\n<h2>The cheaper card</h2>\n<div class=taxrow><div class=tx><div class=l>Passport book</div><div class=n>$130</div><div class=d>Application fee, adult</div></div><div class=tx><div class=l>Passport card</div><div class=n>$30</div><div class=d>Application fee, adult</div></div></div>\n' + note("The card is not valid for international air travel. It works only by land and sea to Canada, Mexico, Bermuda and the Caribbean."),
    '<div class=tag>End of the trail</div>\n<div class=hook style="font-size:86px">$130 to the State Department.<br><em>$35 to the office that takes your form.</em></div>\n<div class=cta>Send this to the friend<br>who <em>still doesn&rsquo;t have a passport.</em></div>\n<div class=src>' + DT_FOLLOW + '<br><br>Source: U.S. Department of State, passport fee chart, updated February 2026. Shares, rush total and family total: our math.</div>',
]
