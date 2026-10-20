import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "tools"))
from lib import *

ACCOUNT = 'dollartrail'
THEME = 'receipt'
TRAIL = '028'
FOLLOWING = 'your 2027 Social Security raise'
SOURCES = ['https://www.ssa.gov/news/en/cola/factsheets/2027.html',
           'https://www.ssa.gov/oact/cola/latestCOLA.html',
           'https://www.ssa.gov/oact/cola/colaseries.html',
           'https://www.ssa.gov/oact/cola/cbb.html']

CAPTION = """Social Security checks rise 3.6% starting with benefits paid in January 2027. For the average retired worker, SSA estimates that's $2,095 to $2,170 a month, about $75 more.

Data: Social Security Administration, 2027 COLA Fact Sheet, Latest COLA, COLA history and wage base pages. Differences: our math.

Will $75 a month cover what's gone up for you?

#socialsecurity #retirement #cola #inflation #personalfinance #dollartrail"""

SLIDES = [
    '<div class=tag>Trail No. 028</div>\n<div class=hook style="font-size:104px">Your Social Security raise for 2027: <em>3.6%.</em></div>\n<div class=hook2>For the average retiree, about $75 a month.</div>\n<div class=mini style="margin-top:60px">Source: Social Security Administration, 2027 COLA Fact Sheet and Latest COLA page. Applies to December 2026 benefits, paid in January 2027. Dollar differences: our math.</div>',
    stack([(3.5, R, ""), (96.5, G, "BEFORE THE RAISE $2,095")],
          [("2027 raise", "+$75", R), ("Before the raise", "$2,095", G), ("After (estimate)", "$2,170", W)],
          "Average monthly benefit, all retired workers. SSA estimate for January 2027. The 3.6% is measured on the old check: $75 of $2,095 (our math). Not what everyone gets.",
          "The average retiree&rsquo;s check, January 2027", height=680),
    stop(1, 5, "The number", "3.6%", "COST-OF-LIVING ADJUSTMENT FOR 2027",
         ["SSA compares the July to September average of the CPI-W: <b>328.746</b> in 2026 vs. <b>317.265</b> in 2025. That&rsquo;s up 3.62% (our math)."],
         "It&rsquo;s the biggest raise since 2023&rsquo;s 8.7%, per SSA&rsquo;s COLA history.", R),
    stop(2, 5, "Retired couple", "+$117", "A MONTH: $3,238 TO $3,355",
         ["SSA&rsquo;s average for an aged couple, both receiving benefits, before and after the raise in January 2027."],
         "That&rsquo;s about $1,404 more over a year (our math).", Y),
    stop(3, 5, "Widow or widower", "+$69", "A MONTH: $1,936 TO $2,005",
         ["SSA&rsquo;s average for an aged widow or widower living alone."],
         "Smaller checks get smaller dollar raises: the 3.6% is the same for everyone.", BL),
    stop(4, 5, "Disabled workers", "+$59", "A MONTH: $1,642 TO $1,701",
         ["SSA&rsquo;s average for all disabled workers. SSI&rsquo;s federal payment rises to <b>$1,029</b> a month for an individual and <b>$1,544</b> for a couple."],
         "SSI&rsquo;s increase starts with January 2027 payments.", P),
    stop(5, 5, "The tax side", "$192,300", "2027 WAGE BASE, UP $7,800 FROM 2026 (OUR MATH)",
         ["Earnings above this aren&rsquo;t taxed for Social Security in 2027. The 2026 limit was <b>$184,500</b>."],
         "The max benefit at full retirement age: $4,188 a month in 2027.", T),
    '<div class=tag>Detour</div>\n<h2>Social Security raises, by year first paid</h2>\n' + cmp([(5.9, "5.9%", False), (8.7, "8.7%", False), (3.2, "3.2%", False), (2.5, "2.5%", False), (2.8, "2.8%", False), (3.6, "3.6%", True)],
        ["2022", "2023", "2024", "2025", "2026", "2027"]) + '\n<div class=mini style="margin-top:24px">SSA COLA history table. SSA lists each raise under the December it takes effect; it is first paid the next January.</div>',
    '<div class=tag>End of the trail</div>\n<div class=hook style="font-size:88px">3.6% for everyone.<br><em>Average raises: $59 to $117 a month.</em></div>\n<div class=cta>Send this to someone<br>who <em>gets a Social Security check.</em></div>\n<div class=src>' + DT_FOLLOW + '<br><br>Source: Social Security Administration, 2027 COLA Fact Sheet, Latest COLA and COLA history pages, contribution and benefit base. Averages are SSA estimates for January 2027. Differences: our math.</div>',
]
