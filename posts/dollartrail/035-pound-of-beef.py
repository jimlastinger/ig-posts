import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "tools"))
from lib import *

ACCOUNT = 'dollartrail'
THEME = 'ledger'
TRAIL = '035'
FOLLOWING = 'a pound of beef'
SOURCES = ['https://www.ers.usda.gov/data-products/meat-price-spreads',
           'https://www.ers.usda.gov/media/5020/choice-beef-values-and-spreads-and-the-all-fresh-retail-value.csv?v=62046',
           'https://www.ers.usda.gov/data-products/meat-price-spreads/documentation']

CAPTION = """A pound of Choice beef averaged $9.94 at retail in September 2026, and the farmer's share was $4.91 of it, per USDA. The packing plant added 71 cents, and $4.33 was added after the meat left the plant.

Data: USDA Economic Research Service, Meat Price Spreads (updated Oct. 14, 2026). Rounding: our math.

Did you expect the farmer's cut to be that big?

#beef #groceryprices #farming #food #personalfinance #dollartrail"""

SLIDES = [
    '<div class=tag>Trail No. 035</div>\n<div class=hook style="font-size:104px">A pound of beef: <em>$9.94.</em></div>\n<div class=hook2>Where the money goes, from the ranch to your cart.</div>\n<div class=mini style="margin-top:60px">Source: USDA Economic Research Service (ERS), Meat Price Spreads, Choice beef, September 2026 (updated Oct. 14, 2026). Retail value is a weighted average of retail cuts.</div>',
    stack([(49, R, "FARM 49%"), (7, Y, "PACKER 7%"), (44, BL, "AFTER THE PLANT 44%")],
          [("Farm (net)", "$4.91", R), ("Farm to packer", "71&cent;", Y), ("Plant to store", "$4.33", BL), ("Retail value", "$9.94", W)],
          "USDA ERS, Choice beef, Sept. 2026, per pound. Dollars and shares rounded (our math), so rows may not add exactly.",
          "Where $9.94 lands", height=700),
    stop(1, 3, "The farm", "$4.91", "NET FARM VALUE, PER POUND",
         ["USDA calls it <b>the value of the meat to the farmer</b>. That&rsquo;s <b>49.3%</b> of the retail price."],
         "A year earlier, in Sept. 2025, the farm share was 54.6%.", R),
    stop(2, 3, "The packing plant", "71&cent;", "SPREAD, FARM TO WHOLESALE",
         ["Meat leaves the packing plant worth <b>$5.62</b> a pound. Subtract the <b>$4.91</b> farm value and you get the <b>7.1%</b> slice."],
         "The rest of the animal (hides, fats, bones, offal) is worth about 40&cent; per pound of beef.", Y),
    stop(3, 3, "After the plant", "$4.33", "SPREAD, WHOLESALE TO RETAIL",
         ["Everything added between the plant door and the price on your package: <b>43.5%</b> of the retail price."],
         "USDA measures this gap but doesn&rsquo;t split it into shipping, cutting and the store.", BL),
    '<div class=tag>Detour</div>\n<h2>The farmer&rsquo;s share of the beef dollar</h2>\n' + cmp([(37.3, "37.3%", False), (36.8, "36.8%", False), (40.5, "40.5%", False), (47.8, "47.8%", False), (50.2, "50.2%", False), (53.5, "53.5%", True)],
        ["2020", "2021", "2022", "2023", "2024", "2025"]) + '\n<div class=mini style="margin-top:24px">USDA ERS, Choice beef, annual averages. September 2026: 49.3%.</div>',
    '<div class=tag>Detour</div>\n<h2>Price per pound, annual average</h2>\n<div class=taxrow><div class=tx><div class=l>2024</div><div class=n>$8.24</div><div class=d>Choice beef retail value</div></div><div class=tx><div class=l>2025</div><div class=n>$9.38</div><div class=d>Choice beef retail value</div></div></div>' + note("Monthly prices peaked at $10.49 in July 2026 (highest month in 2024 to 2026), then eased to $9.94 by September."),
    '<div class=tag>End of the trail</div>\n<div class=hook style="font-size:88px">$9.94 a pound.<br><em>Almost half goes to the farm.</em></div>\n<div class=cta>Send this to the friend<br>who <em>runs the grill.</em></div>\n<div class=src>' + DT_FOLLOW + '<br><br>Source: USDA Economic Research Service, Meat Price Spreads, Choice beef values and spreads (updated Oct. 14, 2026). Figures in cents per pound of retail equivalent, rounded to dollars. Shares: our math.</div>',
]
