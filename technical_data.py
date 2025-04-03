
import yfinance as yf
import pandas as pd
import ta

def get_technical_indicators(ticker="SOL-USD", interval="1h", period="2d"):
    try:
        df = yf.download(ticker, interval=interval, period=period, progress=False)
        if df.empty:
            print("[TECHNICAL] Keine Daten empfangen.")
            return None

        df.dropna(inplace=True)

        # FIX: MultiIndex entfernen (z. B. Close: SOL-USD -> Close)
        if isinstance(df.columns, pd.MultiIndex):
            df.columns = df.columns.get_level_values(0)

        # Jetzt korrekt in 1D umwandeln
        df["Close"] = df["Close"].values.ravel().astype(float)

        df["rsi"] = ta.momentum.RSIIndicator(close=df["Close"]).rsi()
        macd = ta.trend.MACD(close=df["Close"])
        df["macd"] = macd.macd()
        df["macd_signal"] = macd.macd_signal()
        boll = ta.volatility.BollingerBands(close=df["Close"])
        df["bb_high"] = boll.bollinger_hband()
        df["bb_low"] = boll.bollinger_lband()

        latest = df.iloc[-1]
        indicators = {
            "rsi": round(latest["rsi"], 2),
            "macd": round(latest["macd"], 4),
            "macd_signal": round(latest["macd_signal"], 4),
            "bb_high": round(latest["bb_high"], 2),
            "bb_low": round(latest["bb_low"], 2),
            "price": round(latest["Close"], 2),
        }
        return indicators
    except Exception as e:
        print(f"[TECHNICAL] Fehler beim Abrufen technischer Daten: {e}")
        return None
