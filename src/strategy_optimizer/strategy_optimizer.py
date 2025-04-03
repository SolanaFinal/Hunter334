import random
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

class StrategyOptimizer:
    def __init__(self, historical_data):
        """
        Initialisiert den Optimierer mit historischen Marktdaten.
        :param historical_data: Die historischen Marktdaten für die Strategieanalyse.
        """
        self.historical_data = historical_data
        self.model = LinearRegression()
        print("Strategieoptimierung initialisiert.")

    def optimize_strategy(self):
        """
        Optimiert die Handelsstrategie basierend auf historischen Daten.
        :return: Optimierte Strategien (Gewichte und Metriken).
        """
        # Extrahiere Merkmale und Zielgrößen aus den historischen Daten
        X = np.array([data['features'] for data in self.historical_data])  # Merkmale (z.B. RSI, MACD, etc.)
        y = np.array([data['target'] for data in self.historical_data])  # Zielgröße (z.B. Preisveränderung)

        # Teile die Daten in Trainings- und Testsets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Trainiere das Modell
        self.model.fit(X_train, y_train)

        # Vorhersagen machen
        predictions = self.model.predict(X_test)

        # Berechne die Fehler (z.B. Mean Squared Error)
        mse = mean_squared_error(y_test, predictions)
        print(f"Optimierte Strategie-MSE: {mse}")
        
        return self.model.coef_, mse

    def predict(self, features):
        """
        Nutzt das trainierte Modell, um die Marktentwicklung vorherzusagen.
        :param features: Die Merkmale, die für die Vorhersage verwendet werden.
        :return: Vorhergesagte Preisänderung.
        """
        prediction = self.model.predict([features])
        return prediction[0]