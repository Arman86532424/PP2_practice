def add(tas, name, decrip):
    tas[name]= decrip
    print('task added')

def view(tas):
    for name, desc in tas.items():
        print(f"{name}: {desc}")

def delt(tas, name):
    if name in tas:
        del tas[name]
        print("task deleted")


tas = {}

while True:
    ac = input("Choose action: add, view, delete, quit ")

    if ac == "add":
        name = input("Enter task name: ")
        decrip = input("Enter task description: ")
        add(tas, name, decrip)

    elif ac == "view":
        view(tas)

    elif ac == "delete":
        name = input("Enter task name: ")
        delt(tas, name)

    elif ac == "quit":
        break