possible_car_colors = [
    'white',
    'red',
    'yellow',
    'green',
]

class Car:
    def __init__(self, color='white', initial_speed=0):
        if color not in possible_car_colors:
            raise ValueError(f'Unsupported color {color}. Must be one of {possible_car_colors}')
        self.color = color
        try:
            initial_speed = float(initial_speed)
        except ValueError:
            raise ValueError('Speed must be a number')
        self.speed = initial_speed
        self.gear = 0
        if self.speed > 0:
            self.gear = 1
        self.seats = None

    def speed_up(self, value):
        if self.gear > 0:
            self.speed += value

# def create_car():
#     pass

car_dict = {}
car_dict['speed'] = 1
print(car_dict['speed'])

color = input('Chose a color: ')
car = Car(color, initial_speed=1)
# car.gear = 1
print('>>speed', car.speed)
print('>>color', car.color)
print('>>gear', car.gear)
car.speed_up(10)
print('>>speed', car.speed)

print('--------------')
car2 = Car()
car2.gear = 1
car2.speed_up(10)
print('>>speed', car2.speed)