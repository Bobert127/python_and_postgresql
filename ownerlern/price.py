class Price:
    def __int__(self, price: float):
        self.value = round(float(price),2)

    def EURO(self, price_euro):
        value = price_euro * 3.8
        return f'{value}zł'

    def USA(self, price_usa):
        value = price_usa * 3.8
        return f'{value}zł'

    def __str__(self):
        return f'The price is round({self.value},2)'

a = Price()
print(a.EURO(100))
print(a.USA(117.77))
