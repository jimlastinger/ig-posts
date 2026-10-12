import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "tools"))
from lib import *

ACCOUNT = 'dollartrail'
THEME = 'receipt'
TRAIL = '019'
FOLLOWING = 'an airline ticket'
SOURCES = ['https://www.faa.gov/about/budget/aatf/Current-Aviation-Excise-Tax-Structure-and-Rates-2026.pdf',
           'https://www.irs.gov/pub/irs-pdf/p510.pdf',
           'https://www.tsa.gov/for-industry/security-fees',
           'https://www.faa.gov/airports/pfc',
           'https://www.bts.gov/newsroom/second-quarter-2026-average-air-fare-increased-20-first-quarter-2026']

CAPTION = """On a $312 one-way domestic ticket (the average one-way fare in 2Q 2026), about $36 is taxes and fees: a 7.5% ticket tax, a $5.30 segment tax, the $5.60 TSA fee and an airport fee of up to $4.50. Illustrative example: one nonstop flight, one airport fee at the cap.

Data: FAA and IRS (2026 aviation excise tax rates), TSA, FAA Passenger Facility Charge program, Bureau of Transportation Statistics. Breakdown: our math.

Did you know what was in your fare?

#airfare #travel #taxes #flying #traveltips #dollartrail"""

SLIDES = [
    '<div class=tag>Trail No. 019</div>\n<div class=hook style="font-size:104px">A $312 one-way ticket: about <em>$36</em> is taxes and fees.</div>\n<div class=hook2>Illustrative: one nonstop domestic flight, 2026 rates.</div>\n<div class=mini style="margin-top:60px">Source: FAA and IRS (2026 aviation excise tax rates), TSA, FAA Passenger Facility Charge program. $312 = average one-way domestic fare, 2Q 2026 (Bureau of Transportation Statistics). Breakdown: our math.</div>',
    stack([(88.5, G, "BASE FARE $275.91"), (6.6, R, "TICKET TAX"), (1.7, Y, ""), (1.8, BL, ""), (1.4, P, "")],
          [("Base fare", "$275.91", G), ("Ticket tax", "$20.69", R), ("Segment tax", "$5.30", Y), ("TSA fee", "$5.60", BL), ("Airport fee", "$4.50", P)],
          "Illustrative $312 one-way, one flight segment, one airport fee at the $4.50 cap. Our math, rounded to cents.",
          "Follow $312", height=700),
    stop(1, 4, "Ticket tax", "$20.69", "7.5% OF THE BASE FARE",
         ["The federal domestic passenger ticket tax, at its 2026 rate."],
         "International flights carry a separate tax: $23.40 per person.", R),
    stop(2, 4, "Segment tax", "$5.30", "PER PASSENGER, PER FLIGHT SEGMENT",
         ["A flat federal tax on each segment: one takeoff and one landing. It&rsquo;s indexed to inflation (CPI)."],
         "A connection means two segments: $10.60 (our math).", Y),
    stop(3, 4, "TSA security fee", "$5.60", "PER ONE-WAY TRIP FROM A U.S. AIRPORT",
         ["The September 11th Security Fee, collected for the Transportation Security Administration."],
         "Capped at $11.20 per round trip.", BL),
    stop(4, 4, "Airport fee", "$4.50", "PASSENGER FACILITY CHARGE CAP, PER SEGMENT",
         ["Charged by airports under an FAA program. Our example assumes one airport at the cap."],
         "At most two per one-way trip, four per round trip ($18 max per round trip).", P),
    '<div class=tag>Detour</div>\n<h2>Average domestic fares,<br>2Q 2026</h2>\n' + cmp([(312, "$312", True), (445, "$445", False), (549, "$549", False)],
        ["One-way", "All trips", "Round trip"]) + '\n<div class=mini style="margin-top:24px">Bureau of Transportation Statistics, average domestic itinerary fare, 2Q 2026. Includes taxes and fees charged at purchase; excludes bag and seat fees.</div>',
    '<div class=tag>End of the trail</div>\n<div class=hook style="font-size:92px">A $312 one-way ticket.<br><em>About $36 is taxes and fees.</em></div>\n<div class=cta>Send this to someone<br>booking <em>holiday flights.</em></div>\n<div class=src>' + DT_FOLLOW + '<br><br>Source: FAA, Current Aviation Excise Tax Structure and Rates (2026); IRS Publication 510; TSA, Security Fees; FAA, Passenger Facility Charge program; BTS, 2Q 2026 average air fare. Illustrative breakdown: our math.</div>',
]
