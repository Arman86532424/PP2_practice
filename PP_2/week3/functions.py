#functions and oop basics
def greet():
    print("Hello")

greet()
message = greet()
print(message)
#=================================================================
def fare_to_celcius(fah):
    return(fah -32)*5/9

fah = 76
print(fare_to_celcius(fah))
#=================================================================
def my_faction():
    pass
#=================================================================
def greeeeet(name):
    print("Hello",name)
greeeeet(input())
#=================================================================
def add_nums(num1,num2):
    sume = num1 + num2
    print(sume)

add_nums(2,3)
#=================================================================
def some_function(name="friend"):#default value
    print("hello",name)
some_function()
some_function('Jogh')
#=================================================================
def adasdas(animal,name):
    print("I have a",animal)
    print("His name is",name)

adasdas("SKOOBY","dog")#Posisional argument
adasdas(name="Skooby", animal="DOG")#key word argument
#==================================================================
def list_function(fruits):#we can put anything including lists, tuplles, dicts
    for i in fruits:
        print(i)
list_function(['orange', 'apple', 'banana'])
#==================================================================
def another_greet(name,/):#accepts only posisional arguments (*,name)-key word arguments
    print("hello", name)
another_greet("Nilou")
#==================================================================
def multy_greet(greetings,*names):
    for name in names:
        print(greetings,name)

multy_greet('Hello',"Tobl","NIkita","Vania")

