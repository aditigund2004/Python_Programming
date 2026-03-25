'''
Dictionary ->
Dupliacte are not allowed, key-value pair data store
'''
d= {1:23,2:23}
# add -> var[key] =value

d[3]=55
# access -> ver[key]

# update -> var[key] = value

# delete -> var.pop(key)


# method
# var.keys()
# var.values()
# var.items()
# var.clear()
# var.copy()
# var.setdefault(key, defaultvalue)


# dect.fromkeys(iterable, value)


'''
iterable -> container contain value(multiple)
iteration -> operation on that data(in, out) using for loop

for loop use used to perform operation on iterable

iterable is collection of items or datatype like set, tuple, list, dict

syntax : for varname in iterable:

'''


'''
Performing the operations on the dictionary type of data
#CURD Operations
1. Creat
2. Update 
3. Read
4. Delete

--> How to access the values
    a)By using syntax:
         var[key]:  #return value
           -->we access the values using the keys as shown in the syntax and example below

    b)By using get method:
         var.get(key)       
           -->it take the key as input and  provide values as output 
'''

'''
--> How to access the values
    a)By using syntax:
         var[key]:  #return value
           -->we access the values using the keys as shown in the syntax and example below

'''
# #sample example
# s1 = {'name':'raj','per':70,'marks':{'t1':89,'t2':99, 't3':78}}
# print(s1)
# print(s1['per'])
# print(s1['marks'])
# print(s1['marks']['t2'])

'''
 b)By using get method:
         var.get(key)       
           -->it take the key as input and  provide values as output 
'''
#sample example
# s1 = {'name':'raj','per':70,'marks':{'t1':60,'t2':70,'t3':80}}
# print(s1)
# print(s1.get('name'))
# print(s1.get('per'))
# print(s1['marks'].get('t2'))

'''
--->How to add the value
    syntax:
        var[key] = value

'''
#sample example
# s1 = {'name':'raj','per':70,'marks':{'t1':60,'t2':70,'t3':80}}
# print(s1)
# s1['age'] = 23
# s1['city'] = 'pune'
# s1['surname'] = 'name'
# print(s1)

'''
--->How to update the data 
     we can ad multiple values by using update
     we can merge the two dictionary within single also
    syntax:

'''
# # #sample Example 
# result = {'jay':89,'ajay':88,'om':67}
# result.update(sameer=99,pooja=86,arun=65)
# print(result)
# #By giving another dictionary
# result1 ={'neha':90,'ashish':78,'siya':96}
# result1.update(result)
# print(result)
# print(result1)

# dict1 = {'a':12,'b':70}
# dict1.update(c=40,d=57)
# print(dict1)

'''
---->How to update:
      syntax: 
          var[key]=value
'''



'''
access:
   var[key]  or var.get(key)
add:
   var[key]=value   or var.update(p = value)   
update:
   var[key] = uvalue
'''
#ANOTHER EXAMPLE 

# Details = {'emp_name':'ramesh gupta','salary':50000,'roles':{'design':8.0,'coding':9.9, 'testing':7.8}}
# print(Details)
# print(Details['salary'])
# print(Details['emp_name'])
# print(Details.get('emp_name'))
# Details['age']=34
# Details['city']='pune'
# increment = {'june':5000, 'july':6000,'aug':6500}
# Details.update(increment)
# print(Details)

'''
--->How to delete:
     syntax: 
             var.pop(key)   ==> retuen value
             var.popitem()  ==>return (key,value)
'''
#sample example
# r1 = {'riya':90,'tina':89,'siya':99}
# print(r1.pop('riya'))
# print(r1)

# r1 = {'riya':90,'tina':89,'siya':99}
# print(r1.popitem())
# print(r1)

# s1 = {'name':'raj','per':70,'marks':{'t1':60,'t2':70,'t3':80}}
# print(s1)
# # print(s1.pop('t3'))
# print(s1['marks'].pop('t3'))
# print(s1)

'''
Exploring methods in dictionary 
'''

# r1 = {'riya':90,'tina':89,'siya':99,'maya':86}
# print(r1.keys())
# print(r1.values())
# print(r1.items()) #returns list of tuples of keys and values
# print(r1.copy())
# #print(r1.fromkeys(r1)) #helps to make the another dictionary 
# print(r1.setdefault('riya'))
# print(r1.setdefault('pawan',6.0))


'''
the method fromkeys helps to add the elements into the list 
it can be done with the help of using another list/dictionary also 


(method) def fromkeys(
    iterable: Iterable[_T@fromkeys],
    value: None = None,
    /
) -> dict[_T@fromkeys, Any | None]
Create a new dictionary with keys from iterable and values set to value
'''

# b1315 = ['ankita yadav','sameer gupta','nikhil verma']
# marks = dict.fromkeys(b1315)
# print(marks)
# marks = dict.fromkeys(b1315,10)
# print(marks)
# marks = dict.fromkeys(b1315,'ram')
# print(marks)
# marks = dict.fromkeys(b1315,0)
# print(marks)

r1 = {'riya':90,'tina':89,'siya':99,'maya':86}
r1.update(a=45)
print(r1) 