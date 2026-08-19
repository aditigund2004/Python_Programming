# name = 'i am ram'
# for i in name:
#     print(i)


# str = "i am ram"
# for i in str:
#     if i != "":
#         print(i)



# s = "i am ram"
# print(*s.replace(" ", ""), sep="\n")




# arr = [10,203,40,5000]
# print(max(arr))


# arr = [10,203,40,5000]
# larget = arr[0]
# for i in arr:
#     if i > larget:
#        larget = i
# print(larget)
    


# array = [100,0, 10,203, 203, 40,5000]

# larget = array[0] #index from 0 
# second = array[0]#index from 0

# for i in array:  #go through each nu
#     if i > larget:
#         second = larget  #You move the old largest into second.
#         larget = i 
#     # elif i > larget and i != larget:
#     #     second = i
# # print(array.index(second))
# print(second)


# li1 = [2, 3, 4, 4]

# for i in li1:
#     if i % 2 == 0:
#         print(i * i, end=' ')



# prime -> divisible 1 or itself

num = int(input("Enter No:"))

count = 0
for i in range(1, num + 1):
    if num % i == 0:
        count += 1
    
if count == 2:
    print("prime")
else:
    print(" not prime")