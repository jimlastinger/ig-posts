import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "tools"))
from lib import *

ACCOUNT = 'dollartrail'
THEME = 'ledger'
TRAIL = '065'
FOLLOWING = 'A $24.99 gym membership'
SOURCES = ['https://www.sec.gov/Archives/edgar/data/1637207/000163720726000011/plnt-20251231.htm']

CAPTION = """Your $24.99 Planet Fitness Black Card, followed: at a franchised club paying the current 7% royalty, $1.75 goes to Planet Fitness, $2.25 goes to national and local ads, and $20.99 stays with the club to pay for everything else.

Data: Planet Fitness, Inc. 2025 Form 10-K (SEC filing): Black Card price, royalty rate and 2026 ad contribution rates applied to one month; our math.

Did you think the gym itself kept more or less?

#planetfitness #gym #fitness #franchise #personalfinance #dollartrail"""

SLIDES = [
    '<div class=tag>Trail No. 065</div>\n<div class=hook style="font-size:100px">A $24.99 Planet Fitness month: <em>the royalty is $1.75.</em></div>\n<div class=hook2>Ads take $2.25. The club keeps $20.99 to run the place.</div>\n<div class=mini style="margin-top:60px">Source: Planet Fitness, Inc. 2025 Form 10-K (SEC filing). PF Black Card price, the current 7% royalty rate and the 2026 ad contribution rates, applied to one month at a franchised club (our math).</div>',
    stack([(84, G, "84%"), (9, R, "9%"), (7, Y, "7%")],
          [("Stays with the club", "$20.99", G), ("Advertising", "$2.25", R), ("Royalty to Planet Fitness", "$1.75", Y), ("Black Card month", "$24.99", "transparent")],
          "Shares of monthly dues set in the 10-K: 7% royalty, 3% national ad fund and 6% local marketing (2026 rates). Rounded (our math).",
          "Where $24.99<br>goes.", height=700),
    stop(1, 4, "Your monthly bill", "$24.99", "PF BLACK CARD &middot; MONTHLY DUES",
         ["The 10-K lists the PF Black Card at <b>$24.99</b> a month. Classic starts at $15 for new members, and the annual fee is $49."],
         "Black Card penetration hit 66.5% at the end of 2025, up from 62.6% in 2021.", G),
    stop(2, 4, "The royalty", "$1.75", "7% OF DUES &middot; CURRENT RATE",
         ["Franchise clubs pay Planet Fitness a royalty figured as a percentage of their monthly dues and annual fees. The current rate is <b>7%</b>."],
         "Only about 63% of clubs paid the full rate. The average was 6.7%, up from 6.4% in 2021.", Y),
    stop(3, 4, "The ads", "$2.25", "3% NATIONAL FUND + 6% LOCAL",
         ["For 2026, franchisees voted to raise the national ad fund from 2% to <b>3%</b> and cut local marketing from 7% to <b>6%</b>."],
         "That&rsquo;s $0.75 for national ads and $1.50 for local ones (our math).", R),
    stop(4, 4, "Left for the club", "$20.99", "EVERY OTHER COST",
         ["Every other cost of running the club comes out of this. Franchisees must buy the equipment for new clubs from Planet Fitness or its required vendors."],
         "They generally replace it every five to nine years, depending on how busy the club is.", G),
    '<div class=tag>Detour</div>\n<h2>Where Planet Fitness got its revenue, 2025</h2>\n' + cmp([(41.2, "$546M", True), (28.8, "$381M", False), (23.4, "$310M", False), (6.6, "$87M", False)],
        ["Its own clubs", "Franchise fees", "Equipment", "Ad fund"]) + '\n<div class=mini style="margin-top:24px">Total revenue: $1.32 billion, ad fund money included. Members were billed $5.3 billion in dues and annual fees across 2,896 clubs, 2,604 of them franchised.</div>',
    '<div class=tag>End of the trail</div>\n<div class=hook style="font-size:88px">$24.99 a month.<br><em>The royalty: $1.75.</em></div>\n<div class=cta>Send this to the friend<br>who <em>pays for a gym they skip.</em></div>\n<div class=src>' + DT_FOLLOW + '<br><br>Source: Planet Fitness, Inc. Annual Report on Form 10-K for the year ended Dec. 31, 2025 (SEC filing): membership prices, royalty and ad contribution rates, club counts, system-wide sales and revenue. Per-month figures: our math.</div>',
]
