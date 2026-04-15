#Write a pgm to find how many vowels are there in a string
def string(word):
    count = 0
    vowels = "aeiou"
    for char in word:
        if char in vowels:      
            count = count +1
    print(count)        

string('python is a programming language')  



#WAP to reverse the string
name = input('enter the string :')
rev = ''
for char in name:
    rev= char + rev
print(rev)    
    
    


#reverse the name in the list and print the list again
students = ['kunal','rahul','pavan','arjun']
char_reverse = [n[::-1]for n in students]
print(char_reverse)
    
students = ['kunal','rahul','pavan','arjun']
rev_name =[]
for name in students:
    rev = ''
    for char in name:
        rev= char + rev
    rev_name.append(rev)    
print(rev_name)




#WAP to count the no of even numbers and odd numbers from the list
list = [12,45,77,987,454,1413,565,323,45,677,155,67,5,55,2]
even_count = 0
odd_count = 0
for num in list:
    if num%2 == 0:
        even_count=even_count+1
    else:
        odd_count=odd_count+1

print(even_count)
print(odd_count) 





#WAp to check whether the sting is pallindrome or not 
name = input('Enter the name : ')
original = name
reverse = ' '
for char in name:
    char_reverse = char + reverse 
if name ==reverse:
        print('Pallindrome')
else:
        print('Not Pallindrome')    
    




#WAP to find the frequency of the each character from the string
name = 'ram'
dict = {}
count = 0
for char in name:
    if char not in dict:
        dict[char]=1
    else:
        dict[char]=dict[char]+1
print(dict)    




#Create a function to calculate addition of two numbers
def addition(n1,n2):
    add = n1+n2
    print(add)
addition(10,12)

def addition(n1=0,n2=0):
    add = int(n1)+int(n2)
    return add
print(addition('22','12'))

def sum(n1,n2):
    result = int(n1)+int(n2)
    return result
print(sum('10','20'))

def sum(n1=0,n2=0):
    if isinstance(n1,(int,float))and isinstance(n1,(int,float)):
        result=n1+n2
        return result
    else:
        print('Enter only int or float numbers')
        n1=eval(input('enter n1 :'))
        n2=eval(input('enter n2:'))
        result = sum(n1,n2)
        return result
print(sum('10','20'))    






#Write a function to return the square of number
def square(n):
    return n*n
print(square(4))



#write a function to return cube of number
def cube(n):
    return n**3
print(cube(2))




#write a function to return power of number
def power(base,power):
    return base ^ power
print(power(10,2))

def num(b,p):
    return b**p
print(num(12,2))

def get_power(base,power):
    p=1
    for i in range(1, power+1):
        p = p*base
        return p
get_power(10,2)       




#write a function to return count of a number which is divisible by 4 and 7
def function1(n1,n2):
        count = 0
        for i in range(n1,n2+1):
                if i%4==0 and i%7==0:
                        count = count+1
                        return count
print(function1(28,56))




#write a function to check the number is prime or not 
def prime(n):
   count = 0
   for i in range(1,n+1):
      if(n%i==0):
         count+=1
   if(count==2):
         print('Prime number')   
   else:
         print('Not a prime number')         
prime(15)      





#write a function to print prime no from 1 to 100
def prime1(n1,n2):
    for i in range(n1,n2+1):
            count = 0
            for j in range(1,i+1):
                 if i %j==0:
                      count+=1
            if(count==2):
                 print(i)
print(prime1(1,100))

def is_prime(n):
    if n < 2:
        return False
    return all(n%i!=0 for i in range(2,int(n**0.5)+1))
is_prime = list(filter(is_prime,range(1,101)))
print(is_prime)

'''
we can call function within the function instead of rewritting the same logic again 
'''

#write a function to print count of prime number from 1 to 100
# def prime1(n1,n2):
#     count = 0
#     for i in range(n1,n2+1):
#             if n%i==
#             for j in range(1,i+1):
#                  if i %j==0:
#                       count+=1
#             if(count==2):
#                  print(i)
# print(prime1(1,100))

# def is_prime(n):
#     if n < 2 and all(n%i != 0 for i in range(2,int(n**0.5)+1)):
#         total_primes = len(n for n in range(1,101)) 
#         if is_prime(n):
#             print(total_primes)
# is_prime(234)            


    

# write a function to print divisor of a number
def print_divisor(n):
     divisor = [i for i in range(1,n+1) if n % i==0]
     print(divisor)
print_divisor(12)     




#write a function to print divisor of a number
def print_divisor(n):
     for i in range(1,n+1):
          if(n%i==0):
               print(i,end=' ')
               
print_divisor(12)    





#write a function to print the number divisors
def print_divisor(n):
     count = 0
     for i in range(1,n+1):
          if(n%i==0):
               count = count+ 1
               print(i,end=' ')
               return count
print(print_divisor(12)) 



#print the sum of all the divisors of all the numbers
def sum_off_divisor(n):
     sum = 0
     for i in range(1,n+1):
          if n%i==0:
               sum = sum+i
          print(sum)   
sum_off_divisor(12)            




# #finding sum of perfect square
def chechperfectno(n):
     sum = 0
     for i in range(1,n):
          if n%i==0:
               sum = sum+i
     if(sum == n):
               print('perfect')
     else:
               print('not perfect')                
chechperfectno(28)




# write a function to find the total count of no
def prime1(n):
    count = 0
    for i in range(1,n):
            if n % i==0:
               sum = sum+i
            for j in range(1,i+1):
                 if i % j==0:
                      count+=1
            if sum == 0:
                 print('perfect')
print(prime1(28))