import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "tools"))
from lib import *

ACCOUNT = 'dollartrail'
TRAIL = '054'
FOLLOWING = 'a congressional paycheck'
SOURCES = ['https://clerk.house.gov/documents/Salary.pdf', 'https://clerk.house.gov/reference-files/congressional_research_service_report.pdf']

CAPTION = """On Election Day, here's the job's paycheck: $174,000 a year, the base salary for all members of Congress, per the House Clerk. That's the same figure it was raised to in January 2009, and the Congressional Research Service counted 18 scheduled raises that were denied from 1994 through 2021.

Data: Office of the Clerk, U.S. House of Representatives (Oct. 1, 2026); Congressional Research Service report 97-1011 (updated Jan. 25, 2022). Monthly and weekly figures: our math.

Should members of Congress get automatic raises?

#electionday #congress #salary #government #money #dollartrail"""

SLIDES = [
    '<div class=tag>Trail No. 054</div>\n<div class=hook style="font-size:100px">A seat in Congress pays <em>$174,000 a year.</em></div>\n<div class=hook2>Base salary for all members of Congress, as of Jan. 21, 2026.</div>\n<div class=mini style="margin-top:60px">Source: Office of the Clerk, U.S. House of Representatives, &ldquo;Salary in the United States House of Representatives,&rdquo; Oct. 1, 2026; Congressional Research Service report 97-1011. Monthly figure: our math.</div>',
    stack([(78, R, "ACTUAL PAY: $174,000"), (22, G, "SKIPPED RAISES: $49,400")],
          [("Actual salary", "$174,000", R), ("Gap vs. 2022 formula", "+$49,400", G)],
          "CRS: had members received every formula adjustment since 1992, the 2022 salary would have been $223,400. Gap and shares: our math.",
          "Pay vs. the raise formula", height=640),
    stop(1, 4, "Per month", "$14,500", "$174,000 &divide; 12 (OUR MATH), BEFORE TAXES",
         ["About <b>$3,346 a week</b> (our math).", "Same base pay for House and Senate members."],
         "Top leaders were paid more as of 2022 (see the detour).", R),
    stop(2, 4, "Last raise", "Jan. 2009", "A 2.8% RAISE, TO $174,000 (CRS)",
         ["CRS: members &ldquo;last received a pay adjustment in January 2009.&rdquo;", "The House Clerk&rsquo;s 2026 figure is still <b>$174,000</b>."],
         "Same number on the paycheck for more than 17 years.", Y),
    stop(3, 4, "Raises denied", "18", "SCHEDULED RAISES DENIED, 1994 TO 2021 (CRS)",
         ["Accepted <b>13 times</b>, from 1991 to 2009.", "Denied every year from <b>2010 through 2021</b>, the last year CRS counted."],
         "CRS counts every scheduled yearly adjustment from 1991 to 2021.", BL),
    stop(4, 4, "Inflation&rsquo;s cut", "&minus;20.8%", "APPROXIMATE DROP IN MEMBER PAY ADJUSTED FOR INFLATION, 2009 TO 2021 (CRS)",
         ["Same dollars, less buying power.", "CRS&rsquo;s inflation comparison stops at 2021."],
         "A frozen salary is a slow pay cut.", P),
    '<div class=tag>Detour</div>\n<h2>Leadership pay (CRS, Jan. 2022)</h2>\n' + cmp([(223500, "$223,500", True), (193400, "$193,400", False), (174000, "$174,000", False)],
        ["Speaker", "Leaders*", "Members"]) + '\n<div class=mini style="margin-top:24px">*Senate president pro tempore and House and Senate majority and minority leaders. Figures from CRS report 97-1011, updated Jan. 25, 2022.</div>',
    '<div class=tag>End of the trail</div>\n<div class=hook style="font-size:86px">$174,000 a year.<br><em>No raise since 2009.</em></div>\n<div class=cta>Send this to the friend<br>who&rsquo;s <em>voting today.</em></div>\n<div class=src>' + DT_FOLLOW + '<br><br>Source: Office of the Clerk, U.S. House of Representatives, &ldquo;Salary in the United States House of Representatives&rdquo; (clerk.house.gov), Oct. 1, 2026; Congressional Research Service, &ldquo;Salaries of Members of Congress: Recent Actions and Historical Tables,&rdquo; 97-1011, updated Jan. 25, 2022. Monthly, weekly and gap figures: our math.</div>',
]
