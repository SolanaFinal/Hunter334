  def get_balance(self, public_key: str):
        """
        Holt den aktuellen Kontostand eines Solana-Kontos
        :param public_key: Die öffentliche Adresse des Solana-Kontos
        :return: Der Kontostand in SOL
        """
        balance = self.client.get_balance(public_key)
        return balance['result']['value'] / 1e9  # SOL-Betrag

    def transfer(self, recipient: str, amount: float):
        """
        Transferiert SOL von der Wallet an eine andere Adresse
        :param recipient: Die öffentliche Adresse des Empfängers
        :param amount: Die Menge SOL, die überwiesen werden soll
        :return: Transaktionsbestätigung
        """
        sender_public_key = self.wallet.public_key()
        transaction = Transaction()

        # Transaktionsparameter
        transfer_instruction = transfer(
            TransferParams(
                from_pubkey=sender_public_key,
                to_pubkey=recipient,
                lamports=int(amount * 1e9)  # SOL -> lamports
            )
        )

        transaction.add(transfer_instruction)

        # Sende die Transaktion
        result = self.client.send_transaction(transaction, self.wallet)
        return result

    def get_transaction_status(self, transaction_signature: str):
        """
        Überprüft den Status einer gesendeten Transaktion
        :param transaction_signature: Die Transaktionssignatur
        :return: Status der Transaktion
        """
        result = self.client.get_confirmed_transaction(transaction_signature)
        return result['result']