numbers = [1, 2, 2, 3, 4, 4]

unique = list(dict.fromkeys(numbers))
print(unique) 

num1 = eval(input("Enter number to check number is even or odd :"))
# num = 2
if num1%2 == 0:
    print("even")
else:
    print("odd")


number = eval(input("Enter any three number to check the number is largest :"))

if number >= 0:
    print("largets")
elif number <= 0:
    print("smaller")

# print(number)



str1 = 'Welcome Python'

print(str1.split())

print(str1.rsplit())

str2= str1.split()

str3 =" "


for i in str2:
    str3 = i + str3
    print()
    
print(str3)

str3 = str2[::-1]

str4 = " ".join(str3)

print(str4)



# string plindrome
# usign slicing
str = 'aditi'
if str == str[::-1]:
    print("yes")
else:
    print("no")



str5 = 'sham'

rev_str =""
for i in str5:
    rev_str +=i
    
if str5 ==rev_str:
    print("yes")
else:
    print("no")
    




s = "ram"
rev = ''.join(reversed(s))

if s == rev:
    print(rev)
else:
    print(rev)
    
    
    
num1 = 121
num2 = num1
num = 0
while num1 >0:
    digit = num1 % 10
    num = (num * 10) + digit
    num1 = num1 // 10
    
if num2 == num:
    print("yes")
else:
    print("no")
print(num1)




num1 = 1212
s_num1 = str(num1)
r_nm = ''
for i in s_num1:
    r_nm = i + r_nm
    
num2 = int(r_nm)
    
if num1 == num2:
    print("yes")
else:
    print("no")





# def factorialcount(n):
#     fact = 1
#     for i in range(1, n+1):
#         fact *=i
#     print(f"Factorial :{fact}")
# factorialcount(5)
        
        


# a = 0
# b = 1
# c = 10
# print(a)
# print(b)
# for i in range(3, c+1):
#     d = a+b
#     print(d)
#     a=b
#     b=d


# name = "Aditi"
# if name==name[::-1]:
#     print(f"name is palindrome : {name}")
# else:
#     print(f"name is not palindrome : {name}")




def palinfrome_num(num):
    if num < 0:
        return "It is not palindrome number"
          
    original = num
    reve = 0
    
    while num > 0:
        digit = num % 10
        reve = (reve * 10) + digit
        num = num // 10
        
    if original == reve:
        return "Palindrome"
    else:
        return "not palindrome"

print(palinfrome_num(121))
  




year = 2024
if (year % 4 ==0 and year % 100 != 0) or (year % 400 == 0):
    print("leap year")
else:
    print("not leap year")
    
    
    
def check_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return f"{year} is a leap year"
    else:
        return f"{year} is not a leap year"
print(check_leap_year(2024))  
print(check_leap_year(1900))  
print(check_leap_year(2000))  



# def facto(n):
#     if(n==1 or n==0):
#         return 1
#     return facto(n-1) *n
# print(facto(5))




num =10
if num > 1:
    for i in range(2, num):
        if(num % 1) ==0:
            print("not prime")
            break
        else:
            print("prime")
    else:
        
        print("not prime")

