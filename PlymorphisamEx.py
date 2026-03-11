'''
Polymorphisam ->

    one method many formas 
    
    
    Polymorphism in Python is the ability of a single function, method, or operator to behave differently depending on the type of object it is working with. This allows for more flexible, reusable, and maintainable code. 

    1. overloading -> same class
        A. operator
        B. method
    no need to overload the method because python is dynamic programming lan
        
    2. overriding -> parent and child class
    
    
    
With Built-in Functions: Many built-in functions work with various data types.
The len() function, for example, returns the number of characters for a string, the number of items for a list, or the number of key-value pairs for a dictionary.
'''

# class Book:
#     def __init__(self,nm,pg,price):
#         self.bname=nm
#         self.pages=pg
#         self.price=price
        
        
#     def display_details(self):
#         print(f'Book name : {self.bname}\n Pages : {self.pages}\n Price : {self.price}')
        
#     def __add__(self, other):
#         return f'total price : {self.price + other.price}'
        
        
# # overload methoad
# b1 = Book('python', 1000, 1000)
# b2 = Book('java', 1000, 1000)
# b1.display_details()
# b2.display_details()
# print(b1+b2)
# # print(b1.__add__(b2))



'''
method overriding
    redifining method into child class

super keyword -> use to access thr parent properties



override variable

'''

# class A:
#     def m1(self):
#         print("m1 method")
        
#     def m2(self):
#         print("m2 method")
        
#     def m3(self):
#         print("hello")
        
# class B(A):
#     # override m2 method
#     def m2(self):
#         print("m2 method of class B")
    
#     def m3(self):
#         super().m3()
#         print("The Kiram Academy")
        
# # b1 = B()
# # b1.m1()
# # b1.m2()


# a1=A()
# b1=B()

# b1.m2()




# class A:
    
#     var1="value1"
#     var2 = "value2"
#     def m1(self):
#         print("m1 method")
        
#     def m2(self):
#         print("m2 method")
        
#     def m3(self):
#         print("hello")
        
# class B(A):
#     var3 = "value3"
#     # override m2 method
#     def m2(self):
#         print("m2 method of class B")
    
#     def m3(self):
#         super().m3()
#         print("The Kiram Academy")

# a1=A()
# b1=B()

# b1.m2()

# print(b1.var1)
# print(b1.var3)