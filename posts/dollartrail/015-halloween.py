import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "tools"))
from lib import *

ACCOUNT = 'dollartrail'
TRAIL = '015'
FOLLOWING = 'Halloween spending'
SOURCES = ['https://nrf.com/research-insights/holiday-data-and-trends/halloween',
           'https://nrf.com/media-center/press-releases/nrf-halloween-survey-shows-consumer-spending-expected-to-reach-13-5-billion']

CAPTION = """Americans expect to spend $13.5 billion on Halloween this year, up from a record $13.1 billion in 2025. That's $115.14 for each person celebrating, and costumes, decorations and candy take almost all of it.

Data: National Retail Federation 2026 Halloween survey, conducted by Prosper Insights & Analytics.

What's your costume this year?

#halloween #halloween2026 #candy #costume #spending #dollartrail"""

SLIDES = [
    '<div class=tag>Trail No. 015</div>\n<div class=hook style="font-size:104px">Halloween 2026: $13.5 billion. <em>$115 a person.</em></div>\n<div class=hook2>Here&rsquo;s where the money goes.</div>\n<div class=mini style="margin-top:60px">Source: National Retail Federation 2026 Halloween survey (Prosper Insights &amp; Analytics, 7,889 consumers, Sept. 1-9, 2026). Expected spending.</div>',
    stack([(32, R, "COSTUMES"), (32, Y, "DECOR"), (30, BL, "CANDY"), (6, P, "")],
          [("Costumes", "$4.4B", R), ("Decorations", "$4.3B", Y), ("Candy", "$4.1B", BL), ("Greeting cards", "$0.8B", P)],
          "Shares of category spending (our math). Categories sum to $13.6B; NRF&rsquo;s $13.5B total differs due to rounding.",
          "Where $13.5 billion goes", height=700),
    stop(1, 4, "Costumes", "$4.4B", "71% PLAN TO BUY ONE",
         ["Adults: <b>$2 billion</b>. Kids: <b>$1.5 billion</b>. Pets: <b>$0.92 billion</b>."],
         "Top adult costume: witch (4.8 million people). Top kids&rsquo; costume: Spider-Man (4.6 million).", R),
    stop(2, 4, "Decorations", "$4.3B", "78% PLAN TO BUY",
         ["Almost as much as costumes. <b>42%</b> plan to decorate their home or yard."],
         "49% started Halloween shopping in September or earlier.", Y),
    stop(3, 4, "Candy", "$4.1B", "96% PLAN TO BUY",
         ["The one thing nearly every celebrant buys. <b>61%</b> plan to hand out candy."],
         "Candy is the smallest of the big three, but the most widely bought.", BL),
    stop(4, 4, "Greeting cards", "$0.8B", "42% PLAN TO BUY",
         ["Up from <b>38%</b> in 2025. Yes, Halloween cards."],
         "The smallest stop on the trail: about 6% of category spending (our math).", P),
    '<div class=tag>Detour</div>\n<h2>Pets dress up too</h2><div class=amt style="color:#4fd1a5">$0.92B</div><div class=pct>ON PET COSTUMES, 2026</div>\n<p>Top pet costume: <b>pumpkin</b> (11.6% of pet-costume buyers), then <b>hot dog</b> (5.9%) and <b>ghost</b> (2.8%).</p>' + note("Where people shop: discount stores 39%, Halloween stores 32%, online 27%."),
    '<div class=tag>End of the trail</div>\n<div class=hook style="font-size:92px">$13.5 billion.<br><em>94% of it: costumes, decor and candy.</em></div>\n<div class=cta>Send this to the friend<br>who starts decorating in <em>September.</em></div>\n<div class=src>' + DT_FOLLOW + '<br><br>Source: National Retail Federation, 2026 Halloween survey conducted by Prosper Insights &amp; Analytics (nrf.com), released Sept. 22, 2026. 94% = category shares, our math.</div>',
]
