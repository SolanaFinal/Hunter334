import numpy as np
from keras.models import Sequential
from keras.layers import LSTM, Dense
from keras.optimizers import Adam
from keras.models import load_model
import os

def generate_dummy_price_data():
    # Simuliere einfache Preisverläufe
    base_price = 100
    noise = np.random.normal(0, 1, 200)
    price_series = np.cumsum(noise) + base_price
    return price_series

def create_dataset(data, look_back=10):
    X, y = [], []
    for i in range(len(data) - look_back):
        X.append(data[i : i + look_back])
        y.append(data[i + look_back])
    return np.array(X), np.array(y)

def train_lstm_model():
    data = generate_dummy_price_data()
    X, y = create_dataset(data)

    X = X.reshape((X.shape[0], X.shape[1], 1))
    y = y.reshape(-1, 1)

    model = Sequential()
    model.add(LSTM(units=50, return_sequences=False, input_shape=(X.shape[1], 1)))
    model.add(Dense(1))
    model.compile(optimizer=Adam(learning_rate=0.001), loss="mse")

    model.fit(X, y, epochs=20, batch_size=8, verbose=1)

    os.makedirs("model", exist_ok=True)
    model.save("model/lstm_model.h5")
    print("[TRAINING] LSTM-Modell erfolgreich gespeichert.")

if __name__ == "__main__":
    train_lstm_model()