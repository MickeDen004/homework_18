class Vehicle:
    def vehicle_method(self):
        print("Это родительский метод из класса Vehicle")


# Создание класса Car, который наследует Vehicle
class Car(Vehicle):
    def car_method(self):
        print("Это метод из дочернего класса")



class Car:
    # создаем атрибуты класса
    name = "c200"
    make = "mercedez"
    model = 2008

    # создаем методы класса
    def start(self):
        print("Заводим двигатель")

    def stop(self):
        print("Отключаем двигатель")


