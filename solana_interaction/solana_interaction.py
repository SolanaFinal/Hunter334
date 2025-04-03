from solana.rpc.api import Client
from solana.publickey import PublicKey
from solana.wallet import Wallet
from solana.transaction import Transaction
from solana.system_program import transfer
import time

# Solana-RPC-Client initialisieren
rpc_client = Client("https://api.mainnet-beta.solana.com")

# Funktionen zum Abrufen des Kontostands
def get_balance(wallet_address: str):
    """
    Gibt den Kontostand einer Solana-Adresse zurück.
    """
    balance = rpc_client.get_balance(PublicKey(wallet_address))
    if balance["result"]:
        return balance["result"]["value"] / 1_000_000_000  # In SOL
    else:
        print("Fehler beim Abrufen des Kontostands")
        return None

# Funktion zum Senden von SOL
def send_sol(from_wallet: Wallet, to_address: str, amount: float):
    """
    Sendet SOL von einem Wallet zu einer anderen Adresse.
    """
    try:
        to_pubkey = PublicKey(to_address)
        transaction = Transaction()
        transaction.add(transfer(
            from_pubkey=from_wallet.public_key(),
            to_pubkey=to_pubkey,
            lamports=int(amount * 1_000_000_000)  # Umrechnung in Lamports
        ))
        # Signiere die Transaktion mit dem Wallet
        signed_transaction = from_wallet.sign_transaction(transaction)
        # Sende die Transaktion
        response = rpc_client.send_transaction(signed_transaction)
        return response
    except Exception as e:
        print(f"Fehler beim Senden von SOL: {e}")
        return None

# Funktion zum Überprüfen der Transaktionsbestätigung
def wait_for_confirmation(transaction_signature: str):
    """
    Wartet auf die Bestätigung einer abgeschickten Transaktion.
    """
    print(f"Warte auf Bestätigung der Transaktion {transaction_signature}...")
    while True:
        result = rpc_client.get_transaction(transaction_signature)
        if result["result"] and result["result"]["meta"]["status"]["Ok"]:
            print("Transaktion bestätigt!")
            break
        time.sleep(1)

# Wallet-Interaktion
def create_wallet():
    """
    Erstellt ein neues Solana-Wallet und gibt den privaten und öffentlichen Schlüssel zurück.
    """
    wallet = Wallet.generate()
    return wallet

# Beispiel zum Abrufen des Kontostands und Senden von SOL
if __name__ == "__main__":
    # Beispiel-Adresse und Wallet
    wallet = create_wallet()
    print(f"Wallet-Adresse: {wallet.public_key()}")
    print(f"Wallet-Balance: {get_balance(wallet.public_key())} SOL")
    
    # Sende Transaktion (nur zu Testzwecken)
    recipient_address = "Empfänger-Adresse-hier-einfügen"  # Ersetze dies mit einer gültigen Solana-Adresse
    amount = 0.1  # Beispielbetrag
    transaction_response = send_sol(wallet, recipient_address, amount)
    if transaction_response:
        print(f"Transaktionsantwort: {transaction_response}")
        transaction_signature = transaction_response.get("result")
        wait_for_confirmation(transaction_signature)