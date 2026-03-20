# def firstNonRepeating(arr, n):
#     for i in range(n):
#         j = 0
#         while(j < n):
#             if (i != j and arr[i] == arr[j]):
#                 break
#             j +=1
            
#         if (j ==n):
#             return arr[i]
#     return -1

# arr=[9, 4, 9, 6, 7, 4]
# n = len(arr)
# print(firstNonRepeating(arr, n))


# from collections import defaultdict
# def firstNonRepeating(arr, n):
#     mp = defaultdict(lambda: 0)
    
#     for i in range(n):
#         mp[arr[i]] += 1
        
        
#     for i in range(n):
#         if mp[arr[i]] == 1:
#             return arr[i]
#     return -1


# arr = [9, 4, 9, 6, 7, 4]
# n = len(arr)
# print(firstNonRepeating(arr, n))



# def rotatorArr(arr, d):
#     n = len(arr)
    
#     for i in range(d):
#         first = arr[0]
#         for j in range(n - 1):
#             arr[j] = arr[j + 1]
#         arr[n - 1] = first
        
# if __name__=="main":
#     arr = [1, 2, 3, 4, 5, 6]
#     d = 2
    
#     rotatorArr(arr, d)
    
#     for i in range(len(arr)):
#         print(arr[i], end = " ")




# n = int(input())
# arr = list(map(int, input().split()))
# d, x = map(int, input().split())

# countEven = 0
# countOdd = 0

# for i in range(n):
#     if arr[i] % 2 == 0:
#         countEven +=1
#     else:
#         countOdd +=1
        
# if d % 2 !=0:
#     if countEven ==0:
#         print("0")
#     else:
#         print(countEven * x)
# else:
#     if countOdd == 0:
#         print("0")
#     else:
#         print(countOdd * x)



# s = input()
# n = int(input())
# sum = 0
# for i in s:
#     sum +=int(i)
# sum*=n
# s=str(sum)
# while len(s)>1:
#     sum = 0
#     for i in s:
#         sum +=int(i)
#     s=str(sum)
# print(s)


# n = int(input())
# fact = [0] *(n + 1)
# fact[0] = 1
# for i in range(1, n + 1):
#     fact[i] = fact[i - 1] * i
# print(fact[n - 1] * 2)


# palindrome -> If original == reversed → palindrome
# n[::-1] reverses the string
# n = input("enter number :")
# if n ==n[::-1]:
#     print('palindrome')
# else:
#     print("not palindrome")


# n = int(input())
# original = n
# reverse = 0

# while n > 0:
#     digit = n % 10
#     reverse = reverse * 10 + digit
#     n //= 10
    
# if original == reverse:
#     print('palindrome')
# else:
#     print('not palindrome')



# It is greater than 1
# It has only 2 factors → 1 and itself

# n = int(input())
# if n <= 1:
#     print("not prime")
# else:
#     for i in range(2, n):
#         if n % i == 0:
#             print("not prime")
#             break
#     else:
#         print("prime")



# n = int(input())
# total = n * (n + 1) // 2
# print(total)


n = int(input())
total = 0

for i in range(1, n + 1):
    total +=1
    
print(total)