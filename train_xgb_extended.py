
import json
import numpy as np
import pandas as pd
import joblib
from xgboost import XGBClassifier
from technical_data import get_technical_indicators
from intel_news import analyze_sentiment, fetch_news_headlines

# Konfiguration laden
with open("config.json", "r") as f:
    config = json.load(f)

risk_tolerance = config.get("risk_tolerance", "medium")

def generate_training_data(samples=300):
    data = []
    labels = []
    for _ in range(samples):
        seq = np.random.rand(60, 1)
        volatility = np.std(seq)
        momentum = seq[-1][0] - seq[0][0]
        predicted_price = np.mean(seq)  # Dummy Wert

        headlines = fetch_news_headlines("crypto")
        sentiment_score, _ = analyze_sentiment(headlines)

        tech = get_technical_indicators("SOL-USD") or {
            "rsi": 50, "macd": 0, "macd_signal": 0,
            "bb_high": 0, "bb_low": 0, "price": 0
        }

        features = {
            "predicted_price": predicted_price,
            "sentiment_score": sentiment_score,
            "volatility": volatility,
            "momentum": momentum,
            "risk_level": {"low": 0, "medium": 1, "high": 2}[risk_tolerance],
            "rsi": tech["rsi"],
            "macd": tech["macd"],
            "macd_signal": tech["macd_signal"],
            "bb_high": tech["bb_high"],
            "bb_low": tech["bb_low"],
            "price": tech["price"]
        }

        label = np.random.choice([0, 1, 2])  # Dummy: HOLD, BUY, SELL

        data.append(features)
        labels.append(label)

    return pd.DataFrame(data), labels

# Trainingsdaten erzeugen
X, y = generate_training_data()

# Modell trainieren
model = XGBClassifier(use_label_encoder=False, eval_metric="mlogloss")
model.fit(X, y)

# Modell speichern
joblib.dump(model, "model/xgb_model.pkl")
print("[TRAINING] Neues XGBoost-Modell erfolgreich gespeichert.")
