"""Rank fresh posts from WATCHLIST.md accounts for Jim to comment on.

Input: a JSON file of Windsor `instagram_public` rows (the get_data result, either the whole
{"data": [...]} object or just the list) with fields profile_username, profile_followers_count,
media_id, media_timestamp, media_type, media_permalink, media_like_count, media_comments_count,
media_caption.

Usage: python tools/comment_picks.py rows.json [--per-niche 4] [--now 2026-11-05T13:40:00Z]
Prints JSON: {"stoic": [...], "money": [...], "missing": [handles with no rows]}.

Why these rules: a comment helps most on a post that is fresh (people are still seeing it) and moving fast
for its account's size, but not so crowded that a new comment is buried.
"""
import json, math, re, sys, argparse, pathlib, datetime as dt

ROOT = pathlib.Path(__file__).resolve().parents[1]

PAUSED = []

def watchlist():
    niches, cur = {}, None
    for line in (ROOT / "WATCHLIST.md").read_text().splitlines():
        m = re.match(r"##\s+(\w+)", line)
        if m:
            cur = m.group(1).lower()
            if "paused" in line.lower():  # "## money (PAUSED ...)" skips the whole niche
                PAUSED.append(cur); cur = None
            else:
                niches[cur] = []
            continue
        h = line.split("#")[0].strip().lstrip("@").lower()
        if cur and h and re.fullmatch(r"[a-z0-9._]+", h):
            niches[cur].append(h)
    return niches

def parse_ts(s):
    s = str(s).replace("Z", "+00:00")
    if re.search(r"[+-]\d{4}$", s):
        s = s[:-2] + ":" + s[-2:]
    t = dt.datetime.fromisoformat(s)
    return t if t.tzinfo else t.replace(tzinfo=dt.timezone.utc)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("rows"); ap.add_argument("--per-niche", type=int, default=4)
    ap.add_argument("--now"); ap.add_argument("--max-age", type=float, default=24)
    ap.add_argument("--max-comments", type=int, default=400)
    a = ap.parse_args()
    data = json.loads(pathlib.Path(a.rows).read_text())
    rows = data.get("data", data) if isinstance(data, dict) else data
    now = parse_ts(a.now) if a.now else dt.datetime.now(dt.timezone.utc)
    wl = watchlist()
    seen = {(r.get("profile_username") or "").lower() for r in rows}
    out = {"paused": PAUSED, "missing": sorted(h for hs in wl.values() for h in hs if h not in seen)}
    for niche, handles in wl.items():
        cands = []
        for r in rows:
            u = (r.get("profile_username") or "").lower()
            if u not in handles or not r.get("media_permalink") or not r.get("media_timestamp"):
                continue
            age = (now - parse_ts(r["media_timestamp"])).total_seconds() / 3600
            likes = r.get("media_like_count") or 0; comments = r.get("media_comments_count") or 0
            if age < 0.25 or age > a.max_age or comments > a.max_comments:
                continue
            followers = max(r.get("profile_followers_count") or 10000, 1000)
            velocity = (likes + 3 * comments) / max(age, 1)
            score = velocity / math.sqrt(followers) * (1.3 if age <= 6 else 1.0)
            cands.append({"handle": u, "permalink": r["media_permalink"], "type": r.get("media_type"),
                          "age_hours": round(age, 1), "likes": likes, "comments": comments,
                          "followers": r.get("profile_followers_count"), "score": round(score, 3),
                          "caption": (r.get("media_caption") or "")[:600]})
        cands.sort(key=lambda c: -c["score"])
        picks, used = [], set()
        for c in cands:
            if c["handle"] in used:
                continue
            picks.append(c); used.add(c["handle"])
            if len(picks) == a.per_niche:
                break
        out[niche] = picks
    print(json.dumps(out, indent=1))

if __name__ == "__main__":
    main()
