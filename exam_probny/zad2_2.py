def liczba(number):
    for i in range(1, number // 2 + 1):
        if number % i == 0:
            yield i
    yield number

if __name__ == '__main__':
    for i in liczba(17):
        print(i)