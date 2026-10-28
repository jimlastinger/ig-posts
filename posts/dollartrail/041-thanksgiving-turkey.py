import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "tools"))
from lib import *

ACCOUNT = 'dollartrail'
TRAIL = '041'
THEME = 'ledger'
FOLLOWING = 'a Thanksgiving turkey'
SOURCES = ['https://www.ers.usda.gov/newsroom/trending-topics/turkey-sector-background-statistics']

CAPTION = """USDA projects wholesale frozen turkey hens will average $1.76 a pound in 2026, up from $1.36 in 2025 and 94 cents in 2024. For a 16-pound bird, that's about $28 at wholesale, before the store adds its share.

Data: USDA Economic Research Service, Turkey Sector: Background & Statistics (updated Oct. 21, 2026). Wholesale prices, not store prices. 16-lb bird and percent changes: our math.

What did you pay for your turkey last year?

#thanksgiving #turkey #groceries #foodprices #money #dollartrail"""

SLIDES = [
    '<div class=tag>Trail No. 041</div>\n<div class=hook style="font-size:96px">A 16-lb turkey: <em>$15</em> wholesale in 2024. About <em>$28</em> this year.</div>\n<div class=hook2>Following the bird to your table.</div>\n<div class=mini style="margin-top:60px">Source: USDA Economic Research Service (ERS), Turkey Sector: Background &amp; Statistics, updated Oct. 21, 2026. Frozen whole hens, annual average wholesale price; 2026 is a USDA projection. 16-lb values: our math.</div>',
    stack([(17, R, "MINN. 17%"), (15, Y, "N.C. 15%"), (11, BL, "ARK. 11%"), (10, P, "IND. 10%"), (25, T, "VA, MO, IA, PA 25%"), (22, G, "ALL OTHERS 22%")],
          [("Minnesota", "33.5M", R), ("North Carolina", "28.0M", Y), ("Arkansas", "21.5M", BL), ("Indiana", "20.0M", P), ("Next 4 states", "48.4M", T), ("All others", "42.1M", G)],
          "Turkeys raised, 2025 (USDA ERS). Shares and group totals: our math.",
          "193.5 million turkeys, 2025", height=680),
    stop(1, 4, "The farm", "4.84B lb", "TURKEY MEAT PRODUCED, 2025",
         ["The lowest in USDA&rsquo;s table back to 2020, when it was <b>5.74 billion</b> pounds.", "Output is coming back: the first half of 2026 was up <b>7.4%</b> from a year earlier."],
         "USDA projects 5.13 billion pounds for all of 2026.", R),
    stop(2, 4, "The wholesale price", "$1.76", "PER POUND, 2026 PROJECTED",
         ["Frozen whole hens averaged <b>$1.36</b> in 2025 and <b>94&cent;</b> in 2024.", "That&rsquo;s up about <b>29%</b> in one year (our math)."],
         "USDA notes wholesale prices are lower than what shoppers pay at the store.", Y),
    '<div class="tag ghost">Stop 3 of 4</div>\n<h2>A 16-lb bird at wholesale</h2>\n' + cmp([(15.04, "$15.04", False), (21.76, "$21.76", False), (28.16, "$28.16", True)],
        ["2024", "2025", "2026*"]) + '\n<div class=mini style="margin-top:24px">Annual average wholesale price of frozen whole hens &times; 16 pounds (our math from USDA ERS). *2026 is a USDA projection. Not a store price.</div>',
    stop(4, 4, "The table", "13.2 lb", "TURKEY PER PERSON, 2025",
         ["Down from <b>15.7 pounds</b> in 2020.", "Americans used <b>4.51 billion</b> pounds in 2025. Another <b>420 million</b> pounds were exported."],
         "USDA projects 13.6 pounds per person in 2026.", BL),
    '<div class=tag>Detour</div>\n<h2>The whole flock</h2>\n<div class=taxrow><div class=tx><div class=l>Value of production, 2024</div><div class=n>$3.69B</div><div class=d>Low prices</div></div><div class=tx><div class=l>Value of production, 2025</div><div class=n>$5.58B</div><div class=d>Less meat, higher prices</div></div></div>\n' + note("USDA projects turkey exports will rise to 461 million pounds in 2026."),
    '<div class=tag>End of the trail</div>\n<div class=hook style="font-size:86px">Same 16-lb bird.<br><em>About $13 more at wholesale than in 2024.</em></div>\n<div class=cta>Send this to whoever<br>is <em>hosting this year.</em></div>\n<div class=src>' + DT_FOLLOW + '<br><br>Source: USDA Economic Research Service, Turkey Sector: Background &amp; Statistics (updated Oct. 21, 2026). Frozen whole hens, annual average wholesale prices; 2026 projected. 16-lb values, percent changes and shares: our math.</div>',
]
