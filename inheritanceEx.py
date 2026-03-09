'''
Inheritance OOP's ->
inherit the properties from the base (existing class)
new class access the properties from the base class


reusing the properties

reuse the peroperty amd method


Inheritance in Python is a core object-oriented programming (OOP) concept 
that allows a new class (child or derived class) to inherit attributes and methods 
from an existing class (parent or base class). This promotes code reusability, modularity, 
and the modeling of real-world, hierarchical relationships (e.g., a "Car is a Vehicle").

'''

# class Demo:
#     var = 10
    
#     def __init__(self):
#         self.var1 = 'ram'
        
#     def method1(self):
#         print("class Demo method ")
        
        
#     def method2(self):
#         print("class demo method")
#         a = 12

# class Example(Demo):
#     b =12
    
# # objectname = classname()

# ex = Example()
# ex.method1()
# ex.method2()

# # object.variable_name
# print(ex.var)
# print(ex.b)
# # print(ex.a)


# object level -> same data -> class level data -. class attribute

from datetime import date

class Saving_Account:
    # class attribute
    back_name = "BOI"
    IFSC_code = "BOI101"
    branch = "Karve Nagar"

    def __init__(self,nm,ac,bl):
        # instance attribute
        self.name=nm
        self.account_no=ac
        self.balance=bl
        self.transaction = {}
        
        
    def check_balance(self):
        print(f"check balance:  {self.balance}")
        
    def deposite(self,amount):
        if isinstance(amount, (int, float)):
            if amount >0:
                self.amount = self.balance + amount
                self.add_transaction()
                return "done"
            else:
                print("Enter positive maount")
        else:
            print("Enter only numeric value ")
        
    
    def withdraw(self,amount):
        if isinstance(amount, (int, float)):
            if amount >0:
                if amount <=self.balance:
                    self.balance = self.balance-amount
                    return"done"
                else:
                    return "insuffiient blanace"
            else:
                return "enter positive value"
        else:
            return "enter only numeric"
        
        
    def add_transaction(self,type, amount):
        tid = len(self.transaction) + 101
        dt = str(date.today())
        bal = self.balance
        self.transaction[tid] = {"date":dt,}
        return 'done'
        
        
    def show_transaction(self):
        print('-'*105)
        print(f'{"ID":^20} {"Date":^20} {"Type":^20} {"Amount":^20} {"Balance":^20}')
        print('-'*105)
        
        for tid in self.transaction:
            print(f'|{tid:^20}| {self.transaction[tid]['date']:^20}| {self.transaction[tid]['type']:^20} |{self.transaction[tid]['amount']:^20} {self.transaction[tid]['balance']:^20}')
            print('-'*105)
            
ram = Saving_Account('ram patil', 123456789011234,20000)
print(ram.add_transaction)
ram.deposite(5000)

class Current_Account(Saving_Account):
    pass


c1 = Current_Account()
