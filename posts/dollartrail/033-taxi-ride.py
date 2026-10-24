import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "tools"))
from lib import *

ACCOUNT = 'dollartrail'
TRAIL = '033'
FOLLOWING = 'a NYC yellow cab ride'
SOURCES = ['https://www.nyc.gov/site/tlc/passengers/taxi-fare.page']

CAPTION = """Hail a yellow cab below 60th Street in Manhattan at weekday rush hour, and $10.25 is on the fare before the meter adds a single mile, by our math from the city's fare rules. Only $3 of it is the meter's starting charge; $7.25 is surcharges and a toll.

Data: NYC Taxi & Limousine Commission, Taxi Fare (nyc.gov). Totals our math; tips and bridge or tunnel tolls extra.

Did you know about the rush hour charge?

#nyc #taxi #manhattan #congestionpricing #personalfinance #dollartrail"""

SLIDES = [
    '<div class=tag>Trail No. 033</div>\n<div class=hook style="font-size:100px">A yellow cab in Manhattan: <em>$10.25</em> before the meter moves.</div>\n<div class=hook2>Where it goes.</div>\n<div class=mini style="margin-top:60px">Source: NYC Taxi &amp; Limousine Commission, Taxi Fare (nyc.gov). Standard city rate, trip starting south of 60th Street, weekday 4-8 p.m. Our math. Tips and bridge or tunnel tolls not included.</div>',
    stack([(29, Y, "METER START 29%"), (71, R, "SURCHARGES + TOLL 71%")],
          [("Initial charge", "$3.00", Y), ("Congestion surcharge", "$2.50", R), ("Rush hour", "$2.50", R), ("Improvement", "$1.00", R), ("Congestion toll", "75&cent;", R), ("MTA State", "50&cent;", R)],
          "Shares of $10.25: our math, rounded. Then the meter adds 70&cent; per 1/5 mile, or per minute in slow traffic.",
          "Where $10.25 lands", height=640),
    stop(1, 4, "The meter", "$3.00", "INITIAL CHARGE",
         ["Then <b>70&cent; per 1/5 mile</b> above 12 mph, or <b>70&cent; per 60 seconds</b> in slow traffic or stopped. That&rsquo;s <b>$3.50 a mile</b> while moving (our math)."],
         "No extra charge for more passengers, bags, or paying by card.", Y),
    stop(2, 4, "Below 96th Street", "$2.50", "NEW YORK STATE CONGESTION SURCHARGE",
         ["Charged on yellow cab trips that begin, end or pass through <b>Manhattan south of 96th Street</b>. Green cabs pay <b>$2.75</b>; any shared ride, <b>75&cent;</b>."],
         "Below 60th Street, the MTA congestion pricing toll adds another 75&cent;.", R),
    stop(3, 4, "The clock", "$2.50", "RUSH HOUR, WEEKDAYS 4-8 P.M.",
         ["Holidays are excluded. Ride from <b>8 p.m. to 6 a.m.</b> instead and the overnight surcharge is <b>$1.00</b>."],
         "Same ride after 8 p.m.: $8.75 before the meter moves (our math).", BL),
    stop(4, 4, "The flat fees", "$1.50", "IMPROVEMENT $1.00 + MTA STATE 50&cent;",
         ["The <b>$1.00</b> improvement surcharge is part of the standard city rate. The <b>50&cent;</b> MTA State surcharge applies to trips ending in NYC or nearby counties."],
         "Together, $1.50 a ride (our math).", P),
    '<div class=tag>Detour</div>\n<h2>The JFK flat fare</h2>\n<div class=taxrow><div class=tx><div class=l>Flat fare</div><div class=n>$70</div><div class=d>Manhattan&ndash;JFK</div></div><div class=tx><div class=l>Rush hour</div><div class=n>$5.00</div><div class=d>Weekdays 4-8 p.m.</div></div></div>\n<div class=taxrow><div class=tx><div class=l>Other add-ons</div><div class=n>$4.75</div><div class=d>Congestion, toll, MTA, improvement</div></div><div class=tx><div class=l>Total</div><div class=n>$79.75</div><div class=d>Before tip and tolls</div></div></div>' + note("To JFK from below 60th Street at weekday rush hour, our math. Picked up at JFK? Add a $2.00 airport access fee."),
    '<div class=tag>End of the trail</div>\n<div class=hook style="font-size:88px">$10.25 before you move.<br><em>$7.25 of it isn&rsquo;t the meter.</em></div>\n<div class=cta>Send this to the friend<br>who <em>always hails a cab.</em></div>\n<div class=src>' + DT_FOLLOW + '<br><br>Source: NYC Taxi &amp; Limousine Commission, Taxi Fare page (nyc.gov), standard city rate and JFK flat fare. Totals and shares: our math. Tips and bridge or tunnel tolls not included.</div>',
]
