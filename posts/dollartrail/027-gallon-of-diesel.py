import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "tools"))
from lib import *

ACCOUNT = 'dollartrail'
TRAIL = '027'
FOLLOWING = 'a gallon of diesel'
SOURCES = ['https://www.eia.gov/petroleum/gasdiesel/',
           'https://www.eia.gov/energyexplained/diesel-fuel/prices-and-outlook.php']

CAPTION = """Diesel averaged $6.18 a gallon in the U.S. in the week of Oct. 12, up $2.51 from a year earlier. In EIA's breakdown for May 2026, crude oil was 42% of the price, taxes 11%, and refining plus distribution the rest.

Data: U.S. Energy Information Administration, Gasoline and Diesel Fuel Update (Oct. 14, 2026) and Diesel Fuel Explained. Some figures our math.

What are you paying for diesel where you live?

#diesel #gasprices #trucking #energy #inflation #dollartrail"""

SLIDES = [
    '<div class=tag>Trail No. 027</div>\n<div class=hook style="font-size:108px">A gallon of diesel: <em>$6.18.</em> A year ago: about $3.67.</div>\n<div class=hook2>Where the price of a gallon goes.</div>\n<div class=mini style="margin-top:60px">Source: U.S. Energy Information Administration, Gasoline and Diesel Fuel Update (Oct. 14, 2026). U.S. average on-highway diesel, week of Oct. 12, 2026. Year-ago price: $6.18 minus the $2.51 change, our math.</div>',
    stack([(42, R, "CRUDE OIL 42%"), (47, Y, "REFINING, DELIVERY 47%"), (11, BL, "TAXES 11%")],
          [("Crude oil", "42%", R), ("Refining, delivery", "47%", Y), ("Taxes", "11%", BL)],
          "EIA, &ldquo;What we pay for in a gallon of diesel,&rdquo; May 2026, when diesel averaged $5.60. Refining and distribution &amp; marketing combined (100 &minus; 42 &minus; 11), our math.",
          "Where $5.60 of diesel went, May 2026", height=680),
    stop(1, 4, "Crude oil", "42%", "OF THE PUMP PRICE, MAY 2026",
         ["The biggest single piece. At May&rsquo;s $5.60 a gallon, that&rsquo;s about <b>$2.35</b> (our math)."],
         "Crude is the raw material. Everything after it is turning it into fuel and getting it to you.", R),
    stop(2, 4, "Refining + delivery", "47%", "OF THE PUMP PRICE, MAY 2026 (OUR MATH)",
         ["EIA splits this into refining, and distribution &amp; marketing. Together they were about <b>$2.63</b> of May&rsquo;s $5.60 (our math)."],
         "Combined, these were a bigger share of diesel&rsquo;s price than crude oil.", Y),
    stop(3, 4, "Taxes", "60&cent;", "PER GALLON: 24.4&cent; FEDERAL + 35.86&cent; AVERAGE STATE",
         ["Federal tax on highway diesel is <b>24.4&cent;</b> a gallon. State taxes and fees averaged <b>35.86&cent;</b> as of January 2026."],
         "Taxes are cents per gallon, not a percent. At $6.18, 60&cent; is about 10% of the price (11% at May&rsquo;s $5.60).&nbsp;Our math.", BL),
    stop(4, 4, "Where you fill up", "$8.09", "CALIFORNIA AVERAGE, WEEK OF OCT. 12, 2026",
         ["The lowest region EIA lists, the Lower Atlantic, averaged <b>$5.65</b>. That&rsquo;s about a <b>$2.45</b> gap per gallon (our math)."],
         "The West Coast as a whole averaged $7.24.", P),
    '<div class=tag>Detour</div>\n<h2>Diesel vs. gas, a year apart</h2>\n' + cmp([(3.061, "$3.06", False), (4.331, "$4.33", False), (3.665, "$3.67", False), (6.179, "$6.18", True)],
        ["Gas Oct 2025", "Gas now", "Diesel Oct 2025", "Diesel now"]) + '\n<div class=mini style="margin-top:24px">EIA, U.S. average retail, week of Oct. 12, 2026. Year-ago prices: current price minus EIA&rsquo;s year-ago change, our math.</div>',
    '<div class=tag>End of the trail</div>\n<div class=hook style="font-size:90px">Diesel: up $2.51 in a year.<br><em>Gas: up $1.27.</em></div>\n<div class=cta>Send this to someone<br>who <em>drives a diesel.</em></div>\n<div class=src>' + DT_FOLLOW + '<br><br>Source: U.S. Energy Information Administration, Gasoline and Diesel Fuel Update (Oct. 14, 2026), weekly U.S. and regional averages and price breakdown (May 2026); Diesel Fuel Explained, prices and outlook (taxes). Dollar splits and year-ago prices: our math.</div>',
]
