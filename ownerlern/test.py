class Car:
    def __init__(self, color='white', initial_speed=0):
        self.color = color
        self.speed = initial_speed
        self.gear = 0
        if self.speed > 0:
            self.gear = 1

# def create_car():
#     pass

car_dict = {}
car_dict['speed'] = 1
print(car_dict['speed'])

car = Car(initial_speed=1)
# car.gear = 1
print('>>speed', car.speed)
print('>>color', car.color)
print('>>gear', car.gear)