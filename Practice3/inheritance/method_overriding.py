class Animal:
    def speak(self):
        print("Animal sound")

class Dog(Animal):
    def speak(self):
        print("Woof")

Dog().speak()



class Shape:
    def area(self):
        print("Calculating area")

class Circle(Shape):
    def area(self):
        print("Area of circle")

Circle().area()



class Employee:
    def role(self):
        print("General employee")

class Manager(Employee):
    def role(self):
        print("Manager")

Manager().role()
