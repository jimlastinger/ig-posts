# Daily run playbook: @applied_stoic and @dollartrail

Jim owns both accounts. They are fully automated: research, build, host and post without asking him.
The only things he does by hand are Reels (he adds trending audio in the Instagram app).

## Accounts (Windsor connector `instagram`)
| Account | Windsor account ID | Look |
|---|---|---|
| @applied_stoic | 17841415388926249 | Dark, bronze #c9a35a, Cormorant serif + Oswald caps |
| @dollartrail | 17841418409241035 | Charcoal grid, red #ff5a4e, Anton + JetBrains Mono, "case file" bar |

Post a carousel with Windsor `execute_action`, connector `instagram`, action `create_carousel_post`,
params `{"image_urls": [...2-10 URLs in order...], "caption": "..."}`. The result contains the media ID.
Image URLs are raw GitHub URLs: `https://raw.githubusercontent.com/jimlastinger/ig-posts/main/<account>/<NNN>/<file>.jpg`.

## Each day
1. Read `CALENDAR.md` for today's four slots (2 per account) and `LOG.csv` for the next folder number
   (`NNN` per account) and the next dollartrail Trail No. (same as NNN). Never repeat a topic in LOG.csv.
2. Research each post before writing it (see Research rules). If `research/<YYYY-MM-DD>.md` exists for today, use it:
   it holds quotes and figures verified in a live session (approved by Jim, Oct 9 2026, because scheduled runs can't
   open web pages). Use only what's in it; see `research/README.md`. If a topic can't be verified, swap in a
   different topic from the backlog at the bottom of CALENDAR.md and note the swap in the summary.
3. Write `posts/<account>/<NNN>-<slug>.py` using the helpers in `tools/lib.py`
   (study `posts/*/00[2-4]-*.py` for the structure and tone). Then `python tools/render.py <file>`.
   Edit post text with the Edit tool or Python, not `sed`: in a sed replacement an unescaped `&` pastes the
   matched text back in, which is what garbled dollartrail 014's first slide on Oct 9.
