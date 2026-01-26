import random
number = random.randint(1,100)

while True:
    g = input("Guess the number or press 'q' to stop: ")
    if g == "q":
        print("You stopped the game")
        break
    g = int(g)

    if g > number:
        print("Too high")
    elif g < number:
        print("Too low")
    else:
        print("The number was ", number)
        break