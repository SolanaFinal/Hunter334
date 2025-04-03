
import json
import numpy as np
import pandas as pd
from tensorflow.keras.models import load_model
from keras.losses import MeanSquaredError
from sklearn.preprocessing import MinMaxScaler
from intel_news import fetch_news_headlines, analyze_sentiment
from technical_data import get_technical_indicators
import joblib
import yfinance as yf

# Model-Ladepfade
lstm_model = load_model("./model/lstm_model.h5", custom_objects={"mse": MeanSquaredError()})
xgb_model = joblib.load("model/xgb_model.pkl")
scaler = MinMaxScaler()

def safe_float(value):
    if isinstance(value, tuple):
        return float(value[0])
    try:
        return float(value)
    except:
        return 0.0

from intel_social import get_latest_social_sentiment

def get_latest_sentiment():
    try:
        # Aktuellen Preis simulieren (z. B. aus Modell oder Börse)
        last_price = 125.0  # <== optional dynamisch machen

        # Vorhersage mit LSTM
        predicted_price = lstm_model.predict(np.array([[last_price]]))[0][0]

        # News-Sentiment laden
        news_score, headlines = fetch_news_headlines()

        # Social-Sentiment (Twitter)
        social_score, tweets = get_latest_social_sentiment()

        # Kombiniertes Sentiment
        sentiment_score = round((news_score + social_score) / 2, 3)

        # Technische Dummy-Werte (später dynamisch)
        volatility = 0.2
        momentum = 0.4
        risk_level = 0.5

        # XGBoost Input vorbereiten
        xgb_input = pd.DataFrame([{
            "predicted_price": predicted_price,
            "sentiment_score": sentiment_score,
            "volatility": volatility,
            "momentum": momentum,
            "risk_level": risk_level
        }])

        # Entscheidung treffen (Buy/Sell)
        action_class = int(xgb_model.predict(xgb_input)[0])
        action = "BUY" if action_class == 1 else "SELL"

        print(f"[SENTIMENT] Score: {sentiment_score} | Action: {action}")
        return sentiment_score, headlines, tweets, action, predicted_price

    except Exception as e:
        print("[ERROR]", e)
        return 0.0, [], [], "HOLD", 0.0
    # 2. Technische Indikatoren
    tech = get_technical_indicators()
    if not tech:
        tech = {"rsi": 50, "macd": (0.0, 0.0), "bb_high": 0, "bb_low": 0, "price": 0}

    # macd absichern (entweder Tupel oder Dummy-Werte)
    macd_raw = tech.get("macd", (0.0, 0.0))
    if isinstance(macd_raw, tuple):
        macd_line, macd_signal = macd_raw
    else:
        macd_line, macd_signal = 0.0, 0.0

    # 3. Preis-Vorhersage (LSTM)
    df = yf.download("SOL-USD", interval="1h", period="2d", progress=False)
    df = df[["Close"]]
    df.dropna(inplace=True)

    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)

    df["Close"] = df["Close"].values.ravel().astype(float)

    last_sequence = df["Close"].values[-50:]
    scaled_seq = scaler.fit_transform(last_sequence.reshape(-1, 1))
    lstm_input = np.expand_dims(scaled_seq, axis=0)
    predicted_price = lstm_model.predict(lstm_input)[0][0]
    predicted_price = float(scaler.inverse_transform([[predicted_price]])[0][0])

    # 4. Entscheidung durch XGBoost (alle Werte safe gecastet)
    xgb_input = np.array([[
        safe_float(predicted_price),
        safe_float(sentiment_score),
        safe_float(0.5),
        safe_float(0.8),
        safe_float(0.1),
        safe_float(tech.get("rsi", 50)),
        safe_float(macd_line),
        safe_float(macd_signal),
        safe_float(tech.get("bb_high", 0)),
        safe_float(tech.get("bb_low", 0)),
        safe_float(tech.get("price", 0)),
    ]])
    action_class = int(xgb_model.predict(xgb_input)[0])

    return sentiment_score, headlines, tech, predicted_price, action_class
