import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "tools"))
from lib import *

ACCOUNT = 'dollartrail'
TRAIL = '031'
THEME = 'receipt'
FOLLOWING = 'holiday spending 2026'
SOURCES = ['https://nrf.com/media-center/press-releases/affordability-shapes-winter-holiday-shopping-according-to-nrf-holiday-survey']

CAPTION = """The National Retail Federation expects holiday spending in November and December to reach $1.013 trillion, up 4.2% from 2025. But 56% of holiday shoppers say the economy will affect their spending plans, and 43% plan to start before November.

Data: National Retail Federation holiday survey (Prosper Insights & Analytics, 8,094 adults, Oct. 1-7, 2026) and NRF 2026 holiday forecast.

Have you started your holiday shopping yet?

#holidayshopping #christmasshopping #blackfriday #budget #personalfinance #dollartrail"""

SLIDES = [
    '<div class=tag>Trail No. 031</div>\n<div class=hook style="font-size:104px">Holidays 2026: <em>$1.013 trillion.</em></div>\n<div class=hook2>How shoppers plan to spend it.</div>\n<div class=mini style="margin-top:60px">Source: National Retail Federation, Oct. 20, 2026: 2026 holiday forecast (November and December spending) and holiday survey by Prosper Insights &amp; Analytics (8,094 adults, Oct. 1-7, 2026).</div>',
    stack([(43, R, "43%"), (57, W, "57%")],
          [("Start before Nov.", "43%", R), ("The rest", "57%", W)],
          "Share of holiday shoppers who plan to begin browsing and buying before November (42% last year). The rest: our math (100% minus 43%).",
          "When shoppers start", height=680),
    stop(1, 4, "The forecast", "$1.013T", "NOVEMBER + DECEMBER 2026",
         ["NRF expects holiday spending to grow <b>4.2%</b> over 2025."],
         "That is NRF&rsquo;s forecast of total spending, not a survey answer.", R),
    stop(2, 4, "The economy", "56%", "OF HOLIDAY SHOPPERS SAY IT WILL AFFECT THEIR PLANS",
         ["Among them: <b>43%</b> will shop for sales more often, <b>31%</b> will comparison shop online more often, and <b>29%</b> will use coupons more often."],
         "91% of U.S. adults plan to celebrate the winter holidays.", Y),
    stop(3, 4, "The early start", "43%", "PLAN TO BEGIN BEFORE NOVEMBER",
         ["Why? <b>50%</b> of early starters want to spread out their budget. <b>37%</b> say the prices and promotions are too good to pass up."],
         "Last year it was 42%.", BL),
    stop(4, 4, "The big weekend", "64%", "LIKELY TO WAIT UNTIL THANKSGIVING WEEKEND",
         ["Nearly two-thirds of consumers say they are likely to wait until Thanksgiving weekend to do <b>most</b> of their shopping."],
         "Last year: 63%. Starting early isn&rsquo;t the same as doing most of it early.", P),
    '<div class=tag>Detour</div>\n<h2>Where they plan to shop</h2>\n' + cmp([(53, "53%", True), (43, "43%", False), (43, "43%", False), (42, "42%", False)],
        ["Online", "Grocery", "Discount", "Department"]) + '\n<div class=mini style="margin-top:24px">Share planning to shop at each. Top of the wish list: gift cards (47%), then clothing (44%).</div>',
    '<div class=tag>End of the trail</div>\n<div class=hook style="font-size:88px">A trillion-dollar season.<br><em>56% say the economy will shape it.</em></div>\n<div class=cta>Send this to the friend<br>who&rsquo;s <em>already shopping.</em></div>\n<div class=src>' + DT_FOLLOW + '<br><br>Source: National Retail Federation press release, Oct. 20, 2026 (nrf.com): 2026 holiday forecast and annual consumer survey by Prosper Insights &amp; Analytics, 8,094 adults, Oct. 1-7, margin of error &plusmn;1.1 points.</div>',
]
