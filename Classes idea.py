class Car:
    # создаем атрибуты класса
    car_count = 0

    # создаем методы класса
    def start(self, name, make, model):
        print("Engine started")
        self.name = name
        self.make = make
        self.model = model
        Car.car_count += 1


car_a = Car()
car_a.start("Corrola", "Toyota", 2015)
print(car_a.name)
print(car_a.car_count)

car_b = Car()
car_b.start("City", "Honda", 2013)
print(car_b.model)
print(car_b.car_count)


class Square:
    @staticmethod
    def get_squares(a, b):
        return a*a, b*b

print(Square.get_squares(3, 5))

class Laptop:

    def __str__(self):
        return "laptop class object"

    def start(self):
        print("Laptop is on")



laptop_a = Laptop()
print(laptop_a)

class Bike:
    def __init__(self):
        print("Engine started")
        self.name = "Voyager"
        self.__make = "Harley-Davidson"
        self._model = 1978


bike_a = Bike()
print(bike_a.make)



