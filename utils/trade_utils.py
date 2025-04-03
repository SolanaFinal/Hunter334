import random
import time

# Simuliere Fees für eine Transaktion (für die Fake Wallet)
def estimate_fees(token_symbol: str) -> float:
    if token_symbol.upper() in ["SOL", "USDC", "USDT"]:
        return 0.0005
    return 0.001 + random.uniform(0.0001, 0.0005)


# Simuliere einen Preis für einen Trade (z. B. in der Simulation)
def get_simulated_price_change(price: float, volatility: float = 0.01) -> float:
    fluctuation = random.uniform(-volatility, volatility)
    return price * (1 + fluctuation)


# Simuliere einen einfachen Trade (BUY/SELL) in der Fake Wallet
def simulate_trade(balance: float, price: float, direction: str, fees: float) -> float:
    if direction == "BUY":
        amount = (balance - fees) / price
    elif direction == "SELL":
        amount = (balance * price) - fees
    else:
        amount = balance
    return round(amount, 6)


# Zeitformatierung für Logs
def timestamp():
    return time.strftime("[%Y-%m-%d %H:%M:%S]", time.localtime())