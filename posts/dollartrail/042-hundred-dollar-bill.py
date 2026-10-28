import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "tools"))
from lib import *

ACCOUNT = 'dollartrail'
TRAIL = '042'
FOLLOWING = 'a $100 bill'
SOURCES = ['https://federalreserve.gov/faqs/currency_12771.htm',
           'https://www.federalreserve.gov/foia/files/2025currency.pdf',
           'https://federalreserve.gov/faqs/how-long-is-the-life-span-of-us-paper-money.htm',
           'https://www.federalreserve.gov/paymentsystems/2026_currency_print_order.htm']

CAPTION = """A $100 bill cost 11.3 cents to print in 2025, and a $1 bill cost 4.1 cents, per the Federal Reserve. The $100 lasts about 24 years, so per year in your wallet it costs less to make than a $1.

Data: Federal Reserve Board, currency cost FAQ, 2025 currency budget, note lifespan estimates (May 2025) and 2026 print order. Cost per year: our math.

Do you still carry cash?

#money #cash #federalreserve #economics #personalfinance #dollartrail"""

SLIDES = [
    '<div class=tag>Trail No. 042</div>\n<div class=hook style="font-size:100px">A $100 bill costs <em>11.3&cent;</em> to print.</div>\n<div class=hook2>A $1 bill: 4.1&cent;. Here&rsquo;s the rest of the trail.</div>\n<div class=mini style="margin-top:60px">Source: Federal Reserve Board, currency cost FAQ. 2025 variable printing cost per note (paper, ink, labor, direct overhead).</div>',
    stack([(66, R, "FIXED PRINTING 66%"), (27, Y, "PER-NOTE PRINTING 27%"), (6, BL, "FED BOARD 6%"), (1, G, "")],
          [("Fixed printing", "$688.6M", R), ("Per-note printing", "$283.4M", Y), ("Fed Board costs", "$63.1M", BL), ("BEP support", "$5.0M", G)],
          "2025 currency operating budget: $1,040.0 million. Shares: our math.",
          "The Fed&rsquo;s 2025 cash budget", height=680),
    stop(1, 4, "The $100 note", "11.3&cent;", "TO PRINT ONE, 2025",
         ["That&rsquo;s about <b>0.1%</b> of its face value (our math).", "It&rsquo;s the most expensive note to make."],
         "The cost covers paper, ink, labor and direct overhead.", R),
    stop(2, 4, "The $1 note", "4.1&cent;", "TO PRINT ONE, 2025",
         ["That&rsquo;s <b>4.1%</b> of its face value (our math).", "The $5, $10 and $20 cost <b>6.8&cent;</b> to <b>7.3&cent;</b>."],
         "The 2026 order calls for 1.3 billion to 1.44 billion new $1 notes.", Y),
    '<div class="tag ghost">Stop 3 of 4</div>\n<h2>Cost per year it lasts</h2>\n' + cmp([(0.57, "0.57&cent;", False), (1.22, "1.22&cent;", False), (1.19, "1.19&cent;", False), (0.66, "0.66&cent;", False), (0.47, "0.47&cent;", True)],
        ["$1", "$5", "$10", "$20", "$100"]) + '\n<div class=mini style="margin-top:24px">2025 printing cost &divide; estimated lifespan (Fed, May 2025): $1 7.2 years, $5 5.8, $10 5.7, $20 11.1, $100 24.0 (our math).</div>',
    stop(4, 4, "The order", "3.8B&ndash;5.1B", "NEW NOTES ORDERED FOR 2026",
         ["Up to <b>876.8 million</b> of them are $100s, about twice as many as $5s.", "Zero <b>$2</b> notes are on the order."],
         "The 2025 order was 4.7 billion notes, down from 6.3 billion in 2024.", BL),
    '<div class=tag>Detour</div>\n<h2>How long cash lasts</h2>\n<div class=taxrow><div class=tx><div class=l>$100 note</div><div class=n>24.0</div><div class=d>Years. Longest-lived</div></div><div class=tx><div class=l>$10 note</div><div class=n>5.7</div><div class=d>Years. Shortest-lived</div></div></div>\n' + note("Fed estimates as of May 2025. The $1 lasts about 7.2 years."),
    '<div class=tag>End of the trail</div>\n<div class=hook style="font-size:86px">$100 of value.<br><em>11.3&cent; of paper, ink and work.</em></div>\n<div class=cta>Send this to the friend<br>who <em>still pays in cash.</em></div>\n<div class=src>' + DT_FOLLOW + '<br><br>Source: Federal Reserve Board: currency cost FAQ (2025 costs), 2025 Currency Budget, note lifespan FAQ (May 2025), CY 2026 print order. Shares, face-value percents and cost per year: our math.</div>',
]
