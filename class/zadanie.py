class Price:
    def __init__(self, price):
        self.value = round(float(price), 2)

    @classmethod
    def from_usd(cls, value):
        pln_value = value * 3.8
        return cls(pln_value)

    @classmethod
    def from_eur(cls, value):
        pln_value = value * 4.5
        return cls(pln_value)

    def __str__(self):
        return f"{self.value}zł"

    # @classmethod and @staticmethod playground starts here
    # instance method
    def summary(self):
        print(self)

    @classmethod
    def from_price_with_too_many_fraction_numbers(cls, s):
        # input parameters are not som important (except, the first one is the class object)
        s = s[:-1]
        num = float(s)
        # but here, we call the constructor, so the parameters are important
        return cls(num)

    @staticmethod
    def exchange_money(amount, rate):
        return amount * rate

if __name__ == '__main__':
    money = Price(200)
    money.summary()

    money2 = Price.from_eur(1)
    print(money2)
    money3 = money.from_eur(1)
    print(money3)

    print(Price.exchange_money(1, 2))
    print(money.exchange_money(1, 2))

    money4 = Price.from_price_with_too_many_fraction_numbers('10.32')
    print(money4)