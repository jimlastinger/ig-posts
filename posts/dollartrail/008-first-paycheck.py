import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "tools"))
from lib import *

ACCOUNT = 'dollartrail'
TRAIL = '008'
FOLLOWING = 'a $1,000 paycheck'
SOURCES = ['https://www.irs.gov/taxtopics/tc751', 'https://www.ssa.gov/oact/cola/cbb.html']

CAPTION = """On a $1,000 paycheck, $76.50 goes to Social Security and Medicare, and that's before income tax. Your employer quietly pays the same $76.50 again on top.

Data: IRS Topic No. 751 and Social Security Administration, 2026 tax rates and wage base.

Did your first paycheck surprise you?

#paycheck #firstjob #taxes #socialsecurity #personalfinance #dollartrail"""

SLIDES = [
    '<div class=tag>Trail No. 008</div>\n<div class=hook>Your $1,000 paycheck: <em>$76.50</em> is already gone.</div>\n<div class=hook2>That\'s just payroll tax. Income tax comes on top.</div>\n<div class=mini style="margin-top:60px">Source: IRS Tax Topic No. 751 and Social Security Administration, 2026 rates. Employee share, $1,000 of gross wages.</div>',
    stack([(6.2, R, "$62"), (1.45, Y, ""), (92.35, G, "$923.50")],
          [("Social Security", "$62.00", R), ("Medicare", "$14.50", Y), ("Everything else", "$923.50", G)],
          "Everything else = federal and state income tax, benefits and retirement (they depend on your W-4, state and plan), then you.",
          "Follow the<br>first $1,000", height=700),
    stop(1, 4, "Social Security", "$62.00", "6.2% OF YOUR WAGES",
         ["Every paycheck pays 6.2% into Social Security, the program that pays retirement, disability and survivor benefits."],
         "It stops at $184,500 of wages in 2026. Earn more than that and the rest of your year's pay is free of it.", R),
    stop(2, 4, "Medicare", "$14.50", "1.45% OF YOUR WAGES",
         ["Medicare's hospital insurance takes 1.45% of every dollar you earn."],
         "No cap here. Above $200,000 a year, your employer withholds an extra 0.9%.", Y),
    stop(3, 4, "Your employer's copy", "$76.50", "PAID ON TOP OF YOUR $1,000",
         ["Your employer owes the same 6.2% and 1.45% on your wages. It never shows up on your stub."],
         "Total Social Security and Medicare tax on this paycheck: $153.", BL),
    stop(4, 4, "The ceiling", "$11,439", "MOST AN EMPLOYEE PAYS IN SOCIAL SECURITY TAX, 2026",
         ["6.2% of the $184,500 wage base. Earn $50,000 or $5 million, nobody pays more than this."],
         "Medicare has no ceiling, so it keeps going on every dollar.", T),
    '<div class=tag>End of the trail</div>\n<div class=hook style="font-size:96px">7.65% leaves before income tax.<br><em>Your boss pays it again.</em></div>\n<div class=cta>Send this to someone<br>starting their <em>first job.</em></div>\n<div class=src>' + DT_FOLLOW + '<br><br>Source: IRS Tax Topic No. 751, Social Security and Medicare Withholding Rates; SSA, Contribution and Benefit Base, 2026 ($184,500). Employee rates: 6.2% Social Security, 1.45% Medicare.</div>',
]
