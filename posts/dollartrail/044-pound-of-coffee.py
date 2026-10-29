import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "tools"))
from lib import *

ACCOUNT = 'dollartrail'
THEME = 'ledger'
TRAIL = '044'
FOLLOWING = 'a pound of coffee'
SOURCES = ['https://www.bls.gov/regions/mid-atlantic/data/averageretailfoodandenergyprices_usandNortheast_table.htm',
           'https://apps.fas.usda.gov/psdonline/circulars/2026/07/coffee.pdf']

CAPTION = """Ground coffee averaged $9.33 a pound in U.S. stores in September 2026, up 2.1% in a year, per BLS. Meanwhile USDA forecasts a record world crop for 2026/27 and says the ICO's world coffee price index fell 25% in the seven months before July.

Data: U.S. Bureau of Labor Statistics, Average Retail Food and Energy Prices (September 2026); USDA Foreign Agricultural Service, Coffee: World Markets and Trade (July 2026). Shares and pounds: our math.

How much coffee does your house go through in a week?

#coffee #coffeelover #foodprices #inflation #money #dollartrail"""

SLIDES = [
    '<div class=tag>Trail No. 044</div>\n<div class=hook style="font-size:100px">A pound of coffee: <em>$9.33.</em></div>\n<div class=hook2>Up 2.1% in a year. World coffee prices fell 25% in early 2026.</div>\n<div class=mini style="margin-top:60px">Source: U.S. Bureau of Labor Statistics (BLS), average price, coffee, 100% ground roast, U.S. city average, September 2026. USDA Foreign Agricultural Service (FAS), Coffee: World Markets and Trade, July 2026.</div>',
    stack([(38, R, "BRAZIL 38%"), (17, Y, "VIETNAM 17%"), (7, BL, "COLOMBIA 7%"), (38, G, "REST OF WORLD 38%")],
          [("Brazil", "71.9M", R), ("Vietnam", "32.5M", Y), ("Colombia", "13.4M", BL), ("Rest of world", "71.9M", G)],
          "World production forecast, 2026/27: a record 189.7 million 60-kilogram bags (USDA FAS). Shares: our math.",
          "Where the beans come from", height=680),
    stop(1, 4, "Brazil", "71.9M", "BAGS FORECAST FOR 2026/27, A RECORD",
         ["Up <b>8.9 million</b> bags from the year before.", "Brazil grows both Arabica and Robusta beans."],
         "Ethiopia, Uganda and Vietnam are also forecast to set records.", R),
    stop(2, 4, "Vietnam and Colombia", "32.5M", "BAGS FROM VIETNAM, A RECORD FORECAST",
         ["Vietnam is forecast up 800,000 bags.", "Colombia: <b>13.4 million</b> bags, up 900,000."],
         "USDA says Colombia&rsquo;s exports go mostly to the U.S. and the EU.", Y),
    stop(3, 4, "The U.S. cup", "26.95M", "BAGS, U.S. CONSUMPTION, 2026/27 FORECAST",
         ["That&rsquo;s about <b>3.6 billion pounds</b> of coffee beans (our math).", "Imports: <b>26.9 million</b> bags, nearly all of it."],
         "One bag holds 60 kilograms, about 132 pounds (our math).", BL),
    stop(4, 4, "Your shelf", "$9.33", "PER POUND, SEPTEMBER 2026",
         ["Ground coffee averaged <b>$9.14</b> a year earlier.", "That&rsquo;s up <b>2.1%</b>, per BLS."],
         "USDA says world coffee prices fell 25% in the 7 months before July 2026.", R),
    '<div class=tag>Detour</div>\n<h2>The shelf price, per pound</h2>\n' + cmp([(9.139, "$9.14", False), (9.299, "$9.30", False), (9.332, "$9.33", True)],
        ["Sept 2025", "Aug 2026", "Sept 2026"]) + '\n<div class=mini style="margin-top:24px">BLS U.S. city average, coffee, 100% ground roast. The world price is a different measure: the International Coffee Organization (ICO) monthly composite index, cited by USDA FAS.</div>',
    '<div class=tag>End of the trail</div>\n<div class=hook style="font-size:86px">A record crop forecast.<br><em>$9.33 a pound for now.</em></div>\n<div class=cta>Send this to the friend<br>who <em>can&rsquo;t start the day without it.</em></div>\n<div class=src>' + DT_FOLLOW + '<br><br>Source: U.S. Bureau of Labor Statistics, Average Retail Food and Energy Prices, September 2025 to September 2026; USDA Foreign Agricultural Service, Coffee: World Markets and Trade (July 2, 2026). Shares, bag weight and pounds: our math.</div>',
]
