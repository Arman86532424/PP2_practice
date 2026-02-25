def fibonaci(n):
    a,b = 0,1
    for i in range(n):
        yield a
        a,b = b,b+a

x = int(input())
if x == 0:
    print('')
else:
    nums = []
    for i in fibonaci(x):
        nums.append(i)

    for i in range(len(nums)-1):
        print(nums[i],end=',')

    print(nums[len(nums)-1])