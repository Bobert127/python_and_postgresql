class Calculator:
    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b


class LoggingCalculator(Calculator):
    def __init__(self):
        super().__init__()
        self.history = []

    def add(self, a, b):
        result =super().sub(a, b)
        self.history.append(f'{a} + {b} = {result}')

    def sub(self, a, b):
        result =super().sub(a, b)
        self.history.append(f'{a} - {b} = {result}')

    def mul(self, a, b):
        result =super().sub(a, b)
        self.history.append(f'{a} * {b} = {result}')

    def div(self, a, b):
        result =super().sub(a, b)
        self.history.append(f'{a} / {b} = {result}')

a = LoggingCalculator()
a.add(11,2)
a.sub(0,2)
a.div(4,2)
a.mul(7,2)
a.div(10,3)
print(a.history)



