import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "tools"))
from lib import *

ACCOUNT = 'dollartrail'
TRAIL = '011'
FOLLOWING = '$195 billion in tariffs'
SOURCES = ['https://www.cbo.gov/publication/61307',
           'https://www.cbo.gov/system/files/2025-11/61307-MBR-FY25-final.pdf']

CAPTION = """Customs duties brought in $195 billion in fiscal 2025, up from $77 billion the year before. That's still about 4 cents of every federal tax dollar.

Data: Congressional Budget Office, Monthly Budget Review: Summary for Fiscal Year 2025 (Nov. 2025). Fiscal year = Oct. 2024 to Sept. 2025.

Did you think tariffs raised more or less than this?

#tariffs #taxes #federalbudget #economy #moneyfacts #dollartrail"""

SLIDES = [
    '<div class=tag>Trail No. 011</div>\n<div class=hook style="font-size:118px">Tariffs raised <em>$195 billion</em> in fiscal 2025.</div>\n<div class=hook2>How big is that, really?</div>\n<div class=mini style="margin-top:60px">Source: Congressional Budget Office, Monthly Budget Review: Summary for Fiscal Year 2025 (Oct. 2024 to Sept. 2025). Customs duties, including tariffs.</div>',
    stack([(51, BL, "51&cent;"), (33, Y, "33&cent;"), (9, P, "9&cent;"), (4, R, ""), (3, W, "")],
          [("Individual income", "51&cent;", BL), ("Payroll taxes", "33&cent;", Y), ("Corporate taxes", "9&cent;", P), ("Tariffs", "4&cent;", R), ("Everything else", "3&cent;", W)],
          "Per $1 of FY2025 federal revenue ($5,235 billion). Rounded to whole cents; adds to $1.",
          "One tax dollar.<br>Where it came from.", height=700),
    stop(1, 4, "The jump", "+153%", "$77B IN FY2024 &rarr; $195B IN FY2025",
         ["Customs receipts rose by $118 billion in one year."],
         "CBO: the increase is the result of larger tariffs imposed since February on most imported goods.", R),
    stop(2, 4, "Against the economy", "0.6%", "OF GDP IN FY2025",
         ["Up from 0.3% of GDP in 2024. The 50-year average is 0.2%."],
         "Three times the long-run norm, by CBO's count.", Y),
    '<div class="tag ghost" style="color:#b98cff;border-color:#b98cff">Stop 3 of 4</div>\n<h2>Against other taxes</h2><div class=amt style="color:#b98cff">43%</div><div class=pct>TARIFFS AS A SHARE OF CORPORATE TAX</div>\n<div class=taxrow>\n <div class=tx><div class=l>Corporate taxes</div><div class=n>$452B</div><div class=d>Fell in FY2025, per CBO.</div></div>\n <div class=tx><div class=l>Tariffs</div><div class=n>$195B</div><div class=d>Customs duties, including tariffs.</div></div>\n</div>\n' + note("For every $1 corporations paid in income tax, tariffs brought in about 43 cents."),
    stop(4, 4, "Against the deficit", "$1.8T", "FY2025 FEDERAL DEFICIT",
         ["The government spent $7.0 trillion and took in $5.2 trillion, tariffs included."],
         "Tariff money rose $118 billion, but spending rose $275 billion. The deficit shrank just $41 billion.", BL),
    '<div class=tag>Detour</div>\n<h2>Customs duties,<br>three years</h2>\n' + cmp([(80, "$80B", False), (77, "$77B", False), (195, "$195B", True)],
        ["FY2023", "FY2024", "FY2025"]) + '\n<div class=mini style="margin-top:24px">CBO, Monthly Budget Review, Table 2. Billions of dollars, fiscal years.</div>',
    '<div class=tag>End of the trail</div>\n<div class=hook style="font-size:92px">$195 billion.<br><em>About 4&cent; of every tax dollar.</em></div>\n<div class=cta>Send this to the friend<br>who argues about <em>tariffs.</em></div>\n<div class=src>' + DT_FOLLOW + '<br><br>Source: Congressional Budget Office, &ldquo;Monthly Budget Review: Summary for Fiscal Year 2025&rdquo; (Nov. 10, 2025). Customs duties include tariffs. Shares rounded.</div>',
]
