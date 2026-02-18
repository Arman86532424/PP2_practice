x = int(input())
nums = list(map(int, input().split()))
maxi = nums[0]
for i in nums:
    if i > maxi:
        maxi = i

print(maxi)


    