''' make multiple cars '''
from car import Car

NUMBER_CARS = 20
class Cars():

    def __init__(self):
        self.cars = []
        self.create_cars()

    def create_cars(self):
        for _ in range(NUMBER_CARS):
            new_car = Car()
            self.cars.append(new_car)

    def move_cars(self, car_speed):
        for car in self.cars:
            car.move(car_speed)
