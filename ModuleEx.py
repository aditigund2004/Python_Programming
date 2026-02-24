'''
Module ->
        it is simple .pyi file (python file)
        use import keyword
        it is collection of function, class, methods, variable etc




type ->
1. predefined modules->
    eg math, random, collections, datetime etc
    
2. user defined modules ->

 
'''
# one way to import module
import math


# second way to import module
print(math.factorial(5))
'''
(function) def factorial(
    x: SupportsIndex,
    /
) -> int
Find n!.

Raise a ValueError if x is negative or non-integral.
'''


# third way to import module
import math as m
'''
as keyword used to create temporary keyword
'''
print(m.pi)



'''
(function) def sqrt(
    x: _SupportsFloatOrIndex,
    /
) -> float
Return the square root of x.
'''
from math import sqrt
print(sqrt(9))
# return type is float


print(m.ceil(10.2))
# next value return

print(m.floor(10.6))
# previous value return


import datetime


import calendar
print(calendar.monthcalendar(2026,2))

print(calendar.calendar(2026))


import collections

str1 = 'aaabbbccdddeeefffggghhhiiijjjjkkklllmmmnnnooopppqqrrrssstttuuuvvvwwwxxxyyzzz'

# print(collections.Counter(str1))

# dic = {}
# count = 0
# for i in str1:
#     if i =='a':
#         count = count + 1
#         dic[i] = count
# print(dic)


d1={}

for i in str1:
    d1[i]=str1.count(i)
print(i)



l1 = [10,20,30]
q1 = collections.deque(l1)


q1.appendleft(100)
q1.append(100)

q1.rotate(1)
print(q1)



import udefinefunc

add = udefinefunc.addition(10,20)
print(add)



# import keyword
# print(keyword.kwlist)



print(udefinefunc.kwlist)