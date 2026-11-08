import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "tools"))
from lib import *

ACCOUNT = 'dollartrail'
TRAIL = '060'
FOLLOWING = '$100 at Costco'
SOURCES = ['https://www.sec.gov/Archives/edgar/data/0000909832/000090983226000093/cost-20260830.htm']

CAPTION = """Spend $100 at Costco and, going by its latest annual report, $88.91 pays for the goods, $9.15 runs the warehouses and $1.94 is left over. Membership fees add $5.91 billion, about as much as the aisles leave over.

Data: Costco Wholesale Form 10-K for fiscal 2026, year ended Aug. 30, 2026 (SEC filing). Company-wide shares of net sales applied to a $100 example cart; our math.

Did you think Costco made its money on the hot dogs or the card?

#costco #shopping #groceries #personalfinance #money #dollartrail"""

SLIDES = [
    '<div class=tag>Trail No. 060</div>\n<div class=hook style="font-size:110px">$100 at Costco. <em>$1.94 is left.</em></div>\n<div class=hook2>Half its operating profit is the card in your wallet.</div>\n<div class=mini style="margin-top:60px">Source: Costco Wholesale, Form 10-K for fiscal 2026, year ended Aug. 30, 2026 (SEC filing). Each slice = its share of Costco&rsquo;s $297.2 billion net sales, applied to a $100 example cart (our math).</div>',
    stack([(88.91, R, "88.91%"), (9.15, Y, "9.15%"), (1.94, T, "")],
          [("The goods", "$88.91", R), ("Warehouses &amp; staff", "$9.15", Y), ("Left over", "$1.94", T), ("Total", "$100.00", "transparent")],
          "Costco&rsquo;s fiscal 2026 merchandise costs and operating expenses as a share of net sales, applied to $100. Rounded (our math).",
          "Where $100<br>goes.", height=700),
    stop(1, 5, "The goods", "$88.91", "MERCHANDISE COSTS &middot; 88.91% OF NET SALES",
         ["Costco paid <b>$264.3 billion</b> for what it sold, on <b>$297.2 billion</b> of sales."],
         "Its gross margin was 11.09% of net sales, down from 11.12% the year before.", R),
    stop(2, 5, "Warehouses and staff", "$9.15", "SELLING, GENERAL AND ADMINISTRATIVE &middot; 9.15%",
         ["Running the warehouses and the company cost <b>$27.2 billion</b>, 9.15% of net sales, down from 9.25%."],
         "Costco ran 939 warehouses worldwide at the end of the year, 647 of them in the U.S. and Puerto Rico.", Y),
    stop(3, 5, "Left from your cart", "$1.94", "NET SALES MINUS GOODS AND OPERATING COSTS (OUR MATH)",
         ["Across all sales, that leaves <b>$5.78 billion</b> not counting membership fees, interest or taxes."],
         "That&rsquo;s under two dollars on a $100 trip.", T),
    stop(4, 5, "The card", "$65", "U.S. ANNUAL MEMBERSHIP FEE",
         ["Membership fees brought in <b>$5.91 billion</b>, up 11%. Costco had <b>84.1 million</b> paid members."],
         "92.3% of members in the U.S. and Canada renewed. Fees went up in the U.S. and Canada on Sept. 1, 2024.", BL),
    stop(5, 5, "Operating profit", "$11.69B", "OPERATING INCOME &middot; FISCAL 2026",
         ["That&rsquo;s <b>$5.78 billion</b> from the aisles plus <b>$5.91 billion</b> in membership fees.", "About half of it came from the card (our math)."],
         "After interest and a 24.7% tax rate, net income was $9.23 billion, up 14%.", P),
    '<div class=tag>End of the trail</div>\n<div class=hook style="font-size:92px">Your cart: $1.94.<br><em>The card: half the operating profit.</em></div>\n<div class=cta>Send this to your<br><em>Costco run</em> partner.</div>\n<div class=src>' + DT_FOLLOW + '<br><br>Source: Costco Wholesale Corporation, Form 10-K for the fiscal year ended Aug. 30, 2026 (SEC filing), consolidated statements of income, MD&amp;A and Item 1. Company-wide shares applied to a $100 example cart; per-$100 figures and the fee share of operating income: our math.</div>',
]
