import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "tools"))
from lib import *

ACCOUNT = 'dollartrail'
THEME = 'receipt'
TRAIL = '055'
FOLLOWING = "America's food bill"
SOURCES = ['https://www.ers.usda.gov/data-products/charts-of-note/114212', 'https://ers.usda.gov/data-products/chart-gallery/76967']

CAPTION = """America spent $2.51 trillion on food in 2025, and 56.3% of it went to food away from home, per USDA. Consumers spent 9.7% of their take-home income on food: 4.9% eating out and 4.8% on groceries.

Data: USDA Economic Research Service, Food Expenditure Series (charts published June 2026). Per-$100 and growth figures: our math.

Do you spend more on groceries or eating out?

#foodprices #groceries #restaurants #personalfinance #money #dollartrail"""

SLIDES = [
    '<div class=tag>Trail No. 055</div>\n<div class=hook style="font-size:100px">America&rsquo;s food bill: <em>$2.51 trillion.</em></div>\n<div class=hook2>Spent on food in 2025. More than half went to food away from home.</div>\n<div class=mini style="margin-top:60px">Source: USDA Economic Research Service (ERS), Food Expenditure Series, charts published June 2026. Spending by consumers, businesses and government. Per-$100, at-home share and growth figures: our math.</div>',
    stack([(56.3, R, "AWAY FROM HOME: $1.41T"), (43.7, G, "AT HOME: $1.10T")],
          [("Away from home", "56.3%", R), ("At home", "43.7%", G)],
          "USDA ERS, 2025. Away-from-home share from ERS; at-home share is the rest (our math). Includes spending by consumers, businesses and government.",
          "Where the $2.51 trillion went", height=640),
    stop(1, 4, "Take-home pay", "$9.70", "PER $100 OF DISPOSABLE INCOME SPENT ON FOOD, 2025",
         ["ERS: on average, consumers spent <b>9.7%</b> of disposable personal income on food.", "Disposable income is what&rsquo;s left after taxes."],
         "Down from 10.4% in 1997, per ERS.", Y),
    stop(2, 4, "Eating out", "$4.90", "PER $100 OF INCOME, FOOD AWAY FROM HOME, 2025",
         ["Groceries took <b>$4.80</b>.", "Eating out edged ahead of the grocery bill."],
         "In 1997 it was $4.30 out and $6.10 at home.", R),
    stop(3, 4, "The long run", "+72%", "GROWTH IN FOOD-AWAY-FROM-HOME SPENDING, 1997 TO 2025, INFLATION-ADJUSTED (OUR MATH)",
         ["From <b>$818 billion</b> to <b>$1.41 trillion</b> in 2025 dollars.", "Food at home grew about <b>49%</b>: $738 billion to $1.10 trillion."],
         "Both grew, but eating out grew faster.", BL),
    stop(4, 4, "Last year", "$2.51T", "TOTAL FOOD SPENDING IN 2025, UP FROM $2.49T IN 2024 (INFLATION-ADJUSTED)",
         ["Both measured in <b>2025 dollars</b>.", "ERS: spending rose for both food at home and away from home."],
         "That&rsquo;s after removing the effect of price changes.", P),
    '<div class=tag>Detour</div>\n<h2>Food per $100 of take-home pay</h2>\n' + cmp([(6.1, "$6.10", False), (4.3, "$4.30", False), (4.8, "$4.80", False), (4.9, "$4.90", True)],
        ["Home 1997", "Out 1997", "Home 2025", "Out 2025"]) + '\n<div class=mini style="margin-top:24px">USDA ERS: share of disposable personal income spent on food at home and away from home, 1997 and 2025, shown per $100.</div>',
    '<div class=tag>End of the trail</div>\n<div class=hook style="font-size:86px">$2.51 trillion on food.<br><em>56.3% away from home.</em></div>\n<div class=cta>Send this to the friend<br>who <em>orders takeout again.</em></div>\n<div class=src>' + DT_FOLLOW + '<br><br>Source: USDA Economic Research Service, Food Expenditure Series: &ldquo;Total U.S. food spending reached $2.51 trillion in 2025&rdquo; (June 11, 2026) and &ldquo;U.S. consumers spent 9.7 percent of their disposable personal income on food in 2025&rdquo; (June 1, 2026), ers.usda.gov. Per-$100, at-home share and growth figures: our math.</div>',
]
