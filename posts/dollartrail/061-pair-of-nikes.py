import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "tools"))
from lib import *

ACCOUNT = 'dollartrail'
THEME = 'receipt'
TRAIL = '061'
FOLLOWING = '$100 of Nike sales'
SOURCES = ['https://www.sec.gov/Archives/edgar/data/320187/000032018726000076/q4fy26exhibit991er.htm', 'https://www.sec.gov/Archives/edgar/data/320187/000032018726000088/R1.htm']

CAPTION = """For every $100 Nike took in last fiscal year, $57.09 went to the cost of the goods it sold, $10.25 to marketing and $24.48 to running the company. Nike kept $6.70.

Data: NIKE, Inc. fiscal 2026 results, year ended May 31, 2026 (SEC filing). Company-wide shares of revenue applied to a $100 example; our math.

Would you have guessed marketing gets more than profit?

#nike #sneakers #shoes #personalfinance #money #dollartrail"""

SLIDES = [
    '<div class=tag>Trail No. 061</div>\n<div class=hook style="font-size:100px">Every $100 Nike takes in: <em>$6.70 is profit.</em></div>\n<div class=hook2>Marketing gets $10.25 of it.</div>\n<div class=mini style="margin-top:60px">Source: NIKE, Inc., fiscal 2026 results, year ended May 31, 2026 (SEC filing). Each slice = its share of Nike&rsquo;s $46.4 billion revenue, applied to $100 (our math).</div>',
    stack([(57.09, R, "57.09%"), (10.25, Y, "10.25%"), (24.48, BL, "24.48%"), (8.18, T, "8.18%")],
          [("Making the goods", "$57.09", R), ("Marketing", "$10.25", Y), ("Overhead", "$24.48", BL), ("Left over", "$8.18", T), ("Total", "$100.00", "transparent")],
          "Nike&rsquo;s fiscal 2026 cost of sales, demand creation and operating overhead as a share of revenue, applied to $100. Rounded (our math).",
          "Where $100<br>goes.", height=700),
    stop(1, 5, "Making the goods", "$57.09", "COST OF SALES &middot; FISCAL 2026",
         ["The goods Nike sold cost it <b>$26.5 billion</b>, on <b>$46.4 billion</b> of revenue."],
         "Gross margin was 42.9%, up 0.2 points from the year before.", R),
    stop(2, 5, "Marketing", "$10.25", "DEMAND CREATION EXPENSE",
         ["Nike calls its marketing &ldquo;demand creation.&rdquo; It cost <b>$4.75 billion</b>."],
         "That&rsquo;s about four times Converse&rsquo;s whole revenue of $1.17 billion (our math).", Y),
    stop(3, 5, "Overhead", "$24.48", "OPERATING OVERHEAD EXPENSE",
         ["Everything else it takes to run Nike cost <b>$11.36 billion</b>, a little less than the year before."],
         "Marketing and overhead together came to 34.7% of revenue, the same share as the year before.", BL),
    stop(4, 5, "Left over", "$8.18", "REVENUE MINUS THOSE THREE COSTS (OUR MATH)",
         ["That leaves <b>$3.80 billion</b> before interest and taxes."],
         "Interest and other income added about $0.10 billion, for $3.90 billion before taxes.", T),
    stop(5, 5, "What Nike kept", "$6.70", "NET INCOME &middot; FISCAL 2026",
         ["After <b>$792 million</b> in income tax, a 20.3% rate, Nike kept <b>$3.11 billion</b>."],
         "Revenue was flat. Net income fell 3%.", P),
    '<div class=tag>End of the trail</div>\n<div class=hook style="font-size:92px">Profit: $6.70.<br><em>Marketing: $10.25.</em></div>\n<div class=cta>Send this to the friend<br>with the <em>sneaker wall.</em></div>\n<div class=src>' + DT_FOLLOW + '<br><br>Source: NIKE, Inc., fiscal 2026 fourth quarter and full year results, released June 30, 2026 (Exhibit 99.1, SEC filing), consolidated statements of income for the year ended May 31, 2026. Company-wide shares applied to a $100 example; per-$100 figures: our math.</div>',
]
