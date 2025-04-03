import requests
import random

def fetch_onchain_stats():
    try:
        # Wir nutzen public RPC für Demo-Zwecke. In Produktion lieber einen eigenen Node oder Anbieter wie QuickNode.
        url = "https://api.mainnet-beta.solana.com"
        headers = {"Content-Type": "application/json"}

        payload = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "getRecentPerformanceSamples",
            "params": [5],
        }

        response = requests.post(url, headers=headers, json=payload)
        data = response.json()

        samples = data.get("result", [])
        if not samples:
            return 0.0, "Keine On-Chain Daten verfügbar"

        avg_tx_per_sec = sum([sample["numTransactions"] / sample["samplePeriodSecs"] for sample in samples]) / len(samples)

        # Dummy-Logik zur Einschätzung
        if avg_tx_per_sec > 4000:
            sentiment = 0.7
            info = f"Hohe Aktivität (~{int(avg_tx_per_sec)} tx/s)"
        elif avg_tx_per_sec > 2000:
            sentiment = 0.3
            info = f"Normale Aktivität (~{int(avg_tx_per_sec)} tx/s)"
        else:
            sentiment = -0.2
            info = f"Niedrige Aktivität (~{int(avg_tx_per_sec)} tx/s)"

        return sentiment, info

    except Exception as e:
        print(f"[ONCHAIN] Fehler: {e}")
        return 0.0, f"Fehler beim Abruf: {e}"