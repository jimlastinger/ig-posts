import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "tools"))
from lib import *

ACCOUNT = 'dollartrail'
THEME = 'ledger'
TRAIL = '017'
FOLLOWING = 'interest on the debt'
SOURCES = ['https://www.cbo.gov/publication/61985',
           'https://www.cbo.gov/system/files/2026-10/61985-MBR.pdf']

CAPTION = """Net interest on the public debt hit an estimated $1.14 trillion in fiscal 2026, up $115 billion in a year. That's more than Medicare or defense, and about $3.1 billion a day.

Data: Congressional Budget Office, Monthly Budget Review: September 2026 (preliminary estimates). Fiscal year = Oct. 2025 to Sept. 2026.

Did you expect interest to outrank defense?

#nationaldebt #federalbudget #interest #taxes #economy #dollartrail"""

SLIDES = [
    '<div class=tag>Trail No. 017</div>\n<div class=hook style="font-size:110px">Interest on the debt: <em>$1.14 trillion</em> in fiscal 2026.</div>\n<div class=hook2>More than Medicare. More than defense.</div>\n<div class=mini style="margin-top:60px">Source: Congressional Budget Office, Monthly Budget Review: September 2026 (Oct. 8, 2026). Preliminary estimates; fiscal year Oct. 2025 to Sept. 2026. Net interest on the public debt.</div>',
    stack([(25.6, W, "ALL OTHER"), (22.4, BL, "SOCIAL SECURITY"), (15.5, R, "INTEREST"), (14.5, Y, "MEDICARE"), (12.4, P, "DEFENSE"), (9.8, T, "MEDICAID")],
          [("All other", "$1,891B", W), ("Social Security", "$1,654B", BL), ("Net interest", "$1,143B", R), ("Medicare", "$1,069B", Y), ("Defense", "$916B", P), ("Medicaid", "$723B", T)],
          "FY2026 outlays: $7,396B (CBO, preliminary). Defense = DoD-Military. &ldquo;All other&rdquo; and shares: our math.",
          "Where $7.4 trillion went", height=680),
    stop(1, 4, "The jump", "+$115B", "$1,028B IN FY2025 &rarr; $1,143B IN FY2026",
         ["Net interest rose <b>11%</b> in one year."],
         "That&rsquo;s about $3.1 billion a day (our math).", R),
    stop(2, 4, "Against revenue", "21%", "OF FEDERAL RECEIPTS (OUR MATH)",
         ["The government took in <b>$5,403B</b>. About 21 cents of each revenue dollar went to interest."],
         "Receipts rose $169B in FY2026. Interest alone rose $115B.", Y),
    '<div class="tag ghost" style="color:#b98cff;border-color:#b98cff">Stop 3 of 4</div>\n<h2>Against other programs</h2><div class=amt style="color:#b98cff;font-size:150px">No. 2</div><div class=pct>OF THESE FIVE OUTLAYS, AFTER SOCIAL SECURITY</div>\n<div class=taxrow>\n <div class=tx><div class=l>Net interest</div><div class=n>$1,143B</div><div class=d>Up 11%.</div></div>\n <div class=tx><div class=l>Medicare</div><div class=n>$1,069B</div><div class=d>Up 8%.</div></div>\n</div>\n' + note("Also more than defense ($916B). Only Social Security ($1,654B) was bigger."),
    stop(4, 4, "Against the deficit", "$2.0T", "FY2026 DEFICIT, UP $218B",
         ["Spending: <b>$7,396B</b>. Receipts: <b>$5,403B</b>."],
         "Interest alone equals about 57% of the deficit (our math).", BL),
    '<div class=tag>Detour</div>\n<h2>FY2026 outlays,<br>side by side</h2>\n' + cmp([(916, "$916B", False), (1069, "$1,069B", False), (1143, "$1,143B", True), (1654, "$1,654B", False)],
        ["Defense", "Medicare", "Interest", "Soc. Sec."]) + '\n<div class=mini style="margin-top:24px">CBO, Monthly Budget Review: September 2026. Preliminary FY2026 outlays, billions. Defense = DoD-Military.</div>',
    '<div class=tag>End of the trail</div>\n<div class=hook style="font-size:92px">$1.14 trillion.<br><em>About $3.1 billion a day.</em></div>\n<div class=cta>Send this to the friend<br>who follows the <em>federal budget.</em></div>\n<div class=src>' + DT_FOLLOW + '<br><br>Source: Congressional Budget Office, &ldquo;Monthly Budget Review: September 2026&rdquo; (Oct. 8, 2026), preliminary FY2026 estimates. Per-day figure, shares and &ldquo;All other&rdquo;: our math.</div>',
]
