import yfinance as yf
import numpy as np
import pandas as pd
import talib

class TradingViewIntegration:
    def __init__(self, symbol="SOL-USD"):
        """
        Initialisiert die Integration mit TradingView.
        Diese Klasse verwendet yfinance, um historische Preisdaten zu erhalten
        und technische Indikatoren zu berechnen.
        :param symbol: Das handelbare Symbol (Standard: SOL-USD)
        """
        self.symbol = symbol
        self.data = None
        self.fetch_data()

    def fetch_data(self):
        """
        Holt die historischen Preisdaten von Yahoo Finance (wird hier als Proxy für TradingView verwendet).
        """
        print(f"Hole Daten für {self.symbol}...")
        self.data = yf.download(self.symbol, period="1d", interval="1h")
        print(f"Historische Daten für {self.symbol} erfolgreich geladen.")

    def calculate_technical_indicators(self):
        """
        Berechnet die wichtigsten technischen Indikatoren:
        - RSI (Relative Strength Index)
        - MACD (Moving Average Convergence Divergence)
        - Bollinger Bands
        """
        print(f"Berechne technische Indikatoren für {self.symbol}...")
        
        # Berechnung von RSI
        self.data['RSI'] = talib.RSI(self.data['Close'], timeperiod=14)
        
        # Berechnung von MACD
        self.data['MACD'], self.data['MACD_signal'], _ = talib.MACD(self.data['Close'], fastperiod=12, slowperiod=26, signalperiod=9)
        
        # Berechnung von Bollinger Bands
        self.data['BB_upper'], self.data['BB_middle'], self.data['BB_lower'] = talib.BBANDS(self.data['Close'], timeperiod=20, nbdevup=2, nbdevdn=2, matype=0)
        
        print(f"Technische Indikatoren für {self.symbol} erfolgreich berechnet.")

    def get_indicators(self):
        """
        Gibt die zuletzt berechneten technischen Indikatoren zurück.
        :return: Die Indikatoren (RSI, MACD, Bollinger Bands)
        """
        return {
            'RSI': self.data['RSI'].iloc[-1],
            'MACD': self.data['MACD'].iloc[-1],
            'MACD_signal': self.data['MACD_signal'].iloc[-1],
            'BB_upper': self.data['BB_upper'].iloc[-1],
            'BB_middle': self.data['BB_middle'].iloc[-1],
            'BB_lower': self.data['BB_lower'].iloc[-1]
        }