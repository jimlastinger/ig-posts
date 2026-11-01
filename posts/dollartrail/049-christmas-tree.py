import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "tools"))
from lib import *

ACCOUNT = 'dollartrail'
THEME = 'receipt'
TRAIL = '049'
FOLLOWING = 'a real Christmas tree'
SOURCES = ['https://www.ers.usda.gov/data-products/charts-of-note/110530']

CAPTION = """U.S. tree farms cut more than 14.5 million Christmas trees in 2022 and sold $553 million worth, up from $377 million in 2017. That works out to about $38 a tree or less in grower sales (our math).

Data: USDA Economic Research Service, Chart of Note (Dec. 4, 2024), from the USDA NASS 2022 Census of Agriculture. Per-tree and percent figures: our math.

Real tree or artificial at your place?

#christmastree #christmas #holidays #farming #money #dollartrail"""

SLIDES = [
    '<div class=tag>Trail No. 049</div>\n<div class=hook style="font-size:100px">A year of real Christmas trees: <em>$553 million.</em></div>\n<div class=hook2>What U.S. tree farms sold in 2022. About $38 a tree or less (our math).</div>\n<div class=mini style="margin-top:60px">Source: USDA Economic Research Service (ERS), Chart of Note, Dec. 4, 2024, from the USDA NASS 2022 Census of Agriculture.</div>',
    stack([(50, R, "MORE THAN HALF: OR + NC"), (50, G, "THE OTHER 48 STATES")],
          [("OR + NC", "over 50%", R), ("Other 48", "under 50%", G)],
          "ERS: more than half the trees cut in 2022 were grown in Oregon and North Carolina. Exact shares not published; bar shows the 50% line.",
          "Where 2022&rsquo;s trees were cut", height=640),
    stop(1, 4, "The farms", "~16,000", "U.S. CHRISTMAS TREE FARMS (ERS: ABOUT 16,000)",
         ["Christmas trees are grown commercially in <b>all 50 states</b>.", "Also notable: Michigan, Washington, Pennsylvania, Wisconsin and Virginia."],
         "Popular species: Noble, Douglas and Fraser firs (ERS).", BL),
    stop(2, 4, "The harvest", "14.5M+", "TREES CUT IN THE U.S., 2022",
         ["About <b>550,000 fewer</b> than in the 2017 census.", "ERS points to prolonged drought in many growing regions."],
         "That puts 2017&rsquo;s harvest at about 15 million trees (our math).", Y),
    stop(3, 4, "The sales", "$553M", "CUT CHRISTMAS TREES SOLD BY U.S. GROWERS, 2022",
         ["Up from <b>$377 million</b> in 2017, about 47% more (our math).", "Fewer trees, higher value of sales."],
         "$553M divided by 14.5M trees is about $38 a tree; more than 14.5M were cut, so it&rsquo;s a ceiling (our math).", R),
    stop(4, 4, "The imports", "3M+", "CHRISTMAS TREES IMPORTED, 2022",
         ["On top of the trees cut at home, the U.S. imported <b>more than 3 million</b>."],
         "ERS doesn&rsquo;t list the import value on this page, so we don&rsquo;t either.", P),
    '<div class=tag>Detour</div>\n<h2>Grower sales, cut trees</h2>\n' + cmp([(377, "$377M", False), (553, "$553M", True)],
        ["2017", "2022"]) + '\n<div class=mini style="margin-top:24px">USDA ERS, from the NASS Census of Agriculture (2017 and 2022). Dollar figures as reported.</div>',
    '<div class=tag>End of the trail</div>\n<div class=hook style="font-size:86px">$553 million in trees.<br><em>About $38 or less a tree.</em></div>\n<div class=cta>Send this to the friend<br>who <em>already has the tree up.</em></div>\n<div class=src>' + DT_FOLLOW + '<br><br>Source: USDA Economic Research Service, Chart of Note &ldquo;2022 Census of Agriculture: U.S. tree farms cut more than 14.5 million Christmas trees in 2022&rdquo; (ers.usda.gov/data-products/charts-of-note/110530), Dec. 4, 2024. Per-tree and percent figures: our math.</div>',
]
