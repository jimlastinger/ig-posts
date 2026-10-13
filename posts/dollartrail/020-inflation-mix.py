import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "tools"))
from lib import *

ACCOUNT = 'dollartrail'
THEME = 'ledger'
TRAIL = '020'
FOLLOWING = '3.4% inflation'
SOURCES = ['https://www.bls.gov/news.release/cpi.nr0.htm']

CAPTION = """Consumer prices rose 3.4% in the 12 months ending August 2026, but gasoline rose 27.4% and fuel oil 52.0%. Leave out food and energy, and prices rose 2.4%.

Data: U.S. Bureau of Labor Statistics, Consumer Price Index, August 2026 (12-month changes, not seasonally adjusted).

Which price have you noticed most?

#inflation #cpi #gasprices #economy #personalfinance #dollartrail"""

SLIDES = [
    '<div class=tag>Trail No. 020</div>\n<div class=hook style="font-size:116px">Prices rose <em>3.4%</em> in a year.</div>\n<div class=hook2>Gasoline rose 27.4%. Used cars got cheaper.</div>\n<div class=mini style="margin-top:60px">Source: U.S. Bureau of Labor Statistics, Consumer Price Index, August 2026 (released Sept. 11, 2026). 12 months ending August 2026, not seasonally adjusted.</div>',
    '<div class=tag>The trail map</div>\n<h2>One average,<br>very different prices</h2>\n' + cmp([(52.0, "+52.0%", False), (27.4, "+27.4%", False), (23.4, "+23.4%", False), (3.4, "+3.4%", True), (2.4, "+2.4%", False)],
        ["Fuel oil", "Gasoline", "Airfares", "All items", "Core"]) + '\n<div class=mini style="margin-top:24px">BLS CPI, 12 months ending August 2026, not seasonally adjusted. Core = all items less food and energy. Airfares = airline fares.</div>',
    stop(1, 4, "Energy", "+16.3%", "ENERGY PRICES, 12 MONTHS TO AUGUST",
         ["Gasoline <b>+27.4%</b>. Fuel oil <b>+52.0%</b>."],
         "Your utility bills rose much less: electricity +3.8%, piped gas service +4.4%.", R),
    stop(2, 4, "Food", "+2.7%", "ALL FOOD, 12 MONTHS TO AUGUST",
         ["Groceries (food at home) <b>+2.2%</b>. Eating out (food away from home) <b>+3.4%</b>."],
         "Dairy fell 0.3%. Meats, poultry, fish and eggs rose 1.1%.", Y),
    stop(3, 4, "Flying", "+23.4%", "AIRLINE FARES, 12 MONTHS TO AUGUST",
         ["Almost seven times the overall rate of 3.4% (our math)."],
         "On this trail, only fuel oil and gasoline rose faster.", P),
    stop(4, 4, "Cars", "&minus;2.3%", "USED CARS AND TRUCKS, 12 MONTHS TO AUGUST",
         ["New vehicles rose just <b>0.6%</b>."],
         "Gasoline up 27.4%, used cars down 2.3%: same 12 months.", BL),
    '<div class=tag>Detour</div>\n<h2>Take out food and energy</h2>\n<div class=taxrow>\n <div class=tx><div class=l>All items</div><div class=n>3.4%</div><div class=d>The headline number.</div></div>\n <div class=tx><div class=l>Core</div><div class=n>2.4%</div><div class=d>All items less food and energy.</div></div>\n</div>\n' + note("Shelter rose 3.0%, apparel 3.6% and medical care services 2.5%. The biggest jumps on this trail were energy and airfares."),
    '<div class=tag>End of the trail</div>\n<div class=hook style="font-size:92px">3.4% on average.<br><em>27.4% at the pump.</em></div>\n<div class=cta>Send this to the friend<br>who just <em>filled up the tank.</em></div>\n<div class=src>' + DT_FOLLOW + '<br><br>Source: U.S. Bureau of Labor Statistics, Consumer Price Index News Release, August 2026 (USDL-26-1496, Sept. 11, 2026). 12-month changes, not seasonally adjusted. September data due Oct. 14.</div>',
]
