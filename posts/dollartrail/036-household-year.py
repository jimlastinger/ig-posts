import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "tools"))
from lib import *

ACCOUNT = 'dollartrail'
TRAIL = '036'
FOLLOWING = 'a year of household spending'
SOURCES = ['https://www.bls.gov/news.release/pdf/cesan.pdf',
           'https://www.bls.gov/opub/ted/2026/housing-and-transportation-accounted-for-50-percent-of-household-spending-in-2024.htm',
           'https://www.bls.gov/cex/']

CAPTION = """The average U.S. household spent $78,535 in 2024, per BLS. Housing took a third of it, $26,266, and housing plus transportation took half.

Data: U.S. Bureau of Labor Statistics, Consumer Expenditures in 2024 (Dec. 19, 2025, the latest annual release). Some figures our math.

Which line is biggest in your budget?

#budget #personalfinance #housing #costofliving #money #dollartrail"""

SLIDES = [
    '<div class=tag>Trail No. 036</div>\n<div class=hook style="font-size:100px">The average household spent <em>$78,535</em> in 2024.</div>\n<div class=hook2>Where it went.</div>\n<div class=mini style="margin-top:60px">Source: U.S. Bureau of Labor Statistics (BLS), Consumer Expenditures in 2024, released Dec. 19, 2025 (latest annual data). Average for all consumer units.</div>',
    stack([(33, R, "HOUSING 33%"), (17, Y, "TRANSPORT 17%"), (13, T, "FOOD 13%"), (13, BL, "INS., PENSIONS 13%"), (8, P, "HEALTH 8%"), (16, G, "EVERYTHING ELSE 16%")],
          [("Housing", "$26,266", R), ("Transportation", "$13,318", Y), ("Food", "$10,169", T), ("Insurance, pensions", "$9,797", BL), ("Healthcare", "$6,197", P), ("Everything else", "$12,788", G)],
          "BLS, 2024. Shares rounded and &ldquo;everything else&rdquo; total: our math.",
          "Where $78,535 lands", height=720),
    stop(1, 4, "Housing", "$26,266", "33.4% OF SPENDING",
         ["That&rsquo;s <b>$2,189 a month</b>, the biggest line by far."],
         "Housing and transportation together: half of all spending.", R),
    stop(2, 4, "Transportation", "$13,318", "17.0% OF SPENDING",
         ["About <b>$1,110 a month</b> to get around."],
         "Second only to housing.", Y),
    stop(3, 4, "Food", "$10,169", "12.9% OF SPENDING",
         ["<b>$6,224</b> at home and <b>$3,945</b> eating out, or about <b>$847 a month</b> in all."],
         "Eating out was 39% of the food budget (our math).", T),
    stop(4, 4, "Insurance and pensions", "$9,797", "12.5% OF SPENDING",
         ["BLS counts <b>personal insurance and pensions</b> as spending. Healthcare is separate: <b>$6,197</b>, or 7.9%."],
         "Entertainment: $3,609. Apparel and services: $2,001.", BL),
    '<div class=tag>Detour</div>\n<h2>The small lines</h2>\n<div class=taxrow><div class=tx><div class=l>Cash contributions</div><div class=n>$2,292</div><div class=d>2.9%</div></div><div class=tx><div class=l>Education</div><div class=n>$1,569</div><div class=d>2.0%</div></div></div>\n<div class=taxrow><div class=tx><div class=l>Alcohol</div><div class=n>$643</div><div class=d>0.8%</div></div><div class=tx><div class=l>Reading</div><div class=n>$125</div><div class=d>0.2%</div></div></div>' + note("Average income before taxes: $104,207."),
    '<div class=tag>End of the trail</div>\n<div class=hook style="font-size:88px">$78,535 a year.<br><em>Half goes to a roof and a ride.</em></div>\n<div class=cta>Send this to the friend<br>who <em>is making a budget.</em></div>\n<div class=src>' + DT_FOLLOW + '<br><br>Source: U.S. Bureau of Labor Statistics, Consumer Expenditures in 2024 (Dec. 19, 2025); The Economics Daily, Feb. 12, 2026. Monthly figures from BLS. Rounded shares and totals: our math.</div>',
]
