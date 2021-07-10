class Food:
    def __init__(self, name: str, bialko: float, tluszcz: float, weglowodany: float):
        self.name = name
        self.bialko = bialko
        self.tluszcz = tluszcz
        self.weglowodany = weglowodany
    def print_food(self):
        print(self.name)
        print(self.bialko)
        print(self.tluszcz)
        print(self.weglowodany)


class Discount20PercentCart(Food):
    def __init__(self, name: str, bialko: float, tluszcz: float, weglowodany: float, posilek: str):
        super().__init__(name, bialko, tluszcz, weglowodany)
        self.posilek = posilek

    def print_posilek(self):
        super().print_posilek()
        print(self.posilek)

obiad = Discount20PercentCart('bred', 100, 120, 150,'sniadanie')
obiad.print_food()