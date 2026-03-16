# def fun(arr, n):
#     ans = []
#     t =1
#     if arr[0] > 0:
#         t = 0
#     i = 0
#     while i < n:
#         if t == 0:
#             j= i
#             while j < n:
#                 if arr[j] >0:
#                     j +=1
#                 else:
#                     break
#                 ans.append(max(arr[i:j]))
#                 i = j
#                 t = 1
#         else:
#             j = i
#             while j <n:
#                 if arr[j] < 0:
#                     j += 1
#                 else:
#                     break
#             ans.append(max(arr[i:j]))
#             i = j
#             t = 0
#     return sum(ans)
# n = int(input())
# ar = list(map(int, input().split()))
# print(fun(ar, n))
    
    
# def fun(arr, n):
#     ans = []
#     i = 0
    
#     while i < n:
#         j = i
        
#         if arr[i] > 0:
#             while j < n and arr[j] > 0:
#                 j += 1
#         else:
#             while j < n and arr[j] < 0:
#                 j += 1
        
#         ans.append(max(arr[i:j]))
#         i = j
    
#     return sum(ans)


# n = int(input())
# ar = list(map(int, input().split()))
# print(fun(ar, n))



# question 2

# def fun(k, n, arr):
#     left = 0
#     curr_sum = 0
#     max_len = 0
    
#     for right in  range(n):
#         curr_sum += arr[right]
        
#         while curr_sum >= k:
#             curr_sum -= arr[left]
#             left += 1
            
#         max_len = max(max_len, right - left + 1)
        
#     return max_len


# n, k = map(int, input().split())
# arr = list(map(int, input().split()))

# print(fun(n, k, arr))


# def fun(n, k, arr):
#     ans = 0
#     if min(arr) < k:
#         ans = 1
#     for i in range(n - 1):
#         for j in range(i + 1, n):
#             if sum(arr[i:j]) < k:
#                 ans = max(ans, j - i)
#             else:
#                 break
#     return ans
# n, k = map(int, input().split())
# arr = list(map(int, input().split()))
# print(fun(n, k, arr))



# n = int(input())
# j = 0
# l = [0 for i in range(n)]
# for i in range(n):
#     a = int(input())
#     if a!=0:
#         l[j]=0
#         j +=1
        
# for i in l:
#     print(i, end=" ")



# n = int(input())
# j = 0
# l = [0 for i in range(n)]

# for i in range(n):
#     a = int(input())
#     if a != 0:
#         l[j]=a
#         j += 1
        
# for i in l:
#     print(i, end=" ")


# arr = list(map(int, input().split()))
# n = len(arr)

# j = 0
# l = [0]*n

# for i in arr:
#     if i != 0:
#         l[j] = i
#         j += 1

# print(*l)

# import math
# n=int(input())
# k=(1<< int(math.log2(n))+1)-1
# print(n^k)



def main():
    s = input()
    a = int(input())
    m = {
        "mon": 60, "tue": 5, "web":4,
        "thus":3, "fri":2, "sat":1, "sun":0
    }
    ans = 0
    if a - m[s[:3]] >= 1:
        ans = 1 + (a - m[s[:3]])
    print(ans)
    
if __name__ == "__main__":
    main()