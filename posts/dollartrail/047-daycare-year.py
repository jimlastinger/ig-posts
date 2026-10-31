import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "tools"))
from lib import *

ACCOUNT = 'dollartrail'
THEME = 'ledger'
TRAIL = '047'
FOLLOWING = 'a year of daycare'
SOURCES = ['https://www.dol.gov/newsroom/releases/wb/wb20241119',
           'https://www.DOL.gov/sites/dolgov/files/WB/NDCP/Fact-sheet-English-508-compliant.pdf']

CAPTION = """Full-day childcare for one child cost $6,552 to $15,600 a year in 2022, or 8.9% to 16% of median family income, according to the Labor Department's National Database of Childcare Prices (2,512 counties). The Women's Bureau director said the median cost of center-based infant care is more than the median cost of rent.

Data: U.S. Department of Labor, Women's Bureau, news release Nov. 19, 2024 and fact sheet Jan. 2023. Monthly figures: our math.

What does care cost where you live?

#childcare #daycare #parenting #familybudget #money #dollartrail"""

SLIDES = [
    '<div class=tag>Trail No. 047</div>\n<div class=hook style="font-size:100px">A year of daycare: <em>up to $15,600.</em></div>\n<div class=hook2>For one child. Full-day care. 2022 prices.</div>\n<div class=mini style="margin-top:60px">Source: U.S. Department of Labor (DOL), Women&rsquo;s Bureau, National Database of Childcare Prices. News release, Nov. 19, 2024 (2022 annual prices, 2,512 counties).</div>',
    stack([(16, R, "UP TO 16%: CHILDCARE"), (84, G, "EVERYTHING ELSE")],
          [("Childcare", "up to 16%", R), ("Everything else", "84%", G)],
          "DOL: families spend between 8.9% and 16% of their median income on full-day care for one child (2022). Shown: the high end. 84%: our math.",
          "A family&rsquo;s income, at the high end", height=640),
    stop(1, 4, "The low end", "$6,552", "A YEAR, ONE CHILD, FULL-DAY CARE (2022)",
         ["The bottom of the nationwide range of 2022 annual prices.", "That&rsquo;s about <b>$546 a month</b> (our math)."],
         "The range comes from 2,512 U.S. counties (DOL).", BL),
    stop(2, 4, "The high end", "$15,600", "A YEAR, ONE CHILD, FULL-DAY CARE (2022)",
         ["The top of the nationwide range.", "That&rsquo;s <b>$1,300 a month</b> (our math), for one child."],
         "29% of families with kids under 6 have two or more kids under 6 (DOL fact sheet).", R),
    stop(3, 4, "Share of income", "8.9-16%", "OF MEDIAN FAMILY INCOME, ONE CHILD",
         ["What families spend on one child&rsquo;s full-day care.", "The database covers <b>2,512 counties</b> in 48 states, D.C. and Puerto Rico."],
         "Prices in the database run from 2008 to 2022.", Y),
    stop(4, 4, "Infant care vs. rent", "&gt; Rent", "MEDIAN CENTER-BASED INFANT CARE VS. MEDIAN RENT",
         ["Women&rsquo;s Bureau Director Wendy Chun-Hoon: median center-based infant care costing more than median rent &ldquo;should be of urgent concern.&rdquo;"],
         "Quote from the DOL news release, Nov. 19, 2024.", P),
    '<div class=tag>Detour</div>\n<h2>Public spending per child</h2>\n' + cmp([(500, "&lt;$500", True), (2800, "$2,800", False), (12800, "$12,800", False)],
        ["Ages 0-2", "Ages 3-4", "Elementary"]) + '\n<div class=mini style="margin-top:24px">DOL fact sheet (Jan. 2023): federal, state and local spending on early care and education is less than $500 per child in the first three years of life.</div>',
    '<div class=tag>End of the trail</div>\n<div class=hook style="font-size:86px">$6,552 to $15,600 a year.<br><em>For one child.</em></div>\n<div class=cta>Send this to the friend<br>who <em>is touring daycares.</em></div>\n<div class=src>' + DT_FOLLOW + '<br><br>Source: U.S. Department of Labor, Women&rsquo;s Bureau, news release Nov. 19, 2024 (dol.gov/newsroom/releases/wb/wb20241119) and fact sheet Jan. 2023. Monthly figures: our math.</div>',
]
