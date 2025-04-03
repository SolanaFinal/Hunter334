import random
from solana.publickey import PublicKey
from solana.keypair import Keypair
from solana.transaction import Transaction

class SimulationWallet:
    def __init__(self, starting_balance=1000000000):
        # Startbalance von 1.000.000 SOL (simuliert)
        self.balance = starting_balance
        self.keypair = Keypair()
        self.public_key = self.keypair.public_key

    # Zeigt den aktuellen Stand der Simulations-Wallet
    def get_balance(self):
        return self.balance / 1_000_000_000  # SOL

    # Simuliert den Handel (z. B. ein Trade zwischen zwei Token)
    def simulate_trade(self, amount_sol: float, transaction_type: str):
        if transaction_type == 'BUY':
            self.balance -= amount_sol * 1_000_000_000  # Einkaufen
        elif transaction_type == 'SELL':
            self.balance += amount_sol * 1_000_000_000  # Verkaufen

    # Zeigt eine zufällige Simulation der Performance des Trades an
    def simulate_trade_performance(self):
        # Beispiel: Zufälliger Verlust oder Gewinn im Simulationshandel
        performance = random.uniform(0.98, 1.02)  # Veränderung zwischen 2% Gewinn und Verlust
        return performance

# Funktion für das Umschalten zwischen echter und simulierter Wallet
def switch_wallet_to_simulation():
    return SimulationWallet()