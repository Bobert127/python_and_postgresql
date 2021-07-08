from examp_lib import User


class VIPUser(User):
    def __init__(self, name, surname , mail, card_number):
        super().__init__(name=name, surname=surname, mail=mail)
        self._card_number = card_number if self._check_card_number(card_number) else None

    @staticmethod
    def _check_card_number(card_number):
        return card_number > 999 and card_number % 2 == 0

    @staticmethod
    def use_vip_card():
        return  None

    @property
    def card_number(self):
        return self._card_number

    @card_number.setter
    def card_number(self, card_number):
        self._card_number = card_number if self._check_card_number(card_number) else None



if __name__ == '__main__':
    users= VIPUser("Robert", "Trzaska","jan@kowalksi.pl", 200)
    print(users.card_number)
    users.card_number = 9998
    print(users.card_number)
