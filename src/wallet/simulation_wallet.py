import random

class SimulationWallet:
    def __init__(self, initial_balance=1000):
        """
        Initialisiert die Simulation-Wallet mit einem Anfangsbetrag.
        :param initial_balance: Anfangsbetrag der Simulation-Wallet (default: 1000)
        """
        self.balance = initial_balance
        self.history = []  # Um vergangene Transaktionen zu speichern

    def execute_trade(self, action, amount, token):
        """
        Führt eine simulierte Handelsaktion aus (kauft oder verkauft Token).
        :param action: Die Handelsaktion ("buy" oder "sell")
        :param amount: Der Betrag, der gehandelt werden soll
        :param token: Der Token, der gehandelt werden soll
        :return: Erfolgsstatus des Trades
        """
        print(f"Simulierter {action.capitalize()} von {amount} {token}...")
        
        if action == "buy":
            if self.balance >= amount:
                self.balance -= amount
                self.history.append(f"BUY {amount} {token}")
                print(f"Erfolgreicher Kauf von {amount} {token}. Neuer Kontostand: {self.balance}")
                return True
            else:
                print("Nicht genug Guthaben für den Kauf!")
                return False
        elif action == "sell":
            self.balance += amount
            self.history.append(f"SELL {amount} {token}")
            print(f"Erfolgreicher Verkauf von {amount} {token}. Neuer Kontostand: {self.balance}")
            return True
        else:
            print(f"Unbekannte Aktion: {action}")
            return False

    def get_balance(self):
        """
        Gibt den aktuellen Kontostand der Simulation-Wallet zurück.
        :return: Aktuellen Kontostand
        """
        return self.balance

    def get_transaction_history(self):
        """
        Gibt die Historie aller Transaktionen der Simulation-Wallet zurück.
        :return: Transaktionsgeschichte
        """
        return self.history