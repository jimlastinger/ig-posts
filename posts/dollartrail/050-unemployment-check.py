import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "tools"))
from lib import *

ACCOUNT = 'dollartrail'
THEME = 'ledger'
TRAIL = '050'
FOLLOWING = 'a weekly unemployment check'
SOURCES = ['https://oui.doleta.gov/unemploy/content/sigpros/2020-2029/January2026.pdf']

CAPTION = """Lose your job in Washington and the most unemployment can pay you is $1,152 a week. In Mississippi it's $235, and the number of weeks varies too.

Data: U.S. Department of Labor, Significant Provisions of State Unemployment Insurance Laws, effective January 2026. Maximum weekly benefit amounts; some states add dependents' allowances. Totals and ratios: our math.

What's the max in your state?

#unemployment #jobs #layoffs #personalfinance #money #dollartrail"""

SLIDES = [
    '<div class=tag>Trail No. 050</div>\n<div class=hook style="font-size:100px">The most unemployment pays: <em>$235 to $1,152</em> a week.</div>\n<div class=hook2>The max in the 11 states we checked. It depends on where you lost the job.</div>\n<div class=mini style="margin-top:60px">Source: U.S. Department of Labor (DOL), Significant Provisions of State Unemployment Insurance Laws, effective January 2026. Maximum weekly benefit amounts.</div>',
    stack([(80, R, "$917 MORE IN WASHINGTON"), (20, G, "$235: MISSISSIPPI MAX")],
          [("Mississippi max", "$235", G), ("Washington extra", "+$917", R), ("Washington max", "$1,152", R)],
          "Max weekly benefits, January 2026 (DOL). Bar = Washington&rsquo;s max; gray part = Mississippi&rsquo;s. Difference and shares: our math.",
          "Two states, one week", height=640),
    stop(1, 4, "Highest we checked", "$1,152", "WASHINGTON, MAX PER WEEK",
         ["Minimum: <b>$366</b>. Weeks payable: <b>1 to 26</b>.", "Massachusetts is close at <b>$1,105</b>, plus $25 per dependent, with no cap on that allowance."],
         "26 weeks at the Washington max: $29,952 (our math).", R),
    stop(2, 4, "The big states", "$869", "NEW YORK, MAX PER WEEK",
         ["Texas: <b>$605</b>. California: <b>$450</b>.", "New York pays a uniform <b>26 weeks</b>; Texas 10 to 26; California 14 to 26."],
         "California&rsquo;s max is less than 40% of Washington&rsquo;s (our math).", Y),
    stop(3, 4, "The South", "$235-$350", "MAX PER WEEK, FIVE STATES",
         ["North Carolina $350. Louisiana $282. Florida and Alabama $275. Mississippi $235.", "North Carolina and Louisiana pay <b>12 to 20 weeks</b>."],
         "26 weeks at the Mississippi max: $6,110 (our math).", BL),
    stop(4, 4, "How long it lasts", "26", "WEEKS: THE LIMIT IN WA, NY, TX, CA AND MS",
         ["Arizona: <b>8 to 24</b>. Washington: <b>1 to 26</b>.", "In Arizona, the limit drops to 24 weeks when the state&rsquo;s unemployment rate is under 5%."],
         "Some states pay extra weeks in limited cases, like high unemployment (DOL).", P),
    '<div class=tag>Detour</div>\n<h2>Max weekly benefit, Jan. 2026</h2>\n' + cmp([(235, "$235", False), (450, "$450", False), (605, "$605", False), (869, "$869", False), (1152, "$1,152", True)],
        ["MS", "CA", "TX", "NY", "WA"]) + '\n<div class=mini style="margin-top:24px">DOL, Significant Provisions of State UI Laws, effective January 2026. Not a 50-state ranking; states we checked.</div>',
    '<div class=tag>End of the trail</div>\n<div class=hook style="font-size:86px">$235 a week in Mississippi.<br><em>$1,152 in Washington.</em></div>\n<div class=cta>Send this to the friend<br>who <em>just got laid off.</em></div>\n<div class=src>' + DT_FOLLOW + '<br><br>Source: U.S. Department of Labor, Significant Provisions of State Unemployment Insurance Laws, effective January 2026 (oui.doleta.gov). Maximum weekly benefit amounts. Totals and ratios: our math.</div>',
]
