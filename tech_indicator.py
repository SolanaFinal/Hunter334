# tech_indicator.py
import yfinance as yf
import pandas as pd

def get_technical_indicators(symbol="SOL-USD", period="2d", interval="1h"):
    try:
        df = yf.download(tickers=symbol, period=period, interval=interval)

        if df.empty or len(df["Close"]) < 30:
            print("[TECHNICAL] Nicht genügend Daten für Indikatoren.")
            return None

        close = df["Close"].values

        # Volatilität = Standardabweichung der letzten 20 Stunden
        volatility = close[-20:].std()

        # Momentum = letzter Schlusskurs - Schlusskurs vor 10 Stunden
        momentum = close[-1] - close[-10]

        # Risk Level (einfach): (max drawdown letzte 24h)
        drawdown = min(close[-24:]) / max(close[-24:]) - 1
        risk_level = abs(drawdown)

        # RSI (14)
        delta = pd.Series(close).diff()
        gain = delta.where(delta > 0, 0).rolling(14).mean()
        loss = -delta.where(delta < 0, 0).rolling(14).mean()
        rs = gain / loss
        rsi = 100 - (100 / (1 + rs))
        rsi_last = rsi.iloc[-1] if not rsi.empty else 50

        # MACD
        short_ema = pd.Series(close).ewm(span=12, adjust=False).mean()
        long_ema = pd.Series(close).ewm(span=26, adjust=False).mean()
        macd = short_ema - long_ema
        macd_signal = macd.ewm(span=9, adjust=False).mean()

        return (
            round(volatility, 4),
            round(momentum, 4),
            round(risk_level, 4),
            round(rsi_last, 2),
            round(macd.iloc[-1], 4),
            round(close[-1], 2)
        )

    except Exception as e:
        print(f"[TECHNICAL] Fehler beim Abrufen technischer Daten: {e}")
        return None