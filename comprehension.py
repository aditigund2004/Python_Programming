'''
List comprehension ->
    List comprehension in Python provides a concise, single-line way to create a new 
    list by applying an expression to each item in an existing iterable, optionally filtering the items. 
    It is often more readable and efficient than a traditional for loop for simple list generation and transformation. 


set comprehension ->
dict comprehension ->


'''
# membership op -> in 

# WAP of squre of every elemnet
# s_list = []
l1 =[1,2,3,4,5,6]
# for i in l1:
#     s_list.append(i*i)
# print(s_list)


# squre = [i*i for i in l1]
# print(squre)



# squre of even number
# s_list = []
# l1 =[1,2,3,4,5,6]
# for i in l1:
#     if i%2 == 0:
#        s_list.append(i*i)
# print(s_list)


# even = [i*i for i in l1 if i%2 ==0]
# print(even)


# even odd

# e_list = []
# for i in l1:
#     if  i%2==0:
#         e_list.append("even")
       
#     else:
#         print("odd")
# print(e_list)

# even = ["even" if i%2 ==0 else "odd" for i in l1]
# print(even)

'''
list comp
loop
v_name = [expression for_loop]


if condition and for loop
v_name = [expression for_loop if condition]

if else conditon for loop
v_name =[espression loo if conditon else condition els_expression for_loop]

'''



# dic comp
# l2 =[1,2,3,4,5,6]

# dict1 = {i : i*i for i in l2}
# print(dict1)

l2 =[1,2,3,4,5,6]

# dict1 = {i : i*i for i in l2 if i % 2== 0}
# print(dict1)



lambda_square = [lambda i : i*i , l2]
print(lambda_square(l2))