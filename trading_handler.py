
import datetime

def execute_trade(action):
    timestamp = datetime.datetime.utcnow().isoformat()
    log_entry = f"[{timestamp}] Executing trade: {action}"

    # In Konsole ausgeben
    print(log_entry)

    # In Datei schreiben
    with open("trades.log", "a") as f:
        f.write(log_entry + "\n")

    # Placeholder: Hier kann später echter Solana-Trade folgen
    # z. B. über Phantom Wallet Handler
