import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "tools"))
from lib import *

ACCOUNT = 'dollartrail'
THEME = 'receipt'
TRAIL = '067'
FOLLOWING = 'A $20 Domino&rsquo;s order'
SOURCES = ['https://www.sec.gov/Archives/edgar/data/1286681/000119312526062313/dpz-ex99_1.htm', 'https://www.sec.gov/Archives/edgar/data/1286681/000119312526062321/R26.htm']

CAPTION = """Order $20 of Domino's and about $15 of it stays with the store that made your pizza. Domino's itself takes in $4.91, mostly from selling food to those stores, and keeps about 60 cents as profit.

Data: Domino's Pizza, Inc. fourth quarter and fiscal 2025 results (SEC Form 8-K, Feb. 23, 2026) and 2025 Form 10-K. Each 2025 figure as a share of $20.1 billion in global retail sales, applied to a $20 order; our math.

Who did you think made more off your pizza, the store or Domino's?

#dominos #pizza #franchise #personalfinance #money #dollartrail"""

SLIDES = [
    '<div class=tag>Trail No. 067</div>\n<div class=hook style="font-size:100px">A $20 Domino&rsquo;s order: <em>Domino&rsquo;s keeps about 60 cents.</em></div>\n<div class=hook2>Most of your money stays at the store.</div>\n<div class=mini style="margin-top:60px">Source: Domino&rsquo;s Pizza, Inc. fiscal 2025 results (SEC Form 8-K). Each figure = its share of $20.1 billion in 2025 global retail sales, applied to $20 (our math).</div>',
    stack([(75.5, G, "75.5%"), (19.8, R, "19.8%"), (4.7, Y, "4.7%")],
          [("Stays with the stores", "$15.09", G), ("Domino&rsquo;s costs", "$3.96", R), ("Domino&rsquo;s operating profit (4.7%)", "$0.95", Y), ("Your order", "$20", "transparent")],
          "Money that never becomes Domino&rsquo;s revenue, Domino&rsquo;s 2025 costs, and its income from operations, as shares of global retail sales. Rounded (our math).",
          "Where $20<br>goes.", height=700),
    stop(1, 5, "You hit &ldquo;Order&rdquo;", "$20.00", "GLOBAL RETAIL SALES &middot; 2025",
         ["Customers spent <b>$20.1 billion</b> at Domino&rsquo;s stores worldwide in fiscal 2025, at 22,142 stores."],
         "Our $20 order is an example, not Domino&rsquo;s average ticket.", G),
    stop(2, 5, "The store owner", "$15.09", "RETAIL SALES MINUS DOMINO&rsquo;S REVENUE",
         ["<b>75.5%</b> of what customers spend never becomes Domino&rsquo;s revenue. It stays with the stores and pays to run them."],
         "In the U.S., 6,924 of 7,186 Domino&rsquo;s stores are franchised. Domino&rsquo;s owns 262.", G),
    stop(3, 5, "The food supplier", "$2.97", "SUPPLY CHAIN REVENUE &middot; 2025",
         ["Domino&rsquo;s sells food and other products to its franchised stores from its own supply chain centers in the U.S. and Canada. That&rsquo;s <b>$3.0 billion</b> a year."],
         "It&rsquo;s 60.5% of Domino&rsquo;s revenue. After the cost of those goods, about $0.34 is left (our math).", R),
    stop(4, 5, "Royalties and ads", "$1.57", "FRANCHISE ROYALTIES, FEES AND ADVERTISING",
         ["Franchisees pay royalties and ad fees as a share of their sales. Royalties and fees: <b>$1.01</b> ($0.67 U.S., $0.34 international)."],
         "The other $0.56 is the U.S. ad fund. In 2025, $559.5 million came in and the same amount went out on ads.", Y),
    stop(5, 5, "Domino&rsquo;s profit", "$0.95", "INCOME FROM OPERATIONS",
         ["Domino&rsquo;s took in $4.91, including $0.37 from its own stores. Costs used $3.96, leaving <b>$0.95</b>."],
         "Net income after interest, taxes and other items: $601.7 million, about $0.60 per $20 (our math).", Y),
    '<div class=tag>Detour</div>\n<h2>Domino&rsquo;s profit per $100 spent at its stores</h2>\n' + cmp([(3.05, "$3.05", False), (2.99, "$2.99", True)],
        ["2024", "2025"]) + '\n<div class=mini style="margin-top:24px">2024: $584.2 million net income on $19.1 billion in global retail sales. 2025: $601.7 million on $20.1 billion. Sales grew faster than profit, so the cut slipped a little (our math).</div>',
    '<div class=tag>End of the trail</div>\n<div class=hook style="font-size:88px">$20 for the pizza.<br><em>Domino&rsquo;s keeps about 60 cents.</em></div>\n<div class=cta>Send this to the friend<br>who <em>orders Domino&rsquo;s every Friday.</em></div>\n<div class=src>' + DT_FOLLOW + '<br><br>Source: Domino&rsquo;s Pizza, Inc. fourth quarter and fiscal 2025 results, Form 8-K Exhibit 99.1 (Feb. 23, 2026), and 2025 Form 10-K (SEC filings): global retail sales, store counts, revenue, costs and net income. Per-$20 figures: our math.</div>',
]
