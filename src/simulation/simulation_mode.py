import random
from datetime import datetime

class SimulationMode:
    def __init__(self, initial_balance=1000):
        """
        Initialisiert den Simulationsmodus des Bots.
        :param initial_balance: Der Startsaldo für die Simulation.
        """
        self.balance = initial_balance
        self.transaction_history = []
        print(f"Simulationsmodus gestartet mit {self.balance} USD.")

    def execute_simulated_trade(self, action, amount, token):
        """
        Führt einen simulierten Handel aus.
        :param action: Die Handelsaktion ("buy" oder "sell").
        :param amount: Der Betrag, der gehandelt werden soll.
        :param token: Der Token, der gehandelt werden soll.
        :return: Erfolgsstatus des simulierten Handels.
        """
        print(f"Simulierter Handel: {action} {amount} {token}")
        
        # Hier könnten auch komplexere Handelslogiken implementiert werden
        if random.random() > 0.1:  # 90% Chance, dass der Handel "erfolgreich" ist
            print(f"Simulierter {action.capitalize()} von {amount} {token} erfolgreich!")
            self.update_balance(action, amount)
            self.transaction_history.append((action, amount, token, datetime.now()))
            return True
        else:
            print(f"Simulierter Handel fehlgeschlagen!")
            return False

    def update_balance(self, action, amount):
        """
        Aktualisiert den Kontostand nach einem Handel.
        :param action: Die Handelsaktion ("buy" oder "sell").
        :param amount: Der Betrag, der gehandelt wurde.
        """
        if action == "buy":
            self.balance -= amount
        elif action == "sell":
            self.balance += amount
        print(f"Aktueller Kontostand: {self.balance} USD.")

    def get_balance(self):
        """
        Gibt den aktuellen Kontostand zurück.
        :return: Der aktuelle Kontostand.
        """
        return self.balance

    def get_transaction_history(self):
        """
        Gibt die Historie der Handelsgeschäfte zurück.
        :return: Liste der Transaktionen.
        """
        return self.transaction_history