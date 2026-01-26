while True:
    print("\nMenu: ")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Exit")

    c = int(input("Select option(1-4): "))
    
    if c == 4:
        print("Exiting the menu")
        break
    if c > 4 or c < 1:
        print("invalid option")
        continue

    n1 = float(input("Enter first number: "))
    n2 = float(input("Enter second number: "))

    if c == 1:
        print("Result is:", (n1 + n2))
        break
    elif c == 2:
        print("Result is:", (n1 - n2))
        break
    elif c == 3:
        print("Result is:", (n1 * n2))
        break
