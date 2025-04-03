import numpy as np
import pandas as pd
import yfinance as yf
import talib
from datetime import datetime

class StrategyOptimizer:
    def __init__(self, token="SOL", data_source="yfinance"):
        """
        Initialisiert den Strategieoptimierer.
        :param token: Der Token, mit dem gehandelt wird (Standard: SOL)
        :param data_source: Die Quelle der Marktdaten (Standard: yfinance)
        """
        self.token = token
        self.data_source = data_source
        self.data = None
        self.features = None
        self.target = None
        self.load_data()

    def load_data(self):
        """
        Lädt historische Marktdaten für den ausgewählten Token.
        """
        if self.data_source == "yfinance":
            self.data = yf.download(f"{self.token}-USD", period="6mo", interval="1d")
            print(f"Marktdaten für {self.token} heruntergeladen.")
        else:
            print("Datenquelle nicht unterstützt.")

    def add_technical_indicators(self):
        """
        Fügt technische Indikatoren zum Datensatz hinzu, z. B. RSI, MACD, Bollinger Bands.
        """
        print("Füge technische Indikatoren hinzu...")
        
        # RSI
        self.data['RSI'] = talib.RSI(self.data['Close'], timeperiod=14)
        
        # MACD
        self.data['MACD'], self.data['MACD_signal'], _ = talib.MACD(self.data['Close'], fastperiod=12, slowperiod=26, signalperiod=9)
        
        # Bollinger Bands
        self.data['BB_upper'], self.data['BB_middle'], self.data['BB_lower'] = talib.BBANDS(self.data['Close'], timeperiod=20)
        
        print("Technische Indikatoren hinzugefügt.")

    def create_features_and_target(self):
        """
        Erstellt Merkmale (Features) und Zielwerte (Target) für das Modell.
        """
        print("Erstelle Merkmale und Zielwerte...")
        
        # Features: RSI, MACD, Bollinger Bands
        self.features = self.data[['RSI', 'MACD', 'MACD_signal', 'BB_upper', 'BB_middle', 'BB_lower']].shift(1).dropna()
        
        # Target: Kauf- oder Verkaufsaktion basierend auf dem Schlusskurs
        self.target = (self.data['Close'].shift(-1) > self.data['Close']).dropna().astype(int)
        
        print("Merkmale und Zielwerte erstellt.")

    def optimize_strategy(self):
        """
        Optimiert die Handelsstrategie basierend auf technischen Indikatoren.
        """
        print("Optimiere Handelsstrategie...")
        
        self.add_technical_indicators()
        self.create_features_and_target()
        
        # Einfacher Optimierungsansatz: Handel basierend auf RSI (überkauft/überverkauft)
        self.features['RSI_signal'] = np.where(self.features['RSI'] > 70, -1, np.where(self.features['RSI'] < 30, 1, 0))
        self.features['Target'] = self.target
        
        print("Strategie optimiert.")

    def evaluate_strategy(self):
        """
        Evaluierung der Strategie: Backtest oder Erfolgsmetriken
        """
        print("Evaluierung der Strategie...")
        
        # Einfache Bewertung: Genauigkeit der Vorhersage
        correct_predictions = (self.features['RSI_signal'] == self.features['Target']).sum()
        total_predictions = len(self.features)
        
        accuracy = correct_predictions / total_predictions
        print(f"Strategiegenauigkeit: {accuracy:.2f}")
        
        return accuracy

    def run(self):
        """
        Führt den Optimierungs- und Evaluierungsprozess aus.
        """
        self.optimize_strategy()
        accuracy = self.evaluate_strategy()
        return accuracy