#lambda can take as many variables as we want but can have only one expression
x = lambda a:a+10
print(x(5))

y = lambda a,b:a*b
print(y(3,4))

z = lambda a,b,c:a+b+c
print(z(1,3,5))
#=========================================================================================================
def myfunc(n):
    return lambda a:a * n
my_doubler = myfunc(2)
my_tripler = myfunc(3)

print(my_doubler(11))
print(my_tripler(11))
#=========================================================================================================
nums = [1,2,3,4]
doubled = list(map(lambda x:x * 2, nums))
print(doubled)

nums2 = [1,2,3,4,5,6,7,8]
odd_nums = list(filter(lambda x:x % 2 != 0, nums2))
print(odd_nums)

students = [("Emil",24),("Tobl",20),("Rudi",30)]
sorted_student = sorted(students, key=lambda x:x[1])
print(sorted_student)