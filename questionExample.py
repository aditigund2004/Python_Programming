# n = int(input())

# arr = list(map (int, input().split()))

# print((n-arr.count(arr[0])))



# N = int(input())
# D = list(map(int, input().split()))

# count_fail = 0


# if D[0] == 0:
#     count_fail +=1
    
# for i in range(1, N):
#     if D[i] ==0 or D[i] != D[i -1]:
#         count_fail +=1
# print(count_fail)



# N = int(input())
# D = list(map(int, input().split()))

# fail_count = sum(1 for i in range(N) if D[i] == 0 or (i > 0 and D[i] != D[i-1]))

# print(fail_count)




# A = int(input())

# B = input()

# C = input()

# if A == B:
#     print(1)
    
# res, res2 = ''','''

# for x in range(A):
#     if A[x] != B[x]:
#         res += A[x]
#         res2 += B[x]
# ans = 0
# for i in A:
#     if ans != 0:
#         break
#     if i not in B:
#         print(-1)
#         break
#     else:
#         for x in set(res2):
#             if x not in A:
#                 print(-1)
#                 ans += 1
#                 break
#             else:
#                 print(len(set(res2)))
#                 ans += 1
#                 break
#         if ans == 1:
#             break



n = int(input())
a = input()
b = input()

ops = 0

a = list(a)


for c in range(26):
    ch = chr(ord('a') + c) 
    indices = [i for i in range(n) if a[i] != b[i] and b[i] == ch]
    
    if indices:
        smallest = min(a[i] for i in indices)
        if smallest > ch:
            for i in indices:
                if a[i] != ch:
                    a[i] = smallest
            ops +=1 
        else:
            for i in indices:
                a[i] =ch
            ops += 1
            
print(ops)