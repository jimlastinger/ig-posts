import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "tools"))
from lib import *

ACCOUNT = 'dollartrail'
THEME = 'receipt'
TRAIL = '046'
FOLLOWING = 'a national park pass'
SOURCES = ['https://www.nps.gov/planyourvisit/passes.htm',
           'https://www.nps.gov/aboutus/nonresident-fees.htm']

CAPTION = """The America the Beautiful annual pass is $80 for U.S. residents. Since January 1, 2026, the pass costs $250 for visitors who don't live in the U.S. Nonresidents 16 and older without a pass also pay a $100 fee on top of the entrance fee at 11 parks. The Park Service says all entrance-fee money stays in the agency, and at least 80% stays in the park where it was collected.

Data: National Park Service, Entrance Passes and Nonresident Fees pages (2026). Difference on slide 4: our math.

Which park would you use the pass on first?

#nationalparks #roadtrip #travel #outdoors #money #dollartrail"""

SLIDES = [
    '<div class=tag>Trail No. 046</div>\n<div class=hook style="font-size:100px">A year of national parks: <em>$80.</em></div>\n<div class=hook2>If you live in the U.S. Visitors from abroad now pay $250.</div>\n<div class=mini style="margin-top:60px">Source: National Park Service (NPS), Entrance Passes page (updated Oct. 9, 2026) and Nonresident Fees page. America the Beautiful annual pass, 2026 prices.</div>',
    stack([(80, R, "AT LEAST 80%: THIS PARK"), (20, G, "UP TO 20%: REST OF NPS")],
          [("This park", "80%+", R), ("Rest of NPS", "20% max", G)],
          "NPS: &ldquo;All the money from entrance fees remains in the National Park Service, and at least 80 percent stays in the park where it was collected.&rdquo;",
          "Where entrance fees go", height=640),
    stop(1, 4, "The resident pass", "$80", "ANNUAL PASS, U.S. CITIZENS AND RESIDENTS",
         ["Sold to U.S. citizens and residents.", "All entrance-fee money stays in the <b>National Park Service</b>."],
         "Fee-free days in 2026, like Nov. 11, are for U.S. citizens and residents only.", R),
    stop(2, 4, "The new tier", "$250", "ANNUAL PASS, NON-U.S. RESIDENTS",
         ["A new pricing tier that started <b>January 1, 2026</b>.", "Covers the holder, passengers in a private vehicle (up to 15) and any nonresident fees."],
         "That&rsquo;s $170 more than the resident pass (our math).", Y),
    stop(3, 4, "Or pay at the gate", "$100", "PER NONRESIDENT AGE 16+, AT 11 PARKS",
         ["Charged on top of the regular entrance fee, unless they hold an annual pass.", "Parks include Yellowstone, Yosemite, Grand Canyon, Zion and Glacier."],
         "Also on the list: Acadia, Bryce Canyon, Everglades, Grand Teton, Rocky Mountain, Sequoia &amp; Kings Canyon.", BL),
    stop(4, 4, "Seniors", "$80", "LIFETIME PASS, U.S. CITIZENS AND RESIDENTS 62+",
         ["Or <b>$20</b> for a senior annual pass.", "Same eligibility for both: U.S. citizens and residents, age 62 and up."],
         "Some passes are free, including for current military, veterans and U.S. 4th graders.", P),
    '<div class=tag>Detour</div>\n<h2>The annual pass, 2026</h2>\n' + cmp([(20, "$20", False), (80, "$80", False), (250, "$250", True)],
        ["Senior 62+", "U.S. resident", "Nonresident"]) + '\n<div class=mini style="margin-top:24px">NPS Entrance Passes page. Senior annual pass shown; the senior lifetime pass is $80.</div>',
    '<div class=tag>End of the trail</div>\n<div class=hook style="font-size:86px">$80 for a year of parks.<br><em>$250 if you live abroad.</em></div>\n<div class=cta>Send this to the friend<br>who <em>is planning a road trip.</em></div>\n<div class=src>' + DT_FOLLOW + '<br><br>Source: National Park Service, Entrance Passes (nps.gov/planyourvisit/passes.htm, updated Oct. 9, 2026) and Nonresident Fees (nps.gov/aboutus/nonresident-fees.htm). Difference: our math.</div>',
]
