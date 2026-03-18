i = 1
while True:
    if i == 5:
        break
    print(i)
    i += 1


total = 0
i = 1

while i <= 10:
    total += i
    if total >= 10:
        break
    i += 1

print(total)

while True:
    num = int(input("Enter a number: "))
    if num == 0:
        break
    print(num)
