'''
pre-defined fun - input(), print()
print() - pre-defined func used to print the stsement on the terminal
variable - contains value with the reference in the memory


variable = value - creating object
'''
#sum of two number
a = 10
b = 20
print(a+b)
print('--------------------------------------------------------------')

a1, b1 = 10, 20
print(a1+b1)
print('--------------------------------------------------------------')

a2 = 10
b2 = 20
sum = a2+b2
print(a2+b2)
print('--------------------------------------------------------------')

# a3 = int(input("Enter first number:"))
# b3 = int(input("Enter second number:"))
# print("the sum of the two numbers is:",a3+b3)
# print('--------------------------------------------------------------')


#square of the nuber
square = 4
result = square**2
print(result)
print('--------------------------------------------------------------')

print(5**2)
print('--------------------------------------------------------------')


#cube of number
cube = 15
result1 = cube**3
print(result1)
print('--------------------------------------------------------------')

print(15**3)
print('--------------------------------------------------------------')

#area of rectangle
length = 100
width = 50
result3 = length * width
print(result3) 
print('--------------------------------------------------------------')

print(100*50)
print('--------------------------------------------------------------')

#perimeter of rectangle
len = 100
wid = 50
result4 = 2 + (len * wid)
print(result4)
print('--------------------------------------------------------------')

print(2*(100+50))
print('--------------------------------------------------------------')

#average of 3 numbers
n1 = 10
n2 = 20
n3 = 30
avg = (n1+n2+n3)/3
print('The Average of Three Number is:',avg)
print('--------------------------------------------------------------')



#selling price of the product
mrp = 50000
dis = 10
#for percent use / divide
discount_price = mrp * dis / 100
selling_price = mrp - discount_price 
print("selling price is:",selling_price)
print('--------------------------------------------------------------')

mrp1 = 50000
discount = 10
dis_price = mrp1 * discount / 100
sell_price = mrp1 - dis_price 
print("Selling price is:",sell_price)
print('--------------------------------------------------------------')

t1 = 70
t2 = 80
t3 = 90
obtain = t1+t2+t3 
total = 3 * 100
per = (obtain/total)*100 
print("Percentag is:",per)
print('--------------------------------------------------------------')


#diagonal of rectangle
# length5 = 100
# width5 = 50
# diagonal = sqrt((heigth5**2)+(width5**2))
# print(diagonal) 

length5 = 100
width5 = 50

diagonal = (length**2 + width5**2)**0.5
print("Diagonal is",diagonal)
print('--------------------------------------------------------------')


#calculaye new salary of increment
salary = 40000
increment = 20

incre = salary + salary * increment/ 100

print("Increment salary is:",incre)
print('--------------------------------------------------------------')

# String formatting

print("hello welcome to the nexanova protech orgnisation shivajinagar pune")

# def keyward used to define function
# * = contain or have many values

# parameter - pass variable
# argument pass value

# id() - object passing and only pass only one parameter seperating by comma ,
# ex print(name, age, no)
# id() - memory location or addresss
# type() - return data tyoe of object


n1 = 1
n2 = 3
n3 = 4
print(n1, n2, n3)
print(n1, n2, n3, sep='-')
print(n1, n2, n3, sep='')
print(n1, n2, n3, end=' ')

print(id(n1))
print(id(n2))

print(type(n1))



#string fomatting

mrp = 40000
dis = 10
dis_price = mrp * dis / 100
sel_price = mrp - dis_price
print("MRP :", mrp, "Discount :",dis, "Selling price :",sel_price)

print('mrp : %d discount : %d selling price : %d'%(mrp, dis, sel_price))
print('---------------------------------------------------------')

'''
place holder
synatx:
  'msg %d msg %d msg %d'(v1,v2,v3)
%d - integer

'''


#simple interest
#loan
principle_amount = 100000
#intererst or vyaj
rate_interest = 10

time = 1
simple_interest = principle_amount * (rate_interest / 100) * time
#total amount to return
total_amount = principle_amount + simple_interest

print(total_amount)
print(simple_interest)
print(principle_amount)

print('Total Amount to Return : %d \n Rate of Interest :%d \n Simple Interest : %d'%(total_amount, simple_interest, principle_amount))


n1 = 10.5
n2 = 4.6
sum = n1+ n2
print('sum of %0.2f \nand %0.3f is \n%0.1f'%(n1,n2,sum))


name = "ram"
age = 22
city = "pandharpur"

print('My name is %s and i am %d years old and i am from %s'%(name, age, city))