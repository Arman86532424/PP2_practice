a = int(input())
nums = list(map(int,input().split()))
new_list = []

for i in nums:
    if i not in new_list:
        print("YES")
    else:
        print("NO")
    
    new_list.append(i)