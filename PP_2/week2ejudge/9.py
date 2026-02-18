x = int(input())
nums = list(map(int,input().split()))
maxi = mini = nums[0]
for i in nums:
    if i > maxi:
        maxi = i
    if i < mini:
        mini = i

for i in range(x):
    if nums[i] == maxi:
        nums[i] = mini

for i in nums:
    print(i, end=" ")