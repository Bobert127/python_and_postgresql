class Robert:
    def __init__(self, name, surname, address):
        self.name = name
        self.surname = surname
        self.address = address

    def kod(self, kod):
        return kod

    def print_info(self):
        print(f"nazywam się {self.name}  {self.surname} mieszkam porzy ul. {self.address} {self.kod}")


if __name__ == '__main__':
    a = Robert("Jan", "kowalski", "Królewny Śnieżki 40")
    b = a.kod("10-600")
    a.print_info(b)