from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
import numpy as np

model = Sequential([
    LSTM(50, return_sequences=False, input_shape=(60, 1)),
    Dense(1)
])
model.compile(optimizer='adam', loss='mse')

X_dummy = np.random.rand(100, 60, 1)
y_dummy = np.random.rand(100, 1)

model.fit(X_dummy, y_dummy, epochs=1, verbose=0)
model.save("model/lstm_model.h5")
print("✅ Dummy-Modell gespeichert unter: model/lstm_model.h5")