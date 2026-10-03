import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "tools"))
from lib import *

ACCOUNT = 'dollartrail'
TRAIL = '005'
FOLLOWING = 'a $19.99 Netflix plan'
SOURCES = ['https://www.sec.gov/Archives/edgar/data/1065280/000106528026000033/ex991_q425.htm',
           'https://help.netflix.com/en/node/24926']

CAPTION = """Your $19.99 Netflix plan, followed: about $10.30 pays for the shows and movies, and $4.86 is profit.

Data: Netflix full-year 2025 results (SEC filing, Jan. 2026); U.S. Standard plan price from Netflix's help center. Company-wide 2025 shares applied to one $19.99 month.

Did you expect the profit slice to be bigger or smaller?

#netflix #streaming #personalfinance #money #moneytips #dollartrail"""

SLIDES = [
    '<div class=tag>Trail No. 005</div>\n<div class=hook>Your Netflix plan: <em>$19.99</em> a month.</div>\n<div class=hook2>Here\'s where the money goes.</div>\n<div class=mini style="margin-top:60px">Source: Netflix full-year 2025 results (SEC filing). $19.99 = U.S. Standard plan price, per Netflix\'s help center. Each slice = its share of Netflix\'s $45.2 billion 2025 revenue.</div>',
    stack([(51.5, R, "51.5%"), (19.0, Y, "19.0%"), (5.2, BL, "5.2%"), (24.3, T, "24.3%")],
          [("Shows &amp; movies", "$10.30", R), ("Running Netflix", "$3.79", Y), ("Taxes &amp; interest", "$1.04", BL), ("Profit", "$4.86", T), ("Total", "$19.99", "transparent")],
          "Netflix's 2025 costs and profit as a share of revenue, applied to one $19.99 month. Rounded.",
          "One plan.<br>Four stops."),
    stop(1, 4, "The shows and movies", "$10.30", "COST OF REVENUES &middot; 51.5%",
         ["Mostly what Netflix pays for its shows and movies, spread over the years they stream. It also covers streaming delivery, customer service and payment processing."],
         "In 2025 this was $23.3 billion, more than every other cost combined.", R),
    stop(2, 4, "Running the company", "$3.79", "TECH + MARKETING + ADMIN &middot; 19.0%",
         ["Engineers and the app (7.5%), ads and promotion (7.3%), and offices, executives and lawyers (4.2%)."],
         "Netflix spent about as much on technology as on marketing in 2025: $3.4B vs. $3.3B.", Y),
    stop(3, 4, "Taxes and interest", "$1.04", "INCOME TAX + NET INTEREST &middot; 5.2%",
         ["Income taxes were $1.74 billion. Interest on Netflix's debt, minus what it earned on its cash, was another $0.6 billion."],
         "Taxes alone: about 77 cents of your $19.99.", BL),
    stop(4, 4, "What Netflix keeps", "$4.86", "NET INCOME &middot; 24.3%",
         ["After every cost and tax, Netflix earned $11.0 billion in profit in 2025."],
         "Roughly one dollar in four you pay Netflix ends up as profit.", T),
    '<div class=tag>End of the trail</div>\n<div class=hook style="font-size:96px">Half pays for the shows.<br><em>A quarter is profit.</em></div>\n<div class=cta>Send this to the friend<br>who shares <em>your password.</em></div>\n<div class=src>' + DT_FOLLOW + '<br><br>Source: Netflix, Inc. Q4 2025 shareholder letter, consolidated statements of operations, twelve months ended Dec. 31, 2025 (SEC Form 8-K, Jan. 2026); Netflix Help Center, Plans and Pricing (U.S.).</div>',
]
