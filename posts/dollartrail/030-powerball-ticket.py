import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "tools"))
from lib import *

ACCOUNT = 'dollartrail'
TRAIL = '030'
FOLLOWING = 'a $2 Powerball ticket'
SOURCES = ['https://www.powerball.com/powerball-prize-chart',
           'https://www.powerball.com/faqs']

CAPTION = """On average, 70 cents of every $2 Powerball ticket stays where it was sold to fund public programs, per Powerball. By our math from the official odds, the eight set prizes pay back about 32 cents per play on average. The jackpot odds: 1 in 292,201,338.

Data: Powerball prize chart and FAQs (powerball.com). Expected values our math.

Do you play when the jackpot gets big, or never?

#powerball #lottery #jackpot #odds #personalfinance #dollartrail"""

SLIDES = [
    '<div class=tag>Trail No. 030</div>\n<div class=hook style="font-size:108px">A Powerball ticket: <em>$2.</em> Jackpot odds: 1 in 292,201,338.</div>\n<div class=hook2>Where your $2 goes.</div>\n<div class=mini style="margin-top:60px">Source: Powerball prize chart and FAQs (powerball.com). Base $2 play, no Power Play.</div>',
    stack([(35, R, "WHERE IT&rsquo;S SOLD 35%"), (16, Y, "SET PRIZES 16%"), (49, W, "THE REST 49%")],
          [("Where it&rsquo;s sold", "70&cent;", R), ("Set prizes (avg.)", "32&cent;", Y), ("The rest", "98&cent;", W)],
          "35% is Powerball&rsquo;s average for what stays where the ticket is sold. Set prizes: average payout of the 8 non-jackpot prizes per $2, from the official odds (our math). The rest, including the jackpot, isn&rsquo;t broken out on powerball.com. California&rsquo;s prizes work differently.",
          "Where $2 goes, on average", height=640),
    stop(1, 4, "Where it&rsquo;s sold", "70&cent;", "35% OF EVERY $2 TICKET, ON AVERAGE",
         ["Powerball says that share stays in the jurisdiction where the ticket is sold, to support public programs and services."],
         "Every ticket sends money to the state or jurisdiction where it&rsquo;s sold, win or lose.", R),
    stop(2, 4, "Set prizes", "32&cent;", "AVERAGE PAYOUT PER $2 PLAY (OUR MATH)",
         ["Eight prizes, from <b>$4</b> to <b>$1 million</b>, are set cash amounts. Each prize times its odds, added up, comes to about 32&cent;."],
         "Overall odds of winning any prize: 1 in 24.87.", Y),
    stop(3, 4, "The most common win", "$4", "ODDS: 1 IN 38.32",
         ["The most likely prize is twice the ticket price. A second $4 prize has odds of <b>1 in 91.98</b>."],
         "Those two $4 prizes add up to almost half of the 32&cent; (our math).", BL),
    stop(4, 4, "The jackpot", "1 in 292M", "ODDS: 1 IN 292,201,338",
         ["Winners choose a lump sum (the cash option) or an annuity: one payment now, then 29 yearly payments that grow <b>5%</b> a year."],
         "Federal and state or local income taxes may apply to prizes.", P),
    '<div class=tag>Detour</div>\n<h2>Where the 32&cent; comes from</h2>\n' + cmp([(14.8, "14.8&cent;", True), (8.6, "8.6&cent;", False), (5.5, "5.5&cent;", False), (2.2, "2.2&cent;", False), (1.0, "1.0&cent;", False)],
        ["$4 prizes", "$1 million", "$50,000", "$7 prizes", "$100 prizes"]) + '\n<div class=mini style="margin-top:24px">Average payout per $2 play from each prize level: prize &times; odds, from the official Powerball prize chart. Our math.</div>',
    '<div class=tag>End of the trail</div>\n<div class=hook style="font-size:88px">70&cent; to where it&rsquo;s sold.<br><em>About 32&cent; back in set prizes.</em></div>\n<div class=cta>Send this to someone<br>who <em>plays every week.</em></div>\n<div class=src>' + DT_FOLLOW + '<br><br>Source: Powerball prize chart (prizes and odds, base play) and FAQs (ticket price, 35% share, annuity) at powerball.com. Average payouts and cent figures: our math.</div>',
]
