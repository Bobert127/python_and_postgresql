class BankAccount:
    def __init__(self, number, cash=0.0):
        self.number = number
        self.cash = cash

    def deposit_cash(self, amount):
        result = self.cash + amount
        return result

    def print_info(self):
        print(f'konto o {self.number} i stanie {deposit_cash.result}')


a = BankAccount(225, 200)

a.deposit_cash(2020)
a.print_info()



