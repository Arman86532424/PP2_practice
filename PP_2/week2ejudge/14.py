n = int(input())
arr = list(map(int, input().split()))

max_count = 0
answer = arr[0]

for x in arr:
    count = 0
    for y in arr:
        if x == y:
            count += 1

    if count > max_count or (count == max_count and x < answer):
        max_count = count
        answer = x

print(answer)
