import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "tools"))
from lib import *

ACCOUNT = 'dollartrail'
THEME = 'receipt'
TRAIL = '025'
FOLLOWING = '5 prices, one recap'
SOURCES = ['https://www.sec.gov/Archives/edgar/data/829224/000082922425000074/sbux-09282025xexhibit991.htm',
           'https://usa.visa.com/content/dam/VCOM/download/merchants/visa-usa-interchange-reimbursement-fees.pdf',
           'https://www.federalreserve.gov/paymentsystems/regii-average-interchange-fee.htm',
           'https://loudandclear.byspotify.com/',
           'https://loudandclear.byspotify.com/takeaways/',
           'https://loudandclear.byspotify.com/process/',
           'https://loudandclear.byspotify.com/payouts/',
           'https://www.cbo.gov/publication/61985',
           'https://www.cbo.gov/system/files/2026-10/61985-MBR.pdf',
           'https://www.faa.gov/about/budget/aatf/Current-Aviation-Excise-Tax-Structure-and-Rates-2026.pdf',
           'https://www.irs.gov/pub/irs-pdf/p510.pdf',
           'https://www.tsa.gov/for-industry/security-fees',
           'https://www.faa.gov/airports/pfc',
           'https://www.bts.gov/newsroom/second-quarter-2026-average-air-fare-increased-20-first-quarter-2026']

SRC_ALL = "Sources: Trail 006: Starbucks Corp., fiscal 2025 results (SEC Form 8-K, Oct. 2025). Trail 009: Visa USA Interchange Reimbursement Fees, effective April 18, 2026; Federal Reserve, Regulation II, 2024. Trail 012: Spotify, Loud &amp; Clear, 2025 royalty data. Trail 017: CBO, Monthly Budget Review: September 2026, preliminary. Trail 019: FAA; IRS Publication 510; TSA; BTS, 2Q 2026. Breakdowns and shares marked &ldquo;our math&rdquo; are our own arithmetic."

CAPTION = """Five trails, one recap: a $5 latte, a $100 card swipe, a Spotify stream, the interest on the national debt and a $312 plane ticket. The cut that surprised us most: on the same $100 sale, the store pays your card's bank 26 cents to $2.40, depending on your card.

Data: Starbucks fiscal 2025 results (SEC Form 8-K); Visa USA Interchange Reimbursement Fees (April 18, 2026) and Federal Reserve Regulation II data; Spotify Loud & Clear (2025); CBO Monthly Budget Review, September 2026 (preliminary); FAA, IRS, TSA and BTS (2026). Figures marked "our math" are our arithmetic.

Which trail surprised you most?

#money #personalfinance #creditcards #nationaldebt #followthemoney #dollartrail"""

def tstop(k, trail, title, amt, sub, para, finding, src, color, amt_px=150):
    """A recap stop: like stop(), with the trail number in the tag and a smaller amount."""
    return (f'<div class="tag ghost" style="color:{color};border-color:{color}">Trail No. {trail} &middot; {k} of 5</div>\n'
            f'<h2 style="font-size:80px">{title}</h2><div class=amt style="color:{color};font-size:{amt_px}px">{amt}</div>'
            f'<div class=pct style="margin-bottom:30px">{sub}</div><p>{para}</p>{note(finding)}'
            f'<div class=mini style="margin-top:16px">{src}</div>')

SLIDES = [
    '<div class=tag>Trail No. 025</div>\n<div class=hook style="font-size:108px">5 prices we followed. <em>One cut we didn&rsquo;t see coming.</em></div>\n<div class=hook2>A recap of five trails.</div>\n<div class=mini style="margin-top:60px">Sources: each trail&rsquo;s own source and period, printed on its slide. Starbucks (SEC), Visa and the Federal Reserve, Spotify, CBO, and FAA, IRS, TSA and BTS.</div>',
    tstop(1, "006", "A $5 latte", "$2.29", "RUNS THE STORE",
          "<b>$1.57</b> buys the coffee, milk and cup. About <b>25&cent;</b> is profit.",
          "The coffee isn&rsquo;t the big cost. The caf&eacute; is.",
          "Example drink: shares of Starbucks&rsquo;s $37.2B fiscal 2025 revenue. Real prices vary by store and size. Source: Starbucks, fiscal 2025 results, 52 weeks ended Sept. 28, 2025 (SEC 8-K).", R),
    tstop(2, "009", "A $100 card swipe", "26&cent; to $2.40", "PAID BY THE STORE TO YOUR CARD&rsquo;S BANK",
          "Capped debit: <b>$0.26</b>. Premium Visa Infinite: <b>$2.40</b>.",
          "Interchange only. Network and processor fees are set by contract and not published.",
          "Source: Visa USA Interchange Reimbursement Fees, eff. April 18, 2026; Federal Reserve, Regulation II average debit interchange fees, 2024. CPS/Retail card-present rates, rounded to the cent.", Y, 130),
    tstop(3, "012", "One Spotify stream", "No set price", "A SHARE OF $11B+ PAID TO THE MUSIC INDUSTRY IN 2025",
          "Spotify: &ldquo;If your music accounts for 1% of all streams, you get roughly 1% of the royalty pool.&rdquo;",
          "Artists who accounted for 1 in every 1 million streams on Spotify generated over $11,000 on average in 2025.",
          "Source: Spotify, Loud &amp; Clear, 2025 royalty data, as reported by Spotify.", BL, 130),
    tstop(4, "017", "Interest on the debt", "$1.14 trillion", "NET INTEREST, FISCAL 2026 (PRELIMINARY)",
          "More than Medicare (<b>$1,069B</b>). More than defense (<b>$916B</b>).",
          "About 21 cents of each revenue dollar went to interest (our math).",
          "Source: CBO, Monthly Budget Review: September 2026 (Oct. 8, 2026). Fiscal year Oct. 2025 to Sept. 2026.", P, 130),
    tstop(5, "019", "A $312 plane ticket", "About $36", "TAXES AND FEES, ILLUSTRATIVE ONE-WAY",
          "Ticket tax <b>$20.69</b>, segment tax <b>$5.30</b>, TSA fee <b>$5.60</b>, airport fee <b>$4.50</b> (PFC cap).",
          "$312 = average one-way domestic fare, 2Q 2026 (BTS). Illustrative breakdown: our math.",
          "Source: FAA; IRS Pub. 510; TSA; FAA PFC program; BTS. One flight segment, 2026 rates.", T),
    '<div class=tag>The most surprising cut</div>\n<h2>The store&rsquo;s fee on the same $100 sale</h2>\n' + cmp([(0.26, "26&cent;", False), (0.95, "95&cent;", False), (1.53, "$1.53", False), (2.20, "$2.20", True), (2.40, "$2.40", True)],
        ["Debit (capped)", "Debit (exempt)", "Rewards", "Sig. Pref.", "Infinite"]) + '\n<div class=mini style="margin-top:24px">Trail No. 009. Visa in-store retail rates, effective April 18, 2026; Federal Reserve, Regulation II. Interchange only. Rounded to the cent.</div>',
    '<div class=tag>End of the trail</div>\n<div class=hook style="font-size:90px">Same $100 sale.<br><em>26&cent; to $2.40</em>, depending on your card.</div>\n<div class=cta>Send this to the friend<br>who <em>missed a trail.</em></div>\n<div class=src>' + DT_FOLLOW + '<br><br>' + SRC_ALL + '</div>',
]
