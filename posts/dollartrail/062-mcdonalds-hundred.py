import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "tools"))
from lib import *

ACCOUNT = 'dollartrail'
THEME = 'ledger'
TRAIL = '062'
FOLLOWING = '$100 at McDonald&rsquo;s'
SOURCES = ['https://www.sec.gov/Archives/edgar/data/63908/000006390826000035/mcd-20251231.htm']

CAPTION = """For every $100 spent at franchised McDonald's restaurants in 2025, $12.76 went to McDonald's in rent, royalties and fees. After its own property costs, McDonald's kept $10.74, and the franchisees kept $87.24 to run the restaurants.

Data: McDonald's Corp. 2025 Form 10-K (SEC filing). Shares of $129.7 billion in franchised sales applied to $100; our math.

Would you rather own the restaurant or the building under it?

#mcdonalds #fastfood #franchise #personalfinance #money #dollartrail"""

SLIDES = [
    '<div class=tag>Trail No. 062</div>\n<div class=hook style="font-size:96px">Spend $100 at a McDonald&rsquo;s franchise: <em>$12.76 goes to McDonald&rsquo;s.</em></div>\n<div class=hook2>The franchisee keeps $87.24 to run the place.</div>\n<div class=mini style="margin-top:60px">Source: McDonald&rsquo;s Corp. 2025 Form 10-K (SEC filing). Each slice = its share of $129.7 billion in 2025 franchised sales, applied to $100 (our math).</div>',
    stack([(87.24, G, "87.24%"), (2.02, R, ""), (10.74, Y, "10.74%")],
          [("Franchisee keeps", "$87.24", G), ("Property costs", "$2.02", R), ("McDonald&rsquo;s margin", "$10.74", Y), ("Total", "$100.00", "transparent")],
          "McDonald&rsquo;s 2025 franchised revenues, franchised occupancy costs and franchised margin, each as a share of franchised sales. Rounded (our math).",
          "Where $100<br>goes.", height=700),
    stop(1, 4, "At the counter", "$100.00", "FRANCHISED SALES &middot; 2025",
         ["Franchised McDonald&rsquo;s restaurants took in <b>$129.7 billion</b> in 2025."],
         "About 95% of the 45,356 McDonald&rsquo;s restaurants at year-end 2025 were franchised.", G),
    stop(2, 4, "Rent and royalties", "$12.76", "REVENUES FROM FRANCHISED RESTAURANTS",
         ["Franchisees paid McDonald&rsquo;s <b>$16.5 billion</b>. Most pay rent and royalties based on a percent of sales, plus initial fees."],
         "That&rsquo;s 62% of McDonald&rsquo;s $26.9 billion in total revenue (our math).", Y),
    stop(3, 4, "The buildings", "$2.02", "FRANCHISED RESTAURANTS-OCCUPANCY EXPENSES",
         ["McDonald&rsquo;s own property costs for franchised restaurants were <b>$2.6 billion</b>."],
         "Per the 10-K, conventional franchisees pay rent to McDonald&rsquo;s, with set minimum rent payments.", R),
    stop(4, 4, "What McDonald&rsquo;s keeps", "$10.74", "FRANCHISED MARGINS &middot; 2025",
         ["That leaves <b>$13.9 billion</b> in franchised margins."],
         "Per the 10-K, franchised margins were about 90% of McDonald&rsquo;s restaurant margin dollars.", Y),
    '<div class=tag>Detour</div>\n<h2>Margin per $100 of restaurant sales, 2025</h2>\n' + cmp([(10.74, "$10.74", True), (14.67, "$14.67", False)],
        ["Franchised", "Company-run"]) + '\n<div class=mini style="margin-top:24px">Company-run: $1.42 billion margin on $9.69 billion in sales. Franchising earns less per $100, but franchised restaurants are about 95% of the system (our math).</div>',
    '<div class=tag>End of the trail</div>\n<div class=hook style="font-size:88px">$100 at the counter.<br><em>McDonald&rsquo;s keeps $10.74.</em></div>\n<div class=cta>Send this to the friend<br>who <em>wants to buy a franchise.</em></div>\n<div class=src>' + DT_FOLLOW + '<br><br>Source: McDonald&rsquo;s Corp. Annual Report on Form 10-K for the year ended Dec. 31, 2025 (SEC filing): franchised sales, revenues from franchised restaurants, franchised occupancy expenses and restaurant margins. Per-$100 figures: our math.</div>',
]
