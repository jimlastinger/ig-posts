import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "tools"))
from lib import *

ACCOUNT = 'dollartrail'
THEME = 'receipt'
TRAIL = '043'
FOLLOWING = 'a 10-item grocery run'
SOURCES = ['https://www.bls.gov/regions/mid-atlantic/data/averageretailfoodandenergyprices_usandNortheast_table.htm']

CAPTION = """One of each of 10 everyday groceries cost $40.16 at BLS average prices in September 2026, 1.7% less than a year earlier (our math), mostly thanks to cheaper eggs. The gas to drive there went up 34%.

Data: U.S. Bureau of Labor Statistics, Average Retail Food and Energy Prices, U.S. city average, September 2025 and September 2026. Basket totals, shares and basket percent change: our math.

Which grocery price have you noticed most this year?

#groceries #inflation #foodprices #eggs #money #dollartrail"""

SLIDES = [
    '<div class=tag>Trail No. 043</div>\n<div class=hook style="font-size:100px">10 groceries: <em>$40.16.</em></div>\n<div class=hook2>A year ago, the same list cost $40.86.</div>\n<div class=mini style="margin-top:60px">Source: U.S. Bureau of Labor Statistics (BLS), Average Retail Food and Energy Prices, U.S. city average, September 2026 vs. September 2025. One unit of each: eggs, ground beef, coffee, bacon, chicken breast, milk, strawberries, bread, pasta, bananas. Totals: our math.</div>',
    stack([(23, R, "COFFEE 23%"), (17, Y, "GROUND BEEF 17%"), (17, BL, "BACON 17%"), (21, P, "CHICKEN + MILK 21%"), (22, G, "OTHER 5 ITEMS 22%")],
          [("Coffee, 1 lb", "$9.33", R), ("Ground beef, 1 lb", "$6.79", Y), ("Bacon, 1 lb", "$6.76", BL), ("Chicken + milk", "$8.31", P), ("Other 5 items", "$8.97", G)],
          "September 2026 U.S. average prices. Other 5: strawberries, eggs, bread, pasta, bananas. Shares: our math.",
          "Where the $40.16 goes", height=680),
    stop(1, 4, "A dozen eggs", "$2.27", "DOWN 34.9% IN A YEAR",
         ["Grade A large eggs averaged <b>$3.49</b> in September 2025.", "That <b>$1.22</b> drop is more than the whole basket&rsquo;s savings (our math)."],
         "Without eggs, the other 9 items cost about 52 cents more (our math).", R),
    stop(2, 4, "Ground beef", "$6.79", "PER POUND, UP 7.4%",
         ["100% ground beef averaged <b>$6.32</b> a year earlier.", "Bacon went the other way: <b>$6.76</b> a pound, down 7.3%."],
         "Beef and bacon now cost almost the same per pound.", Y),
    stop(3, 4, "Pasta", "$1.38", "PER POUND, UP 14.1%",
         ["Spaghetti and macaroni: the biggest jump on the list.", "Strawberries were next, up <b>10.4%</b> to $2.84 a pint."],
         "Big percentages, small dollars: pasta rose 17 cents a pound (our math).", BL),
    stop(4, 4, "Coffee", "$9.33", "PER POUND, UP 2.1%",
         ["The priciest item in the basket.", "Milk ($4.11 a gallon) and bread ($1.83 a pound) both dipped slightly."],
         "Bananas: still about 66 cents a pound.", P),
    '<div class=tag>Detour</div>\n<h2>The drive to the store</h2>\n<div class=taxrow><div class=tx><div class=l>September 2025</div><div class=n>$3.34</div><div class=d>Regular gas, per gallon</div></div><div class=tx><div class=l>September 2026</div><div class=n>$4.48</div><div class=d>Up 34.2%</div></div></div>\n' + note("At $1.14 more a gallon, a 10-gallon fill-up costs about $11 more (our math)."),
    '<div class=tag>End of the trail</div>\n<div class=hook style="font-size:86px">Our 10-item basket: down 1.7%.<br><em>Gas: 34% pricier.</em></div>\n<div class=cta>Send this to the friend<br>who <em>does the grocery run.</em></div>\n<div class=src>' + DT_FOLLOW + '<br><br>Source: U.S. Bureau of Labor Statistics, Average Retail Food and Energy Prices, U.S. city average, September 2025 and September 2026. Basket totals, basket percent change, shares, differences and fill-up cost: our math.</div>',
]
