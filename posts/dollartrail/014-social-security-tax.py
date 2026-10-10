import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "tools"))
from lib import *

ACCOUNT = 'dollartrail'
THEME = 'ledger'
TRAIL = '014'
FOLLOWING = 'your Social Security tax'
SOURCES = ['https://www.ssa.gov/oact/cola/cbb.html',
           'https://www.ssa.gov/oact/ProgData/taxRates.html',
           'https://www.ssa.gov/oact/TR/2026/II_A_highlights.html']

CAPTION = """Your 6.2% Social Security tax isn't set aside in an account with your name on it. In 2025 Social Security paid $1,597 billion in benefits to 70 million people, and it spent more than it took in.

Data: Social Security Administration, Office of the Chief Actuary; 2026 OASDI Trustees Report.

Did you know the tax stops at $184,500 of earnings?

#socialsecurity #taxes #paycheck #retirement #personalfinance #dollartrail"""

SLIDES = [
    '<div class=tag>Trail No. 014</div>\n<div class=hook style="font-size:96px">Your 6.2% Social Security tax isn&rsquo;t saved for you. <em>It pays someone today.</em></div>\n<div class=hook2>Here&rsquo;s the 2025 money trail.</div>\n<div class=mini style="margin-top:40px">Source: Social Security Administration, Office of the Chief Actuary; 2026 OASDI Trustees Report (calendar 2025 data).</div>',
    stack([(91, R, "PAYROLL TAXES"), (5, BL, ""), (4, Y, "")],
          [("Payroll taxes", "$1,323B", R), ("Interest", "$69B", BL), ("Tax on benefits", "$58B", Y)],
          "Social Security (OASDI) income, calendar 2025: $1,449B total. Shares: 91% / 5% / 4%. Parts don't add exactly due to SSA rounding.",
          "Where Social Security&rsquo;s<br>money came from", height=700),
    stop(1, 4, "The rate", "6.2%", "OF WAGES, UP TO $184,500 (2026)",
         ["Your employer pays another 6.2% on top. Earnings above <b>$184,500</b> aren&rsquo;t taxed for Social Security in 2026."],
         "Most an employee can pay in 2026: about $11,439 (our math). Self-employed people pay both halves: 12.4%.", R),
    stop(2, 4, "Where it goes", "$1,597B", "BENEFITS PAID IN 2025",
         ["In December 2025, Social Security paid <b>70 million</b> people. About <b>185 million</b> workers paid the tax that year."],
         "That&rsquo;s roughly 2.6 workers paying in for every person collecting (our math).", Y),
    stop(3, 4, "More out than in", "&minus;$160B", "2025: COST $1,609B VS. INCOME $1,449B",
         ["The gap came out of the trust fund reserves, which fell from <b>$2,721B</b> to <b>$2,561B</b> during 2025."],
         "Reserves are the surplus from past years, held in the trust funds.", BL),
    stop(4, 4, "The clock", "2034", "PROJECTED RESERVE DEPLETION (OASDI)",
         ["After the combined reserves run out, <b>83%</b> of scheduled benefits would still be payable (Trustees&rsquo; intermediate projection)."],
         "The retirement fund (OASI) alone runs out sooner: 2032, then 78% payable.", T),
    '<div class=tag>Detour</div>\n<h2>2025, in and out</h2>\n'
    + cmp([(1449, "$1,449B", False), (1609, "$1,609B", True)], ["Income", "Cost"])
    + note("Cost includes $1,597B in benefit payments."),
    '<div class=tag>End of the trail</div>\n<div class=hook style="font-size:92px">Your 6.2% doesn&rsquo;t wait for you.<br><em>It pays 70 million people now.</em></div>\n<div class=cta>Send this to someone<br>who checks their <em>pay stub.</em></div>\n<div class=src>' + DT_FOLLOW + '<br><br>Source: SSA Office of the Chief Actuary, Contribution and Benefit Base and Tax Rates pages (ssa.gov/oact); 2026 OASDI Trustees Report, Highlights. Figures are calendar 2025 unless noted.</div>',
]
