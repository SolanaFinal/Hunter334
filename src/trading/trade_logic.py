import random
from datetime import datetime

class TradeLogic:
    def __init__(self, model, risk_level="medium"):
        """
        Initialisiert die Handelslogik mit dem Modell und Risikoniveau.
        :param model: Das Modell zur Vorhersage von Preistrends (z.B. XGBoost, LSTM)
        :param risk_level: Das Risikoniveau für den Handel (z. B. "low", "medium", "high")
        """
        self.model = model
        self.risk_level = risk_level
        self.trades = []  # Eine Liste, die durchgeführte Trades speichert
        print(f"Handelslogik initialisiert mit Modell: {model.__class__.__name__} und Risikoniveau: {risk_level}")

    def should_trade(self, market_data, sentiment_score):
        """
        Entscheidet, ob ein Handel auf Basis der Markt- und Sentiment-Daten durchgeführt werden sollte.
        :param market_data: Die aktuellen Marktdaten (Preis, Volumen, etc.)
        :param sentiment_score: Der Sentiment-Score (z.B. aus Social Media, Nachrichten)
        :return: Boolescher Wert, ob gehandelt werden sollte
        """
        print(f"Marktdaten erhalten: {market_data}")
        print(f"Sentiment-Score erhalten: {sentiment_score}")

        # Vorhersage des Modells (kann zu "BUY", "SELL" oder "HOLD" führen)
        prediction = self.model.predict([market_data + [sentiment_score]])  # Kombinierte Eingabedaten

        print(f"Modellvorhersage: {prediction}")

        # Entscheide, ob gehandelt werden soll
        if prediction == "BUY":
            print(f"{datetime.now()} - Kaufen empfohlen")
            return True
        elif prediction == "SELL":
            print(f"{datetime.now()} - Verkaufen empfohlen")
            return True
        else:
            print(f"{datetime.now()} - Kein Handel empfohlen")
            return False

    def execute_trade(self, action, amount, token, trade_execution):
        """
        Führt den Handel aus, wenn die Entscheidung getroffen wurde.
        :param action: Die Entscheidung des Modells ("buy", "sell")
        :param amount: Der Betrag, der gehandelt werden soll
        :param token: Der gehandelte Token
        :param trade_execution: Die Instanz der Handelsausführung
        :return: Das Ergebnis der Handelsaktion
        """
        print(f"Handel wird ausgeführt: {action} {amount} {token}")
        if action == "buy":
            return trade_execution.execute_trade("buy", amount, token)
        elif action == "sell":
            return trade_execution.execute_trade("sell", amount, token)
        else:
            return False

    def record_trade(self, action, amount, token, status):
        """
        Speichert den ausgeführten Trade in der Handelshistorie.
        :param action: Die Handelsaktion ("buy", "sell")
        :param amount: Die Menge des gehandelten Tokens
        :param token: Der gehandelte Token
        :param status: Der Status des Trades (z.B. "erfolgreich", "fehlgeschlagen")
        """
        trade_info = {
            "action": action,
            "amount": amount,
            "token": token,
            "status": status,
            "timestamp": datetime.now()
        }
        self.trades.append(trade_info)
        print(f"Handel aufgezeichnet: {trade_info}")

    def get_trade_history(self):
        """
        Gibt die Handelsgeschichte zurück.
        :return: Liste der ausgeführten Trades
        """
        return self.trades