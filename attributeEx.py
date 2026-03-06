'''
class -> blue print and can create object as many want


syntax:
class student -> class
  def __init__(self): -> constructure ans self parametr
      pass
      #code


s1 = student() -> object


class ->
1.properties -> attributes
2.operation -> methods



attribute ->  variable it used to store value or data and reperent properties / data -> properties
example(student ) -> age = 22

type
1. instance attribute-> object level
2. class or static attribute -> class level -> inside class and outside the method
3. local attribute ->



1. instance attribute-> object level
ex -> student management system so the student is object wich have
name
age
address
spefic for each student or different
->
 #########       which is define within construtr by using self

syntax of instance when the object level
self.varivle_name = value

class student:
    #attribute -> varible -> store value
    def __init__(self): -> constructure 
    # method

class student:
    def _init__(self,nm, ag,ct, per):
        #instance attribute and create within any method
        self.name=nm -> initialize
        self.age=ag
        self.city=ct
        self.percentage=per

s1 = student('ram', 22, 'pune', 89)


print(s1.age) -> s1 is reference outside of the class to access
outside use reference varible means object name to access the variable

access inside class -> self 


1.new method used to aallocate the memory
2. init method 




2. class or static attribute ->
class level data which is same for all 
which is define within class and outside of the method

class student:
    #attribute -> varible -> store value
    
    c_var = value
    
    def __init__(self): -> constructure 
    # method




class student:
    # class attribute
    course = ""
    triner = ""
    institute = ""
    # all object can access and only one memeory will allocate
    def _init__(self,nm, ag,ct, per):
        #instance attribute and create within any method
        self.name=nm -> initialize
        self.age=ag
        self.city=ct
        self.percentage=per

s1 = student('ram', 22, 'pune', 89)


how to access

print(s1.course)
print(s1.triner)
print(s2.course) -> instance attribute by referrnce name
# print(student.course)  access by using class



3. local attribute -> method level
within method v_name

syntax:
def method_name(self):
    var=result
'''

# class student:
#     def __init__(self, nm, ag, ct, per):
#         self.name = nm
#         self.age = ag
#         self.city = ct
#         self.percentage = per
        


# # (nm: Any, ag: Any, ct: Any, per: Any) -> student
# s1 = student('ram', 22, 'pune', 89)

# print(s1)


# class employee:
#     company_name = "NexaNova Protect company"
#     Reporting_Manager = "Amita"
#     location = "Shivaji nagar pune"
#     def __init__(self, eid, nm, dep, sal):
#         self.emp_id = eid
#         self.name = nm
#         self.department=dep
#         self.salary= sal
        
# ram = employee(101, 'ram ', 'Hr', 40000)



# print(employee.company_name)



class account:
    branch = "pune"
    
    def __init__(self, acc, ifsc, bala):
        self.account_no = acc
        self.IFSC_code=ifsc
        self.balance= bala
        
    # def detail():
    #     f'account number: {acc}\n IFSC code: {ifsc}\n Account balance: {bala}'
        
        
a1 = account(123123123123456, 'BOI20254', 250000)
print(account.branch)
print(a1.account_no)
print(a1.IFSC_code)
print(a1.balance)



'''

method ->
functiona which is define within class it used to perform operation on data or reusable block of code

type of method ->
1. instance method -> function which will work (operation) on the object level
self (parameter in function) refernce
by using the reference of the objrct can call the method within class using self

obj -> outside
reference -> within

syntax:
def m1(self):
    # instace
    pass 


call method by using the object refernece
o1=class_name()

and inside class user self.m_name



2. class method ->
function used to perform operation on the class attribute
use decorator

decorator @classmethod

call by suing object ref
self within class
or class name


syntax:
@classmethod
def m1(cls):
    passs
'''
