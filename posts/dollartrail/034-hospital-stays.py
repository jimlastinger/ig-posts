import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "tools"))
from lib import *

ACCOUNT = 'dollartrail'
TRAIL = '034'
THEME = 'receipt'
FOLLOWING = 'a year of hospital stays'
SOURCES = ['https://hcup-us.ahrq.gov/reports/statbriefs/sb316-most-expensive-conditions-by-payer-2022.pdf']

CAPTION = """U.S. nonfederal acute care hospitals spent $548.5 billion to provide 32.9 million inpatient stays in 2022, about $16,700 a stay by our math. Medicare was the expected payer for 46.7% of those costs; private insurance, 25.8%.

Data: AHRQ Healthcare Cost and Utilization Project, Statistical Brief #316 (Feb. 2026), 2022 National Inpatient Sample. Hospital costs, not charges or payments. Per-stay figures our math.

Did any of these numbers surprise you?

#healthcare #hospital #medicare #healthinsurance #personalfinance #dollartrail"""

SLIDES = [
    '<div class=tag>Trail No. 034</div>\n<div class=hook style="font-size:100px">One year of U.S. hospital stays: <em>$548.5 billion.</em></div>\n<div class=hook2>Who was expected to pay.</div>\n<div class=mini style="margin-top:60px">Source: AHRQ Healthcare Cost and Utilization Project (HCUP), Statistical Brief #316, Feb. 2026: 2022 National Inpatient Sample, nonfederal acute care hospitals. Hospital costs to provide care, not charges or what payers paid.</div>',
    stack([(47, R, "MEDICARE 47%"), (26, Y, "PRIVATE 26%"), (21, BL, "MEDICAID 21%"), (3, P, ""), (3, W, "")],
          [("Medicare", "46.7%", R), ("Private insurance", "25.8%", Y), ("Medicaid", "20.6%", BL), ("Self-pay/no charge", "3.3%", P), ("Other/missing", "3.6%", W)],
          "Share of 2022 inpatient hospital costs by expected payer. Other/missing: our math (100% minus the four named payers). Bar rounded.",
          "Where $548.5B lands", height=640),
    stop(1, 4, "Medicare", "$256.4B", "13.2 MILLION STAYS",
         ["About <b>$19,400 per stay</b> (our math), the highest of the four named payers."],
         "Medicare was the expected payer for 46.7% of all hospital costs.", R),
    stop(2, 4, "Private insurance", "$141.6B", "9.4 MILLION STAYS",
         ["About <b>$15,000 per stay</b> (our math)."],
         "25.8% of hospital costs.", Y),
    stop(3, 4, "Medicaid", "$112.9B", "7.8 MILLION STAYS",
         ["About <b>$14,600 per stay</b> (our math)."],
         "20.6% of hospital costs.", BL),
    stop(4, 4, "Self-pay / no charge", "$18.0B", "1.4 MILLION STAYS",
         ["About <b>$13,100 per stay</b> (our math). The group includes self-pay, no charge, charity and no expected payment."],
         "3.3% of hospital costs.", P),
    '<div class=tag>Detour</div>\n<h2>The most expensive conditions</h2>\n' + cmp([(60.0, "$60.0B", True), (19.6, "$19.6B", False), (18.2, "$18.2B", False)],
        ["Septicemia", "Newborns", "Heart failure"]) + '\n<div class=mini style="margin-top:24px">2022 aggregate hospital costs, all payers. Septicemia alone was 10.9% of the total.</div>',
    '<div class=tag>End of the trail</div>\n<div class=hook style="font-size:88px">32.9 million stays.<br><em>About $16,700 each.</em></div>\n<div class=cta>Send this to someone<br>who <em>works in health care.</em></div>\n<div class=src>' + DT_FOLLOW + '<br><br>Source: AHRQ HCUP Statistical Brief #316, &ldquo;National Inpatient Hospital Costs: The Most Expensive Conditions by Payer, 2022&rdquo; (Feb. 2026), hcup-us.ahrq.gov. Hospital costs, not charges or payments; excludes separately billed physician fees. Per-stay figures and other/missing share: our math.</div>',
]
