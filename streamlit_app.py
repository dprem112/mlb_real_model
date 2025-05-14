import streamlit as st
import pandas as pd
from mlb_api import get_today_matchups
from generate_features import build_features
from predictor import predict_game

st.set_page_config(page_title="MLB Predictions", layout="centered")
st.title("⚾ MLB Prediction Dashboard")

games = get_today_matchups()
if not games:
    st.warning("No games found for today.")
else:
    results = []
    for game in games:
        features = build_features(game)
        prediction, confidence = predict_game(features)
        results.append({
            "Matchup": f"{game['away']} @ {game['home']}",
            "Predicted Winner": game["home"] if prediction else game["away"],
            "Confidence": f"{confidence:.2%}"
        })
    df = pd.DataFrame(results)
    st.subheader("Today's Predictions")
    st.table(df)
