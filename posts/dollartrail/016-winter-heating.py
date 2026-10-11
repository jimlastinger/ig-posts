import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "tools"))
from lib import *

ACCOUNT = 'dollartrail'
THEME = 'receipt'
TRAIL = '016'
FOLLOWING = 'your winter heating bill'
SOURCES = ['https://www.eia.gov/outlooks/steo/report/perspectives/2026/10-winterfuels/article.php',
           'https://www.eia.gov/todayinenergy/detail.php?id=68264']

CAPTION = """EIA expects the average home that heats with oil to spend $2,115 this winter, up 21%, while homes on natural gas spend about $640, down 9%. Electricity and propane land in between.

Data: U.S. Energy Information Administration, Short-Term Energy Outlook (Oct. 2026), forecast for Nov. 2026 to Mar. 2027.

How do you heat your home?

#heating #energybills #winter #naturalgas #utilities #dollartrail"""

SLIDES = [
    '<div class=tag>Trail No. 016</div>\n<div class=hook style="font-size:104px">Heating with oil this winter: <em>$2,115.</em> With natural gas: $640.</div>\n<div class=hook2>Same winter. Very different bills.</div>\n<div class=mini style="margin-top:60px">Source: U.S. Energy Information Administration, Short-Term Energy Outlook (Oct. 6, 2026). Forecast average household spending, U.S., Nov. 2026 to Mar. 2027.</div>',
    stack([(46, BL, "NATURAL GAS 46%"), (3, R, ""), (51, W, "ALL OTHER ~51%")],
          [("Natural gas", "46%", BL), ("Heating oil", "~3%", R), ("All other", "~51%", W)],
          "Primary heating fuel. Natural gas: 2024 American Community Survey, via EIA. Heating oil: about 3% (EIA). All other, our math: includes electricity and propane.",
          "How U.S. homes heat", height=680),
    stop(1, 4, "Heating oil", "$2,115", "FORECAST, UP 21% FROM LAST WINTER",
         ["The priciest way to heat, and the fastest-rising. About <b>3%</b> of U.S. households use it."],
         "EIA: higher heating oil prices push this winter&rsquo;s spending up.", R),
    stop(2, 4, "Propane", "$1,246", "FORECAST, DOWN 3% FROM LAST WINTER",
         ["Lower propane prices pull this bill down, EIA says."],
         "Propane and natural gas together heat about half of U.S. households.", Y),
    stop(3, 4, "Electricity", "$1,196", "FORECAST, UP 4% FROM LAST WINTER",
         ["Higher electricity prices push this bill up, EIA says."],
         "Now within $50 of the propane bill: $1,196 vs. $1,246.", P),
    stop(4, 4, "Natural gas", "$640", "FORECAST, DOWN 9% FROM LAST WINTER",
         ["The most common heating fuel: <b>46%</b> of U.S. homes in 2024. Lower prices cut this winter&rsquo;s bill."],
         "About 30% of what a heating-oil home is expected to spend (our math).", BL),
    '<div class=tag>Detour</div>\n<h2>Four winter bills</h2>\n' + cmp([(640, "$640", False), (1196, "$1,196", False), (1246, "$1,246", False), (2115, "$2,115", True)],
        ["Gas", "Electric", "Propane", "Oil"]) + '\n<div class=mini style="margin-top:24px">EIA forecast, average household spending, Nov. 2026 to Mar. 2027, U.S. average.</div>',
    '<div class=tag>End of the trail</div>\n<div class=hook style="font-size:92px">Same winter.<br><em>Oil homes expected to spend 3.3x gas homes.</em></div>\n<div class=cta>Send this to someone<br>who heats with <em>oil.</em></div>\n<div class=src>' + DT_FOLLOW + '<br><br>Source: U.S. Energy Information Administration, Short-Term Energy Outlook, winter fuels (Oct. 6, 2026) and Today in Energy (Oct. 7, 2026). Forecasts. 3.3x = $2,115 / $640, our math.</div>',
]
