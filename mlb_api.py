import requests
from datetime import date

def get_today_matchups():
    today = date.today().isoformat()
    url = f"https://statsapi.mlb.com/api/v1/schedule?sportId=1&date={today}"
    r = requests.get(url)
    data = r.json()
    seen = set()
    matchups = []
    for d in data.get("dates", []):
        for game in d.get("games", []):
            game_pk = game["gamePk"]
            if game_pk in seen:
                continue
            seen.add(game_pk)
            matchups.append({
                "gamePk": game_pk,
                "home": game["teams"]["home"]["team"]["name"],
                "away": game["teams"]["away"]["team"]["name"]
            })
    return matchups
