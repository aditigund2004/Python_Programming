'''
Encapsulation ->
    binding data(attribute) and methods
    different type of data
    

private -> within method only
'''
# class counter_machine:
#     def __init__(self):
#         self.in_count = 0
#         self.out_count = 0
    
#     def display_count(self):
#         print(f'''
#               In count : {self.in_count}
#               Outn count : {self.out_count}
                
#               ''')
        
        
#     def inc_in_count(self):
#         self.in_count = self.in_count + 1
        
        
        
#     def inc_out_count(self):
#         self.out_count = self.out_count + 1
        

#     def reset(self):
#         self.in_count = 0
#         self.out_count = 0
        
# demart = counter_machine()
# demart.display_count()
# demart.inc_in_count()
# demart.inc_in_count()
# demart.inc_in_count()
# demart.inc_in_count() 
# demart.in_count=233
# # access attribute outside of the class

# demart.display_count()
# demart.inc_out_count()
# demart.inc_out_count()
# demart.display_count()



# class counter_machine:
#     def __init__(self):
#         self.__in_count = 0
#         self.__out_count = 0
    
#     def display_count(self):
#         print(f'''
#               In count : {self.__in_count}
#               Outn count : {self.__out_count}
                
#               ''')
        
        
#     def inc_in_count(self):
#         self.__in_count = self.__in_count + 1
        
        
#     def inc_out_count(self):
#         self.__out_count = self.__out_count + 1
        
#     def reset(self):
#         self.__in_count = 0
#         self.__out_count = 0
        
        
# demart = counter_machine()

# demart.inc_in_count()
# demart.inc_in_count()
# demart.inc_in_count()
# demart.inc_in_count()
# demart.display_count()

# demart.inc_out_count()

# demart.display_count()


# private -> update using gatter and setter

# getter merhod use to get method outside the class or method

class Student:
    def __init__(self,nm,ag ):
        self.__name = nm 
        self.__age = ag
        
    def display(self):
        print(f' Name : {self.__name}\nAge : {self.__age}')       
        
    def get_name(self,nm):
        if isinstance(nm, str) and nm.isalpha():
             return self.__name 
        
    def get_age(self,ag,nm):
        if isinstance(nm, str):
            self.__age=ag
    
     
    def set_name(self,nm):
        self.__name=nm
        
    def set_age(self,ag):
        self.__age = ag
        
s1 = Student("ram", 22)
s1.display()

s1.set_name("ram")

s1.set_age(22)
s1.display()
        
        