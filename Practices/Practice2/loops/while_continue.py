i = 1
while i <= 10:
    if i % 2 == 0:
        i += 1
        continue
    print(i)
    i += 1


numbers = [4, -2, 7, -5, 3]
i = 0

while i < len(numbers):
    if numbers[i] < 0:
        i += 1
        continue
    print(numbers[i])
    i += 1


i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)
