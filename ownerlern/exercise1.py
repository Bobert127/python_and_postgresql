class Calculator:
    def __init__(self):
        self.history = []

    def add(self, num1, num2):
        result = num1 + num2
        self.history.append(f'added {num1} to {num2} got {result}')
        return  result

    def multiplay(self, num1, num2):
        result = num1 * num2
        self.history.append(f'added {num1} to {num2} got {result}')
        return result

    def  print_operations(self):
        print(self.history)


cal1 = Calculator()
print(cal1.add(7, 8))
print(cal1.add(11, 12))
print(cal1.multiplay(10, 16))
cal1.print_operations()


