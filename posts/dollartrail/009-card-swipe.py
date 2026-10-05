import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "tools"))
from lib import *

ACCOUNT = 'dollartrail'
TRAIL = '009'
FOLLOWING = 'a $100 card swipe'
SOURCES = ['https://usa.visa.com/content/dam/VCOM/download/merchants/visa-usa-interchange-reimbursement-fees.pdf',
           'https://usa.visa.com/support/small-business/regulations-fees.html',
           'https://www.federalreserve.gov/paymentsystems/regii-average-interchange-fee.htm']

CAPTION = """When you tap a card for $100, the store pays your card's bank a fee: as little as 26 cents on some debit cards, up to $2.40 on a premium Visa Infinite credit card.

Data: Visa USA Interchange Reimbursement Fees (effective April 18, 2026), CPS/Retail card-present rates; Federal Reserve, Regulation II debit interchange data (2024).

Does knowing this change which card you hand over at a small shop?

#creditcards #debitcard #smallbusiness #swipefees #personalfinance #dollartrail"""

SLIDES = [
    '<div class=tag>Trail No. 009</div>\n<div class=hook>You tap a card for <em>$100.</em></div>\n<div class=hook2>The store pays your bank up to $2.40 of it.</div>\n<div class=mini style="margin-top:60px">Source: Visa USA Interchange Reimbursement Fees, effective April 18, 2026 (in-store retail rates); Federal Reserve Regulation II data, 2024.</div>',
    stack([(2.2, R, ""), (97.8, G, "$97.80")],
          [("Your card's bank", "$2.20", R), ("Left for the store", "$97.80", G), ("Your purchase", "$100", "transparent")],
          "Visa Signature Preferred credit card, in-store retail rate: 2.10% + $0.10. The store's network and processor fees come out of what's left; they're set by contract and not published.",
          "One swipe,<br>one fee", height=640),
    stop(1, 4, "Your card's bank", "$2.20", "INTERCHANGE &middot; 2.10% + 10&cent;",
         ["Visa calls it an interchange reimbursement fee: a transfer from the store's bank to the bank that issued your card, on every sale."],
         "Visa sets the rates and publishes them. This is the in-store rate for a Visa Signature Preferred card.", R),
    '<div class="tag ghost" style="color:#f2b84b;border-color:#f2b84b">Stop 2 of 4</div>\n<h2>Fancier card, bigger fee</h2><div class=amt style="color:#f2b84b">+57%</div><div class=pct>INFINITE VS. REWARDS CARD, SAME $100 SALE</div>\n<div class=taxrow>\n <div class=tx><div class=l>Rewards card</div><div class=n>$1.53</div><div class=d>Visa Traditional Rewards: 1.43% + 10&cent;.</div></div>\n <div class=tx><div class=l>Visa Infinite</div><div class=n>$2.40</div><div class=d>Spend-qualified Infinite: 2.30% + 10&cent;.</div></div>\n</div>\n' + note("The top-tier card costs the store 87 cents more on the same sale."),
    '<div class="tag ghost" style="color:#6aa9ff;border-color:#6aa9ff">Stop 3 of 4</div>\n<h2>Capped debit</h2><div class=amt style="color:#6aa9ff">26&cent;</div><div class=pct>CAPPED VISA DEBIT, $100 SALE</div>\n<div class=taxrow>\n <div class=tx><div class=l>Regulated bank</div><div class=n>$0.26</div><div class=d>0.05% + 21&cent;, the Fed\'s Regulation II cap. +1&cent; for fraud prevention.</div></div>\n <div class=tx><div class=l>Exempt bank</div><div class=n>$0.95</div><div class=d>0.80% + 15&cent;. These banks aren\'t covered by the cap.</div></div>\n</div>\n' + note("Same sale. The fee depends on which bank issued the card."),
    stop(4, 4, "The real averages", "23&cent;", "AVERAGE REGULATED DEBIT FEE, 2024",
         ["Across all networks, the Fed found regulated debit swipes averaged 23&cent; (0.47% of a $48.95 average sale). Exempt banks averaged 51&cent; (1.21% of $42.27)."],
         "Debit from an exempt bank costs stores more than twice as much per swipe on average.", T),
    '<div class=tag>Detour</div>\n<h2>The store\'s fee on a $100 sale</h2>\n' + cmp([(0.26, "26&cent;", False), (0.95, "95&cent;", False), (1.53, "$1.53", False), (2.20, "$2.20", True), (2.40, "$2.40", True)],
        ["Debit (capped)", "Debit (exempt)", "Rewards", "Sig. Pref.", "Infinite"]) + '\n<div class=mini style="margin-top:24px">Visa in-store retail rates, effective April 18, 2026. Interchange only.</div>',
    '<div class=tag>End of the trail</div>\n<div class=hook style="font-size:92px">Same $100 sale.<br><em>26&cent; to $2.40</em>, depending on your card.</div>\n<div class=cta>Send this to the friend<br>with the <em>fanciest card</em> in their wallet.</div>\n<div class=src>' + DT_FOLLOW + '<br><br>Source: Visa USA Interchange Reimbursement Fees, effective April 18, 2026, CPS/Retail card-present rates; Federal Reserve, Regulation II average debit interchange fees, 2024. Rounded to the cent.</div>',
]
