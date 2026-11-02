import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "tools"))
from lib import *

ACCOUNT = 'dollartrail'
THEME = 'receipt'
TRAIL = '052'
FOLLOWING = 'a gallon of regular gas'
SOURCES = ['https://www.eia.gov/petroleum/gasdiesel/']

CAPTION = """Regular gas averaged $4.27 a gallon in the U.S. the week of Oct. 26, $1.23 more than a year earlier, per EIA. Where you fill up matters: California averaged $5.89 and Texas $3.63, a $33.84 gap on a 15-gallon tank (our math).

Data: U.S. Energy Information Administration, Gasoline and Diesel Fuel Update (released Oct. 27, 2026). Fill-up math: ours.

What did you pay at your last fill-up?

#gasprices #gas #inflation #personalfinance #money #dollartrail"""

SLIDES = [
    '<div class=tag>Trail No. 052</div>\n<div class=hook style="font-size:100px">A gallon of regular: <em>$4.27.</em></div>\n<div class=hook2>U.S. average, week of Oct. 26. That&rsquo;s $1.23 more than a year ago.</div>\n<div class=mini style="margin-top:60px">Source: U.S. Energy Information Administration (EIA), Gasoline and Diesel Fuel Update, released Oct. 27, 2026. Year-ago price and fill-up totals: our math.</div>',
    stack([(71, G, "A YEAR AGO: $3.04"), (29, R, "THE INCREASE: $1.23")],
          [("Price a year ago", "$3.04", G), ("Added since", "+$1.23", R)],
          "U.S. regular, week of Oct. 26, 2026: $4.27. Year-ago price is EIA&rsquo;s $4.269 minus its $1.234 change (our math).",
          "Inside today&rsquo;s $4.27", height=640),
    stop(1, 4, "Your tank", "$64.04", "15 GALLONS AT THE U.S. AVERAGE (OUR MATH)",
         ["A year ago the same fill-up was about <b>$45.53</b>.", "That&rsquo;s <b>$18.51 more</b> per tank."],
         "EIA prices are weekly retail averages for regular gasoline.", Y),
    stop(2, 4, "California", "$5.89", "AVERAGE PRICE, GALLON OF REGULAR, WEEK OF OCT. 26",
         ["Highest of every region, state and city in EIA&rsquo;s weekly table.", "15 gallons: about <b>$88.32</b> (our math)."],
         "Up $1.53 from a year ago, though it fell 14.3 cents in the latest week.", R),
    stop(3, 4, "Texas", "$3.63", "AVERAGE PRICE, GALLON OF REGULAR, WEEK OF OCT. 26",
         ["Lowest of the nine states in EIA&rsquo;s weekly table. Gulf Coast region: <b>$3.70</b>.", "15 gallons: about <b>$54.48</b> (our math)."],
         "A California tank costs $33.84 more than a Texas one (our math).", BL),
    stop(4, 4, "Ohio&rsquo;s week", "+33&cent;", "ONE-WEEK JUMP IN OHIO, OCT. 19 TO OCT. 26",
         ["From <b>$4.05</b> to <b>$4.38</b> a gallon.", "The Midwest rose 12.4 cents; the U.S. average fell 1.5 cents."],
         "Prices can swing by region in a single week.", P),
    '<div class=tag>Detour</div>\n<h2>A gallon of regular, week of Oct. 26</h2>\n' + cmp([(5.417, "$5.42", True), (4.458, "$4.46", False), (4.269, "$4.27", False), (4.022, "$4.02", False), (3.702, "$3.70", False)],
        ["West Coast", "Rockies", "Midwest", "East Coast", "Gulf Coast"]) + '\n<div class=mini style="margin-top:24px">EIA regional averages (PADD regions), regular gasoline, week of Oct. 26, 2026. The Midwest matched the U.S. average.</div>',
    '<div class=tag>End of the trail</div>\n<div class=hook style="font-size:86px">$4.27 a gallon.<br><em>$1.23 more than last year.</em></div>\n<div class=cta>Send this to the friend<br>with <em>the long commute.</em></div>\n<div class=src>' + DT_FOLLOW + '<br><br>Source: U.S. Energy Information Administration, Gasoline and Diesel Fuel Update (eia.gov/petroleum/gasdiesel), released Oct. 27, 2026, prices for week of Oct. 26. Year-ago price and fill-up totals: our math.</div>',
]
