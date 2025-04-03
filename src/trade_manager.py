import time
import random
from datetime import datetime
from learning_module import LearningModule
from trade_execution import TradeExecution

class TradeManager:
    def __init__(self, solana_client, wallet, learning_module, trade_execution, token="SOL"):
        """
        Initialisiert den TradeManager, der das Lernen und die Handelsausführung kombiniert.
        :param solana_client: Die Solana-Client-Verbindung.
        :param wallet: Die Wallet, die den Handel ausführt.
        :param learning_module: Das Lernmodul, das Vorhersagen trifft.
        :param trade_execution: Die Handelsausführungseinheit, die den Handel auf der Blockchain ausführt.
        :param token: Der gehandelte Token (Standard: SOL).
        """
        self.solana_client = solana_client
        self.wallet = wallet
        self.learning_module = learning_module
        self.trade_execution = trade_execution
        self.token = token

    def manage_trade(self):
        """
        Verwalte den Handelsprozess: Vorhersagen treffen, entscheiden und handeln.
        """
        while True:
            # Sammeln der aktuellen Marktdaten (Platzhalter)
            current_data = self.collect_market_data()
            
            # Vorhersage durch das Modell
            prediction = self.learning_module.predict([current_data])
            
            # Handel basierend auf der Vorhersage (buy/sell)
            if prediction == 1:
                self.execute_trade("buy", random.randint(1, 10))  # Hier könnte die Menge angepasst werden
            else:
                self.execute_trade("sell", random.randint(1, 10))  # Hier könnte die Menge angepasst werden

            # Warten vor dem nächsten Handel
            time.sleep(10)  # Zum Beispiel alle 10 Sekunden handeln

    def collect_market_data(self):
        """
        Simuliert die Sammlung von Marktdaten (z.B. von TradingView oder Solana).
        :return: Ein Array von Daten, das als Eingabe für das Modell verwendet wird.
        """
        # Beispiel-Daten, hier könnten echte Marktdaten abgefragt werden
        market_data = [random.random() for _ in range(5)]  # Dummy-Daten für 5 Merkmale
        return market_data

    def execute_trade(self, action, amount):
        """
        Führt die Handelsentscheidung aus.
        :param action: Die Handelsaktion ("buy" oder "sell").
        :param amount: Der Betrag, der gehandelt werden soll.
        """
        trade_success = self.trade_execution.execute_trade(action, amount, self.token)
        
        if trade_success:
            print(f"{datetime.now()} - Handel {action} von {amount} {self.token} erfolgreich!")
        else:
            print(f"{datetime.now()} - Handel fehlgeschlagen.")