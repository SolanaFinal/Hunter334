import yfinance as yf
import talib
import pandas as pd

class TradingViewIntegration:
    def __init__(self, symbol="SOL-USD", period="1d", interval="1h"):
        """
        Initialisiert die Verbindung zu TradingView oder einer anderen Quelle für technische Indikatoren.
        :param symbol: Der gehandelte Token (Standard: "SOL-USD")
        :param period: Der Zeitraum, für den die Daten abgerufen werden sollen (Standard: "1d")
        :param interval: Das Zeitintervall für die Kursdaten (Standard: "1h")
        """
        self.symbol = symbol
        self.period = period
        self.interval = interval
        self.data = None
        print(f"TradingView Integration initialisiert für {symbol}.")

    def fetch_data(self):
        """
        Holt die historischen Kursdaten von TradingView (über yfinance) und berechnet technische Indikatoren.
        """
        print(f"Hole Daten für {self.symbol}...")
        self.data = yf.download(self.symbol, period=self.period, interval=self.interval)
        self.calculate_indicators()

    def calculate_indicators(self):
        """
        Berechnet technische Indikatoren wie RSI, MACD, etc. für die Daten.
        """
        if self.data is not None:
            # Berechnung des RSI (Relative Strength Index)
            self.data['RSI'] = talib.RSI(self.data['Close'], timeperiod=14)

            # Berechnung des MACD (Moving Average Convergence Divergence)
            self.data['MACD'], self.data['MACD_signal'], _ = talib.MACD(self.data['Close'], fastperiod=12, slowperiod=26, signalperiod=9)

            # Berechnung der Bollinger Bands
            self.data['BB_upper'], self.data['BB_middle'], self.data['BB_lower'] = talib.BBANDS(self.data['Close'], timeperiod=20)

            print(f"Technische Indikatoren berechnet: RSI, MACD, Bollinger Bands.")
        else:
            print(f"Fehler: Keine Kursdaten vorhanden!")

    def get_indicators(self):
        """
        Gibt die technischen Indikatoren zurück.
        :return: DataFrame mit technischen Indikatoren.
        """
        if self.data is not None:
            return self.data[['RSI', 'MACD', 'MACD_signal', 'BB_upper', 'BB_middle', 'BB_lower']]
        else:
            print(f"Fehler: Keine Indikatoren berechnet!")
            return None

    def display_indicators(self):
        """
        Zeigt die letzten berechneten Indikatoren an.
        """
        indicators = self.get_indicators()
        if indicators is not None:
            print(indicators.tail())  # Zeigt die letzten Indikatoren
        else:
            print("Fehler beim Anzeigen der Indikatoren!")