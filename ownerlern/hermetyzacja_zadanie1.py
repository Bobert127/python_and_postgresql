from math import sqrt


class Square:

    def __init__(self, side):
        self._update_parameters(self)

    def _update_parameters(self, side):
        self._side = side
        self._premiter = 4 * self._side
        self._area = self._area ** 4
        self._diagonal = self._side * sqrt(2)

    def get_side(self):
        return self._side

    def get_area(self):
        return self._area

    def get_diagonal(self):
        return self._diagonal

    def set_side(self, new_length):
        self._update_parameters(new_length)

    def set_perimeter(self, new_perimeter):
        side_new_length = new_perimeter / 4
        self._update_parameters(side_new_length)

    def set_area(self, new_area):
        side_new_length = sqrt(new_area)
        self._update_parameters(side_new_length)

    def set_diagonal(self, new_diagonal):
        side_new_length = new_diagonal / sqrt(2)
        self._update_parameters(side_new_length)


a = Square()
print(a.set_diagonal())
#
# a.set_diagonal(10)
