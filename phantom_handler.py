import random

class WalletSimulator:
    def __init__(self, start_balance=100.0):
        self.balance = start_balance
        self.tokens = {"SOL": start_balance}
        self.trade_log = []

    def get_balance(self, token="SOL"):
        return self.tokens.get(token, 0)

    def simulate_trade(self, token_in, token_out, amount):
        if self.get_balance(token_in) >= amount:
            self.tokens[token_in] -= amount
            received_amount = amount * random.uniform(0.9, 1.1)
            self.tokens[token_out] = self.tokens.get(token_out, 0) + received_amount
            self.trade_log.append((token_in, token_out, amount, received_amount))
            return True, received_amount
        return False, 0

    def get_trade_log(self):
        return self.trade_log

class PhantomWalletHandler:
    def __init__(self, private_key=None):
        self.simulation_mode = private_key is None
        if self.simulation_mode:
            self.sim_wallet = WalletSimulator()
        else:
            self.private_key = private_key
            # TODO: Integrate with actual Phantom wallet libraries

    def get_balance(self, token="SOL"):
        if self.simulation_mode:
            return self.sim_wallet.get_balance(token)
        else:
            # TODO: Use real wallet logic here
            return 0

    def execute_trade(self, token_in, token_out, amount):
        if self.simulation_mode:
            return self.sim_wallet.simulate_trade(token_in, token_out, amount)
        else:
            # TODO: Real trade logic with Phantom wallet
            return False, 0

    def get_trade_log(self):
        if self.simulation_mode:
            return self.sim_wallet.get_trade_log()
        return []