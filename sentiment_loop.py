import time
import numpy as np
from tensorflow.keras.models import load_model
from xgboost import XGBClassifier
import joblib

from combined_sentiment import get_combined_sentiment
from tech_indicator import get_technical_indicators

lstm_model = load_model("./model/lstm_model.h5")
xgb_model = joblib.load("model/xgb_model.pkl")

def get_latest_sentiment():
    sentiment_score, headlines = get_combined_sentiment()
    tech = get_technical_indicators()

    if tech is None or len(tech) != 6:
        print("[TECHNICAL] Ungültige technische Indikatoren.")
        return sentiment_score, headlines, tech, "HOLD", 0.0

    predicted_price = lstm_model.predict(np.array([tech[5]]).reshape(1, 1), verbose=0)[0][0]

    xgb_input = np.array([[
        predicted_price,
        sentiment_score,
        tech[0],  # volatility
        tech[1],  # momentum
        tech[2],  # risk_level
        tech[3],  # rsi
        tech[4],  # macd
        tech[5],  # price
        tech[5] + 2,  # dummy bb_high
        tech[5] - 2,  # dummy bb_low
        tech[4] - 1  # dummy macd_signal
    ]])

    try:
        action_class = int(xgb_model.predict(xgb_input)[0])
        action = ["SELL", "HOLD", "BUY"][action_class]
        return sentiment_score, headlines, tech, action, predicted_price
    except Exception as e:
        print(f"[ERROR] Entscheidungsproblem: {e}")
        return sentiment_score, headlines, tech, "HOLD", predicted_price

if __name__ == "__main__":
    while True:
        score, headlines, tech, action, predicted_price = get_latest_sentiment()
        print(f"[SENTIMENT] Score: {score} | Action: {action} | Price: {predicted_price}")
        for h in headlines:
            print("📰", h)
        print("[LOOP] Warte 5 Minuten...\n")
        time.sleep(300)