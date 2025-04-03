import matplotlib.pyplot as plt
import os
import json
from datetime import datetime

def visualize_learning_progress(log_path="logs/learning_metrics.json"):
    if not os.path.exists(log_path):
        print("[VISUALIZER] Lernmetriken-Datei nicht gefunden.")
        return

    with open(log_path, "r") as f:
        data = json.load(f)

    if not data:
        print("[VISUALIZER] Keine Daten zum Anzeigen.")
        return

    timestamps = [datetime.strptime(entry["timestamp"], "%Y-%m-%dT%H:%M:%S") for entry in data]
    accuracy = [entry["xgb_accuracy"] for entry in data]
    risk_score = [entry["risk_score"] for entry in data]
    sentiment = [entry["sentiment"] for entry in data]

    plt.figure(figsize=(12, 6))
    plt.plot(timestamps, accuracy, label="XGBoost-Accuracy", marker="o")
    plt.plot(timestamps, risk_score, label="Risiko-Bewertung", linestyle="--")
    plt.plot(timestamps, sentiment, label="Durchschnittlicher Sentiment-Score", linestyle=":")

    plt.xlabel("Zeit")
    plt.ylabel("Wert")
    plt.title("Hunter-Lernfortschritt")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()