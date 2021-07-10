class Cart:
    def __init__(self, products):
        self.products = products

    def add(self, name, price):
        self.name = str(name)
        self.price = float(price)

    def summary(self):
        return self.products


