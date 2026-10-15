import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "tools"))
from lib import *

ACCOUNT = 'dollartrail'
THEME = 'ledger'
TRAIL = '023'
FOLLOWING = 'your Social Security raise'
SOURCES = ['https://www.ssa.gov/oact/cola/latestCOLA.html',
           'https://www.ssa.gov/oact/cola/colaseries.html',
           'https://www.ssa.gov/news/en/cola/factsheets/2026.html',
           'https://www.ssa.gov/news/en/press/releases/2025-10-24.html',
           'https://www.bls.gov/news.release/cpi.nr0.htm']

CAPTION = """Social Security's yearly raise comes from one measure: the July-September average of the CPI-W, compared with the same quarter of the last year a raise took effect. That gave a 2.8% raise paid from January 2026, about +$56 a month for the average retired worker.

Data: Social Security Administration (COLA history, 2026 COLA Fact Sheet, Oct 24, 2025 press release); Bureau of Labor Statistics CPI. Breakdowns: our math.

Did you know the raise isn't based on a full year of prices?

#socialsecurity #retirement #inflation #cola #personalfinance #dollartrail"""

SLIDES = [
    '<div class=tag>Trail No. 023</div>\n<div class=hook style="font-size:100px">Your Social Security raise is set by <em>3 months of prices.</em></div>\n<div class=hook2>The raises from 2021 to 2026, and where the number comes from.</div>\n<div class=mini style="margin-top:60px">Source: Social Security Administration, COLA history, 2026 COLA Fact Sheet and Oct 24, 2025 press release; Bureau of Labor Statistics CPI. Breakdowns: our math.</div>',
    stack([(2.7, R, ""), (97.3, G, "BEFORE THE RAISE $2,015")],
          [("2026 raise", "+$56", R), ("Before the raise", "$2,015", G), ("After (estimate)", "$2,071", W)],
          "Average monthly benefit, all retired workers. SSA estimate for January 2026, after the 2.8% raise. Shares: $56 is 2.7% of $2,071 (our math). Not what everyone gets.",
          "The average retiree&rsquo;s check, January 2026", height=680),
    stop(1, 5, "The measure", "CPI-W", "PRICES FOR URBAN WAGE EARNERS AND CLERICAL WORKERS",
         ["SSA: COLAs &ldquo;are based on increases in the Consumer Price Index for Urban Wage Earners and Clerical Workers (CPI-W).&rdquo; BLS publishes it."],
         "Since 1975, raises have been COLAs. Before that, benefit increases were set by legislation.", R),
    stop(2, 5, "The window", "Q3", "JULY TO SEPTEMBER AVERAGE VS. THE SAME QUARTER OF THE LAST RAISE",
         ["For the 2026 raise: the 2025 third-quarter CPI-W average, <b>317.265</b>, against 2024&rsquo;s, <b>308.729</b>. That&rsquo;s up 2.76% (our math), which SSA lists as 2.8%."],
         "So the 12-month inflation number in the news is not the raise.", Y),
    stop(3, 5, "The 2026 raise", "2.8%", "PAID FROM JANUARY 2026",
         ["The average retired worker went from <b>$2,015</b> to an estimated <b>$2,071</b> a month: about <b>+$56</b>, or $672 a year (our math)."],
         "SSA says the raise reaches 75 million Americans, including SSI recipients.", BL),
    stop(4, 5, "Five raises stacked", "+25.2%", "ABOUT. THE 2022 TO 2026 RAISES, COMPOUNDED (OUR MATH)",
         ["5.9%, then 8.7%, 3.2%, 2.5% and 2.8%. Each raise builds on the last one."],
         "Add 2021&rsquo;s 1.3% and 2021 to 2026 comes to about +26.8% (our math).", P),
    stop(5, 5, "The tax side", "$184,500", "2026 WAGE BASE, UP $8,400 FROM 2025",
         ["Earnings above this aren&rsquo;t taxed for Social Security in 2026. Payroll tax rates didn&rsquo;t change: 7.65% for employees, 15.30% for the self-employed."],
         "The max benefit at full retirement age rose $134, to $4,152 a month.", T),
    '<div class=tag>Detour</div>\n<h2>Social Security raises, by year first paid</h2>\n' + cmp([(1.3, "1.3%", False), (5.9, "5.9%", False), (8.7, "8.7%", True), (3.2, "3.2%", False), (2.5, "2.5%", False), (2.8, "2.8%", False)],
        ["2021", "2022", "2023", "2024", "2025", "2026"]) + '\n<div class=mini style="margin-top:24px">SSA COLA history table. SSA lists each raise under the December it took effect; it is first paid the next January.</div>',
    '<div class=tag>End of the trail</div>\n<div class=hook style="font-size:84px">Three months of prices.<br><em>One raise for a whole year.</em></div>\n<div class=hook2 style="font-size:44px">The 2027 raise uses the July to September 2026 average.</div>\n<div class=cta>Send this to someone<br>who <em>gets a Social Security check.</em></div>\n<div class=src>' + DT_FOLLOW + '<br><br>Source: Social Security Administration, Latest COLA and COLA history pages, 2026 COLA Fact Sheet, press release (Oct 24, 2025); Bureau of Labor Statistics, CPI for August 2026. Breakdowns: our math.</div>',
]
