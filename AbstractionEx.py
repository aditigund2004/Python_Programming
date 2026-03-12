'''
Abstraction in python->
    Abstraction in Python is a core principle of Object-Oriented Programming (OOP) that involves hiding the 
    complex implementation details and showing only the essential features or functionality to the user. This 
    approach simplifies code, improves readability, and helps in managing the complexity of large applications


mandetory to keep one abstarct method

syntax:

class Abstract ->
    from abc import ABC
    class cla_name(ABC):
            # abstarct methoda 
            # non abstract methods



# no object
# must -> one abstcat method
cannot create object



class Abstract ->
    from abc import ABC
    class cla_name(ABC):
        @abstractmethod
        def m1(self):
            pass



Abstact Class ->
    In Python, an abstract class is a blueprint for other classes that cannot be instantiated on its own. It is used 
    to define a common interface and enforce that subclasses implement specific methods, which helps in managing 
    complexity and ensuring consistency in large projects. 
    
    
    
    
    mandatory to impelement each and every method
'''

# from abc import ABC, abstractmethod
# class C1(ABC):
#     @abstractmethod
#     def m1(self):
#         pass


# c1=C1()





from abc import ABC, abstractmethod
class C1(ABC):
    @abstractmethod
    def m1(self):
        pass
    
    @abstractmethod
    def m2(self):
        pass
    
class x1(C1):
    def a1(self):
        print("code....")
        
        
    def m1(self):
        print('code!!!!!!!!!')
        
        
    def m2(self):
        print('code???????')
        
        
x=x1()
x.a1()

'''
Traceback (most recent call last):
  File "d:\1315\OOP\AbstractionEx.py", line 74, in <module>
    x=x1()
TypeError: Can't instantiate abstract class x1 without an implementation for abstract method 'm1' and 'm2'
'''