4. Proofread before anything is pushed (added Oct 10, 2026 after the 014 typo; Jim does not approve posts):
   a. Text check: `render.py` runs `tools/lint.py` first and refuses to render a post with leftover HTML
      (`rsquo;`), doubled words ("HereHere", "the the"), words jammed after punctuation, words not in the
      dictionary, a post number on @applied_stoic, or a missing source line on @dollartrail. Fix the post and
      re-render. Add a word to `tools/allow.txt` only if it's a real word or name you've confirmed is spelled right.
      Never bypass the check or post slides from a failed render.
   b. Read `_build/<account>-<NNN>-text.txt` (every slide's text + the caption) line by line, as a reader would.
   c. Second reviewer: start a separate agent (Agent tool) that didn't write the post. Give it the text file, the
      post file and today's `research/` file, and ask it to report, with slide numbers: typos and grammar, any
      number, quote or citation that doesn't exactly match the research file, captions that don't match the
      slides, and anything confusing. Fix every real issue, re-render and re-check. If it can't be fixed with
      verified material, swap in a backlog topic. List what the reviewer caught in Jim's summary.
   d. Look at `_build/<account>-<NNN>-preview.png` with the Read tool. Fix any text overflow, wrapped
      legend labels, overlapping footers, or slides that are too dense, and re-render until clean.
5. Commit and push the JPEGs and post files (`git pull --rebase` first). Verify every URL returns
   `200 image/jpeg` with curl before posting. GitHub's raw CDN can lag a few seconds after a push.
6. Schedule each post at a jittered time inside its window (see Posting windows), then publish it at that time.
7. Append each published post to `LOG.csv` (with media ID and time) and push.
8. Send Jim one short summary: what posted, when, media IDs, any swaps, plus any Reel files with captions.

## Posting windows (America/New_York)
| | Slot 1 | Slot 2 |
|---|---|---|
| @applied_stoic weekdays | 6:30 to 8:30 a.m. | 8:00 to 10:00 p.m. |
| @applied_stoic weekends | 8:30 to 10:30 a.m. | 7:00 to 9:00 p.m. |
| @dollartrail weekdays | 11:30 a.m. to 1:15 p.m. | 5:00 to 7:15 p.m. |
| @dollartrail weekends | 10:00 a.m. to 12:00 p.m. | 4:00 to 6:00 p.m. |
Pick a random minute inside each window each day (not on :00 or :30), keep the two accounts at least
15 minutes apart, and keep two posts on the same account at least 4 hours apart. If a window has already
passed when the run starts, post that one 20 to 60 minutes from now instead.

## Design rotation (approved by Jim, Oct 8 2026)
Each account rotates through three looks by post number, so the grid doesn't repeat:
| NNN mod 3 | @applied_stoic | @dollartrail |
|---|---|---|
| 0 | original (dark, bronze) | original (charcoal grid) |
| 1 | `THEME = 'parchment'` (cream paper, oxblood accent) | `THEME = 'receipt'` (paper receipt, red totals) |
| 2 | `THEME = 'bronze'` (solid bronze, black type) | `THEME = 'ledger'` (navy ledger, yellow highlights) |
Set `THEME` near the top of the post file (omit it for the original). The look is defined in `tools/themes.py`
as CSS overrides, so every helper in `tools/lib.py` works in every look. Check the preview as usual; colored
chart segments must still read clearly on the light looks.

## Reels (calendar slots marked R)
Instagram's licensed music can only be added in the app, so Reels are made silent and Jim posts them.
Run `python tools/render.py posts/<account>/<file>.py --reel` on the named earlier post. That
re-renders slides into `<account>/<NNN>/` again (identical, harmless); don't commit duplicates. Send the
`_build/...-reel.mp4` to Jim with a ready-to-paste caption. Don't post Reels through Windsor.
"Best performer of week 1": pick the carousel with the most saves+shares (or likes if those are unavailable)
from Windsor's read connector `instagram_public`; if no data, pick the newest carousel that hasn't been a Reel.

## Research rules (non-negotiable)
- Every number on a @dollartrail slide comes from an official or primary source fetched that day (or pre-verified in `research/`)
  (EIA, BLS, BEA, Census, CBO, Treasury, USDA ERS, FRB, CMS, SSA, company 10-Ks, NRF, etc.).
  Print the source on the hook slide (`.mini`) and the final slide (`.src`), and in the caption.
- Use the latest full-period figure and say which period. Don't put a monthly number in a chart of
  annual averages. Don't compare across methodology breaks. Show arithmetic in your head, round consistently,
  and make segment shares add to 100.
- @applied_stoic quotes come only from public-domain translations: George Long (Marcus Aurelius,
  Epictetus), Richard Gummere (Seneca's letters), John W. Basore (Seneca's essays). Hays, Robin
  Hard and other modern translations are copyrighted, so never use them. Cite as "Author · Work ref · tr. Translator".
  Verify the exact wording against MIT Classics, Wikisource, Gutenberg or archive.org scans.
  Never post a quote you can't find in the primary text; many viral "Stoic quotes" are fake.
- No AI images of real people. No fabricated claims, prices, or quotes. When in doubt, leave it out.

## Content rules
- @applied_stoic: NO post numbers anywhere on the slides. 6-8 slides: hook, who's talking,
  the quote, apply it to a modern situation, a second idea or story, a practical exercise, close + CTA.
  End slide uses `STOIC_FOLLOW`. Caption: 2-3 short sentences, source line, 5-6 hashtags.
- @dollartrail: header bar "Trail No. NNN / Following: <thing>". 7-9 slides: hook with the
  price, trail map (`stack`), 3-5 stops (`stop`), optional detour (`cmp`), end of the trail + CTA
  + `DT_FOLLOW` + source. Caption: 1-2 sentences, "Data: <source>", a question, 5-6 hashtags.
- Plain language, active voice, no clickbait claims the slides don't back up.

## If something fails
- Windsor error about write actions: tell Jim to enable "write actions for Claude" in Windsor settings.
- Push refused: the Claude GitHub App must have access to jimlastinger/ig-posts.
- Image URL not 200: wait 30 s and recheck; don't post broken URLs.
- Never post the same carousel twice: check LOG.csv for the media ID before retrying a post.
- An "Application request limit reached" error can still publish the post (it did on Oct 8). Before any retry,
  list today's media with Windsor `get_data` (connector `instagram`, fields date, media_id, media_caption,
  timestamp, `force_refresh`) and match the caption; if it's there, log that media ID instead of reposting.
