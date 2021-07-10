class Calculator:
    def __init__(self):
        self.history = []

    def add(self, num1, num2):
        result = num1 + num2
        self.history.append(f'added {num1} to {num2} got {result}')
        return result

    def multiply(self, num1, num2):
        result = num1 * num2
        self.history.append(f'multiply {num1} with {num2} got {result}')
        return result

    def print_operations(self):
        print(self.history)


c1 = Calculator()
print(c1.add(7, 8))
print(c1.add(2, 17))
print(c1.multiply(2, 18))
c1.print_operations()