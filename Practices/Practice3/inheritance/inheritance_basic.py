class Animal:
    def eat(self):
        print("Eating")

class Dog(Animal):
    def bark(self):
        print("Barking")

d1 = Dog()
d1.eat()
d1.bark()

class Parent:
    def show(self):
        print("Parent")
class Child(Parent):
    pass

c1 = Child()
c1.show()