'''
datatype defination -
datatype in python tells what kind of data or value holds and it help python understand what operation can be perform on that data

type of data in python
fundamental datatype - numric ex - int, float, complex, str, bool (store single value) and also called Primitive data type
collective datatype - list, tuple, set, dictionary, frozanset, range (store multiple values) also called Non-Primitive

numeric datatype - whole number - number without decimal point 

int - it is predefined dataype in pyton used  to represent whole number ex - age , count, pin_code

float - used to represent decimal number (number with decimal point) ex - percentag, weigth

complex -
predefined datatype in python and it used to represent complex number
number with character ex- aj, namej, agej 
var = a + bj
a - real part of complex
bj - imagnary part of complex

to access imagnary complex number by using (img) property
imagnary part of complex number must be decimal or float
c = 10 + 15j
print(type(c))

<class 'complex'>

c1 = 11+50j
print(c1.real)
output11.0

imag = c1.imag
print(img)

real part of complex number can be int or float
c1 = 11.5+10j
print(c1)



binary number to reprent 
var = 0bvalue


'''
# real part of complex number can be int or float
c1 = 11.5+10j
c1 = 10+10j
c1 = 0o12 +12j
c1 = 0b1010 +10j
c1 = 0x123+12j
print(c1)


# imagnary part of complex number must be decimal or float
c2 = 10 +10.5j
c2 = 10 +10j
# c2 = 10 + 0o12j
# c2 = 10 + 0b101j
# c2 = 10 + 0x12bj
print(c2)



num = 100
print(type(num))
print(dir(num))


# binary
num2 = 1010
print(num2)

x = 0b1010
print(x)

print(bin(x))  
# Return the binary representation of an integer.

'''
octal 
value - 0-7
var = 0ovalue
'''

num3 = 0o123
print(num3)

print(oct(10))
# Return the octal representation of an integer.

'''
decimal
value - 0-9
num = value
'''

'''
hexadecimal

value = 0-9 or a-f/A-F
var = 0xvalue 
'''

num4 = 0x12abc
print(num4)
print(hex(189))
# Return the hexadecimal representation of an integer.

'''
bool datatype

'''
a = True
print(type(a))
print(True + True)


b = False 
print(type(b))
print(False + False)

print(int(True))
print(int(False))
