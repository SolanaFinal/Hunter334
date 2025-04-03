import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import xgboost as xgb
import joblib

class LearningModule:
    def __init__(self, model_path="model/xgb_model.pkl"):
        """
        Initialisiert das Lernmodul mit einem bestehenden Modell (oder lädt ein neues Modell).
        :param model_path: Pfad zu einem bestehenden XGBoost-Modell.
        """
        self.model_path = model_path
        self.model = None
        self.load_model()

    def load_model(self):
        """
        Lädt das Modell aus der Datei.
        """
        try:
            self.model = joblib.load(self.model_path)
            print(f"Modell erfolgreich geladen von {self.model_path}")
        except Exception as e:
            print(f"Fehler beim Laden des Modells: {e}")
            self.model = None

    def train_model(self, data, labels):
        """
        Trainiert ein neues Modell.
        :param data: Die Eingabedaten für das Modell.
        :param labels: Die zugehörigen Labels.
        """
        print("Training des Modells...")
        X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, random_state=42)
        
        self.model = xgb.XGBClassifier(use_label_encoder=False, eval_metric="mlogloss")
        self.model.fit(X_train, y_train)

        # Modell speichern
        joblib.dump(self.model, self.model_path)
        print(f"Modell erfolgreich trainiert und gespeichert an {self.model_path}")

        # Modell bewerten
        y_pred = self.model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        print(f"Modellgenauigkeit: {accuracy:.4f}")

    def predict(self, data):
        """
        Gibt die Vorhersage des Modells für die Eingabedaten zurück.
        :param data: Eingabedaten für die Vorhersage.
        :return: Vorhersage des Modells.
        """
        if self.model:
            return self.model.predict(data)
        else:
            print("Modell nicht geladen.")
            return None

    def save_model(self):
        """
        Speichert das aktuelle Modell.
        """
        if self.model:
            joblib.dump(self.model, self.model_path)
            print(f"Modell gespeichert an {self.model_path}")
        else:
            print("Kein Modell zum Speichern.")