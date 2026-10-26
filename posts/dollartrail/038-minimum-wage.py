import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "tools"))
from lib import *

ACCOUNT = 'dollartrail'
THEME = 'ledger'
TRAIL = '038'
FOLLOWING = 'one hour at minimum wage'
SOURCES = ['https://www.dol.gov/agencies/whd/minimum-wage/state',
           'https://dol.gov/newsroom/releases/esa/esa20090716']

CAPTION = """The federal minimum wage is $7.25 an hour, where it has been since July 24, 2009. In D.C. it's $18.40, and 20 states either match $7.25, set less, or have no minimum wage law at all.

Data: U.S. Department of Labor, Wage and Hour Division, State Minimum Wage Laws (updated July 1, 2026), and DOL's July 16, 2009 news release. Yearly totals our math.

What was your first hourly wage?

#minimumwage #wages #economy #personalfinance #money #dollartrail"""

SLIDES = [
    '<div class=tag>Trail No. 038</div>\n<div class=hook style="font-size:104px">One hour of work: <em>$7.25</em> or <em>$18.40.</em></div>\n<div class=hook2>It depends where you clock in.</div>\n<div class=mini style="margin-top:60px">Source: U.S. Department of Labor (DOL), Wage and Hour Division, State Minimum Wage Laws, updated July 1, 2026. Basic state rates; some cities and counties set higher ones.</div>',
    stack([(61, R, "ABOVE $7.25: 31"), (25, Y, "$7.25: 13"), (4, P, ""), (10, BL, "NO LAW: 5")],
          [("Above $7.25", "31", R), ("At $7.25", "13", Y), ("Below $7.25", "2", P), ("No state law", "5", BL)],
          "Above $7.25: 30 states plus D.C. Counts from the DOL table and shares: our math.",
          "50 states and D.C.", height=700),
    stop(1, 4, "The federal floor", "$7.25", "PER HOUR, SINCE JULY 24, 2009",
         ["Full time, that&rsquo;s <b>$15,080 a year</b> before taxes (40 hours &times; 52 weeks, our math)."],
         "The last raise before that: to $6.55, in July 2008.", BL),
    stop(2, 4, "The top", "$18.40", "WASHINGTON, D.C., PER HOUR",
         ["Full time: <b>$38,272 a year</b> (our math). That&rsquo;s about <b>2.5 times</b> the federal rate."],
         "D.C. adjusts its rate every July 1 by formula.", R),
    '<div class="tag ghost">Stop 3 of 4</div>\n<h2>The top five</h2>\n' + cmp([(18.40, "$18.40", True), (17.13, "$17.13", False), (17.00, "$17.00", False), (16.94, "$16.94", False), (16.90, "$16.90", False), (7.25, "$7.25", False)],
        ["D.C.", "Wash.", "N.Y.*", "Conn.", "Calif.", "Federal"]) + '\n<div class=mini style="margin-top:24px">*New York: $17.00 in NYC, Nassau, Suffolk and Westchester; $16.00 in the rest of the state. DOL basic rates as of July 1, 2026.</div>',
    stop(4, 4, "The floor states", "20", "STATES AT, BELOW OR WITHOUT $7.25",
         ["<b>13</b> set $7.25. Georgia and Wyoming list <b>$5.15</b>. Alabama, Louisiana, Mississippi, South Carolina and Tennessee have <b>no state law</b>."],
         "Employers covered by federal law must still pay $7.25.", Y),
    '<div class=tag>Detour</div>\n<h2>A raise on the calendar</h2>\n<div class=taxrow><div class=tx><div class=l>Michigan now</div><div class=n>$13.73</div><div class=d>Per hour</div></div><div class=tx><div class=l>Jan. 1, 2027</div><div class=n>$15.00</div><div class=d>Scheduled</div></div></div>\n' + note("After that, DOL says Michigan&rsquo;s rate will adjust each year by formula."),
    '<div class=tag>End of the trail</div>\n<div class=hook style="font-size:88px">Same hour of work.<br><em>$15,080 or $38,272 a year.</em></div>\n<div class=cta>Send this to the friend<br>who <em>just got a first job.</em></div>\n<div class=src>' + DT_FOLLOW + '<br><br>Source: U.S. Department of Labor, Wage and Hour Division, State Minimum Wage Laws (updated July 1, 2026); DOL news release, July 16, 2009. Full-time totals (2,080 hours) and counts: our math.</div>',
]
