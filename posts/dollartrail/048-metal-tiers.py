import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "tools"))
from lib import *

ACCOUNT = 'dollartrail'
TRAIL = '048'
FOLLOWING = 'a Marketplace health plan'
SOURCES = ['https://www.healthcare.gov/choose-a-plan/plans-categories/',
           'https://healthcare.gov/health-insurance-marketplace/',
           'https://www.cms.gov/marketplace/outreach-and-education/key-dates-health-insurance-marketplace.pdf']

CAPTION = """Marketplace open enrollment starts November 1 (enroll by December 15 for coverage that starts January 1). HealthCare.gov estimates a Bronze plan pays about 60% of covered care costs and you pay 40%; Silver is 70/30, Gold 80/20 and Platinum 90/10.

Data: HealthCare.gov, Health plan categories; CMS, Key Dates. Dollar amounts on $10,000 of care: our math, estimates only.

Which metal are you on?

#healthinsurance #openenrollment #obamacare #personalfinance #money #dollartrail"""

SLIDES = [
    '<div class=tag>Trail No. 048</div>\n<div class=hook style="font-size:96px">$10,000 of care. On Bronze, <em>you pay about $4,000.</em></div>\n<div class=hook2>Open enrollment starts Nov. 1. Your metal decides the split.</div>\n<div class=mini style="margin-top:60px">Source: HealthCare.gov, Health plan categories (estimated share of costs for covered services) and Get answers page (Nov. 1 start). Dollar amounts: our math, estimates only; premiums not included.</div>',
    stack([(40, R, "YOU: ~40%"), (60, G, "BRONZE PLAN: ~60%")],
          [("You pay", "~40%", R), ("Bronze plan pays", "~60%", G)],
          "HealthCare.gov: &ldquo;estimates of the plan&rsquo;s share and your share of costs when you get covered services. The actual costs you pay vary by plan.&rdquo;",
          "Who pays a Bronze plan&rsquo;s bill", height=640),
    stop(1, 4, "Bronze", "~$4,000", "YOUR SHARE OF $10,000 IN COVERED CARE",
         ["Plan pays about <b>60%</b>, you pay about <b>40%</b>.", "Deductible is generally <b>high</b>."],
         "All Bronze plans work with Health Savings Accounts.", R),
    stop(2, 4, "Silver", "~$3,000", "YOUR SHARE OF $10,000 IN COVERED CARE",
         ["Plan pays about <b>70%</b>, you pay about <b>30%</b>.", "Deductible is generally <b>moderate</b>."],
         "With income-based extra savings, Silver pays 73-94% and you pay 6-27%. Only on Silver.", Y),
    stop(3, 4, "Gold", "~$2,000", "YOUR SHARE OF $10,000 IN COVERED CARE",
         ["Plan pays about <b>80%</b>, you pay about <b>20%</b>.", "Deductible is generally <b>low</b>."],
         "The metal names have nothing to do with the quality of care.", BL),
    stop(4, 4, "Platinum", "~$1,000", "YOUR SHARE OF $10,000 IN COVERED CARE",
         ["Plan pays about <b>90%</b>, you pay about <b>10%</b>.", "Deductible is generally <b>low</b>."],
         "These splits leave out your monthly premium (the monthly amount you pay for coverage).", P),
    '<div class=tag>Detour</div>\n<h2>Your share of $10,000 in care</h2>\n' + cmp([(4000, "$4,000", True), (3000, "$3,000", False), (2000, "$2,000", False), (1000, "$1,000", False)],
        ["Bronze", "Silver", "Gold", "Platinum"]) + '\n<div class=mini style="margin-top:24px">Our math from HealthCare.gov&rsquo;s estimated shares. Real costs vary by plan. Catastrophic plans are a 5th category for people under 30 or with a hardship or affordability exemption.</div>',
    '<div class=tag>End of the trail</div>\n<div class=hook style="font-size:80px">Open enrollment: Nov. 1.<br><em>Enroll by Dec. 15<br>for Jan. 1 coverage.</em></div>\n<div class=cta>Send this to the friend<br>who <em>buys their own insurance.</em></div>\n<div class=src>' + DT_FOLLOW + '<br><br>Source: HealthCare.gov, Health plan categories (healthcare.gov/choose-a-plan/plans-categories) and Get answers page; CMS, Key Dates. $10,000 example: our math.</div>',
]
