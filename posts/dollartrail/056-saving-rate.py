import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "tools"))
from lib import *

ACCOUNT = 'dollartrail'
THEME = 'ledger'
TRAIL = '056'
FOLLOWING = 'a take-home dollar'
SOURCES = ['https://bea.gov/news/2026/personal-income-and-outlays-september-2026', 'https://www.bea.gov/sites/default/files/2026-10/pi0926.pdf']

CAPTION = """In September, Americans saved 3.8% of their after-tax income, or $3.80 of every $100, per BEA. Consumer spending rose $113.1 billion while after-tax income rose $52.7 billion (seasonally adjusted annual rates).

Data: U.S. Bureau of Economic Analysis, Personal Income and Outlays, September 2026 (released Oct. 29, 2026). Per-$100 figures: our math.

How much of your paycheck did you save last month?

#saving #personalfinance #inflation #economy #money #dollartrail"""

SLIDES = [
    '<div class=tag>Trail No. 056</div>\n<div class=hook style="font-size:100px">Of every $100 Americans took home, <em>$3.80 got saved.</em></div>\n<div class=hook2>The U.S. personal saving rate in September 2026.</div>\n<div class=mini style="margin-top:60px">Source: U.S. Bureau of Economic Analysis (BEA), Personal Income and Outlays, September 2026, released Oct. 29, 2026. Per-$100 figures: our math.</div>',
    stack([(96.2, G, "SPENT (OUTLAYS): $96.20"), (3.8, R, "")],
          [("Spent", "$96.20", G), ("Saved", "$3.80", R)],
          "Per $100 of disposable (after-tax) personal income, September 2026. Saving is what&rsquo;s left after outlays: spending, interest and transfers (our math from BEA&rsquo;s 3.8% saving rate).",
          "Where $100 of take-home pay went", height=640),
    stop(1, 4, "Saved", "$911.1B", "PERSONAL SAVING, SEPTEMBER 2026, SEASONALLY ADJUSTED ANNUAL RATE",
         ["That&rsquo;s <b>3.8%</b> of disposable personal income.", "Disposable income is personal income minus personal taxes."],
         "BEA&rsquo;s monthly figures are stated at annual rates.", R),
    stop(2, 4, "Outlays vs. income", "+$113.0B", "INCREASE IN PERSONAL OUTLAYS (SPENDING, INTEREST, TRANSFERS) IN SEPTEMBER, ANNUAL RATE",
         ["After-tax income rose <b>$52.7 billion</b>.", "Outlays grew a bit over <b>twice</b> as much (our math)."],
         "When spending outruns income, saving shrinks.", Y),
    stop(3, 4, "Where it went", "$78.1B", "MORE CONSUMER SPENDING ON SERVICES IN SEPTEMBER, ANNUAL RATE",
         ["Spending on goods rose <b>$35.1 billion</b>.", "Services were about <b>69%</b> of the rise in consumer spending (our math)."],
         "Consumer spending rose $113.1 billion in all.", BL),
    stop(4, 4, "Prices", "+3.6%", "PCE PRICE INDEX, SEPTEMBER 2026 VS. A YEAR AGO",
         ["Without food and energy: <b>+3.1%</b>.", "After inflation, take-home income <b>fell 0.3%</b> from August."],
         "Real consumer spending was nearly flat: less than 0.1% higher.", P),
    '<div class=tag>Detour</div>\n<h2>September increases, billions</h2>\n' + cmp([(113.1, "$113.1B", True), (54.5, "$54.5B", False), (52.7, "$52.7B", False)],
        ["Spending", "Income", "After-tax"]) + '\n<div class=mini style="margin-top:24px">BEA, September 2026: change from August in personal consumption expenditures, personal income and disposable personal income, seasonally adjusted annual rates.</div>',
    '<div class=tag>End of the trail</div>\n<div class=hook style="font-size:86px">$100 taken home.<br><em>$3.80 saved.</em></div>\n<div class=cta>Send this to the friend<br>who&rsquo;s <em>building an emergency fund.</em></div>\n<div class=src>' + DT_FOLLOW + '<br><br>Source: U.S. Bureau of Economic Analysis, Personal Income and Outlays, September 2026 (BEA 26-46, released Oct. 29, 2026), bea.gov. Seasonally adjusted annual rates. Per-$100 and share figures: our math.</div>',
]
