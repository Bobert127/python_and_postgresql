import itertools


class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        if not Book.check_isbn(self.isbn):
            raise ValueError("Wrong ISBN")

    @staticmethod
    def check_isbn(isbn):
        raw_isbn = isbn.replace("-", "")
        if len(raw_isbn) == 10:
            control_sum = 0
            for i, value in enumerate(raw_isbn[:-1]):
                control_sum += int(value) * (i + 1)
            if raw_isbn[-1] == "X":
                return control_sum % 11 == 10
            else:
                return control_sum % 11 == int(raw_isbn[-1])
        elif len(raw_isbn) == 13:
            control_sum = 0
            for i, value in enumerate(raw_isbn[:-1]):
                value = int(value)
                control_sum += value * 3 if (i + 1) % 2 == 0 else value

            if int(raw_isbn[-1]) == 0:
                return control_sum % 10 == int(raw_isbn[-1])
            else:
                return 10 - control_sum % 10 == int(raw_isbn[-1])

        return False


if __name__ == '__main__':
    print(Book.check_isbn('978-83-7181-517-2'))
    print(Book.check_isbn('0-306-40615-2'))