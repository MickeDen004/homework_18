class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

# Use the Person class to create an object, and then execute the
# printname method:


x = Person("John", "Dee")
x.printname()

class Student(Person):
    def __init__(self, fname, lname, year):
      super().__init__(fname, lname)
      self.graduationyear = year

    def welcome(self):
        print(f"Welcome {self.firstname} {self.lastname} to the class of {self.graduationyear}")

x = Student("Mike", "Olsen", 2019)


class Vehicle:
    def vehicle_method(self):
        print("This is a parent method from class Vehicle")

class Car(Vehicle):
    def car_method(self):
        print(f"This is a daughter method from class {self.__name__}")

class Cycle(Vehicle):
    def cycleMethod(self):
        print(f"This is a daughter method from class {self.__name__}")


car_1= Car()
car_1.vehicle_method()


class Camera:
    def camera_method(self):
        print(f"This is a parent method from class {self.__name__} ")

class Radio:
    def radio_method(self):
        print(f"This is a parent method from class {self.__name__} ")

class CellPhone(Camera, Radio):
    def cell_phone_method(self):
        print(f"This is a daughter method from class {self.__name__} ")

cell_phone_a = CellPhone()
cell_phone_a.camera_method()
cell_phone_a.cell_phone_method()
cell_phone_a.radio_method()








