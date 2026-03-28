'''
def count_el(iterable):
    # body
    
return - send value back to the caller(function)

'''

'''
type function
1. positonal ar
2. keyword ar
3. defualt ar
4. arbitary ar
A. positonal arbitary ar -> return tuple
B. keyword arbitary ar
sy :
def fname(**kwargs):
    
    
    
return dictionary
'''

# create a function to calculate mean of all numbers

# def cal_mean(*args):
#     sun = 0
#     for num in args:
#         sum = sum + num
#     return sum
# print(cal_mean(12,23,43,5,46,67))


# # avg of all number
# def mean(*numbers):
#     sum = 0
#     for num in numbers:
#         sum = sum + num
#     total_no= len(numbers)
#     avg = sum / total_no
#     return avg
# print(mean(12,12,23,67,99))

'''
A lambda function in Python is a small, anonymous function defined using the lambda 
keyword that can take any number of arguments but is limited to a single expression. 
The expression's result is implicitly returned, without the need for a return keyword. 


(parameter) kwargs: dict[str, Any]

(function) def detail(**kwargs: Any) -> None
'''

# def detail(**kwargs):
#     print(kwargs)
# print(detail(name = 'ram',course = 'data science',age = 22, city = 'pandharpur'))


# def total_sales(**courses):
#     total = 0
#     for sales in courses.values():
#         total = total + sales
#     return total
# print(total_sales(java= 10000, python=40000,aws = 500000))

'''
lambda function - >

single line function which is used to perform single opreation and which is created by sing lambda functio 

single line function  

without name

take any(multiple ) arg but give only one 

define using lambda keyword
sys ->
lambda parameter : expression



 '''

# add_ten = lambda x: x + 10
# print(add_ten(5)) 

# print((lambda num : num **2) (7))


# print((lambda n1,n2 : n1+n2) (20,30))

# create a function is eve or not

# print((lambda num : num%2==0) (12))

# calci = lambda n1, n2 : (n1+n2,n1-n2,n1*n2)
# print(calci(10,3))
# sum,sub,mul=(calci)

# create function to calculate simple interest and total amount and simple interest

# simp_int = lambda p, r, t : (p (*r/100)*t, p (*r/100)*t + p)
# print(simp_int(10000,5,2))
# total , rate = simp_int(10000,5,2) 
# print(total)
# print(rate)


# create a lamda function reurn selling price and discount price

# selling price
# cal = lambda amt , dic : (amt -(amt * dic / 100))
# amt, dic= cal(100000,10)
# print('sell price', amt)



'''
used in higher order function -> 

def f2(fuun):
    pass
    
    if function return a function calle higher order function
    
    
    
1. filter() -> class ->

filter(fuun, iterable)

filter the iterable element based on the condition

ex
num =[10,-20,-20,-30,-40,60,70] 
def ispositive(num):
    if num >0:
        return True
    else:
        return False
filter(fun,num)



use filter to find positive
return filter object

------------------------

class filter(
    function: None,
    iterable: Iterable[Any | None],
    /
): ...

class filter(
    function: (_S@__new__) -> TypeGuard,
    iterable: Iterable[_S@__new__],
    /
): ...

class filter(
    function: (_S@__new__) -> TypeIs,
    iterable: Iterable[_S@__new__],
    /
): ...

class filter(
    function: (Any) -> Any,
    iterable: Iterable,
    /
): ...

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true.

178 x 14


'''

# number = [10,20,33,40,56,70,30,33,44,66]
# def ispositive(num):
#     if num%2==0:
#         return True
#     else:
#         return False
    
# print(list(filter(ispositive, number)))


# number = [10,20,33,40,56,70,30,33,44,66]
# print(list(filter(lambda num : num%2==0,number)))


# student = ['kunal','raul','karan','vijay','varun','kiran','krushna','sujay','ajay']
# print(list(filter(lambda stud : stud.startswith('k'), student)))

# print(list(filter(lambda stud : stud.endswith('jay'), student)))

# # print(list(filter(lambda )))


# print(list(filter(lambda stud : stud[0]=='k', student)))


# student = {'kunal':90,'rahul':20,'karan':89,'vijay':69,'varun':79,'kiran':90,'krushna':50,'sujay':10,'ajay':70}

# # print(list(filter(lambda name : student[name] >= 40, student)))



# print(tuple(filter(lambda name : student[name] >= 40, student)))


# print(set(filter(lambda name : student[name] >= 40, student)))


# print(dict(filter(lambda t : t[1] >= 40, student.items())))



'''
map() -> 


'''

# number = [10,20,30,40,50,60,70]
# print(list(map( lambda num : num/2, number)))


# student = ['kunal kale','varun sharam', 'ram kale', 'sham mane']
# print(list(map(lambda name : name.title(), student)))


# print(tuple(map(lambda name : name.title(), student)))


# product = {'laptop': 60000, 'mobile':30000, 'fan':20000, 'TV':40000}
# print(dict(map(lambda pname : (pname, product[pname]-1000) ,product)))
# # price 


'''
reduce() ->

'''


number = [1,2,3,4,5]
from functools import reduce
print(reduce(lambda sum,num : sum + num, number,0))



student = ['kunal','vrun','kale']
# print(reduce(lambda fname,nm : fname + ' 'num, student, ' '))



employee = {'ram':40000, 'sham':20000,'varun':90000,'sham':54000,'kunal':45000,'rahul':30000,'karan':89000,'vijay':69000,'kiran':90,'siya':35000}

# print(list(map(lambda )))


#  10% salry and print list use map

#  40 to 60k print dict use filter

# total salary (additon of all) reduce