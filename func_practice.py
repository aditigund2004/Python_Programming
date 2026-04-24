# cube of number

# def cube():
#     num = int(input("Enter number to find cube: "))
#     cu = num ** 3
#     print(cu)
    
# cube()


# even or odd

# def even_odd():
#     nu = int(input("Enter number :"))
#     if nu%2 == 0:
#         print("Even")
#     else:
#         print("Odd")
            
# even_odd()



# def even_odd(nu):
#     if nu%2 == 0:
#         print("Even")
#     else:
#         print("Odd")
            
# even_odd(3)



# prime number 1 to n
# divisible by 1 or divisible by itself



# n = int(input("ENter number :"))

# print("prime number 1 to n :")
# for num in range(2, n + 1):
#     for i in range(2, num):
#         if (num % i) == 0:
#             break
#     else:
#         print(num, end=" ")


'''

यहाँ कोड का आसान स्पष्टीकरण दिया गया है:
range(2, n + 1): हम गिनती 2 से शुरू करते हैं क्योंकि 1 को अभाज्य (prime) नहीं माना जाता। यह लूप 2 से लेकर आपके दिए गए नंबर n तक एक-एक करके जाता है।
for i in range(2, num): अब हर नंबर (जिसे हम num कह रहे हैं) को जाँचने के लिए हम एक छोटा लूप चलाते हैं। यह 2 से लेकर उस नंबर से ठीक पहले वाले अंक तक जाता है।
if (num % i) == 0: यहाँ हम भाग देकर देख रहे हैं। अगर num किसी भी बीच वाले नंबर i से पूरी तरह कट जाता है (शेषफल 0 आता है), तो इसका मतलब है कि यह अभाज्य नहीं है।
break: जैसे ही हमें पता चलता है कि नंबर अभाज्य नहीं है, हम break का उपयोग करके उस नंबर की जाँच वहीं रोक देते हैं और अगले नंबर पर बढ़ जाते हैं।
else: (For-Else Magic): यह पाइथन की एक खास खूबी है। अगर अंदर वाला लूप पूरा खत्म हो गया और उसे कोई भी ऐसा नंबर नहीं मिला जो num को काट सके (यानी break हिट नहीं हुआ), तो else वाला हिस्सा चलता है और वह उस नंबर को Prime मानकर प्रिंट कर देता है।

'''


# n = int(input("Entr numeber :"))
# print(f"prime number from 1 to  {n} :")
# def prime_no():
#     for num in range(2, n + 1):
#         for i in range(2, num):
#             if (num % i) == 0:
#                 break
#         else:
#             print(num, end = " ")

# prime_no()
# import math

# def prime(num):
#     if num <= 1:
#         return False
    
    
#     for i in range(2, int(math.sqrt(num)) + 1):
#         if num % i == 0:
#             return False
#     return True

# num = 29
# if prime(num):
#     print(f'{num} is prime')
    
# else:
#     print(f"{num } is not prme")
    



# def palindrome(n):
#     return str(n) == str(n)[::-1]

# num ='12321'
# if palindrome(num):
#     print(f"{num} id pallin")
# else:
#     print(f'{num} is not pali')
    
    
    
    
# num = 121
# n = num[::-1]
# print(n)
# TypeError: 'int' object is not subscriptable



# num = 'aditi'
# n = num[::-1]
# print(n)
# itida



# print number fron 1 to n
# def num():
#     num = int(input("Enter number from 1 to n :"))
#     for i in range( 1, num + 1):
#        print(i)
# num ()






# def print_numbers(n):
#     for i in range(1, n + 1):
#         print(i)
# print_numbers(5)



# sum of two number take input from user

# def sum():
#     n = int(input("ENter num :"))
#     n2 = int(input("ENter num :"))
#     sum = 0
#     for i in range(n, n+n2):
#         sum = sum + i
#     print(i)
    
# sum()

# def sum(n1, n2):
#     return n1 + n2

# n1 = int(input("Enter number :"))

# n2 = int(input("Enter number :"))

# result = sum(n1, n2)

# print(f"sum is {n1} and {n2} is : {result}")




# def positive():
#     num = int(input("ENter number  : "))
#     if num == 0:
#         print("zero")
#     elif num >= 0:
#         print("positive ")
#     else:
#         print("nagative")

# positive()        




# Write a function to check whether a number is divisible by 7.

# def divisible(num):
#     if num%2 ==0:
#         print("divisible")
#     else:
#         print("not divisible")
        
# divisible(7)




# def divisible(num):
    
#     return num%2==0
# num=7
# if divisible(num):
#     print(f"{num} is divisible")
# else:
#     print(f"{num} is not divisible")
        



# def divi(num):
#     return num%2 ==0 and num%5 ==0

# num = 9
# if divi(num):
#     print(f'{num} divisible by both 2 and 5')
# else:
#     print(f"{num} not divisible by 2 and 5")



def leap():
    year = int(input("Enter number :"))
    if(year%4==0 and year%100!=0 or year%400==0):
        print(f" {year} is leap year")
    else:
        print(f" {year} is not leap yera")
leap()

# Enter number :2004
#  2004 leap year 


# TypeError: leap() missing 1 required positional argument: 'year'

