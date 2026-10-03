import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "tools"))
from lib import *

ACCOUNT = 'dollartrail'
TRAIL = '006'
FOLLOWING = 'a $5 latte'
SOURCES = ['https://www.sec.gov/Archives/edgar/data/829224/000082922425000074/sbux-09282025xexhibit991.htm',
           'https://www.sec.gov/Archives/edgar/data/829224/000082922425000114/sbux-20250928.htm']

CAPTION = """A $5 latte, followed through Starbucks's books: $2.29 runs the store, $1.57 buys the coffee, milk and cup, and about 25 cents is profit.

Data: Starbucks fiscal 2025 results (52 weeks ended Sept. 28, 2025, SEC filing). Company-wide shares of revenue applied to a $5 example drink; real prices vary.

Would you have guessed the coffee is not the biggest cost?

#starbucks #coffee #latte #personalfinance #money #dollartrail"""

SLIDES = [
    '<div class=tag>Trail No. 006</div>\n<div class=hook>A latte: <em>$5.</em></div>\n<div class=hook2>Where your coffee money goes.</div>\n<div class=mini style="margin-top:60px">Source: Starbucks fiscal 2025 results (SEC filing). Each slice = its share of Starbucks\'s $37.2 billion fiscal 2025 revenue, applied to a $5 example drink. Real prices vary by store and size.</div>',
    stack([(45.9, R, "45.9%"), (31.4, Y, "31.4%"), (15.5, BL, "15.5%"), (2.2, P, ""), (5.0, T, "5.0%")],
          [("Running stores", "$2.29", R), ("Coffee, milk, cup", "$1.57", Y), ("Corporate costs", "$0.78", BL), ("Taxes &amp; interest", "$0.11", P), ("Profit", "$0.25", T), ("Total", "$5.00", "transparent")],
          "Starbucks's fiscal 2025 costs and profit as a share of revenue, applied to $5. Rounded.",
          "One latte.<br>Five stops.", height=700),
    stop(1, 5, "Running the store", "$2.29", "STORE OPERATING EXPENSES &middot; 45.9%",
         ["The cost of running the cafés Starbucks operates itself: the people behind the counter, rent and other store costs."],
         "Inside Starbucks-run cafés alone, store costs took 55.5% of every dollar those cafés brought in. On $5, that's $2.77.", R),
    stop(2, 5, "Coffee, milk and cup", "$1.57", "PRODUCT &amp; DISTRIBUTION COSTS &middot; 31.4%",
         ["Coffee, dairy, food, cups, and trucking it all to roughly 41,000 stores worldwide."],
         "How much of this reaches the coffee farmer? Starbucks doesn't report that number, so we won't guess.", Y),
    stop(3, 5, "Corporate costs", "$0.78", "OVERHEAD, DEPRECIATION, CHARGES &middot; 15.5%",
         ["Corporate overhead ($2.6B), wear on equipment and stores ($1.7B), and $0.9B in restructuring and impairment charges, plus other costs."],
         "The restructuring charges alone cost more than Starbucks paid in income tax.", BL),
    stop(4, 5, "Taxes and interest", "$0.11", "INCOME TAX + NET INTEREST &middot; 2.2%",
         ["Income tax was $651 million. Interest on debt, minus interest earned and income from partner companies, added a bit more."],
         "Tax alone: about 9 cents on your $5 drink.", P),
    stop(5, 5, "What Starbucks keeps", "$0.25", "NET EARNINGS &middot; 5.0%",
         ["After every cost, Starbucks earned $1.86 billion in fiscal 2025, on $37.2 billion of revenue."],
         "A quarter of profit on a $5 drink. Running the store costs nine times more.", T),
    '<div class=tag>End of the trail</div>\n<div class=hook style="font-size:96px">The coffee isn\'t the big cost.<br><em>The café is.</em></div>\n<div class=cta>Send this to your<br><em>daily latte</em> friend.</div>\n<div class=src>' + DT_FOLLOW + '<br><br>Source: Starbucks Corp., Q4 and fiscal 2025 results, consolidated statements of earnings, 52 weeks ended Sept. 28, 2025 (SEC Form 8-K, Oct. 2025); Starbucks Form 10-K, fiscal 2025 (store counts).</div>',
]
