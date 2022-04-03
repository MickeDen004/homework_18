"""
Класс - проект обьекта
dir() - список всех методов
x - экземпляр
object - то, на чем основан класс
__init__ - вызываетсявсегда когда объект создается
или вызывается на основе класса, конструктор
Атртбуты и методы

"""

x = "Mike"
print(type(x))
print(dir(x))


class Vehicle:
    """docstring"""

    def __init__(self, color, doors, tires, vtype):
        """Constructor"""
        # Properties
        # Car properties
        self.color = color
        self.doors = doors
        self.tires = tires
        self.vtype = vtype

    def brake(self):
        """
        Stop the car
        """
        return "%s Braking" % self.vtype

    def drive(self):
        """Drive the car"""
        return "I'm driving a %s %s!" % (self.color, self.vtype)


if __name__ == "__main__":
    car = Vehicle("blue", 5, 4, "car")
    print(f"Car color: {car.color}, {type(car.color)}")
    print(car.drive())
    print(car.brake())
    print(type(car.drive()))


class Car(Vehicle):
    """The Car class"""
    # ----------------------------------------------------------------------------
    def brake(self):
        """override brake method"""
        return "The car class is braking slowly"

if __name__ == "__main__":
    car = Car('green', 4, 4, "car")
    print(car.brake())
    print(car.drive())

from datetime import date

