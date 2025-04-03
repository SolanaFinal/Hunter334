
import json
import pandas as pd
import joblib
from xgboost import XGBClassifier
import time

def train_new_model():
    try:
        with open("memory.json", "r") as f:
            memory = json.load(f)
    except FileNotFoundError:
        print("[LEARNING] Keine Gedächtnisdaten vorhanden.")
        return

    if not memory:
        print("[LEARNING] Gedächtnis ist leer.")
        return

    # Daten vorbereiten
    df = pd.DataFrame([{
        **item["inputs"],
        "action": item["action"]
    } for item in memory])

    # Ziel (Label) umwandeln
    action_map = {"HOLD": 0, "BUY": 1, "SELL": 2}
    df["action"] = df["action"].map(action_map)

    X = df.drop("action", axis=1)
    y = df["action"]

    # Neues Modell trainieren
    model = XGBClassifier(use_label_encoder=False, eval_metric="mlogloss")
    model.fit(X, y)

    # Modell speichern
    joblib.dump(model, "model/xgb_model.pkl")
    print("[LEARNING] Neues Modell wurde erfolgreich trainiert & gespeichert.")

if __name__ == "__main__":
    while True:
        train_new_model()
        print("[LEARNING] Warte 10 Minuten auf nächste Lernrunde...")
        time.sleep(600)  # 10 Minuten
