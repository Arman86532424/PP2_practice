x = int(input())
nums = list(map(int,input().split()))
maxi = nums[0]
for i in nums:
    if maxi < i:
        maxi = i
pos = 1
for i in nums:
    if i == maxi:
        print(pos)
    pos+=1

