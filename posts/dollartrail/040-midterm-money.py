import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "tools"))
from lib import *

ACCOUNT = 'dollartrail'
THEME = 'receipt'
TRAIL = '040'
FOLLOWING = 'the midterm money'
SOURCES = ['https://www.fec.gov/updates/statistical-summary-of-18-month-campaign-activity-of-the-2025-2026-election-cycle/']

CAPTION = """House and Senate candidates raised $2.8 billion from Jan. 1, 2025 to June 30, 2026, per the FEC. That's more than the same stretch of any recent cycle the FEC lists, and 15.5% above the 2022 midterms (not adjusted for inflation).

Data: Federal Election Commission, Statistical Summary of 18-Month Campaign Activity of the 2025-2026 Election Cycle (Oct. 1, 2026). Averages, shares and percent change: our math.

Where does campaign money end up, in your view?

#midterms #election2026 #campaignfinance #politics #money #dollartrail"""

SLIDES = [
    '<div class=tag>Trail No. 040</div>\n<div class=hook style="font-size:104px">Races for Congress: <em>$2.8 billion</em> raised.</div>\n<div class=hook2>In 18 months, before the final stretch.</div>\n<div class=mini style="margin-top:60px">Source: Federal Election Commission (FEC), Statistical Summary of 18-Month Campaign Activity of the 2025-2026 Election Cycle, Oct. 1, 2026. House and Senate candidates, Jan. 1, 2025 to June 30, 2026.</div>',
    stack([(69, R, "HOUSE 69%"), (31, BL, "SENATE 31%")],
          [("House", "$1.9B", R), ("Senate", "$864.3M", BL), ("Total", "$2.8B", G)],
          "Receipts reported by House and Senate candidates, Jan. 1, 2025 to June 30, 2026. Shares: our math from FEC totals.",
          "Who raised the $2.8 billion", height=680),
    stop(1, 4, "The House", "$1.9B", "RAISED BY 2,427 HOUSE CANDIDATES",
         ["That averages about <b>$780,000</b> per candidate (our math).", "Every House seat is on the ballot."],
         "House candidates also reported $326.1 million in debts.", R),
    stop(2, 4, "The Senate", "$864.3M", "RAISED BY 315 SENATE CANDIDATES",
         ["That averages about <b>$2.74 million</b> per candidate (our math)."],
         "Fewer candidates, far more raised per candidate.", BL),
    '<div class="tag ghost">Stop 3 of 4</div>\n<h2>Midterm after midterm</h2>\n' + cmp([(1143.4, "$1.14B", False), (1699.2, "$1.70B", False), (2422.8, "$2.42B", False), (2799.1, "$2.80B", True)],
        ["2014", "2018", "2022", "2026"]) + '\n<div class=mini style="margin-top:24px">Congressional candidate receipts, first 18 months of each midterm cycle (FEC). Not adjusted for inflation. 2026 is 15.5% above 2022 (our math).</div>',
    stop(4, 4, "Outside money", "$643.4M", "INDEPENDENT EXPENDITURES",
         ["Spending for or against candidates by groups not coordinating with them.", "Super PACs made <b>$529.6 million</b> of it."],
         "All 9,176 federal PACs together reported $8.3 billion in receipts.", Y),
    '<div class=tag>Detour</div>\n<h2>Spent vs. still in the bank</h2>\n<div class=taxrow><div class=tx><div class=l>Spent</div><div class=n>$2B</div><div class=d>Through June 30</div></div><div class=tx><div class=l>Cash on hand</div><div class=n>$1.3B</div><div class=d>As of June 30, 2026</div></div></div>\n' + note("Cash on hand can include money carried over from before 2025. These reports stop at June 30."),
    '<div class=tag>End of the trail</div>\n<div class=hook style="font-size:86px">$2.8 billion raised.<br><em>Your vote: Nov. 3.</em></div>\n<div class=cta>Send this to the friend<br>who <em>hasn&rsquo;t checked their polling place.</em></div>\n<div class=src>' + DT_FOLLOW + '<br><br>Source: Federal Election Commission, Statistical Summary of 18-Month Campaign Activity of the 2025-2026 Election Cycle (Oct. 1, 2026). Not adjusted for inflation. Averages, shares and percent change: our math.</div>',
]
