class Product:
    def __init__(self, name, price):
        self.id = id
        self.name = name
        self.price = price


class ShoppingCart:
    def __init__(self):
        products = {id: 'self.id', product: 'Product'}
        quantities = {id: 'id', guantitie: 'Quantitie'}

    def add_product(self, product):
        product[1] = [name, price]


class Robert:
    def __init__(self, bok):
        self._bok = bok
        self.pole = bok ** 2
        self.obwod = bok * 4

    def get_bok(self):
        return self._bok

    @property
    def bok(self):
        return self.get_bok()

    @bok.setter
    def bok(self, new_bok):
        self._bok = new_bok
        self.pole = new_bok ** 2
        self.obwod = new_bok * 4


a = Robert(15)
print(a.pole)
print(a.obwod)




