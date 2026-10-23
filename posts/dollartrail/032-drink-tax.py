import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "tools"))
from lib import *

ACCOUNT = 'dollartrail'
TRAIL = '032'
THEME = 'ledger'
FOLLOWING = 'federal drink taxes'
SOURCES = ['https://www.ttb.gov/taxes/tax-audit/tax-and-fee-rates',
           'https://www.ttb.gov/regulated-commodities/beverage-alcohol/cbma/tax-reform-cbma',
           'https://www.ecfr.gov/current/title-27/chapter-I/subchapter-A/part-27',
           'https://www.bls.gov/news.release/cpi.t02.htm']

CAPTION = """Buy a bottle of wine, a six-pack and a 750 ml bottle of 80-proof spirits, and up to about $2.68 of federal excise tax rides along, by our math from TTB's general (top) rates. The spirits bottle carries $2.14 of it. Wine: 21 cents.

Data: TTB federal excise tax rates (ttb.gov), 27 CFR 27.11 definitions, BLS CPI September 2026. Per-bottle amounts our math.

Which of the three surprised you most?

#wine #beer #whiskey #taxes #personalfinance #dollartrail"""

SLIDES = [
    '<div class=tag>Trail No. 032</div>\n<div class=hook style="font-size:96px">Wine, a six-pack and a bottle of spirits: up to <em>$2.68</em> in federal excise tax.</div>\n<div class=hook2>Where it lands.</div>\n<div class=mini style="margin-top:60px">Source: TTB federal excise tax rates (general, top rates) at ttb.gov; units from 27 CFR 27.11. One 750 ml bottle of still wine (16% alcohol or less), one six-pack of 12 oz beers, one 750 ml bottle of 80-proof spirits. Our math. State and local taxes not included.</div>',
    stack([(80, R, "SPIRITS 80%"), (12, Y, "BEER 12%"), (8, BL, "WINE 8%")],
          [("80-proof spirits", "$2.14", R), ("Six-pack of beer", "33&cent;", Y), ("Bottle of wine", "21&cent;", BL)],
          "Federal excise tax at TTB&rsquo;s general (top) rates, per container. Shares of the $2.68: our math, rounded. Small producers can pay less (see stop 4).",
          "Where $2.68 lands", height=680),
    stop(1, 4, "The spirits bottle", "$2.14", "750 ML, 80 PROOF",
         ["Spirits are taxed at <b>$13.50 per proof gallon</b>: a gallon at 50% alcohol. A 750 ml bottle at 40% alcohol works out to about <b>$2.14</b> (our math)."],
         "About 10 times the wine tax (our math). That&rsquo;s the top rate: $13.34 or less applies to a distiller&rsquo;s first 22.23 million proof gallons.", R),
    stop(2, 4, "The six-pack", "33&cent;", "SIX 12 OZ CANS OR BOTTLES",
         ["Beer is taxed at <b>$18 per barrel</b>, and a barrel is <b>31 gallons</b>. That&rsquo;s about <b>5&cent;</b> a can (our math)."],
         "That&rsquo;s the top rate. Domestic brewers pay $16 on their first 6 million barrels, small ones less (stop 4).", Y),
    stop(3, 4, "The bottle of wine", "21&cent;", "750 ML, 16% ALCOHOL OR LESS",
         ["Still wine is taxed at <b>$1.07 per gallon</b>. Bubbly costs more: sparkling wine is <b>$3.40</b> a gallon, about <b>67&cent;</b> a bottle (our math)."],
         "Over 16% and up to 21% alcohol, the rate rises to $1.57 a gallon.", BL),
    stop(4, 4, "The small-producer break", "1&cent;", "PER CAN, SMALL BREWER (OUR MATH)",
         ["Small brewers: <b>$3.50</b> a barrel on their first 60,000 barrels. Small wineries: as low as <b>7&cent;</b> a gallon. Distillers: <b>$2.70</b> a proof gallon on their first 100,000."],
         "A December 2020 law made most of these breaks permanent.", P),
    '<div class=tag>Detour</div>\n<h2>Prices in the past year</h2>\n<div class=taxrow><div class=tx><div class=l>Beer at home</div><div class=n>+2.2%</div><div class=d>12 months</div></div><div class=tx><div class=l>Wine at home</div><div class=n>&minus;0.7%</div><div class=d>12 months</div></div></div>\n<div class=taxrow><div class=tx><div class=l>Spirits at home</div><div class=n>&minus;1.2%</div><div class=d>12 months</div></div><div class=tx><div class=l>All items</div><div class=n>+3.7%</div><div class=d>12 months</div></div></div>' + note("BLS CPI, Sept. 2025 to Sept. 2026, unadjusted. The federal tax is a set dollar amount, not a share of the price."),
    '<div class=tag>End of the trail</div>\n<div class=hook style="font-size:88px">Spirits: up to $2.14.<br><em>Wine: up to 21&cent;.</em></div>\n<div class=cta>Send this to whoever<br>is <em>buying this round.</em></div>\n<div class=src>' + DT_FOLLOW + '<br><br>Source: TTB tax and fee rates and CBMA tax reform pages (ttb.gov); 27 CFR 27.11 (barrel of 31 gallons, proof gallon, wine gallon); BLS CPI Table 2, September 2026. Per-container taxes and shares: our math. State and local taxes not included.</div>',
]
