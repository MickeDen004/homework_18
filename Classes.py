def scope_test():
    def do_local():
        spam = "local"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment: ", spam)
    do_nonlocal()
    print("After nonlocal assignment: ", spam)
    do_global()
    print("After global assignment: ", spam)


scope_test()
print("in global scope:", spam)

class MyClass:
    """A simple example class"""
    i = 12345

    def __init__(self):
        self.data = []

    def f(self):
        return "Hello World"

class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

x = Complex(3.0, -4.5)
print(x.r, x.i)


x.counter = 1
while x.counter < 1:
    x.counter = x.counter * 2
print(x.counter)


class Rectangle():
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h

    def perimeter(self):
        return 2 * (self.w + self.h)


class Square(Rectangle):
    def __init__(self, s):
        # call parent constructor, w and h are both s
        super().__init__(s, s)
        self.s = s


r = Rectangle(12, 6)
s = Square(2)
print(r.area(), r.perimeter())
print(s.area(), s.perimeter())

