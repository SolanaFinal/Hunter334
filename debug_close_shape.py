
import yfinance as yf
import pandas as pd

print("== Starte technischen Daten-Debug ==")
df = yf.download("SOL-USD", interval="1h", period="2d", progress=False)
df.dropna(inplace=True)

print("\n--- df.head() ---")
print(df.head())

print("\n--- df['Close'] ---")
print(df["Close"])

print("\n--- df[['Close']] ---")
print(df[["Close"]])

print("\n--- df['Close'].values ---")
print(df["Close"].values)

print("\n--- df['Close'].values.shape ---")
print(df["Close"].values.shape)

print("\n--- df['Close'].values.ravel() ---")
print(df["Close"].values.ravel())

print("\n--- df['Close'].values.ravel().shape ---")
print(df["Close"].values.ravel().shape)
