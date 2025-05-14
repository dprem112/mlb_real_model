from team_stats import get_team_rolling_stats

def build_features(game):
    home = get_team_rolling_stats(game["home"])
    away = get_team_rolling_stats(game["away"])
    return [
        home["hits"] - away["hits"],
        away["era"] - home["era"],
        home["strikeouts_pitch"] - away["strikeouts_pitch"],
        away["strikeouts_bat"] - home["strikeouts_bat"],
        home["innings"] - away["innings"]
    ]
