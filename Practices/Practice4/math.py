import math

degree = int(input('Input degree:'))
radians = degree * (math.pi / 180)
print('Output radian:',radians)

#==================================================================================================

hight = int(input('Height:'))
v1 = int(input('Base, first value:'))
v2 = int(input('Base, second value:'))

area1 = ((v1 + v2)/2) * hight
print(area1)

#==================================================================================================
sides = int(input('Input number of sides:'))
le = int(input('Input the length of a side:'))
area = (le*le * sides)/(4 * math.tan(math.pi / sides))
print('The area of the polygon is:',area)

#==================================================================================================
para_base = int(input('Length of base:'))
para_hight = int(input('Height of parallelogram:'))
print(para_base * para_hight)