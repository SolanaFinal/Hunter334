import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
from xgboost import XGBClassifier
import random
import time

class StrategyOptimizer:
    def __init__(self, model=None):
        """
        Initialisiert den Optimizer mit einem Modell.
        """
        self.model = model if model else XGBClassifier(use_label_encoder=False, eval_metric="mlogloss")
        self.scaler = StandardScaler()

    def optimize(self, features, labels):
        """
        Optimiert die Handelsstrategie auf Basis der gegebenen Features und Labels.
        :param features: Eingabedaten (Features) für das Modell
        :param labels: Zielvariablen (Labels)
        """
        # Daten aufteilen: 80% Training, 20% Test
        X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)

        # Daten skalieren
        X_train = self.scaler.fit_transform(X_train)
        X_test = self.scaler.transform(X_test)

        # Modell trainieren
        self.model.fit(X_train, y_train)

        # Vorhersage und Genauigkeit
        predictions = self.model.predict(X_test)
        accuracy = accuracy_score(y_test, predictions)

        print(f"Optimierungs-Genauigkeit: {accuracy * 100:.2f}%")

        return self.model

    def predict(self, data):
        """
        Gibt eine Vorhersage basierend auf den trainierten Modellen.
        :param data: Neue Eingabedaten für die Vorhersage
        :return: Vorhersage
        """
        data_scaled = self.scaler.transform(data)
        return self.model.predict(data_scaled)

    def simulate_trade(self, action, amount, token):
        """
        Simuliert den Handel, um die Performance des Optimierers zu testen.
        """
        print(f"Optimierungs-Trade simuliert: {action} {amount} {token}")
        time.sleep(random.uniform(1, 2))  # Simuliert eine zufällige Zeit für den Handel
        print(f"Optimierungs-Trade abgeschlossen: {action} {amount} {token}")