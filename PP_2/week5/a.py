#Regular expression
import re

pattern = 'a...s$' #stars with a and ends with s
test_str = 'abyss' #success
test_str2 = 'Alias' #not success

#==============================================================================================

# [abc] it will match if the string you are trying to match contains any of the a,b,c

a = 'a' #1
b = 'ac' #2 
c = 'abc de ca' #5 matches

#[^abc] - everthing exept a b c

#==============================================================================================

# . - period

a = 'a' #no match
b = 'ac' #1
c = 'abcd' #2 

#==============================================================================================

# ^a checks if str stars with a
# $a checks if str ends with a

#==============================================================================================

# * matches ZERO or more occurences of the pattern left to it [mn] [man] [maaaaaan]
# + matches ONE or more occurences of the pattern left to it [man] [maaan]
# ? matches ONE or ZERO occurences of the pattern left to it [man] [woman]

#==============================================================================================

# {} - a{2,3} atleats 2 and at max 3 letters a in one sequnce [aabc daaaat](2 matches)
# [0-9]{3,4} [123,1234]

#==============================================================================================

