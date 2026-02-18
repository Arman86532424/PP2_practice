class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

d = Dog("Buddy")
print(d.name)


class Person:
    def __init__(self, name):
        self.name = name

class Employee(Person):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary

e = Employee("Alice", 50000)
print(e.name, e.salary)


class Vehicle:
    def __init__(self, brand):
        self.brand = brand

class Bike(Vehicle):
    def __init__(self, brand, type):
        super().__init__(brand)
        self.type = type

b = Bike("Yamaha", "Sport")
print(b.brand, b.type)
