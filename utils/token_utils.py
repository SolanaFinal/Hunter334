import requests
import json
import time

# Quelle: Jupiter Aggregator API für Solana
TOKEN_LIST_URL = "https://quote-api.jup.ag/v4/tokens"


def fetch_available_tokens():
    try:
        response = requests.get(TOKEN_LIST_URL)
        response.raise_for_status()
        tokens = response.json().get("data", [])
        return tokens
    except Exception as e:
        print(f"[TOKEN] Fehler beim Abrufen verfügbarer Tokens: {e}")
        return []


def get_top_tokens_by_volume(limit=10):
    tokens = fetch_available_tokens()
    if not tokens:
        return []

    # Sortieren nach 24h Volumen (sofern verfügbar)
    sorted_tokens = sorted(tokens, key=lambda t: float(t.get("volume", 0)), reverse=True)
    return sorted_tokens[:limit]


def classify_token(token):
    try:
        if "USDC" in token["symbol"] or "USDT" in token["symbol"]:
            return "stablecoin"
        elif float(token.get("volume", 0)) > 1_000_000:
            return "high-volume"
        else:
            return "low-volume"
    except:
        return "unknown"


def summarize_token(token):
    return {
        "symbol": token.get("symbol", "Unknown"),
        "address": token.get("address", ""),
        "name": token.get("name", "Unknown"),
        "volume": token.get("volume", 0),
        "class": classify_token(token)
    }