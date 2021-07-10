class Price23Vat:
    def __init__(self, brutto):
        self._brutto = brutto
        self._netto = netto = round((self._brutto / 1.23),2)
        self._vat = round((self._brutto*23/123),2)

    def get_netto(self):
        return self._netto

    def get_vat(self):
        return self._vat



a = Price23Vat(100.17)

print(a.get_netto())
print(a.get_vat())


class Price23Vat:
    def __init__(self, brutto):
        self._brutto = brutto
        self._tax = self._brutto * 0.23
        self._netto = self._brutto - self._tax

    def get_netto(self):
        return self._netto

    @property
    def netto(self):
        return self._netto

    @netto.setter
    def netto(self, value):
        self._brutto = value / 0.77
        self._netto = value
        self._tax = self._brutto * 0.23
        return

    @property
    def brutto(self):
        return self._brutto

    @brutto.setter
    def brutto(self, value):
        self._brutto = value
        self._tax = self._brutto * 0.23
        self._netto = self._brutto - self._tax
        return

    @property
    def tax(self):
        return self._tax

    @tax.setter
    def tax(self, value):
        self._brutto = value / 0.23
        self._tax = value
        self._netto = self._brutto - self._tax
        return