import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "tools"))
from lib import *

ACCOUNT = 'dollartrail'
THEME = 'receipt'
TRAIL = '037'
FOLLOWING = 'your grocery bill'
SOURCES = ['https://ers.usda.gov/data-products/food-price-outlook/summary-findings']

CAPTION = """USDA expects grocery prices to rise 2.3% in 2026, but not evenly: beef and veal +8.7%, sugar and sweets +6.5%, eggs down 29.3%.

Data: USDA Economic Research Service, Food Price Outlook (updated Oct. 23, 2026). 2026 figures are forecasts.

Which grocery price have you noticed most?

#groceries #foodprices #inflation #beef #costofliving #dollartrail"""

SLIDES = [
    '<div class=tag>Trail No. 037</div>\n<div class=hook style="font-size:104px">Groceries: set to rise <em>2.3%</em> this year.</div>\n<div class=hook2>Beef up 8.7%. Eggs down 29.3%.</div>\n<div class=mini style="margin-top:60px">Source: USDA Economic Research Service (ERS), Food Price Outlook, updated Oct. 23, 2026. 2026 forecasts, annual average change in retail prices.</div>',
    '<div class=tag>The trail map</div>\n<h2>One cart,<br>very different prices</h2>\n' + cmp([(8.7, "+8.7%", False), (6.5, "+6.5%", False), (5.8, "+5.8%", False), (4.4, "+4.4%", False), (2.3, "+2.3%", True)],
        ["Beef", "Sweets", "Fresh veg", "Drinks", "All groceries"]) + '\n<div class=mini style="margin-top:24px">USDA ERS forecasts for 2026. Beef = beef and veal. Sweets = sugar and sweets. Drinks = nonalcoholic beverages. Eggs (&minus;29.3%) and dairy (&minus;0.4%) fall and are not shown.</div>',
    stop(1, 4, "Beef", "+8.7%", "BEEF AND VEAL, 2026 FORECAST",
         ["The biggest forecast rise on this trail.", "Wholesale beef is forecast up <b>8.8%</b>."],
         "In September, beef and veal cost 3.5% more than a year earlier.", R),
    stop(2, 4, "Sugar and sweets", "+6.5%", "SUGAR AND SWEETS, 2026 FORECAST",
         ["Just in time for Halloween."],
         "September prices were 5.5% higher than a year earlier.", Y),
    stop(3, 4, "Drinks", "+4.4%", "NONALCOHOLIC BEVERAGES, 2026 FORECAST",
         ["Coffee: <b>7.1%</b> higher in September than a year earlier."],
         "USDA counts coffee in this group.", BL),
    stop(4, 4, "Eggs", "&minus;29.3%", "EGGS, 2026 FORECAST",
         ["The big drop on the receipt. At the farm, egg prices are forecast to fall <b>81.2%</b>."],
         "September eggs were 20.6% cheaper than a year earlier.", T),
    '<div class=tag>Detour</div>\n<h2>Eating out is rising faster</h2>\n<div class=taxrow><div class=tx><div class=l>Groceries</div><div class=n>+2.3%</div><div class=d>Food at home, 2026</div></div><div class=tx><div class=l>Restaurants</div><div class=n>+3.5%</div><div class=d>Food away from home, 2026</div></div></div>\n' + note("Both are forecasts. The 2006-25 averages: 2.6% a year for groceries, 3.5% for eating out."),
    '<div class=tag>End of the trail</div>\n<div class=hook style="font-size:88px">2.3% on average.<br><em>8.7% for beef.</em></div>\n<div class=cta>Send this to the friend<br>who <em>does the grocery run.</em></div>\n<div class=src>' + DT_FOLLOW + '<br><br>Source: USDA Economic Research Service, Food Price Outlook, Summary Findings (updated Oct. 23, 2026; uses September 2026 CPI and PPI data). 2026 figures are forecasts.</div>',
]
