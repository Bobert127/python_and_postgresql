class Calculator:
    def __init__(self):
        self.history = []

    def add(self, num1, num2):
        result = num1 + num2
        self.history.append(f'added {num1} to {num2} got {result}')
        return result

    def multiply(self, num1, num2):
        result = num1 * num2
        self.history.append(f'multiply {num1} to {num2} got {result}')
        return result

    def print_operation(self):
        print(self.history)


calc1 = Calculator()
print(calc1.add(1, 8))
print(calc1.add(7, 9))
print(calc1.multiply(9, 7))
calc1.print_operation()