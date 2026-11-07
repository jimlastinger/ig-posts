import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "tools"))
from lib import *

ACCOUNT = 'dollartrail'
THEME = 'ledger'
TRAIL = '059'
FOLLOWING = '$10 at Chipotle'
SOURCES = ['https://www.sec.gov/Archives/edgar/data/1058090/000105809026000009/cmg-20251231.htm']

CAPTION = """Spend $10 at Chipotle and, going by the company's 2025 books, $2.96 buys the food and packaging, $2.51 pays the crew, and $1.29 ends up as profit.

Data: Chipotle Mexican Grill Form 10-K for 2025 (SEC filing). Company-wide shares of revenue applied to a $10 example order; our math.

Which one surprised you more: the labor or the profit?

#chipotle #burrito #fastfood #personalfinance #money #dollartrail"""

SLIDES = [
    '<div class=tag>Trail No. 059</div>\n<div class=hook style="font-size:110px">$10 at Chipotle. <em>$1.29 is profit.</em></div>\n<div class=hook2>Where your burrito money goes.</div>\n<div class=mini style="margin-top:60px">Source: Chipotle Mexican Grill, Form 10-K for 2025 (SEC filing). Each slice = its share of Chipotle&rsquo;s $11.9 billion 2025 revenue, applied to a $10 example order (our math).</div>',
    stack([(29.6, R, "29.6%"), (25.1, Y, "25.1%"), (19.9, BL, "19.9%"), (9.1, P, "9.1%"), (3.4, G, ""), (12.9, T, "12.9%")],
          [("Food &amp; packaging", "$2.96", R), ("Restaurant crew", "$2.51", Y), ("Rent &amp; running", "$1.99", BL), ("Corporate costs", "$0.91", P), ("Net taxes", "$0.34", G), ("Profit", "$1.29", T), ("Total", "$10.00", "transparent")],
          "Chipotle&rsquo;s 2025 costs and profit as a share of total revenue, applied to $10. Rounded (our math).",
          "Where $10<br>goes.", height=700),
    stop(1, 5, "The food", "$2.96", "FOOD, BEVERAGE AND PACKAGING &middot; 29.6% OF REVENUE",
         ["Ingredients, drinks and packaging cost Chipotle $3.53 billion in 2025."],
         "Its share fell from 29.8% in 2024, even with beef and chicken inflation and new tariffs.", R),
    stop(2, 5, "The crew", "$2.51", "LABOR &middot; 25.1% OF REVENUE",
         ["Pay for restaurant workers: $2.99 billion, or 25.1% of revenue, up from 24.7% in 2024."],
         "Chipotle cites lower sales volumes and restaurant wage inflation.", Y),
    stop(3, 5, "Rent and running the store", "$1.99", "OCCUPANCY + OTHER OPERATING COSTS &middot; 19.9%",
         ["<b>$0.52</b> is rent and occupancy. <b>$1.47</b> covers other restaurant bills, like marketing and utilities."],
         "Chipotle ran 4,042 company-operated restaurants at the end of 2025.", BL),
    stop(4, 5, "Headquarters and more", "$0.91", "G&amp;A, DEPRECIATION, NEW-STORE AND CLOSURE COSTS &middot; 9.1%",
         ["Corporate overhead was $652.0 million. Wear on equipment and buildings added $361.4 million."],
         "Getting new restaurants ready to open cost $49.5 million.", P),
    stop(5, 5, "What Chipotle keeps", "$1.29", "NET INCOME &middot; 12.9% OF REVENUE",
         ["After every cost, Chipotle earned <b>$1.54 billion</b> on <b>$11.9 billion</b> of revenue.", "Income tax took about 40 cents of each $10, partly offset by interest Chipotle earned. Net: 34 cents."],
         "Food and crew together take $5.47 of your $10 (our math).", T),
    '<div class=tag>End of the trail</div>\n<div class=hook style="font-size:92px">Food: $2.96.<br><em>Profit: $1.29.</em></div>\n<div class=cta>Send this to your<br><em>burrito bowl</em> friend.</div>\n<div class=src>' + DT_FOLLOW + '<br><br>Source: Chipotle Mexican Grill, Inc., Form 10-K for the year ended Dec. 31, 2025 (SEC filing), consolidated statements of income and MD&amp;A. Company-wide shares applied to a $10 example order; per-$10 figures: our math.</div>',
]
