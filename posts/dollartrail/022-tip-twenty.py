import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "tools"))
from lib import *

ACCOUNT = 'dollartrail'
THEME = 'receipt'
TRAIL = '022'
FOLLOWING = 'your 20% tip'
SOURCES = ['https://www.dol.gov/agencies/whd/fact-sheets/15-tipped-employees-flsa',
           'https://www.dol.gov/agencies/whd/state/minimum-wage/tipped',
           'https://www.dol.gov/agencies/whd/flsa/tips',
           'https://www.irs.gov/newsroom/what-the-no-tax-on-tips-deduction-means-for-you',
           'https://www.irs.gov/newsroom/one-big-beautiful-bill-act-tax-deductions-for-working-americans-and-seniors',
           'https://www.irs.gov/publications/p15',
           'https://www.irs.gov/taxtopics/tc761']

CAPTION = """Illustrative: on a $20 card tip, if the employer passes on the card fee (DOL's own 3% example: $0.60) and Social Security and Medicare take the 7.65% employee share, your server keeps about $17.92 before income tax. Beyond the card fee, federal law bars the employer and managers from keeping any of the tip.

Data: U.S. Department of Labor (Fact Sheet #15; state tipped minimum wage table, rev. July 1, 2026), IRS (Publication 15 for 2026; no tax on tips deduction). Breakdown: our math.

Did you know the card fee could come out of the tip?

#tipping #restaurants #servers #minimumwage #taxes #dollartrail"""

SLIDES = [
    '<div class=tag>Trail No. 022</div>\n<div class=hook style="font-size:104px">You tip $20 on a card. Your server keeps about <em>$17.92.</em></div>\n<div class=hook2>Illustrative: a $20 tip on a $100 bill, before income tax.</div>\n<div class=mini style="margin-top:60px">Source: U.S. Department of Labor, Fact Sheet #15 and state tipped minimum wage table (rev. July 1, 2026); IRS Publication 15 (2026). Breakdown: our math.</div>',
    stack([(3.0, R, ""), (7.4, Y, "PAYROLL TAX"), (89.6, G, "SERVER KEEPS $17.92")],
          [("Card fee", "$0.60", R), ("Payroll tax", "$1.48", Y), ("Server keeps", "$17.92", G)],
          "Illustrative $20 card tip. Card fee uses DOL&rsquo;s own 3% example, not an average fee. Payroll tax = 7.65% employee share on $19.40. Before income tax. Our math.",
          "Follow $20", height=680),
    stop(1, 5, "The card fee", "$0.60", "3% OF $20 (OUR MATH), DOL&rsquo;S EXAMPLE FEE",
         ["If the card company charges the restaurant 3%, the employer may pay the server 97% of the tip."],
         "Never more than the actual fee. Some states may have more protective laws.", R),
    stop(2, 5, "Payroll tax", "$1.48", "7.65% OF $19.40, EMPLOYEE SHARE (OUR MATH)",
         ["Social Security (6.2%) plus Medicare (1.45%). The IRS says tips are still generally subject to both."],
         "The new &ldquo;no tax on tips&rdquo; deduction doesn&rsquo;t remove these.", Y),
    stop(3, 5, "No tax on tips", "$25,000", "MAX DEDUCTION A YEAR, 2025 TO 2028",
         ["Eligible workers can deduct qualified tips from federal income. It phases out above $150,000 of modified AGI ($300,000 joint)."],
         "Mandatory service charges on the bill aren&rsquo;t qualified tips.", BL),
    stop(4, 5, "The tip credit", "$5.12", "AN HOUR: THE FEDERAL MAX TIP CREDIT",
         ["Under federal law, the boss can pay just <b>$2.13</b> an hour in cash. Tips can count toward the rest of the <b>$7.25</b> minimum wage."],
         "$2.13 + $5.12 = $7.25 (our math).", P),
    stop(5, 5, "The tip pool", "$0", "WHAT THE BOSS AND MANAGERS CAN TAKE FROM STAFF TIPS",
         ["Tips can be pooled with other tipped staff, or with cooks and dishwashers if the employer pays at least $7.25 an hour in cash wages."],
         "DOL: employers can&rsquo;t keep &ldquo;any portion of employees&rsquo; tips for any purpose.&rdquo;", T),
    '<div class=tag>Detour</div>\n<h2>Minimum cash wage before tips</h2>\n' + cmp([(2.13, "$2.13", True), (14.00, "$14.00", False), (16.90, "$16.90", False), (17.13, "$17.13", False)],
        ["Federal", "Alaska", "California", "Washington"]) + '\n<div class=mini style="margin-top:24px">DOL state table, rev. July 1, 2026. Our count: 7 states plus Guam require the full state minimum wage before tips; 15 states plus 3 territories set the minimum at the federal $2.13.</div>',
    '<div class=tag>End of the trail</div>\n<div class=hook style="font-size:92px">A $20 tip on a card.<br><em>About $17.92 reaches your server, before income tax.</em></div>\n<div class=cta>Send this to someone<br>who <em>tips on the card.</em></div>\n<div class=src>' + DT_FOLLOW + '<br><br>Source: U.S. Department of Labor, Fact Sheet #15 (as of Oct 2026), state tipped minimum wage table (rev. July 1, 2026), FLSA tips page; IRS Publication 15 (2026), Topic 761, no tax on tips guidance. Illustrative breakdown: our math.</div>',
]
