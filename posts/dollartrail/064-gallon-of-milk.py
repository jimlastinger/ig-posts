import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "tools"))
from lib import *

ACCOUNT = 'dollartrail'
THEME = 'receipt'
TRAIL = '064'
FOLLOWING = 'A $3.98 gallon of milk'
SOURCES = ['https://www.ers.usda.gov/data-products/charts-of-note/112769', 'https://ers.usda.gov/data-products/price-spreads-from-farm-to-consumer/highlights-and-interactive-charts']

CAPTION = """A gallon of whole milk averaged $3.98 at the store in 2024, and the dairy farm's share was $1.97 of it. The other $2.01 paid for everything after the farm gate, all the way to checkout.

Data: USDA Economic Research Service, Chart of Note on whole milk (June 17, 2025) and Price Spreads from Farm to Consumer (Cheddar).

Did you think the farmer got more or less than half?

#milk #dairy #farmers #groceries #personalfinance #dollartrail"""

SLIDES = [
    '<div class=tag>Trail No. 064</div>\n<div class=hook style="font-size:104px">A $3.98 gallon of milk: <em>the farm gets $1.97.</em></div>\n<div class=hook2>The other $2.01 goes to everyone after the farm gate.</div>\n<div class=mini style="margin-top:60px">Source: USDA Economic Research Service, Chart of Note &ldquo;Farmers earn about half of retail price for whole milk&rdquo; (June 17, 2025). Retail price and farm value of a gallon of whole milk, 2024.</div>',
    stack([(49, G, "49%"), (51, R, "51%")],
          [("The dairy farm", "$1.97", G), ("After the farm", "$2.01", R), ("Gallon", "$3.98", "transparent")],
          "USDA ERS, whole milk, 2024: farm value $1.97 of a $3.98 retail price (farm share 49%). $2.01 = $3.98 minus $1.97 (our math).",
          "Where $3.98<br>goes.", height=700),
    stop(1, 4, "At the store", "$3.98", "RETAIL PRICE &middot; 2024",
         ["A gallon of whole milk cost <b>$3.98</b> in 2024, down 5 cents from the year before."],
         "The milk itself got cheaper. The farmer still got paid more.", R),
    stop(2, 4, "At the farm", "$1.97", "FARM VALUE &middot; 2024",
         ["The milk inside that gallon was worth <b>$1.97</b> to the farmer, up 9 cents from 2023."],
         "So the farm&rsquo;s share rose to 49% from 47% while the shelf price fell.", G),
    stop(3, 4, "After the farm", "$2.01", "RETAIL PRICE MINUS FARM VALUE (OUR MATH)",
         ["The rest of the price, <b>$2.01</b>, covers everything after the farm gate, all the way to the store&rsquo;s checkout."],
         "The farmer&rsquo;s cut and everyone else&rsquo;s were almost exactly even.", R),
    stop(4, 4, "Over 10 years", "47&ndash;56%", "FARM SHARE OF WHOLE MILK &middot; 2015&ndash;2024",
         ["From 2015 to 2024, the retail price ranged from <b>$2.90 to $4.09</b> a gallon. The farm value ranged from <b>$1.51 to $2.27</b>."],
         "The farm&rsquo;s share never fell below 47% or rose above 56%.", G),
    '<div class=tag>Detour</div>\n<h2>Farm share of what you pay</h2>\n' + cmp([(49, "49%", True), (36, "36%", False)],
        ["Whole milk (2024)", "Cheddar cheese (2022)"]) + '\n<div class=mini style="margin-top:24px">USDA ERS: dairy farmers got 36% of the grocery price of Cheddar cheese in 2022. It takes 10.3 pounds of milk (1.2 gallons) to make a pound of Cheddar.</div>',
    '<div class=tag>End of the trail</div>\n<div class=hook style="font-size:88px">$3.98 for the gallon.<br><em>$1.97 for the farm.</em></div>\n<div class=cta>Send this to the friend<br>who <em>grew up on a farm.</em></div>\n<div class=src>' + DT_FOLLOW + '<br><br>Source: USDA Economic Research Service, Price Spreads from Farm to Consumer; Chart of Note &ldquo;Farmers earn about half of retail price for whole milk&rdquo; (June 17, 2025). $2.01 after the farm: our math.</div>',
]
