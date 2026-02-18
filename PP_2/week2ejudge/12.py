x = int(input())
nums = list(map(int,input().split()))
for i in range(x):
    nums[i] = nums[i] * nums[i]

print(*nums)