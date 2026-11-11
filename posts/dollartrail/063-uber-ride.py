import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "tools"))
from lib import *

ACCOUNT = 'dollartrail'
TRAIL = '063'
FOLLOWING = 'A $25 Uber ride'
SOURCES = ['https://www.sec.gov/Archives/edgar/data/1543151/000154315126000015/uber-20251231.htm']

CAPTION = """On a $25 Uber ride, Uber takes in about $7.61 in revenue and ends up with about $2.03 of segment profit. The remaining $17.39 of the fare isn't Uber revenue. That part includes the driver's earnings, plus taxes, tolls and fees.

Data: Uber Technologies 2025 Form 10-K (SEC filing). Shares of $97.5 billion in 2025 Mobility Gross Bookings applied to a $25 fare; our math.

Did you think Uber kept more or less than that?

#uber #rideshare #gigeconomy #personalfinance #money #dollartrail"""

SLIDES = [
    '<div class=tag>Trail No. 063</div>\n<div class=hook style="font-size:100px">A $25 Uber ride: <em>Uber takes in $7.61.</em></div>\n<div class=hook2>It keeps about $2.03 after running the ride business.</div>\n<div class=mini style="margin-top:60px">Source: Uber Technologies 2025 Form 10-K (SEC filing). Each figure = its share of $97.5 billion in 2025 Mobility Gross Bookings, applied to $25 (our math).</div>',
    stack([(69.57, G, "69.6%"), (22.33, R, "22.3%"), (8.10, Y, "8.1%")],
          [("Not Uber&rsquo;s revenue", "$17.39", G), ("Uber&rsquo;s ride costs", "$5.58", R), ("Uber&rsquo;s segment profit", "$2.03", Y), ("Fare", "$25.00", "transparent")],
          "Uber 2025 Mobility revenue and Mobility Adjusted EBITDA as shares of Mobility Gross Bookings (sum of the four 2025 quarters). Rounded (our math).",
          "Where $25<br>goes.", height=700),
    stop(1, 4, "You tap &ldquo;Confirm&rdquo;", "$25.00", "MOBILITY GROSS BOOKINGS &middot; 2025",
         ["Riders booked <b>$97.5 billion</b> in Uber rides in 2025, counting taxes, tolls and fees but not tips."],
         "That&rsquo;s the four quarters added up (our math). Ride bookings grew 17% from 2024.", G),
    stop(2, 4, "Not Uber&rsquo;s money", "$17.39", "GROSS BOOKINGS MINUS MOBILITY REVENUE",
         ["<b>69.6%</b> of what riders pay never becomes Uber revenue. It includes the driver&rsquo;s earnings, plus taxes, tolls and fees."],
         "Tips aren&rsquo;t in the $25 at all. Per the 10-K, they aren&rsquo;t counted in Gross Bookings.", G),
    stop(3, 4, "Uber&rsquo;s cut", "$7.61", "MOBILITY REVENUE &middot; 2025",
         ["Mobility revenue was <b>$29.7 billion</b>. Per the 10-K, Uber&rsquo;s revenue is almost all fees drivers and merchants pay to use its platform."],
         "In some markets Uber books the full fare as revenue and puts driver pay in its costs, so this is an average.", Y),
    stop(4, 4, "What Uber keeps", "$2.03", "MOBILITY SEGMENT ADJUSTED EBITDA",
         ["After the costs of running rides, the segment earned <b>$7.9 billion</b>, before corporate overhead and other items."],
         "Insurance cost Uber $851 million more in 2025, as rates per mile and miles driven rose.", Y),
    '<div class=tag>Detour</div>\n<h2>Uber revenue per $100 booked, 2025</h2>\n' + cmp([(30.43, "$30.43", True), (18.98, "$18.98", False)],
        ["Rides", "Delivery orders"]) + '\n<div class=mini style="margin-top:24px">Mobility: $29.7 billion revenue on $97.5 billion booked. Delivery: $17.25 billion on $90.9 billion. Uber gets a bigger share of a ride than of a delivery order (our math).</div>',
    '<div class=tag>End of the trail</div>\n<div class=hook style="font-size:88px">$25 for the ride.<br><em>Uber keeps about $2.</em></div>\n<div class=cta>Send this to the friend<br>who <em>drives for Uber.</em></div>\n<div class=src>' + DT_FOLLOW + '<br><br>Source: Uber Technologies, Inc. Annual Report on Form 10-K for the year ended Dec. 31, 2025 (SEC filing): quarterly Mobility Gross Bookings, segment revenue and segment Adjusted EBITDA. Per-$25 figures: our math.</div>',
]
