import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "tools"))
from lib import *

ACCOUNT = 'dollartrail'
TRAIL = '051'
FOLLOWING = '$1,000 on a credit card'
SOURCES = ['https://www.federalreserve.gov/releases/g19/current/']

CAPTION = """Credit card accounts that paid interest were charged an average 22.36% in August 2026, per the Federal Reserve. Carry $1,000 at that rate for a year and you pay about $223.60 in interest (our math, before compounding).

Data: Federal Reserve, Consumer Credit G.19 (released Oct. 7, 2026). Dollar amounts: our math.

Do you pay your card off every month?

#creditcard #debt #interest #personalfinance #money #dollartrail"""

SLIDES = [
    '<div class=tag>Trail No. 051</div>\n<div class=hook style="font-size:96px">$1,000 on a card for a year: <em>$223.60 in interest.</em></div>\n<div class=hook2>At the average rate on accounts that paid interest, August 2026.</div>\n<div class=mini style="margin-top:60px">Source: Federal Reserve, Consumer Credit G.19, released Oct. 7, 2026 (rate 22.36%). Dollar amounts: our math, simple interest, before compounding.</div>',
    stack([(82, G, "YOUR $1,000: 82%"), (18, R, "INTEREST: 18%")],
          [("What you borrowed", "$1,000.00", G), ("A year of interest", "$223.60", R)],
          "Total paid back after 12 months: $1,223.60 (our math at 22.36%, no compounding, no new charges).",
          "What $1,000 turns into", height=640),
    stop(1, 4, "The rate", "22.36%", "AVERAGE RATE, CARD ACCOUNTS ASSESSED INTEREST, AUG. 2026",
         ["That&rsquo;s accounts that actually paid interest.", "Across <b>all</b> card accounts, the average was <b>21.19%</b>."],
         "Federal Reserve G.19, commercial bank credit card plans. August figures are preliminary.", R),
    stop(2, 4, "Per month", "$18.63", "INTEREST ON $1,000 PER MONTH (OUR MATH)",
         ["$223.60 a year divided by 12.", "Real card interest compounds, so carrying the balance costs <b>a bit more</b>."],
         "That&rsquo;s before any new purchases or late fees.", Y),
    stop(3, 4, "Back in 2021", "16.45%", "AVERAGE RATE, ACCOUNTS ASSESSED INTEREST, 2021",
         ["Same $1,000 for a year: about <b>$164.50</b> (our math).", "At August&rsquo;s rate it&rsquo;s <b>$59.10 more</b>."],
         "Highest yearly average, 2021 to 2025: 22.89% in 2024.", BL),
    stop(4, 4, "The national tab", "$1.35T", "U.S. REVOLVING CREDIT OUTSTANDING, AUG. 2026",
         ["$1,352.4 billion, seasonally adjusted.", "It fell at a <b>4.2%</b> annual rate in August."],
         "Revolving credit includes card balances; this total isn&rsquo;t cards alone.", P),
    '<div class=tag>Detour</div>\n<h2>Average card rate, accounts assessed interest</h2>\n' + cmp([(16.45, "16.45%", False), (17.91, "17.91%", False), (22.15, "22.15%", False), (22.89, "22.89%", True), (22.32, "22.32%", False)],
        ["2021", "2022", "2023", "2024", "2025"]) + '\n<div class=mini style="margin-top:24px">Federal Reserve G.19, annual figures, commercial bank credit card plans.</div>',
    '<div class=tag>End of the trail</div>\n<div class=hook style="font-size:86px">$1,000 carried a year.<br><em>About $223.60 to the bank.</em></div>\n<div class=cta>Send this to the friend<br>who <em>only pays the minimum.</em></div>\n<div class=src>' + DT_FOLLOW + '<br><br>Source: Federal Reserve, Consumer Credit G.19, released Oct. 7, 2026 (federalreserve.gov/releases/g19/current). Dollar amounts: our math at 22.36%, simple interest.</div>',
]
