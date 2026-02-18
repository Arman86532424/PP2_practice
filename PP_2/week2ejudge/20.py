x = int(input())
dataBase = {}
for i in range(x):
    command = input().split()
    if command[0] == "set":
        dataBase[command[1]] = command[2]
    elif command[0] == "get":
        if command[1] in dataBase:
            print(dataBase[command[1]])
        else:
            print(f"KE: no key {command[1]} found in the document")
