import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "tools"))
from lib import *

ACCOUNT = 'dollartrail'
TRAIL = '057'
FOLLOWING = 'one hour of your work'
SOURCES = ['https://www.bls.gov/news.release/ecec.nr0.htm', 'https://www.bls.gov/news.release/archives/ecec_09092026.htm', 'https://www.bls.gov/opub/ted/2026/compensation-costs-for-private-industry-workers-averaged-46-89-per-hour-worked-in-june-2026.htm']

CAPTION = """Private employers spent an average of $46.89 for every hour worked in June 2026, per BLS. $32.82 of that was wages and salaries; the other $14.07 (30%) went to benefits like paid leave, insurance and retirement.

Data: U.S. Bureau of Labor Statistics, Employer Costs for Employee Compensation, June 2026 (released Sept. 9, 2026). Per-$100 figures: our math.

Did you know what your benefits cost per hour?

#paycheck #benefits #salary #personalfinance #money #dollartrail"""

SLIDES = [
    '<div class=tag>Trail No. 057</div>\n<div class=hook style="font-size:100px">The average private employer pays $46.89 per hour worked. <em>$32.82 is wages.</em></div>\n<div class=hook2>Where the rest of that hour&rsquo;s cost goes.</div>\n<div class=mini style="margin-top:60px">Source: U.S. Bureau of Labor Statistics (BLS), Employer Costs for Employee Compensation, June 2026, private industry average per hour worked. Released Sept. 9, 2026.</div>',
    stack([(70, G, "WAGES &amp; SALARIES: $70"), (8, R, "INSURANCE"), (8, Y, "PAID LEAVE"), (7, BL, "REQUIRED"), (4, P, ""), (3, T, "")],
          [("Wages", "$70", G), ("Insurance", "$8", R), ("Paid leave", "$8", Y), ("Required by law", "$7", BL), ("Supplemental", "$4", P), ("Retirement", "$3", T)],
          "Per $100 of employer compensation cost, private industry, June 2026. Rounded to whole dollars from BLS figures (our math).",
          "Where $100 of your pay package goes", height=640),
    stop(1, 4, "Insurance", "$3.69", "PER HOUR WORKED, PRIVATE INDUSTRY, JUNE 2026",
         ["That&rsquo;s <b>7.9%</b> of total compensation.", "Health insurance alone: <b>$3.48</b> an hour (7.4%)."],
         "The biggest benefit category per hour (our math).", R),
    stop(2, 4, "Paid leave", "$3.54", "PER HOUR WORKED, PRIVATE INDUSTRY, JUNE 2026",
         ["That&rsquo;s <b>7.5%</b> of total compensation.", "Paid leave: <b>$3.54</b> of every $46.89."],
         "Full-time workers: $4.40 an hour. Part-time: $0.90.", Y),
    stop(3, 4, "Required by law", "$3.40", "LEGALLY REQUIRED BENEFITS, PER HOUR WORKED, PRIVATE INDUSTRY",
         ["That&rsquo;s <b>7.2%</b> of total compensation.", "BLS reports it as its own category, separate from wages."],
         "Almost as much per hour as paid leave.", BL),
    stop(4, 4, "Extra pay + retirement", "$3.45", "SUPPLEMENTAL PAY ($1.88) + RETIREMENT AND SAVINGS ($1.57) PER HOUR",
         ["Supplemental pay: <b>4.0%</b> of compensation.", "Retirement and savings: <b>3.3%</b>."],
         "Combined figure: our math from the BLS table.", P),
    '<div class=tag>Detour</div>\n<h2>Benefits per hour, private industry</h2>\n' + cmp([(17.03, "$17.03", True), (5.05, "$5.05", False)],
        ["Full-time", "Part-time"]) + '\n<div class=mini style="margin-top:24px">BLS, June 2026. Full-time workers: $54.00 an hour in total compensation, 31.5% benefits. Part-time: $25.20, 20.0% benefits.</div>',
    '<div class=tag>End of the trail</div>\n<div class=hook style="font-size:86px">$46.89 an hour.<br><em>$14.07 in benefits.</em></div>\n<div class=cta>Send this to the friend<br>who&rsquo;s <em>comparing job offers.</em></div>\n<div class=src>' + DT_FOLLOW + '<br><br>Source: U.S. Bureau of Labor Statistics, Employer Costs for Employee Compensation, June 2026 (released Sept. 9, 2026), bls.gov. Private industry, average cost per hour worked. Per-$100 and combined figures: our math.</div>',
]
