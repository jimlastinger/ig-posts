import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "tools"))
from lib import *

ACCOUNT = 'dollartrail'
THEME = 'ledger'
TRAIL = '029'
FOLLOWING = 'a month of Medicare premiums'
SOURCES = ['https://www.cms.gov/newsroom/press-releases/medicare-advantage-medicare-prescription-drug-programs-expected-remain-stable-2027',
           'https://www.cms.gov/files/document/july-28-2026-parts-c-d-announcement.pdf',
           'https://www.cms.gov/newsroom/fact-sheets/2026-medicare-parts-b-premiums-deductibles']

CAPTION = """Medicare open enrollment runs Oct. 15 to Dec. 7. The standard Part B premium is $202.90 a month in 2026, and stand-alone drug plans average $36 a month for 2027, per CMS. Medicare Advantage premiums average $12.00 in 2027, down from $14.37 in 2026.

Data: Centers for Medicare & Medicaid Services (Sept. 28, 2026 release; 2026 Part B fact sheet; Part D bid information release, July 28, 2026). Some figures our math.

Are you switching plans this year, or staying put?

#medicare #openenrollment #retirement #healthinsurance #personalfinance #dollartrail"""

SLIDES = [
    '<div class=tag>Trail No. 029</div>\n<div class=hook style="font-size:104px">Medicare Part B in 2026: <em>$202.90</em> a month.</div>\n<div class=hook2>What a month of Medicare premiums costs. Open enrollment for 2027 runs to Dec. 7.</div>\n<div class=mini style="margin-top:60px">Source: Centers for Medicare &amp; Medicaid Services (CMS), 2026 Medicare Parts A &amp; B Premiums and Deductibles; Sept. 28, 2026 Medicare Advantage and Part D release.</div>',
    stack([(85, R, "PART B 85%"), (15, BL, "PART D 15%")],
          [("Part B (standard)", "$202.90", R), ("Avg. Part D plan", "$35.09", BL), ("Monthly total", "$237.99", W)],
          "2026 monthly premiums: standard Part B plus the average stand-alone Part D drug plan. Total and shares our math. Plans vary; higher incomes pay more for Part B.",
          "Original Medicare + a drug plan, per month, 2026", height=680),
    stop(1, 4, "Part B", "$202.90", "STANDARD MONTHLY PREMIUM, 2026",
         ["Up <b>$17.90</b> from $185.00 in 2025. That&rsquo;s <b>$2,434.80</b> a year (our math), before the <b>$283</b> annual deductible."],
         "CMS hasn&rsquo;t announced the 2027 Part B premium yet.", R),
    stop(2, 4, "Higher incomes", "$689.90", "TOP 2026 PART B PREMIUM, PER MONTH",
         ["Extra charges start above <b>$109,000</b> of income for individuals and <b>$218,000</b> for joint filers. The first step up is <b>$284.10</b> a month."],
         "CMS says these income-related amounts affect roughly 8% of people with Part B.", Y),
    stop(3, 4, "Drug plan (Part D)", "$36", "AVERAGE STAND-ALONE PLAN, PER MONTH, 2027",
         ["Up from <b>$35.09</b> in 2026, an increase of less than $1. CMS&rsquo;s Part D base beneficiary premium rises to <b>$41.33</b> from $38.99 (6%, our math)."],
         "That&rsquo;s an average across plans. Your plan&rsquo;s premium can be higher or lower.", BL),
    stop(4, 4, "Medicare Advantage", "$12.00", "AVERAGE MONTHLY PREMIUM, 2027",
         ["Down <b>16.5%</b> from $14.37 in 2026. CMS projects <b>34 million</b> people in these plans in 2027, about 47.4% of everyone on Medicare."],
         "In Advantage plans with drug coverage, the average drug premium falls to $7 from $11.32.", P),
    '<div class=tag>Detour</div>\n<h2>Average monthly premiums, 2026 vs. 2027</h2>\n' + cmp([(14.37, "$14.37", False), (12.00, "$12.00", True), (35.09, "$35.09", False), (36.00, "$36", True)],
        ["Advantage 2026", "Advantage 2027", "Part D 2026", "Part D 2027"]) + '\n<div class=mini style="margin-top:24px">CMS, Sept. 28, 2026. Medicare Advantage: weighted average of all plans. Part D: stand-alone drug plans.</div>',
    '<div class=tag>End of the trail</div>\n<div class=hook style="font-size:88px">Open enrollment ends <em>Dec. 7.</em></div>\n<p style="font-size:40px">CMS says about 8 in 10 Medicare Advantage members can stay in their current plan in 2027.</p>\n<div class=cta>Send this to someone<br>who&rsquo;s <em>on Medicare.</em></div>\n<div class=src>' + DT_FOLLOW + '<br><br>Source: CMS, &ldquo;Medicare Advantage and Medicare Prescription Drug Programs Expected to Remain Stable in 2027&rdquo; (Sept. 28, 2026); 2026 Medicare Parts A &amp; B Premiums and Deductibles (Nov. 14, 2025); Annual Release of Part D National Average Monthly Bid Amount and Other Part C &amp; D Bid Information (July 28, 2026). Totals and annual figures: our math.</div>',
]
