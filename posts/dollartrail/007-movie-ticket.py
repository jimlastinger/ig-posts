import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "tools"))
from lib import *

ACCOUNT = 'dollartrail'
TRAIL = '007'
FOLLOWING = 'a $12.09 movie ticket'
SOURCES = ['https://investor.amctheatres.com/sec-filings/all-sec-filings/content/0001411579-26-000018/0001411579-26-000018.pdf',
           'https://www.sec.gov/Archives/edgar/data/1411579/000141157926000016/amc-20251231x10k.htm']

CAPTION = """AMC's average ticket in 2025 was $12.09, and $5.81 of it went to the studios. The theater makes its money at the snack bar, and even then it barely broke even.

Data: AMC Entertainment, full-year 2025 results (SEC Form 8-K, Feb. 2026). Per-visit figures = AMC's 2025 totals divided by 219.4 million admissions.

Would you have guessed the popcorn pays the rent?

#movies #movietheater #amc #popcorn #personalfinance #dollartrail"""

SLIDES = [
    '<div class=tag>Trail No. 007</div>\n<div class=hook>A movie ticket: <em>$12.09.</em></div>\n<div class=hook2>Who gets it, and why the popcorn matters.</div>\n<div class=mini style="margin-top:60px">Source: AMC Entertainment, full-year 2025 results (SEC Form 8-K, Feb. 2026). $12.09 = AMC\'s average ticket price across its U.S. and European theaters in 2025.</div>',
    stack([(48.1, R, "48.1%"), (51.9, Y, "51.9%")],
          [("The studios", "$5.81", R), ("The theater", "$6.28", Y), ("Ticket", "$12.09", "transparent")],
          "AMC's 2025 film exhibition costs were 48.1% of its admissions revenue, applied to its $12.09 average ticket. Rounded.",
          "One ticket.<br>Two hands out.", height=680),
    stop(1, 4, "The studios", "$5.81", "FILM EXHIBITION COSTS &middot; 48.1% OF TICKETS",
         ["Theaters rent each movie from the studio that made it. The rent is a share of ticket sales."],
         "AMC paid studios $1.28 billion in 2025, on $2.65 billion of ticket sales.", R),
    stop(2, 4, "The snack bar", "$7.62", "FOOD &amp; DRINK PER VISIT",
         ["Moviegoers spent $1.67 billion on food and drinks at AMC in 2025. The food itself cost AMC $327 million."],
         "That's about $1.49 of food for every $7.62 spent. AMC keeps about 80 cents of each snack-bar dollar, and the studios get none of it.", Y),
    '<div class="tag ghost" style="color:#6aa9ff;border-color:#6aa9ff">Stop 3 of 4</div>\n<h2>The bills</h2><div class=amt style="color:#6aa9ff">$12.18</div><div class=pct>PER VISIT &middot; RUNNING THEATERS + RENT</div>\n<div class=taxrow>\n <div class=tx><div class=l>Running theaters</div><div class=n>$8.14</div><div class=d>Operating expense: the day-to-day cost of running theaters. $1.79 billion.</div></div>\n <div class=tx><div class=l>Rent</div><div class=n>$4.04</div><div class=d>Leases on the buildings. $887 million.</div></div>\n</div>\n' + note("Those two bills alone are bigger than the whole $12.09 ticket."),
    '<div class="tag ghost" style="color:#4fd1a5;border-color:#4fd1a5">Stop 4 of 4</div>\n<h2>The bottom line</h2><div class=amt style="color:#4fd1a5">&minus;8&cent;</div><div class=pct>OPERATING RESULT PER VISIT</div>\n<div class=taxrow>\n <div class=tx><div class=l>In per visit</div><div class=n>$22.10</div><div class=d>Ticket $12.09, food &amp; drink $7.62, other theater revenue $2.39.</div></div>\n <div class=tx><div class=l>Out per visit</div><div class=n>$22.18</div><div class=d>Studios, food, staff, rent, overhead, wear on theaters.</div></div>\n</div>\n' + note("After interest on its debt and other costs, AMC lost $632 million in 2025."),
    '<div class=tag>End of the trail</div>\n<div class=hook style="font-size:96px">The ticket pays the studio.<br><em>The popcorn pays the rent.</em></div>\n<div class=cta>Send this to your<br><em>movie night</em> friend.</div>\n<div class=src>' + DT_FOLLOW + '<br><br>Source: AMC Entertainment Holdings, Inc., fourth quarter and full year 2025 results, year ended Dec. 31, 2025 (SEC Form 8-K, Feb. 23, 2026). Per-visit = totals &divide; 219.4 million admissions. Rounded.</div>',
]
