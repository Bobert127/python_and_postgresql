class BankAccount:

    def __init__(self, number, cash=0.0):
        self.number = number
        self.cash = cash

    def deposit_cash(self, amount):
        self.cash += amount
        return

    def withdraw_cash(self, amount):
        self.cash -= amount
        return

    def print_info(self):
        print(self.number, self.cash)


if __name__ == '__main__':
    a = BankAccount(5111255243, 300.0)
    b = a.deposit_cash(377)
    c = a.withdraw_cash(666.0)

    print(a.print_info())
