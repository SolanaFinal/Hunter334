import numpy as np
import yfinance as yf
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM
from tensorflow.keras.callbacks import EarlyStopping
import joblib

def download_close_prices(symbol="SOL-USD", interval="1h", period="30d"):
    df = yf.download(symbol, interval=interval, period=period)
    return df["Close"].values.reshape(-1, 1)

def create_dataset(data, look_back=10):
    X, y = [], []
    for i in range(len(data) - look_back):
        X.append(data[i:i + look_back])
        y.append(data[i + look_back])
    return np.array(X), np.array(y)

def train_lstm_model():
    prices = download_close_prices()
    scaler = MinMaxScaler()
    scaled_prices = scaler.fit_transform(prices)

    X, y = create_dataset(scaled_prices)
    X = np.reshape(X, (X.shape[0], X.shape[1], 1))

    model = Sequential()
    model.add(LSTM(50, return_sequences=False, input_shape=(X.shape[1], 1)))
    model.add(Dense(1))
    model.compile(optimizer="adam", loss="mse")

    es = EarlyStopping(monitor="loss", patience=5)
    model.fit(X, y, epochs=30, batch_size=16, verbose=1, callbacks=[es])

    model.save("./model/lstm_model.h5")
    joblib.dump(scaler, "./model/lstm_scaler.save")
    print("[LSTM] Modell & Scaler erfolgreich gespeichert.")

if __name__ == "__main__":
    train_lstm_model()