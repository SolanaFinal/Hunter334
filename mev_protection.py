import random

def detect_mev_patterns(trade_history):
    warnings = []
    if len(trade_history) < 3:
        return warnings

    for i in range(len(trade_history) - 2):
        t1, t2, t3 = trade_history[i:i+3]
        if (
            t1["amount"] == t3["amount"]
            and t1["token"] == t3["token"]
            and t2["token"] != t1["token"]
            and t2["type"] == "BUY"
            and t1["type"] == "SELL"
            and t3["type"] == "BUY"
        ):
            warnings.append(
                f"[MEV WARNING] Verdächtiges Sandwich-Muster entdeckt zwischen {t1['token']} und {t2['token']}."
            )
    return warnings

def simulate_mev_check():
    fake_history = [
        {"token": "SOL", "type": "SELL", "amount": 10},
        {"token": "BONK", "type": "BUY", "amount": 99999},
        {"token": "SOL", "type": "BUY", "amount": 10},
    ]
    return detect_mev_patterns(fake_history)