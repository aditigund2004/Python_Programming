'''
 type casting
converting one object into another onject


eval() - convert any datatype into another datatpype 
used only with input() or string

'''


# WAP to calculate squre of any number
num1 = int(input('Enter number to find out the squre:'))
squre = num1**2
print(squre)

x = input('Enter something:')
print(type(x))

x1 = float(input("Enter something:"))
print(type(x1))


x2 = list(input("Enter something"))
print(type(x2))


num = 29.54
print(type(num))
num=int(num)
print(num)
print('-'*100)


num3 = 100
text = str(num3)
print(text)
print(type(text))
print('-'*100)



num=eval(input("Enter number"))
sq = num**2
print(type(num))
print(sq)
print('-'*100)


#WAP to cal peri-meter of square
side = eval(input("Enter side:"))
peri_mete=4 +(side * side)
print(peri_mete)
print('-'*100)


#WAP to cal sercumference of number
radius = eval(input("Enter the radius of the circle:"))
pi = 3.14
cir = 2*pi*radius
print(cir)
print('-'*100)


#WAP to cal ligth bill
unit = eval(input("Enter unit:"))
rate = eval(input("enter rate per unit:"))
bill = unit * rate
print("Your bill is:",bill)
print('-'*100)


# new salary after increment
current_salary = eval(input("ENetr current salary:"))
incremet = eval(input("Encrement: "))
new_salary = current_salary * incremet / 100
current = current_salary + new_salary
print("Current salary is:", current)
print(f"your salary after {incremet} % increment is {current}")
print('-'*100)


# multiple input in one line
a, b = input("Enter two numbers: ").split()
print(a, b)

a, b = map(int, input("Enter two numbers: ").split())
print(a, b)
print('-'*100)


print("Python", "is", "easy", sep="-")
