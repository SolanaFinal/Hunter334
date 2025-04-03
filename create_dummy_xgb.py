import pandas as pd
import numpy as np
from xgboost import XGBClassifier
import joblib

# Dummy-Daten erzeugen
X = pd.DataFrame({
    "predicted_price": np.random.rand(100),
    "sentiment_score": np.random.rand(100),
    "volatility": np.random.rand(100),
    "momentum": np.random.rand(100),
    "risk_level": np.random.randint(0, 3, 100)
})
y = np.random.choice([0, 1, 2], size=100)  # 0=HOLD, 1=BUY, 2=SELL

# Modell trainieren
model = XGBClassifier(use_label_encoder=False, eval_metric="mlogloss")
model.fit(X, y)

# Speichern
joblib.dump(model, "model/xgb_model.pkl")
print("✅ Dummy-XGBoost-Modell gespeichert unter: model/xgb_model.pkl")