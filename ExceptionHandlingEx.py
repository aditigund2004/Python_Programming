'''
Exception handling ->
Exception handling is used to handle runtime errors so that the program does not crash.

An exception is an error that occurs during program execution.


Examples ->

   1. Division by zero
   2. Invalid input
   3. File not found

Exception Handling -> ubnormal situation occure suring excution of program

what is error ->
type of error
1.synatx error -> written wrong logic

2. logic wrror -> logic is wrong


3. runtime error -> type error, indentation error , handle ueing exception handling


# blocks
1. try - where error in the program
use only once in program

2. except -> handle the error

3. else ->

4. finally -> always execute if thier is exception in program or not

keyword
1. raise -> 

as-> temporary name


Exception ->
(class) Exception
Common base class for all non-exit exceptions.

1.
try 
excepte

2.
try 
except
except


try:
    # risky code
except:
    # runs if error occurs
 '''
num1 = 10

try:
    print(num1/10)
    
except Exception as e:
    print(e)



try:
    a = int(input("Enter number: "))
    b = int(input("Enter number: "))
    print(a / b)
except:
    print("Error: Division by zero not allowed")



num2 = 20
print(num1+20)
print("operation complete")



l1 = [10,20,30]
try:
    print(l1.remove(100))
    
except Exception as e:
    print(e)
    
else:
    print("else block")
    
finally:
    print("finally block")


try:
    num = int(input("Enter number: "))
    print(10 / num)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid input")





age = 18
try :
    if age < 18:
        print("eligible")
    else:
        raise Exception 
    
except Exception as e:
    e = 'age is blow 18'
    print(e)
    
    
    
    
try:
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    print(a / b)
except ZeroDivisionError:
    print("Zero division error")
else:
    print("Operation successful")
    
    
    
# WAP fro type error

num = 10
str = '10' 
print(num + str)



# value error
num = int(input("Enter number"))
print(num)


username = "ram"
password = "ram@123"

try:
    if username == "ram" and password == "ram@12":
        print("enter home page")

    else:
        raise Exception
        
except Exception as e:
    e = 'username and password not match'
    print(e)
    
    
    
try:
    f = open("data.txt", "r")
    print(f.read())
except FileNotFoundError:
    print("File not found")
finally:
    print("Program ended")
    
    
'''
try:
    pass
except ExceptionName:
    pass
else:
    pass
finally:
    pass

'''