class Test:
    def __init__(self, bok):
        self.bok = bok

    def obwod(self):
        a = 4 * self.bok
        return a

    def display(self):
        print(f'kwadra o {self.bok} ma obwód {self.obwod()}')


kwadrat = Test(17)
kwadrat.display()
