'''
range datatype -> is used to generate sequence of whole number

synatx 
var = range(start, stop, step)

r = range(start, stop,step)

r = range(start,stop)  # step = +1 by default

r = range(stop) # start = 0, step =1


(stop: SupportsIndex, /) -> range
stop (exclusive) by step. range(i, j) produces i, i+1, i+2, ..., j-1.


range(stop) -> range object range(start, stop[, step]) -> range object

Return an object that produces a sequence of integers from start (inclusive) to stop (exclusive) by step. 
range(i, j) produces i, i+1, i+2, ..., j-1. start defaults to 0, and stop is omitted! range(4) produces 0, 1, 2, 3. 
These are exactly the valid indices for a list of 4 elements. When step is given, it specifies the increment (or decrement).


getsizeof in sys module
'''

r= range(1,11,1)
print(type(r))


l=[1,2,3,4,5,6,7,8,9,10]
r=range(1,111,1)

from sys import getsizeof
print(getsizeof(l))  #memeroy size increse if number of elemnt added ex:output:136
print(getsizeof(r)) # memory size does not change even if number of element or incresed ex:output:48



for num in range(1,11,1):
    print(num)


for num in range(1,11,2):
    print(num)


for num in range(1,11):
    print(num)



for num in range(11):
    print(num)


# WAP to print numbers from 11 to 20
for num in range(11,21):
    print(num)
    
    
# WAP to print numbers from 50 to 40
for num in range(50,39,-1):
    print(num)
    
    
# WAP to print list of numbers from 10 to 50

li = []
for i in range(10,51):
    li.append(i)
print(li)


list = []
for li in range(10,51):
    list.append(li)
print(list)


# by using type casing 
# print(list(range(1,21)))

# WAP to print dic of squre of 11 to 20

dic = {}
for i in range(11,21):
    r = i**2
    # var[key]
    dic[i]=r
print(dic)


dict = {}
for li in range(10,21):
    cube = li**3
    dict[li]=cube
print(dict) 




# range() with list()
# Convert range into a list:

numbers5 = list(range(1, 6))
print(numbers5)



# Sum of Numbers
total = 0
for i in range(1, 6):
    total += i
print(total)