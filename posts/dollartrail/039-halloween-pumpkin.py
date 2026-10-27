import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "tools"))
from lib import *

ACCOUNT = 'dollartrail'
TRAIL = '039'
FOLLOWING = 'a Halloween pumpkin'
SOURCES = ['https://www.ers.usda.gov/newsroom/trending-topics/pumpkins-background-statistics']

CAPTION = """U.S. farms grew 1.47 billion pounds of pumpkins in 2025, and the farm price ran from about $48 per 1,000 pounds in Illinois to about $269 in Pennsylvania. For a 20-pound pumpkin, that's 96 cents to $5.38 for the grower, depending on the state and whether it's grown for processing or the porch.

Data: USDA Economic Research Service, Pumpkins: Background & Statistics (updated Sept. 29, 2026). Farm prices, not store prices. Per-pumpkin figures: our math.

What did you pay for your pumpkin this year?

#halloween #pumpkins #farming #agriculture #money #dollartrail"""

SLIDES = [
    '<div class=tag>Trail No. 039</div>\n<div class=hook style="font-size:100px">A 20-lb pumpkin: the farmer got <em>96&cent;</em> or <em>$5.38.</em></div>\n<div class=hook2>It depends where it grew, and what it&rsquo;s for.</div>\n<div class=mini style="margin-top:60px">Source: USDA Economic Research Service (ERS), Pumpkins: Background &amp; Statistics, updated Sept. 29, 2026. 2025 average farm prices, Illinois and Pennsylvania. Per-pumpkin figures: our math.</div>',
    stack([(36, R, "ILLINOIS 36%"), (11, Y, "CALIF. 11%"), (9, BL, "IND. 9%"), (16, P, "MICH. + PA. 16%"), (28, G, "ALL OTHERS 28%")],
          [("Illinois", "533M lb", R), ("California", "162M lb", Y), ("Indiana", "135M lb", BL), ("Mich. + Pa.", "~16%", P), ("Other states", "~28%", G)],
          "Top 5 states: nearly 72% of the 2025 crop. Shares and the Mich. + Pa. figure: our math from ERS totals.",
          "1.47 billion pounds of pumpkins, 2025", height=680),
    stop(1, 4, "Illinois", "533M lb", "PUMPKINS GROWN IN 2025",
         ["Slightly more than the other four top states <b>combined</b>.", "Nearly <b>70%</b> of Illinois pumpkin acres are grown for processing, not for porches."],
         "Average farm price: $48 per 1,000 pounds, about 4.8&cent; a pound. The lowest of the top five.", R),
    stop(2, 4, "Pennsylvania", "$269", "PER 1,000 POUNDS, 2025",
         ["The highest price among the top five states.", "That&rsquo;s about <b>$5.38</b> for a 20-pound pumpkin (our math)."],
         "Nationally, about 85% of pumpkin acres grow for the fresh and ornamental market.", Y),
    '<div class="tag ghost">Stop 3 of 4</div>\n<h2>Five states, five prices</h2>\n' + cmp([(269, "$269", True), (237, "$237", False), (198, "$198", False), (160, "$160", False), (48, "$48", False)],
        ["Pa.", "Ind.", "Mich.", "Calif.", "Ill."]) + '\n<div class=mini style="margin-top:24px">Average 2025 farm price per 1,000 pounds, top five producing states (USDA ERS, approximate). Processing pumpkins usually sell for less.</div>',
    stop(4, 4, "The whole crop", "$259M", "U.S. PUMPKIN VALUE, 2025",
         ["Down from <b>$286 million</b> in 2022.", "Indiana&rsquo;s crop was worth the most: <b>$32 million</b>. Pennsylvania: <b>$28 million</b>."],
         "That works out to about 17.6&cent; a pound at the farm, across all states (our math).", BL),
    '<div class=tag>Detour</div>\n<h2>Who grows them</h2>\n<div class=taxrow><div class=tx><div class=l>Fresh-market farms</div><div class=n>15,000+</div><div class=d>Across the U.S.</div></div><div class=tx><div class=l>Processing farms</div><div class=n>959</div><div class=d>Nearly 15% in Illinois</div></div></div>\n' + note("Americans had about 5.2 pounds of pumpkin per person available in 2025."),
    '<div class=tag>End of the trail</div>\n<div class=hook style="font-size:86px">A 20-lb pumpkin.<br><em>96&cent; or $5.38 at the farm.</em></div>\n<div class=cta>Send this to the friend<br>who <em>buys three for the porch.</em></div>\n<div class=src>' + DT_FOLLOW + '<br><br>Source: USDA Economic Research Service, Pumpkins: Background &amp; Statistics (updated Sept. 29, 2026). Farm prices, not store prices. 20-lb pumpkin values, per-pound values and shares: our math.</div>',
]
