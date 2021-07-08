
def dividers(number):
    for x in range(1, number // 2 + 1):
        if number % x == 0:
            yield  x
    yield  number


if __name__ == '__main__':
    for x in dividers(16):
        print(x)