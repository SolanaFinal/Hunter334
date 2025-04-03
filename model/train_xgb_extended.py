import yfinance as yf
import numpy as np
import pandas as pd
import joblib
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from xgboost import XGBClassifier

nltk.download("vader_lexicon")
sentiment_analyzer = SentimentIntensityAnalyzer()

def fetch_news_headlines():
    headlines = [
        "Solana surges after major upgrade announcement",
        "Crypto market experiences slight dip amid global uncertainty",
        "Solana achieves new partnership with leading DeFi platform"
    ]
    return headlines

def analyze_sentiment(headlines):
    if not headlines:
        return 0.0
    score = sum(sentiment_analyzer.polarity_scores(h)["compound"] for h in headlines) / len(headlines)
    return score

def fetch_technical_indicators():
    df = yf.download("SOL-USD", interval="1h", period="7d")
    close = df["Close"].values.reshape(-1, 1).ravel()

    if len(close) < 20:
        raise ValueError("Not enough data for indicators.")

    rsi = [50 + 10 * np.sin(i / 10) for i in range(len(close))][-1]
    macd = close[-1] - np.mean(close[-12:])
    macd_signal = np.mean(close[-9:])
    bb_high = np.max(close[-20:]) + 2
    bb_low = np.min(close[-20:]) - 2
    price = close[-1]

    return rsi, macd, macd_signal, bb_high, bb_low, price

def train_xgb():
    sentiment_score = analyze_sentiment(fetch_news_headlines())

    try:
        rsi, macd, macd_signal, bb_high, bb_low, price = fetch_technical_indicators()
    except Exception as e:
        print(f"[TECHNICAL] Fehler beim Abrufen technischer Daten: {e}")
        return

    X = []
    y = []

    for _ in range(100):
        volatility = np.random.rand()
        momentum = np.random.rand()
        risk_level = np.random.rand()
        action = np.random.choice([0, 1, 2])

        X.append([price, sentiment_score, volatility, momentum, risk_level,
                  rsi, macd, macd_signal, bb_high, bb_low, price])
        y.append(action)

    model = XGBClassifier(use_label_encoder=False, eval_metric="mlogloss")
    model.fit(np.array(X), np.array(y))
    joblib.dump(model, "./model/xgb_model.pkl")
    print("[TRAINING] Neues XGBoost-Modell erfolgreich gespeichert.")

if __name__ == "__main__":
    train_xgb()