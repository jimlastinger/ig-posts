import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "tools"))
from lib import *

ACCOUNT = 'dollartrail'
THEME = 'ledger'
TRAIL = '053'
FOLLOWING = 'a brand-new house'
SOURCES = ['https://www.census.gov/construction/nrs/current/index.html', 'https://www.census.gov/construction/nrs/pdf/newressales.pdf']

CAPTION = """The median new house sold in September went for $400,400, per the Census Bureau, about $16,400 less than a year earlier, a drop Census says isn't statistically significant. The average was $472,800, and 61% of new homes sold were in the South (differences and shares: our math).

Data: U.S. Census Bureau, Monthly New Residential Sales, September 2026 (released Oct. 27, 2026). Preliminary figures.

What would $400,400 buy where you live?

#housing #realestate #newhome #homebuying #personalfinance #dollartrail"""

SLIDES = [
    '<div class=tag>Trail No. 053</div>\n<div class=hook style="font-size:100px">A brand-new house: <em>$400,400.</em></div>\n<div class=hook2>Median sales price of new houses sold in the U.S., September 2026.</div>\n<div class=mini style="margin-top:60px">Source: U.S. Census Bureau, Monthly New Residential Sales, September 2026, released Oct. 27, 2026. Preliminary. Regional shares: our math.</div>',
    stack([(61, R, "SOUTH: 61%"), (21, Y, "WEST: 21%"), (13, BL, "MIDWEST: 13%"), (5, G, "NE: 5%")],
          [("South", "413,000", R), ("West", "142,000", Y), ("Midwest", "89,000", BL), ("Northeast", "32,000", G)],
          "New houses sold, September 2026, seasonally adjusted annual rate. U.S. total: 676,000. Shares: our math.",
          "Where new homes sell", height=640),
    stop(1, 4, "The middle house", "$400,400", "MEDIAN SALES PRICE, SEPTEMBER 2026",
         ["Half of new houses sold for more, half for less.", "A year earlier: <b>$416,800</b>, so <b>$16,400 lower</b> now."],
         "Census says that 3.9% drop is not statistically significant.", R),
    stop(2, 4, "The average house", "$472,800", "AVERAGE SALES PRICE, SEPTEMBER 2026",
         ["<b>$72,400</b> above the median: higher-priced homes pull the average up (our math).", "A year earlier: <b>$506,800</b>, down 6.7%."],
         "Census counts this drop as statistically significant.", Y),
    stop(3, 4, "Houses waiting", "476,000", "NEW HOUSES FOR SALE, END OF SEPTEMBER",
         ["At the current sales pace, that&rsquo;s <b>8.4 months</b> of supply.", "A year earlier: 487,000 for sale, 8.2 months."],
         "Seasonally adjusted. In August: 481,000 for sale.", BL),
    stop(4, 4, "The pace", "676,000", "SALES AT A SEASONALLY ADJUSTED ANNUAL RATE",
         ["That&rsquo;s the yearly pace if September&rsquo;s sales held all year.", "A year earlier: <b>714,000</b>. Now 5.3% lower."],
         "Census can&rsquo;t say for sure sales fell: the range includes zero.", P),
    '<div class=tag>Detour</div>\n<h2>New-house prices, a year apart</h2>\n' + cmp([(416800, "$416,800", False), (400400, "$400,400", True), (506800, "$506,800", False), (472800, "$472,800", True)],
        ["Median Sept. &rsquo;25", "Median Sept. &rsquo;26", "Average Sept. &rsquo;25", "Average Sept. &rsquo;26"]) + '\n<div class=mini style="margin-top:24px">Prices are not seasonally adjusted. Census notes they reflect the mix of homes sold (size, region), not only price changes.</div>',
    '<div class=tag>End of the trail</div>\n<div class=hook style="font-size:86px">$400,400 for the middle new house.<br><em>61% of sales in the South.</em></div>\n<div class=cta>Send this to the friend<br>who&rsquo;s <em>touring model homes.</em></div>\n<div class=src>' + DT_FOLLOW + '<br><br>Source: U.S. Census Bureau, Monthly New Residential Sales, September 2026 (census.gov/construction/nrs), released Oct. 27, 2026. Preliminary. Differences and shares: our math.</div>',
]
