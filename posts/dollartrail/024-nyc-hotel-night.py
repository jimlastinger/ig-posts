import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "tools"))
from lib import *

ACCOUNT = 'dollartrail'
TRAIL = '024'
FOLLOWING = 'a $300 NYC hotel night'
SOURCES = ['https://www.nyc.gov/site/finance/business/business-hotel-room-occupancy-tax.page',
           'https://www.nyc.gov/assets/finance/downloads/pdf/08pdf/fm3608htx.pdf',
           'https://portal.311.nyc.gov/article/?kanumber=KA-02794',
           'https://www.tax.ny.gov/pubs_and_bulls/tg_bulletins/st/hotel_and_motel_occupancy.htm',
           'https://www.tax.ny.gov/e-services/stmi/sch_n.htm',
           'https://www.tax.ny.gov/pdf/publications/sales/pub718.pdf',
           'https://www.tax.ny.gov/pubs_and_bulls/tg_bulletins/st/sales_tax_rates_additional_sales_taxes_and_fees.htm']

CAPTION = """Illustrative: one $300 night in a New York City hotel comes with about $47.75 in state and city taxes and fees: 8.875% sales tax, the city's 5.875% hotel tax, a $2 room charge and a $1.50 unit fee. That's before any hotel or resort fees.

Data: NYC Department of Finance, NYC311, NYS Department of Taxation and Finance (TB-ST-331, Schedule N, Pub 718, TB-ST-825). Breakdown: our math.

What's the biggest hotel tax bill you've been surprised by?

#nyc #hotels #travel #taxes #newyorkcity #dollartrail"""

SLIDES = [
    '<div class=tag>Trail No. 024</div>\n<div class=hook style="font-size:100px">Book a $300 hotel night in NYC. You&rsquo;ll pay about <em>$347.75.</em></div>\n<div class=hook2>Illustrative, before any hotel or resort fees.</div>\n<div class=mini style="margin-top:60px">Source: NYC Department of Finance; NYC311; NYS Department of Taxation and Finance (TB-ST-331, Schedule N, Pub 718, TB-ST-825). Breakdown: our math.</div>',
    stack([(86.3, G, "THE ROOM $300"), (7.7, R, "SALES TAX"), (5.0, Y, ""), (1.0, BL, "")],
          [("Room rate", "$300.00", G), ("Sales tax", "$26.63", R), ("City hotel tax", "$17.63", Y), ("Flat fees", "$3.50", BL)],
          "One night, stay under 90 days. Assumes each percentage tax applies to the $300 rent only. Total about $347.75 (lines rounded to the cent). Our math.",
          "Follow the $300 room", height=680),
    stop(1, 4, "Sales tax", "$26.63", "8.875% OF THE ROOM RATE",
         ["New York State&rsquo;s 4%, plus 0.375% for the Metropolitan Commuter Transportation District, plus NYC&rsquo;s 4.5% local tax."],
         "From day 91 to day 180 of a stay, only the 4.5% local part applies.", R),
    stop(2, 4, "City hotel tax", "$17.63", "5.875% OF THE ROOM RATE",
         ["NYC&rsquo;s Hotel Room Occupancy Tax, run by the city&rsquo;s Department of Finance. This rate took effect December 20, 2013."],
         "Permanent residents (180+ consecutive days) don&rsquo;t pay it.", Y),
    stop(3, 4, "The room charge", "$2.00", "PER ROOM, PER NIGHT, ON ROOMS $40 AND UP",
         ["Part of the city hotel tax, charged on top of the 5.875%. Cheaper rooms pay less: $0.50 to $1.50 a day, and $0 under $10."],
         "It&rsquo;s a flat amount, the same on a $40 room as on a $1,000 suite.", BL),
    stop(4, 4, "The unit fee", "$1.50", "PER UNIT, PER DAY, NYC ONLY",
         ["Hotels and booking services in New York City must charge it. The state collects it."],
         "NYS: the unit fee &ldquo;is not subject to state and local sales taxes.&rdquo;", P),
    '<div class=tag>Detour</div>\n<h2>Flat fees hit cheap rooms harder</h2>\n' + cmp([(18.25, "18.25%", True), (15.92, "15.9%", False)],
        ["$100 room", "$300 room"]) + '\n<div class=mini style="margin-top:24px">Taxes and fees as a share of one night&rsquo;s room rate. Same 14.75% in percentage taxes, plus the same $3.50 flat. Our math, same assumptions.</div>',
    '<div class=tag>End of the trail</div>\n<div class=hook style="font-size:88px">About $47.75 in taxes and fees on a $300 night.<br><em>Stay 180 days and most of it goes away.</em></div>\n<div class=cta>Send this to someone<br>who&rsquo;s <em>booking a NYC trip.</em></div>\n<div class=src>' + DT_FOLLOW + '<br><br>Source: NYC Department of Finance (Hotel Room Occupancy Tax page; Finance Memorandum 08-1REV); NYC311; NYS Department of Taxation and Finance (TB-ST-331, Schedule N, Publication 718, TB-ST-825). Illustrative breakdown: our math.</div>',
]
