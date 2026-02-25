def Limited_cycle(nums,n):
    new = nums * n
    for i in range(len(new)):
        yield new[i]

nums = list(input().split())
n = int(input())

for i in Limited_cycle(nums,n):
    print(i,end=' ')
