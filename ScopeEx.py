'''
scope ->
Global scope - >
variable which is defined within (inside) function called globle scope or globle variable
outside of the function is called as global scope
can't updated global variable within function

example:
x = 10
def fun():
    # body
    # code

local scope ->
varivle inside function called local scope varible
varivle which is defined outside function local scope called globle variable

example:
def fun():
    x = 10
    # body
    # code
'''

# student = {}
# count = 0

# def registration(nm,course):
#     student[nm]=course
#     print("register.")
#     global count
#     count = count +1

# registration('anuradha mane','Data Analytics')
# print(count)




'''
return is a keyword in python which send value back to the caller

return function return value outside function and terminate tye execution

'''

# def add(n1,n2):
#     sum=n1+n2
#     return sum


# print(add(10,20))


# result = add(3,4)
# print(result**2)



# def full_name(f_name,m_name,l_name):
#     full = f'{f_name} {m_name} {l_name}'
    
#     print("start..")
#     return full
#     print("stop..")

# full_name('anuradha','vishnu','name')
# print(full_name)


# def calci(n1,n2):
#     add=n1+n2
#     sub=n1-n2
#     mul=n1*n2
#     div=n1/n2
    
#     return add,sub,mul,div
# print(calci(10,5))

# var = calci(10,5)
# print(var)


# a,s,m,d =calci(10,5)
# print(a)
# print(s)


# def simple_inter(p,r,t):
#     return(p*r*t)/100
# print(simple_inter(10000,2,10))
    
    

# def iseven_odd(num):
    
#     if num%2 ==0:
#         print("even") 
#     else:
#         print("odd")   
# num = eval(input("ENter number"))
# iseven_odd(num)



def issqure(num):
    sq = num**2
    print(sq)
num = eval(input("Entr number"))
issqure(num)

    