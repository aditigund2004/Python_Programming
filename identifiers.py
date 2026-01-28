'''
idetifiers

1. canot start with alph-number
1num = 10
print(1num)
error:  1num = 10
    ^
SyntaxError: invalid decimal literal

2. can start with _ 
_number = 10
print(_number)

3.not allow space
student_name = adi
print(student name)


5. identifiers are case sensitive
name = 'data science'
#Python Memory Management  - allocate and de-allocate the memoery
name = 'web development'
print(name)

6. keyword canot use as identifiers

'''
num = 10
print(num)

_number = 10
print(_number)

student_name = 'aditi'
print(student_name)

name = 'data science'
#Python Memory Management  - allocate and de-allocate the memoery
name = 'web development'
print(name)

name1 = 'data science'
Name = 'web development'
print(name1)
print(Name)


# print(course)
# NameError: name 'course' is not defined

import keyword
print(keyword.iskeyword("for"))   # True
print(keyword.iskeyword("myvar")) # False

from keyword import kwlist
print(kwlist)
'''
output - ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 
'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 
'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
'''
print(len(kwlist))