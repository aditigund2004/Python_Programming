'''

    Inheritance in Python is a core object-oriented programming (OOP) concept 
    that allows a new class (child or derived class) to inherit attributes and methods 
    from an existing class (parent or base class). This promotes code reusability, modularity, 
    and the modeling of real-world, hierarchical relationships (e.g., a "Car is a Vehicle").


type 
    1. single/ simple inheritance
    syntax:
        class a:
        
        class b(a):
            
    2. multi-level inherintance (single inher) -> a class inhert from another class and that class inherit froom the base class called multi -lev l inher
    syntax:
        class a:
            
        class b:(a)
        
        class c(b):
            
            
    3. multiple inheritance -> single child class inherit from multiple parent class called multiple inheritnace
    syntax:
        class a:
        
        class b:
        
        class c:
            
        class d(a,b,c):
            


'''

'''
Inheritance in Object-Oriented Programming (OOP) is a mechanism where a new class (child/derived) acquires properties and behaviors from an existing class (parent/base), promoting code reusability and establishing "is-a" relationships. The five main types are Single, Multiple, Multilevel, Hierarchical, and Hybrid. 


Types of Inheritance:
    Single Inheritance: A derived class inherits from only one base class. (e.g., Class B inherits from Class A).

    Multiple Inheritance: A derived class inherits from multiple base classes. Note: Not supported in Java classes, but supported in C++ and Python.

    Multilevel Inheritance: A class is derived from another derived class, creating a chain of inheritance. (e.g., Class C inherits from B, which inherits from A).

    Hierarchical Inheritance: Multiple derived classes inherit from a single base class. (e.g., Class B and C both inherit from Class A).

    Hybrid Inheritance: A combination of two or more types of inheritance. 

Advantages:

    Code Reusability: Derived classes can use code from base classes without redefining it.

    Method Overriding: Derived classes can provide specific implementations for inherited methods.

    Polymorphism: Enables objects of different derived classes to be treated as objects of a common base class. 


'''


# single inheritance -> one child class inherited from one super (parent) class called as single inheritance

# class A:
#     def m1(self):
#         print("method 1 of the class A")
        
        
# class B(A):
#     def m2(self):
#         print("method 2 of the class B")
        
# b1 = B()
# b1.m2()
# b1.m1()


# multi - level inheritance -> 

# class A:
#     def m1(self):
#         print("method 1 of the class B")


# class B(A):
#     def m2(self):
#         print("method 2 of the class B inherited from class A")
        
        
# class C(B):
#     def m3(self):
#         print("method 3 of the class C inherited from class B")
        
        
# c1 = C()
# c1.m3() 
# c1.m2()
# c1.m1()


# multiple inheritance -> single child class inherit from multiple base class called as multiple inhertinace


# class A:
#     def m1(self):
#         print("Class A")
        
        
# class B:
#     def m2(self):
#         print("Class B")
        
        
# class C:
#     def m3(self):
#         print("Class C")
        
# class D(A,B,C):
#     def m4(self):
#         print("Class D")
        
        
        
# d1 = D()
# d1.m4()
# d1.m3()
# d1.m2()
# d1.m1()


# hierarchical inheritance -> multiple childe class inherit from single parent class


class parent1:
    def m1(self):
        print("parent class")
        
        
        
class child1(parent1):
    def m2(self):
        print("childe class method 1")
        
cd = child1()
cd.m1()
cd.m2()



class child2(parent1):
    def m3(self):
        print("")