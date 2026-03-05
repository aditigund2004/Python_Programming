'''
OOP's -> object oriented programming in python used to create user defined class and define thier behaviouor to perform the operation

class -> template or user defined class, blue print
object ->  of the class or behavior of the class, real word entity

polymorphism -> one form many methods

abstraction ->

inheritnce
1. single inheritance -> deriving a single class from base class called single inheritance
2. multiple iinheritance -> 
3. multi level inheritance -> deriving multiple classes from single base class called multi level inheritance
4. hierarchical inheritance ->
5. hybride inheritance -. 


syntax:
class class_name:
    pass
    # code

'''
'''
Programming Paradigm :--->
    1. Sequential Programming
    2. functional Programming
    3. OOP (Object Oriented) Programming 

    
    # What is OOP in python 
--> Object-Oriented Programming (OOP) in Python is a programming paradigm 
    that organizes code using objects and classes.
    It helps in making code reusable, modular, and easy to maintain.

    # What is class
-->    Definition:
     
     ~ A class is a blueprint or template used to create objects.
       It defines the properties (variables) and behaviors (methods/functions)
       that the objects will have.
     ~  its a blueprint of an object
     ~  its an imaginary entity
     ~ its does not required memory
-->    Syntax: 
             Class class_name:
                 #Body of code    
👉 In simple words:
A class is like a design or plan. 

    # What is Object 
--> Definition:
    An object in Python is an instance of a class.
    It represents a real-world entity and contains data (variables)
    and methods (functions) that operate on that data.
--> Syntax :
          class_name()
          Class_name()    
👉 In simple words:
An object is a real thing created from a class (blueprint).


   # 🔹 What is a Reference Variable in Python?

-->  Definition:
      A reference variable is a variable that stores the address 
      (reference) of an object, not the actual object itself.
👉 In simple words:
A reference variable points to an object in memory.
'''

class Student:
    pass
s1 = Student()
s2 = Student()
print(type(s1))
print(Student)


class Employee:
    pass
e1 = Employee()
e2 = Employee()
print(type(e1))
print(Employee)

class Books:
    pass
b1 = Books()
b2 = Books()
print(type(b1))
print(Books)
print(dir(b1))

'''
--new--  (Create new object in memory and returns to the init method)
--init--  (initialization attributes of object)
    #Constructor
    #pyhton has some special method within it which executes automatically
    #the methods name starts with double (__) and Ends with (__)
'''

class Employee:
    def __new__(cls):
        print('Hello, i am new method')
        obj = super().__new__(cls)
        return obj
    def __init__(self):
        print('hii , i am init method')
    def display():
        print('Hello')    
e1 = Employee()


'''
All the classes are written in the object class which is inbuilt in python
super().__new__ used to call the object from parent class
'''

'''
# What is Constructor in Python

A constructor in Python is a special method that automatically
runs when you create a new object from a class.
It is used to initialize (set up) the object’s data.
In Python, the constructor method is called:
__init__()

'''

class member:
    def __init__(self):
        print(f"the id of self is : {id(self)}")

m1 = member()  
print(f"the id of m1 is : {id(m1)}")  

print('hello')

m2 = member()  
print(f"the id of m2 is : {id(m2)}") 



#Example to check the id of the objects 
class account:
    def __init__(self):
        print(f"the ID of self in account class is : {id(self)}")

a1=account()
print(f"the ID of a1 object in account class is : {id(a1)}")

print('Hello we are checking the memory locations of the created object')

a2=account()
print(f"the ID of a2 object in account class is : {id(a2)}")
