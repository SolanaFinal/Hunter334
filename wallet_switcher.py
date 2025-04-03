import json
import os

CONFIG_PATH = "config/wallet_mode.json"

def load_wallet_mode():
    if not os.path.exists(CONFIG_PATH):
        return "simulation"

    with open(CONFIG_PATH, "r") as f:
        data = json.load(f)
        return data.get("mode", "simulation")

def save_wallet_mode(mode):
    os.makedirs(os.path.dirname(CONFIG_PATH), exist_ok=True)
    with open(CONFIG_PATH, "w") as f:
        json.dump({"mode": mode}, f)

def is_simulation():
    return load_wallet_mode() == "simulation"

def toggle_wallet_mode():
    current_mode = load_wallet_mode()
    new_mode = "real" if current_mode == "simulation" else "simulation"
    save_wallet_mode(new_mode)
    print(f"[WALLET] Modus gewechselt zu: {new_mode}")
    return new_mode