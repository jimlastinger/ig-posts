import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "tools"))
from lib import *

ACCOUNT = 'dollartrail'
TRAIL = '066'
FOLLOWING = 'A $1,000 Airbnb booking'
SOURCES = ['https://www.sec.gov/Archives/edgar/data/1559720/000155972026000004/abnb-20251231.htm']

CAPTION = """Book $1,000 on Airbnb and about $134 of it is Airbnb's revenue. After its own costs, it keeps about $28. The other $866 is the host's earnings, cleaning fees and taxes.

Data: Airbnb, Inc. 2025 Form 10-K (SEC filing). Each 2025 figure as a share of $91.3 billion in Gross Booking Value, applied to $1,000; our math.

Did you think Airbnb kept more or less than that?

#airbnb #travel #vacationrental #personalfinance #money #dollartrail"""

SLIDES = [
    '<div class=tag>Trail No. 066</div>\n<div class=hook style="font-size:100px">A $1,000 Airbnb booking: <em>Airbnb takes in $134.</em></div>\n<div class=hook2>It keeps about $28 after paying its own bills.</div>\n<div class=mini style="margin-top:60px">Source: Airbnb, Inc. 2025 Form 10-K (SEC filing). Each figure = its share of $91.3 billion in 2025 Gross Booking Value, applied to $1,000 (our math).</div>',
    stack([(86.6, G, "86.6%"), (10.6, R, "10.6%"), (2.8, Y, "2.8%")],
          [("Not Airbnb&rsquo;s revenue", "$865.89", G), ("Airbnb&rsquo;s costs", "$106.24", R), ("Airbnb&rsquo;s operating profit (2.8%)", "$27.87", Y), ("Booking", "$1,000", "transparent")],
          "Airbnb 2025 revenue, total costs and income from operations as shares of Gross Booking Value. Rounded (our math).",
          "Where $1,000<br>goes.", height=700),
    stop(1, 5, "You hit &ldquo;Reserve&rdquo;", "$1,000", "GROSS BOOKING VALUE &middot; 2025",
         ["Guests booked <b>$91.3 billion</b> on Airbnb in 2025, counting host earnings, service fees, cleaning fees and taxes."],
         "That covered 533 million nights and seats, about $171 each (our math).", G),
    stop(2, 5, "Not Airbnb&rsquo;s money", "$865.89", "BOOKINGS MINUS AIRBNB REVENUE",
         ["<b>86.6%</b> of what guests book never becomes Airbnb revenue. It&rsquo;s mostly the host&rsquo;s earnings, the cleaning fee and the taxes."],
         "Airbnb says it has over 5 million hosts.", G),
    stop(3, 5, "Airbnb&rsquo;s fees", "$134.11", "REVENUE &middot; 2025",
         ["Airbnb&rsquo;s revenue is its service fees, net of incentives and refunds. In 2025 that came to <b>$12.2 billion</b>."],
         "In October 2025 it began moving to one fee charged only to the host. Before, guests and hosts each paid a fee.", Y),
    stop(4, 5, "Running Airbnb", "$106.24", "TOTAL COSTS AND EXPENSES",
         ["Sales and marketing is the biggest line at <b>$28.35</b>. Product development is $25.79 and cost of revenue is $22.85."],
         "General and administrative is $14.70, and operations and support is $14.54 (our math).", R),
    stop(5, 5, "What Airbnb keeps", "$27.87", "INCOME FROM OPERATIONS",
         ["Airbnb earned <b>$2.54 billion</b> from operations in 2025, about flat with 2024."],
         "Net income was $2.51 billion, or $27.51 per $1,000 booked, after interest income, other expense and taxes (our math).", Y),
    '<div class=tag>Detour</div>\n<h2>Airbnb revenue per $100 booked</h2>\n' + cmp([(13.57, "$13.57", False), (13.41, "$13.41", True)],
        ["2024", "2025"]) + '\n<div class=mini style="margin-top:24px">2024: $11.1 billion revenue on $81.8 billion booked. 2025: $12.2 billion on $91.3 billion. Bookings grew 12% and revenue 10%, so Airbnb&rsquo;s cut slipped a little (our math).</div>',
    '<div class=tag>End of the trail</div>\n<div class=hook style="font-size:88px">$1,000 for the stay.<br><em>Airbnb keeps about $28.</em></div>\n<div class=cta>Send this to the friend<br>who <em>rents out their place.</em></div>\n<div class=src>' + DT_FOLLOW + '<br><br>Source: Airbnb, Inc. Annual Report on Form 10-K for the year ended Dec. 31, 2025 (SEC filing): Gross Booking Value, Nights and Seats Booked, revenue, costs and income from operations. Per-$1,000 figures: our math.</div>',
]
