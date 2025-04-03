import requests
from solana.rpc.api import Client
from solana.wallet import Wallet
from solana.transaction import Transaction
from solana.system_program import TransferParams, transfer

# Solana Client und Wallet
class SolanaInteraction:
    def __init__(self, rpc_url: str, private_key: str):
        self.client = Client(rpc_url)
        self.wallet = Wallet(private_key)

    def get_balance(self):
        """ Holt das SOL-Guthaben des Wallets """
        balance = self.client.get_balance(self.wallet.public_key())
        return balance['result']['value'] / 10**9  # SOL in der richtigen Einheit (SOL)

    def send_transaction(self, recipient: str, amount: float):
        """ Sendet SOL von diesem Wallet zu einem anderen Wallet """
        params = TransferParams(
            from_pubkey=self.wallet.public_key(),
            to_pubkey=recipient,
            lamports=int(amount * 10**9)  # Betrag in Lamports
        )
        tx = Transaction()
        tx.add(transfer(params))

        # Signieren und Senden der Transaktion
        signature = self.client.send_transaction(tx, self.wallet)
        return signature

    def check_transaction_status(self, signature: str):
        """ Überprüft den Status einer Transaktion """
        result = self.client.get_confirmed_transaction(signature)
        return result