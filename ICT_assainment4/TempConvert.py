temp = float(input("Enter temperature value: "))
direction = input("Convert to (C or F): ")

if direction == "C":
    cel = (temp - 32) * 5 / 9
    print (temp, "in celsius is ", cel)
elif direction == "F":
    far = temp * 9 / 5 + 32
    print(temp, "in fahrenheit is " ,far)
else:
    print("Invalid option! Enter 'C' or 'F' ")