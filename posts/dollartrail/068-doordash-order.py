import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "tools"))
from lib import *

ACCOUNT = 'dollartrail'
THEME = 'ledger'
TRAIL = '068'
FOLLOWING = 'A $40 DoorDash order'
SOURCES = ['https://www.sec.gov/Archives/edgar/data/1792789/000179278926000012/prodq4dashex991-pressrelea.htm']

CAPTION = """Spend $40 on DoorDash and about $34.62 never becomes DoorDash's money. Most of it goes to the restaurant, the Dasher and taxes. DoorDash's revenue is $5.38 of it, and after costs, taxes and the interest it earns on its cash, it keeps about 37 cents.

Data: DoorDash, Inc. fourth quarter and full year 2025 results (SEC Form 8-K, Feb. 18, 2026). Each 2025 figure as a share of $102.0 billion in Marketplace GOV (sum of the four quarters), applied to a $40 order; our math.

Did you think DoorDash kept more than that?

#doordash #fooddelivery #takeout #personalfinance #money #dollartrail"""

SLIDES = [
    '<div class=tag>Trail No. 068</div>\n<div class=hook style="font-size:100px">A $40 DoorDash order: <em>DoorDash keeps about 37 cents.</em></div>\n<div class=hook2>Most of the money passes straight through.</div>\n<div class=mini style="margin-top:60px">Source: DoorDash, Inc. full year 2025 results (SEC Form 8-K). Each figure = its share of $102.0 billion in 2025 Marketplace GOV, applied to $40 (our math).</div>',
    stack([(86.6, G, "86.6%"), (12.7, R, "12.7%"), (0.7, Y, "")],
          [("Passes through", "$34.62", G), ("DoorDash costs", "$5.09", R), ("Operating profit", "$0.28", Y), ("Your order", "$40", "transparent")],
          "Money that passes through, mostly to restaurants, Dashers and taxes, DoorDash&rsquo;s 2025 costs, and its income from operations, as shares of Marketplace GOV. Rounded (our math).",
          "Where $40<br>goes.", height=700),
    stop(1, 5, "You tap &ldquo;Place order&rdquo;", "$40.00", "MARKETPLACE GOV &middot; 2025",
         ["DoorDash orders added up to <b>$102.0 billion</b> in 2025, with taxes, tips and fees (four quarters added, our math)."],
         "Our $40 is an example. Includes Deliveroo, bought Oct. 2, 2025.", G),
    stop(2, 5, "The restaurant and the Dasher", "$34.62", "GOV MINUS DOORDASH REVENUE",
         ["<b>86.6%</b> never becomes DoorDash revenue. Most goes to restaurants, Dashers and taxes."],
         "DoorDash says 2025 meant nearly $75 billion in sales for merchants and over $20 billion for Dashers.", G),
    stop(3, 5, "DoorDash&rsquo;s cut", "$5.38", "REVENUE &middot; 2025",
         ["DoorDash&rsquo;s 2025 revenue was <b>$13.7 billion</b>, about 13.4% of Marketplace GOV (our math)."],
         "DoorDash calls this its Net Revenue Margin. Each quarter of 2025 it ran between 13.1% and 13.8%.", R),
    stop(4, 5, "Running the app", "$5.09", "TOTAL COSTS AND EXPENSES",
         ["Cost of revenue <b>$2.64</b>, sales and marketing $0.97, general and administrative $0.63, research and development $0.56, depreciation $0.29."],
         "Sales and marketing alone cost over three times its operating profit. Rounded (our math).", R),
    stop(5, 5, "DoorDash&rsquo;s profit", "$0.28", "INCOME FROM OPERATIONS",
         ["What&rsquo;s left of revenue after costs: <b>$723 million</b> in 2025, about $0.28 per $40 (our math)."],
         "After interest on its cash, taxes and other items, net income for stockholders was $935 million, about $0.37 per $40 (our math).", Y),
    '<div class=tag>Detour</div>\n<h2>DoorDash net income, in millions</h2>\n' + cmp([(123, "$123M", False), (935, "$935M", True)],
        ["2024", "2025"]) + '\n<div class=mini style="margin-top:24px">Net income attributable to DoorDash, Inc. common stockholders. 2024 revenue: $10.7 billion. 2025: $13.7 billion.</div>',
    '<div class=tag>End of the trail</div>\n<div class=hook style="font-size:88px">$40 for dinner.<br><em>DoorDash keeps about 37 cents.</em></div>\n<div class=cta>Send this to the friend<br>who <em>orders DoorDash every night.</em></div>\n<div class=src>' + DT_FOLLOW + '<br><br>Source: DoorDash, Inc. fourth quarter and full year 2025 results, Form 8-K Exhibit 99.1 (Feb. 18, 2026, SEC filing): Marketplace GOV by quarter, revenue, costs and net income. Per-$40 figures: our math.</div>',
]
