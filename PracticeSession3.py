import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius

    def perimeter(self):
        return 2 * math.pi * self.radius

c = Circle(5)

print("Area:", c.area())
print("Perimeter:", c.perimeter())







from datetime import date

class Person:
    def __init__(self, name, country, birth_year):
        self.name = name
        self.country = country
        self.birth_year = birth_year

    def age(self):
        current_year = date.today().year
        return current_year - self.birth_year

p = Person("Aditi", "India", 2004)

print("Name:", p.name)
print("Age:", p.age())





import math

class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return math.pi * self.r * self.r

    def perimeter(self):
        return 2 * math.pi * self.r

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

    def perimeter(self):
        return 4 * self.side

c = Circle(3)
s = Square(4)

print("Circle Area:", c.area())
print("Square Perimeter:", s.perimeter())







class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, name, price):
        self.items[name] = price

    def remove_item(self, name):
        if name in self.items:
            del self.items[name]

    def total_price(self):
        return sum(self.items.values())

cart = ShoppingCart()
cart.add_item("Book", 200)
cart.add_item("Pen", 50)

print("Total:", cart.total_price())

cart.remove_item("Pen")
print("After removing Pen:", cart.total_price())





class Bank:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def show_balance(self):
        print("Balance:", self.balance)

b = Bank()
b.deposit(1000)
b.withdraw(300)
b.show_balance()




class Calculator:
    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b

c = Calculator()

print("Add:", c.add(10, 5))
print("Multiply:", c.mul(10, 5))




class Box:
    def __init__(self, l=None, b=None, h=None):
        if l is None:
            self.l = int(input("Enter L: "))
            self.b = int(input("Enter B: "))
            self.h = int(input("Enter H: "))
        elif b is None and h is None:
            self.l = self.b = self.h = l
        else:
            self.l = l
            self.b = b
            self.h = h

    def show(self):
        print("L:", self.l, "B:", self.b, "H:", self.h)

# Objects
box1 = Box()
box2 = Box(5)
box3 = Box(2, 3, 4)

box1.show()
box2.show()
box3.show()




class Largest:
    def __init__(self, a, b, c):
        self.max = max(a, b, c)

    def show(self):
        print("Largest:", self.max)

l = Largest(10, 25, 15)
l.show()





class Vehicle:
    def __init__(self, name):
        self.name = name

    def show(self):
        print("Vehicle:", self.name)

class Bus(Vehicle):
    pass

b = Bus("Volvo Bus")
b.show()





class ClassOne:
    def display1(self):
        print("This is ClassOne")

class ClassTwo(ClassOne):
    def display2(self):
        print("This is ClassTwo")

obj = ClassTwo()
obj.display1()
obj.display2()




class Vehicle:
    def show(self):
        print("This is Vehicle")

class Car(Vehicle):
    pass

class Truck(Vehicle):
    pass

c = Car()
t = Truck()

c.show()
t.show()




class Student:
    def student_info(self):
        print("Student details")

class Sports:
    def sports_info(self):
        print("Sports details")

class AthleteStudent(Student, Sports):
    pass

a = AthleteStudent()
a.student_info()
a.sports_info()