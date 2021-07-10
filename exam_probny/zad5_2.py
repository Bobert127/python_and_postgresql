from exam_lib import User


class VIPUser(Users):
    def __init__(self, mail, name, surname, card_number):
        super().__init__(mail, name, surname, card_number)
        self._card_number = card_number



if __name__ == '__main__':
