import base64
from solana.publickey import PublicKey
from solana.keypair import Keypair
from solana.rpc.api import Client
from solana.transaction import Transaction, TransactionInstruction

# Initialisiere Solana-Client
client = Client("https://api.mainnet-beta.solana.com")

# Lade Keypair aus Private Key String
def load_wallet_from_private_key(private_key_str: str):
    key_bytes = base64.b64decode(private_key_str)
    return Keypair.from_secret_key(key_bytes)


# Erhalte aktuellen SOL Kontostand
def get_sol_balance(pubkey: str) -> float:
    balance = client.get_balance(PublicKey(pubkey))["result"]["value"]
    return balance / 1_000_000_000  # In SOL


# Beispiel: Dummy-Funktion um echten Trade zu simulieren
def execute_sol_transfer(from_wallet: Keypair, to_pubkey: str, amount_sol: float):
    txn = Transaction()
    txn.add(
        TransactionInstruction(
            keys=[],
            program_id=PublicKey("11111111111111111111111111111111"),
            data=bytes(f"SEND {amount_sol} SOL TO {to_pubkey}", "utf-8")
        )
    )
    try:
        response = client.send_transaction(txn, from_wallet)
        return response
    except Exception as e:
        return {"error": str(e)}


# Erkenne, ob gültiger Phantom Private Key vorliegt
def validate_private_key(private_key_str: str) -> bool:
    try:
        load_wallet_from_private_key(private_key_str)
        return True
    except Exception:
        return False