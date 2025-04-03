
import pandas as pd
import numpy as np
from sentiment_loop import get_latest_sentiment

# Dummy Handelsmodell: zufälliger Trade auf Basis von Sentiment
def dummy_model_predict(candle_row, sentiment_score):
    if sentiment_score > 0.3:
        return "BUY"
    elif sentiment_score < -0.3:
        return "SELL"
    else:
        return "HOLD"

def run_backtest(csv_path="historical_data.csv"):
    try:
        df = pd.read_csv(csv_path)
    except FileNotFoundError:
        print("❌ Historische Daten nicht gefunden:", csv_path)
        return

    balance = 1000  # Simuliertes Startkapital
    position = None
    trades = []

    sentiment_score, _ = get_latest_sentiment()  # Fixer Dummy-Wert im Testlauf

    for index, row in df.iterrows():
        decision = dummy_model_predict(row, sentiment_score)

        if decision == "BUY" and position is None:
            position = float(row['close'])
            trades.append(("BUY", position))
        elif decision == "SELL" and position is not None:
            profit = float(row['close']) - position
            balance += profit
            trades.append(("SELL", float(row['close']), profit))
            position = None

    print("\n📊 BACKTEST-ERGEBNIS")
    print("Abschließendes Kapital:", round(balance, 2))
    print("Anzahl Trades:", len(trades))
    if trades:
        gewinne = [t[2] for t in trades if len(t) == 3]
        print("Ø Gewinn pro Trade:", round(np.mean(gewinne), 4) if gewinne else "n/a")

if __name__ == "__main__":
    run_backtest()
