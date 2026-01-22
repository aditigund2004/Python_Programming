'''
string is collection of character represent in '' or "" or ''' ''' 
indexing is techning which ised ti access single character
syntax
var[indexNumber]

sclicing to access multiple character from string
syntax 
var[startindex:endingindex:stepvalue]


reverse [step value = -1]

defualt value = 0

'''


name = 'ram'
print(name[0])

name1 = 'data'
print(name1[0:4])


institute = 'The Kiran Academy'
print(institute[2])
print(institute[-2])
print(institute[4])
print(institute[-9])
print(institute[-17])
print('-----------------------------------')


cls_name = institute[0] + institute[4] + institute [10]
print(cls_name)
print('------------------------------')


# name = 'shri ram'
# print(name[0:4:1]) #shri

# print(name[4:-1:1])

# print(name[4: : -1])

# print(name[4:-1])

# print(name[4:])

# print(name[4:-1:1])
# print('---------------------------------------')



language = 'Python Programming Language'
print(language[0:6])

print(language[7:-8])

print(language[19:])

print(language[-1:-9:-1])

print(language[:-1])

print(language[5:-28:-1])

print(language[:-28:-1])

print(language[:-28:])


# #startingindex
name = 'shri ram'

print(name[2:-5:1])

print(name[1:-3:-1])

print(name[:-5:-1])

print(name[-3:-6:-1])

print(name[:-6:-1])


# endingindex
name1 = 'shri ram'

print(name1[2:-5:1])

print(name1[2::1])

print(name1[4:1:-1])

print(name1[4: :-1])

# stepvalue
institute = 'the kiran academy'
print(institute[0:3:1])

print(institute[0:3:])

print(institute[:3:])

print(institute[-7::])

print(institute[0:4:-1])

print(institute[-8::-1])

print(institute[::-1])


# example
defination = 'Python is a simple programming language'

print(defination)

print(defination[-9: -1:-1])

print(defination[1:4:-1])

print(defination[12:18:-1])


'''
String methods
block of code used to perform operation on the data and variable
variableName.metod() to call the method
'''

class_name = 'the kiran academy'

print(class_name)

class1 = class_name.lower()
print(class1)
print(class_name.upper())
print(class_name.lower())


institute = "the kiran academy"
ins = institute.title()
print(ins)


# onle first character capital
capital = institute.capitalize()
print(capital)


# isalpha
name = 'ram'
print(name.isalpha())

print(name.isnumeric())


# # isnumeric()
num = '180'
print(num.isnumeric())


# # isspace()
space = ' '
print(space.isspace())

# # islower()
low1 = 'Ram'
print(low1.islower()) #False

low = 'ram'
print(low.islower())  


# isupper()
name1 = "RAM"
print(name1.isupper())

# istitle()
title = "Title"
print(title.istitle())


# isrepace
'''
(old: LiteralString, new: LiteralString, /, count: SupportsIndex = -1) -> LiteralString

Return a copy with all occurrences of substring old replaced by new.

count

Maximum number of occurrences to replace.
-1 (the default value) means replace all occurrences.

If the optional argument count is given, only the first count occurrences are replaced.

'''
rep = 'the replace word will replace with new replaced word'
print(rep)
print(rep.replace('the', 'these'))
print(rep.replace('replace', 'new',2))
print('-'*100)


# index method
'''
(sub: str, start: SupportsIndex | None = None, end: SupportsIndex | None = None, /) -> int

Return the lowest(start) index in S where substring sub is found, such that sub is contained within S[start:end].

Optional arguments start and end are interpreted as in slice notation. Raises ValueError when the substring is not found.
'''
name = 'vaishnavi'
print(name.index('v'))
print(name.index('a'))
nm = name.index('h')
print(nm)
print('-'*100)

# count
count1= 'the kiran academy institute'
print(count1.count('t'))
print(count1.count('t',2))
print('-'*100)


# split
name = 'shri ram'
print(name.split())
print(name.split('i'))
print('-'*100)



# center
'''
(width: SupportsIndex, fillchar: LiteralString = " ", /) -> LiteralString

Return a centered string of length width.

Padding is done using the specified fill character (default is a space).
'''
name = 'shri ram'
nm= name.center(100)
print(nm)



# strip
'''
(chars: LiteralString | None = None, /) -> LiteralString

Return a copy of the string with leading and trailing whitespace removed.

If chars is given and not None, remove characters in chars instead.


remove white space
'''
name1 = ' the kiram academy '
print(name1)
nm1 = name1.strip()
print(nm1)
print('-'*100)

# rstrip
name3 = 'the kiram academy'
nm3 = name3.lstrip('t')
print(nm3.rstrip('y'))
print(nm3)


# endswith
'''
suffix: str | tuple[str, ...], start: SupportsIndex | None = None, end: SupportsIndex | None = None, /) -> bool

Return True if the string ends with the specified suffix, False otherwise.

suffix

A string or a tuple of strings to try.

start

Optional start position. Default: start of the string.
'''
name4 = 'the kiram academy'
nm4 = name4.endswith("y")
print(nm4)
print('-'*100)

name5 = 'the kiram academy'
nm5 = name5.startswith('t')
print(nm5)

# print(nm5.startwith('k',4))


