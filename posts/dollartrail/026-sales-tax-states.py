import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "tools"))
from lib import *

ACCOUNT = 'dollartrail'
THEME = 'ledger'
TRAIL = '026'
FOLLOWING = 'state sales tax on $100'
SOURCES = ['https://www.cdtfa.ca.gov/taxes-and-fees/sales-use-tax-rates.htm',
           'https://www.in.gov/dor/business-tax/sales-tax/',
           'https://www.dor.ms.gov/business/sales-use-tax/sales-tax-rates',
           'https://tax.ri.gov/tax-sections/sales-excise-taxes/sales-use-tax',
           'https://www.tn.gov/revenue/taxes/sales-and-use-tax.html',
           'https://www.nj.gov/treasury/taxation/su_over.shtml',
           'https://tax.colorado.gov/marijuana-sales-tax',
           'https://tax.colorado.gov/sales-tax-guide',
           'https://tax.colorado.gov/DR1002',
           'https://www.commerce.alaska.gov/web/dcra/OfficeoftheStateAssessor/AlaskaSalesTaxInformation.aspx',
           'https://revenue.delaware.gov/business-tax-forms/doing-business-in-delaware/step-4-gross-receipts-taxes/',
           'https://revenue.mt.gov/taxes/general-sales-tax',
           'https://www.revenue.nh.gov/resource-center/frequently-asked-questions/general-information',
           'https://www.oregon.gov/dor/programs/businesses/pages/sales-tax.aspx']

SRC = "Source: official state tax agency pages, checked Oct. 2026: California CDTFA (rates effective July 1, 2024); Indiana, Mississippi, Tennessee, Montana and Oregon Departments of Revenue; Rhode Island and New Jersey Divisions of Taxation; Colorado Department of Revenue; Alaska Office of the State Assessor; Delaware Division of Revenue; New Hampshire Department of Revenue Administration. State base rates only. Dollar amounts: our math."

CAPTION = """On a $100 taxable purchase, the state sales tax runs from $7.25 in California to $0 in Alaska, Delaware, Montana, New Hampshire and Oregon, among the 12 states we checked. These are statewide base rates; local taxes can add more.

Data: official state tax agency pages for CA, IN, MS, RI, TN, NJ, CO, AK, DE, MT, NH and OR, checked Oct. 2026. Dollar amounts: our math.

What's the sales tax where you live?

#salestax #taxes #shopping #personalfinance #money #dollartrail"""

SLIDES = [
    '<div class=tag>Trail No. 026</div>\n<div class=hook style="font-size:104px">Same $100 cart. State sales tax: <em>$7.25</em>&hellip; or $0.</div>\n<div class=hook2>12 states we checked. Statewide base rates only.</div>\n<div class=mini style="margin-top:60px">Source: official state tax agency pages for CA, IN, MS, RI, TN, NJ, CO, AK, DE, MT, NH and OR, checked Oct. 2026. Not a 50-state ranking. Local taxes not included. Dollar amounts: our math.</div>',
    '<div class=tag>The trail map</div>\n<h2>State tax on<br>a $100 cart</h2>\n' + cmp([(7.25, "$7.25", True), (7.00, "$7.00", False), (6.625, "$6.63", False), (2.90, "$2.90", False), (0.0, "$0", False)],
        ["CA", "7% club", "NJ", "CO", "Zero five"]) + '\n<div class=mini style="margin-top:24px">Statewide base rate applied to a $100 taxable purchase (our math). NJ&rsquo;s $6.625 rounded to $6.63. 7% club: IN, MS, RI, TN. Zero five: AK, DE, MT, NH, OR.</div>',
    stop(1, 4, "California", "7.25%", "STATEWIDE RATE, EFFECTIVE JULY 1, 2024",
         ["CDTFA: &ldquo;In most areas of California, local jurisdictions have added district taxes that increase the tax owed by a seller.&rdquo;"],
         "Those district taxes &ldquo;range from 0.10% to 1.50%.&rdquo; The highest state rate we checked.", R),
    stop(2, 4, "The 7% club", "7%", "INDIANA, MISSISSIPPI, RHODE ISLAND, TENNESSEE",
         ["Four states, the same <b>$7.00</b> on a $100 taxable cart (our math), per each state&rsquo;s revenue department, Oct. 2026."],
         "Mississippi lists a 5% rate for groceries. Tennessee: &ldquo;The local tax rate varies by county and/or city.&rdquo;", Y),
    stop(3, 4, "New Jersey", "6.625%", "ON TAXABLE SALES SINCE JAN. 1, 2018",
         ["That&rsquo;s <b>$6.63</b> on a $100 cart, rounded (our math)."],
         "Below California and the 7% club. Above Colorado.", BL),
    stop(4, 4, "Colorado", "2.9%", "TANGIBLE PERSONAL PROPERTY, PER COLORADO DEPT. OF REVENUE, OCT. 2026",
         ["The lowest rate above zero that we checked: <b>$2.90</b> on $100, or <b>$4.35</b> less than California (our math)."],
         "Colorado: &ldquo;The total tax rate for any jurisdiction must be computed by adding all taxes applicable to that jurisdiction.&rdquo;", P),
    '<div class=tag>Detour</div>\n<h2>The zero five</h2>\n<p><b>Alaska:</b> the state does not levy a sales tax, but &ldquo;several local municipalities&rdquo; do.</p>\n<p><b>Delaware:</b> no state or local sales tax, but a gross receipts tax on sellers.</p>\n<p><b>Montana:</b> &ldquo;does not have a general sales tax.&rdquo;</p>\n<p><b>New Hampshire:</b> &ldquo;no general sales tax on goods purchased in New Hampshire.&rdquo;</p>\n<p><b>Oregon:</b> no general sales tax, but a use tax on new vehicles bought out of state.</p>',
    '<div class=tag>End of the trail</div>\n<div class=hook style="font-size:92px">$7.25 to $0 on the same $100 cart.<br><em>Local taxes can add more.</em></div>\n<div class=cta>Send this to the friend<br>who <em>shops across state lines.</em></div>\n<div class=src>' + DT_FOLLOW + '<br><br>' + SRC + '</div>',
]
