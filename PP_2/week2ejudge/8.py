x = int(input())
i = 1
nums = []
while i <= x:
    nums.append(i)
    i*=2

for i in nums:
    print(i, end=" ")