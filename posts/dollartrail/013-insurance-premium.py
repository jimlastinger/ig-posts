import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "tools"))
from lib import *

ACCOUNT = 'dollartrail'
THEME = 'receipt'
TRAIL = '013'
FOLLOWING = '$1 of health premium'
SOURCES = ['https://www.cms.gov/marketplace/private-health-insurance/medical-loss-ratio',
           'https://www.healthcare.gov/glossary/medical-loss-ratio-mlr/',
           'https://www.cms.gov/marketplace/resources/data/medical-loss-ratio-data-systems-resources',
           'https://www.cms.gov/files/document/2024-rebates-state.pdf']

DR, DB, DP, DG = "#d8352a", "#2f6fd6", "#7a4fd0", "#1f8a5f"

CAPTION = """Under the Affordable Care Act, insurers have to spend at least 80 cents of each premium dollar (85 in the large group market) on medical care and quality improvement. Insurers that fell short owed $1.64 billion in rebates for 2024.

Data: CMS, Medical Loss Ratio rules and 2024 MLR Rebates by State; HealthCare.gov glossary.

Did you ever get an MLR rebate check from your insurer?

#healthinsurance #affordablecareact #personalfinance #healthcare #money #dollartrail"""

SLIDES = [
    '<div class=tag>Trail No. 013</div>\n<div class=hook style="font-size:100px">Out of every $1 of premium, <em>at least 80&cent;</em> must go to your care.</div>\n<div class=hook2>It&rsquo;s the law. Here&rsquo;s where the rest goes.</div>\n<div class=mini style="margin-top:40px">Source: CMS, Medical Loss Ratio rules and 2024 MLR Rebates by State; HealthCare.gov.</div>',
    stack([(80, DG, "80&cent; CARE"), (20, DR, "20&cent;")],
          [("Claims + quality", "80&cent;", DG), ("Overhead + profit", "20&cent;", DR)],
          "The minimum split of $1 under the 80% rule. In the large group market the floor is 85%, leaving 15&cent;.",
          "Your $1 of premium,<br>at minimum"),
    stop(1, 4, "The floor", "80%", "MINIMUM OF PREMIUM SPENT ON CARE",
         ["The Affordable Care Act requires insurers to spend at least 80% or 85% of premium dollars on medical care."],
         "The 85% floor applies in the large group market.", DG),
    stop(2, 4, "What counts as care", "Claims", "PLUS QUALITY IMPROVEMENT",
         ["Paying customers&rsquo; medical claims, and activities that improve the quality of care."],
         "Marketing, salaries, admin costs, agent commissions and profits all come out of the other 20&cent;.", DB),
    stop(3, 4, "Miss it, pay it back", "$1.64B", "REBATES OWED FOR 2024",
         ["Since 2012, an insurer that misses the floor has to send its customers a rebate. For 2024: <b>$1,640,091,858</b>."],
         "8.56 million consumers benefited. That&rsquo;s about $190 each on average (our math).", DR),
    '<div class="tag ghost" style="color:#7a4fd0;border-color:#7a4fd0">Stop 4 of 4</div>\n<h2>Where the rebates went</h2>\n'
    + cmp([(1180, "$1.18B", True), (274, "$274M", False), (186, "$186M", False)], ["Individual", "Small group", "Large group"])
    + note("Individual plans got 72% of the 2024 rebate dollars, spread across 5.06 million people."),
    '<div class=tag>Detour</div>\n<h2>Biggest 2024 rebates,<br>by state</h2>\n'
    + cmp([(182, "$182M", True), (156, "$156M", False), (138, "$138M", False), (130, "$130M", False), (127, "$127M", False)],
          ["AL", "MO", "SC", "LA", "TX"])
    + note("All markets combined. Alabama alone was owed more than Texas."),
    '<div class=tag>End of the trail</div>\n<div class=hook style="font-size:92px">80&cent; for your care.<br><em>Miss it, and you get paid back.</em></div>\n<div class=cta>Send this to someone<br>who just got an <em>insurance refund.</em></div>\n<div class=src>' + DT_FOLLOW + '<br><br>Source: CMS, Medical Loss Ratio (cms.gov) and 2024 MLR Rebates by State (MLR reports filed through Sept. 12, 2025); HealthCare.gov glossary: Medical Loss Ratio.</div>',
]
