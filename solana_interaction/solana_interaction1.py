import solana
from solana.account import Account
from solana.rpc.api import Client
from solana.system_program import TransferParams, transfer

class SolanaInteraction:
    def __init__(self, is_real_wallet=False, private_key=None):
        self.is_real_wallet = is_real_wallet
        self.client = Client("https://api.mainnet-beta.solana.com")  # Solana Mainnet
        self.private_key = private_key
        self.account = None
        if self.is_real_wallet:
            self.account = Account(private_key)
        else:
            self.account = Account()

    def get_balance(self):
        """ Returns the balance of the wallet """
        response = self.client.get_balance(self.account.public_key())
        return response['result']['value']

    def send_transaction(self, recipient, amount):
        """ Sends a transaction """
        transfer_txn = transfer(
            TransferParams(
                from_pubkey=self.account.public_key(),
                to_pubkey=recipient,
                lamports=amount  # Lamports are smallest units of SOL (1 SOL = 10^9 Lamports)
            )
        )
        transaction = self.client.send_transaction(transfer_txn, self.account)
        return transaction

    def switch_wallet(self, new_private_key):
        """ Switches to a new wallet by updating the private key """
        self.private_key = new_private_key
        self.account = Account(self.private_key)
        print(f"Wallet switched to new private key: {self.account.public_key()}")