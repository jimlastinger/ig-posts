import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "tools"))
from lib import *

ACCOUNT = 'dollartrail'
TRAIL = '010'
FOLLOWING = '$1,000 spent at Apple'
SOURCES = ['https://www.sec.gov/Archives/edgar/data/320193/000032019325000079/R3.htm',
           'https://www.sec.gov/Archives/edgar/data/320193/000032019325000079/aapl-20250927.htm']

CAPTION = """For every $1,000 Apple took in during fiscal 2025, $269 was left as profit after making the products, R&D, running the company and taxes.

Data: Apple Inc. Form 10-K, fiscal year ended Sept. 27, 2025 (Consolidated Statements of Operations). Company-wide averages, not one product.

Did you expect the profit slice to be bigger or smaller?

#apple #iphone #personalfinance #business #moneyfacts #dollartrail"""

SLIDES = [
    '<div class=tag>Trail No. 010</div>\n<div class=hook style="font-size:120px">You spend <em>$1,000</em> at Apple.</div>\n<div class=hook2>$269 of it ends up as profit.</div>\n<div class=mini style="margin-top:60px">Source: Apple Inc. Form 10-K, fiscal year ended Sept. 27, 2025. Every $1,000 of Apple\'s $416.2 billion in net sales, on average.</div>',
    stack([(53.1, W, "$531"), (8.3, BL, "$83"), (6.6, Y, "$66"), (5.0, P, "$50"), (0.1, G, ""), (26.9, R, "$269")],
          [("Making it", "$531", W), ("Research", "$83", BL), ("Selling + admin", "$66", Y), ("Income taxes", "$50", P), ("Other, net", "$1", G), ("Profit", "$269", R)],
          "Per $1,000 of Apple's FY2025 net sales ($416,161 million). Rounded to whole dollars; adds to $1,000.",
          "$1,000.<br>Five stops.", height=700),
    stop(1, 5, "Making it", "$531", "COST OF SALES &middot; $221.0 BILLION",
         ["What it cost Apple to make the products and provide the services it sold."],
         "More than half of every dollar goes right back out the door.", W),
    stop(2, 5, "Research", "$83", "R&amp;D &middot; $34.6 BILLION",
         ["Research and development: designing next year's products and improving this year's."],
         "Apple spent more on research than on selling and running the company.", BL),
    stop(3, 5, "Selling + admin", "$66", "SG&amp;A &middot; $27.6 BILLION",
         ["Selling, general and administrative: the cost of selling everything and running the company."],
         "Together, research and SG&amp;A came to $62.2 billion.", Y),
    stop(4, 5, "Income taxes", "$50", "TAX PROVISION &middot; $20.7 BILLION",
         ["Apple's provision for income taxes was 15.6% of its $132.7 billion pre-tax income."],
         "That's the rate on profit, not on what you paid at the register.", P),
    stop(5, 5, "Profit", "$269", "NET INCOME &middot; $112.0 BILLION",
         ["What's left after everything else. About 27 cents of every dollar Apple took in."],
         "$112 billion in one year: about $307 million a day.", R),
    '<div class=tag>Detour</div>\n<h2>Gadgets vs. subscriptions</h2>\n' + cmp([(36.8, "$36.80", False), (75.4, "$75.40", True)],
        ["Products (iPhone, Mac&hellip;)", "Services (App Store, iCloud&hellip;)"]) + '\n' + note("Gross margin per $100 of sales, FY2025: products $112.9B on $307.0B in sales; services $82.3B on $109.2B. Services keep twice as much before overhead."),
    '<div class=tag>End of the trail</div>\n<div class=hook style="font-size:92px">$1,000 in.<br><em>$269 kept.</em></div>\n<div class=cta>Send this to the friend<br>who just <em>upgraded their phone.</em></div>\n<div class=src>' + DT_FOLLOW + '<br><br>Source: Apple Inc. Form 10-K, fiscal year ended Sept. 27, 2025, Consolidated Statements of Operations. Company-wide averages, not a single product. Rounded.</div>',
]
