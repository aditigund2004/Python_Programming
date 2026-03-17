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



# def main():
#     s = input()
#     a = int(input())
#     m = {
#         "mon": 60, "tue": 5, "web":4,
#         "thus":3, "fri":2, "sat":1, "sun":0
#     }
#     ans = 0
#     if a - m[s[:3]] >= 1:
#         ans = 1 + (a - m[s[:3]])
#     print(ans)
    
# if __name__ == "__main__":
#     main()



def getmax(money, price, volume, n):
    K = []
    for i in range(n = 1):
        temp = []
        for j in range(money + 1):
            temp.append(0)
            K.append(temp)
        for i in range(n + 1):
            for m in range(money + 1):
                if i == 0 or m ==0:
                    K[i][m]=0
                elif price[i - 1] <= m:
                    K[i][m] = max(volume [ i - 1] + K[i - 1][m  -price [ i -1]], K[i - 1][m])
                else:
                    K[i][m] = K[i - 1][m]
    return K[n][money]

N, money = map(int, input().split())
price = list(map(int, input().split()))
volume = list(map(int, input().split()))
print(getmax(money, price, volume, len(volume)))