import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "tools"))
from lib import *

ACCOUNT = 'dollartrail'
TRAIL = '021'
FOLLOWING = '$5.4 trillion in revenue'
SOURCES = ['https://www.cbo.gov/publication/61985',
           'https://www.cbo.gov/system/files/2026-10/61985-MBR.pdf']

CAPTION = """The federal government took in an estimated $5.4 trillion in fiscal 2026, up 3%. Individual income and payroll taxes made up 86% of it, while corporate taxes and customs duties both fell.

Data: Congressional Budget Office, Monthly Budget Review: September 2026 (preliminary estimates). Fiscal year = Oct. 2025 to Sept. 2026.

Did you expect income taxes to be more than half?

#taxes #federalbudget #incometax #economy #moneyfacts #dollartrail"""

SLIDES = [
    '<div class=tag>Trail No. 021</div>\n<div class=hook style="font-size:110px">Washington took in <em>$5.4 trillion</em> in fiscal 2026.</div>\n<div class=hook2>86% came from individual income and payroll taxes.</div>\n<div class=mini style="margin-top:60px">Source: Congressional Budget Office, Monthly Budget Review: September 2026 (Oct. 8, 2026). Preliminary estimates; fiscal year Oct. 2025 to Sept. 2026. 86%: our math.</div>',
    stack([(53, BL, "53%"), (34, Y, "34%"), (7, P, ""), (3, W, ""), (3, R, "")],
          [("Individual income", "$2,844B", BL), ("Payroll taxes", "$1,815B", Y), ("Corporate taxes", "$382B", P), ("Other receipts", "$190B", W), ("Customs duties", "$172B", R)],
          "FY2026 receipts: $5,403B (CBO, preliminary). Shares: our math, rounded to add to 100.",
          "Where $5.4 trillion<br>came from", height=700),
    stop(1, 4, "Individual income taxes", "+$188B", "$2,656B IN FY2025 &rarr; $2,844B IN FY2026",
         ["Up <b>7%</b>, the biggest gain of any source."],
         "CBO: revenue growth was &ldquo;driven by larger collections of individual income and payroll taxes.&rdquo;", BL),
    stop(2, 4, "Payroll taxes", "+$67B", "$1,748B IN FY2025 &rarr; $1,815B IN FY2026",
         ["Up <b>4%</b>."],
         "Individual income and payroll taxes together: 86% of all federal revenue (our math).", Y),
    stop(3, 4, "Corporate income taxes", "&minus;$70B", "$452B IN FY2025 &rarr; $382B IN FY2026",
         ["Down <b>16%</b>."],
         "Now about 7 cents of each revenue dollar (our math).", P),
    stop(4, 4, "Customs duties", "&minus;11%", "$195B IN FY2025 &rarr; $172B IN FY2026",
         ["Customs duties include tariffs."],
         "About 3 cents of each revenue dollar (our math).", R),
    '<div class=tag>Detour</div>\n<h2>Revenue vs. spending</h2>\n<div class=taxrow>\n <div class=tx><div class=l>Took in</div><div class=n>$5,403B</div><div class=d>Total receipts, up 3%.</div></div>\n <div class=tx><div class=l>Spent</div><div class=n>$7,396B</div><div class=d>Total outlays.</div></div>\n</div>\n' + note("Revenue covered about 73% of spending (our math)."),
    '<div class=tag>End of the trail</div>\n<div class=hook style="font-size:84px">$5.4 trillion.<br><em>86% from individual income and payroll taxes.</em></div>\n<div class=cta>Send this to the friend<br>who just <em>checked their pay stub.</em></div>\n<div class=src>' + DT_FOLLOW + '<br><br>Source: Congressional Budget Office, &ldquo;Monthly Budget Review: September 2026&rdquo; (Oct. 8, 2026), preliminary FY2026 estimates. Shares, 86% and 73%: our math.</div>',
]
