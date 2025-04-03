import numpy as np

def detect_sandwich_pattern(trade_log, window=3, threshold=0.01):
    """
    Überprüft, ob in den letzten Trades ein Sandwich-Muster zu erkennen ist.
    Ein Sandwich-Muster kann auf MEV-Angriffe hindeuten.
    """
    if len(trade_log) < window:
        return False

    recent_trades = trade_log[-window:]
    amounts = [abs(trade["amount"]) for trade in recent_trades]

    mean_amount = np.mean(amounts)
    deviations = [abs(a - mean_amount) / mean_amount for a in amounts]

    suspicious = all(dev < threshold for dev in deviations)

    if suspicious:
        print("[MEV-DETECTOR] Möglicher Sandwich-Angriff erkannt!")
    return suspicious