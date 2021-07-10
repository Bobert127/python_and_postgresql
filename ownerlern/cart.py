class Cart:
    def __init__(self, products):
        self.basket = []

    def add(self, produkt, price):
        self.produkt = produkt
        self.price = price

    def summary(self):