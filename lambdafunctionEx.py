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

def cal_mean(*args):
    sun = 0
    for num in args:
        sum = sum + num
    return sum
print(cal_mean(12,23,43,5,46,67))


# avg of all number
def mean(*numbers):
    sum = 0
    for num in numbers:
        sum = sum + num
    total_no= len(numbers)
    avg = sum / total_no
    return avg
print(mean(12,12,23,67,99))

'''
A lambda function in Python is a small, anonymous function defined using the lambda 
keyword that can take any number of arguments but is limited to a single expression. 
The expression's result is implicitly returned, without the need for a return keyword. 


(parameter) kwargs: dict[str, Any]

(function) def detail(**kwargs: Any) -> None
'''

def detail(**kwargs):
    print(kwargs)
print(detail(name = 'ram',course = 'data science',age = 22, city = 'pandharpur'))


def total_sales(**courses):
    total = 0
    for sales in courses.values():
        total = total + sales
    return total
print(total_sales(java= 10000, python=40000,aws = 500000))

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

add_ten = lambda x: x + 10
print(add_ten(5)) 

print((lambda num : num **2) (7))


print((lambda n1,n2 : n1+n2) (20,30))

# create a function is eve or not

print((lambda num : num%2==0) (12))

calci = lambda n1, n2 : (n1+n2,n1-n2,n1*n2)
print(calci(10,3))
sum,sub,mul=(calci)

# create function to calculate simple interest and total amount and simple interest

simp_int = lambda p, r, t : (p (*r/100)*t, p (*r/100)*t + p)
print(simp_int(10000,5,2))
total , rate = simp_int(10000,5,2) 
print(total)
print(rate)


# create a lamda function reurn selling price and discount price

# selling price
cal = lambda amt , dic : (amt -(amt * dic / 100))
amt, dic= cal(100000,10)
print('sell price', amt)