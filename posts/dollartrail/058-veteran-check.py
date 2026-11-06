import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "tools"))
from lib import *

ACCOUNT = 'dollartrail'
THEME = 'receipt'
TRAIL = '058'
FOLLOWING = 'a VA disability check'
SOURCES = ['https://www.va.gov/disability/compensation-rates/veteran-rates/', 'https://www.ssa.gov/news/en/cola/factsheets/2027.html']

CAPTION = """Ahead of Veterans Day: a veteran rated 100% disabled, with no dependents, gets $3,938.58 a month from VA. At a 10% rating it's $180.42 (rates effective Dec. 1, 2025).

Data: U.S. Department of Veterans Affairs, Veteran disability compensation rates (effective Dec. 1, 2025), va.gov; Social Security Administration 2027 COLA fact sheet. Yearly figure: our math.

Did you know what each VA rating pays?

#veteransday #veterans #va #disability #money #dollartrail"""

SLIDES = [
    '<div class=tag>Trail No. 058</div>\n<div class=hook style="font-size:100px">100% disabled veteran: <em>$3,938.58 a month.</em></div>\n<div class=hook2>What a VA disability rating pays, ahead of Veterans Day.</div>\n<div class=mini style="margin-top:60px">Source: U.S. Department of Veterans Affairs, veteran disability compensation rates, effective Dec. 1, 2025. Veteran alone, no dependents.</div>',
    '<div class=tag>The trail map</div>\n<h2>Monthly VA payment by rating</h2>\n' + cmp([(180.42, "$180", False), (552.47, "$552", False), (1132.90, "$1,133", False), (1808.45, "$1,808", False), (3938.58, "$3,939", True)],
        ["10%", "30%", "50%", "70%", "100%"]) + '\n<div class=mini style="margin-top:24px">VA rates effective Dec. 1, 2025, veteran alone with no dependents, rounded to the dollar. Exact amounts on the next slides.</div>',
    stop(1, 4, "The first step", "$180.42", "MONTHLY, 10% RATING, VETERAN ALONE",
         ["At <b>20%</b>, it&rsquo;s <b>$356.66</b>.", "At <b>30%</b>, it&rsquo;s <b>$552.47</b>."],
         "Every 10 points of rating adds to the check.", R),
    stop(2, 4, "Halfway", "$1,132.90", "MONTHLY, 50% RATING, VETERAN ALONE",
         ["At <b>60%</b>, it&rsquo;s <b>$1,435.02</b>.", "At <b>70%</b>, it&rsquo;s <b>$1,808.45</b>."],
         "All rates here are for a veteran with no dependents.", Y),
    stop(3, 4, "The top rate", "$3,938.58", "MONTHLY, 100% RATING, VETERAN ALONE",
         ["That&rsquo;s <b>$47,262.96</b> a year (our math).", "At <b>90%</b>, it&rsquo;s <b>$2,362.30</b> a month."],
         "The jump from 90% to 100% is $1,576.28 a month (our math).", BL),
    stop(4, 4, "Social Security&rsquo;s raise", "3.6%", "SOCIAL SECURITY COLA, STARTING WITH DECEMBER 2026 BENEFITS",
         ["VA says it&rsquo;s required by law to match Social Security&rsquo;s cost-of-living raise."],
         "VA hasn&rsquo;t posted its new rate table yet (checked Nov. 6, 2026).", P),
    '<div class=tag>End of the trail</div>\n<div class=hook style="font-size:86px">10%: $180.42.<br><em>100%: $3,938.58.</em></div>\n<div class=cta>Send this to a veteran<br>who <em>should know their numbers.</em></div>\n<div class=src>' + DT_FOLLOW + '<br><br>Source: U.S. Department of Veterans Affairs, veteran disability compensation rates, effective Dec. 1, 2025 (veteran alone, no dependents), va.gov; Social Security Administration, 2027 COLA fact sheet, ssa.gov. Yearly and difference figures: our math.</div>',
]
