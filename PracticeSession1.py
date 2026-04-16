# Even Odd number
number = eval(input("Enter number:"))
if number%2 ==0:
    print("even")
else:
    print("odd")
    
    
#  pass Fail
mark = eval(input("Enetr marks"))
if mark >=40:
    print("pass")
else:
    print("fail")
    
    
# max number 
list = [121,34,5,56,77,8,23,21]
max = list[0]
for li in list:
    if li > max:
        max = li
print(max)
        
    
# min number
list = [121,34,5,56,77,8,23,21]
min = list[0]
for li in list:
    if li < min:
        min = li
print(min)


        
        
        
number = eval(input("Enetr number to check number is divisible or not:"))
if (number%3==0 and number%5==0):
    print("divisible by 3 ")
elif (number%5==0):
    print("divisible by 3 and 5 ")
elif (number%3==0 ):
    print("divisible by 3 ")
    
else:
    print("not divisible by 3 and 5")


# leap year
year = eval(input("Enetr year :"))
if(year%4==0 and year%100!=0 or year%400==0):
    print("leap year")
else:
    print("not leap year")



# WAP to print sum of 1 to 10
n1=int(input("Enetr number"))
n2=int(input("Enetr number"))
sum=0
for i in range(n1,n2+1):
    sum=sum+i;
print(sum)


# 55 to 23 in reverse order
n1=int(input("Enetr number"))
n2=int(input("Enetr number"))
sum=0
for i in range(n1,n2-1,-1):
    sum=sum+i;
print(sum)



n1=int(input("Enetr number"))
n2=int(input("Enetr number"))
if n1>n2:
    n1,n2=n2,n1
sum=0
if n1<n2:
    for i in range(n1,n2+1):
        sum=sum+i;
print(sum)


emp_salary = {'jay':60000,'ajay':30000,'rajesh':78000,'om':64000,'kunal':35000}
sum =0 
for salary in emp_salary.values():
    total=total+sum
print(sum)
    
    



emp_salary = {'operation':{'jay':60000,'ajay':30000},
              'placement' :{'rajesh':78000,'om':64000},
              'sales':{'kunal':35000,'ram':40000}}

total_salary={}
for dep,emp in emp_salary.items():
    
    total = 0
    for sal in emp.values():   
        total +=sal
    total_salary[dep]=total
print(total_salary)
    
    
# emp slary  addition of all dep with increnemt 
emp_salary = {'operation':{'jay':60000,'ajay':30000},
              'placement' :{'rajesh':78000,'om':64000},
              'sales':{'kunal':35000,'ram':40000}}

total_salary={}
for dep,emp in emp_salary.items():
    
    total = 0
    for sal in emp.values():
        total=total+sal*15/100
   
        total +=sal
    total_salary[dep]=total
print(total_salary)
    
    
# percentag
bhushan = {'t1':78,'t2':89,'t3':78,'t4':84}
obt = 0

for marks in bhushan.values():
    obt = obt + marks
total =len(bhushan)
per = (obt/total)

print("Percentag is:",per)