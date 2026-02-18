class parrot:
    name = ''
    age = 0

parrot1 = parrot()
parrot1.name = "Blu"
parrot1.age = 10

parrot2 = parrot()
parrot2.name = "Jo"
parrot2.age = 15

print(f'{parrot1.name},{parrot1.age}')
print(f'{parrot2.name},{parrot2.age}')
#=====================================================================================================
class Myclass:
    x=5

p1=Myclass()
print(p1.x)
#del p1
#=====================================================================================================
class room:
    lenght = 0.0
    widht = 0.0

    def calculate_area(self):
        print("Area of room = ", self.lenght * self.widht)

study_room = room()
study_room.lenght = 18
study_room.widht = 15

study_room.calculate_area()

#=========================================================================================================
