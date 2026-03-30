
'''

parameter and argument
parameter -> varible which define within paranthesis at aa time of function defination and take input from user at time of function calling

argument - >actual value pass to function at function calling


def f_name(p1,p2): -> parameter
    # block
    
f_name(v1,v2) -> argumenet

'''

def sum(n1,n2):
    num=n1+n2
    print(num)
    
sum(10,20)


def max_num(n1,n2):
    if n1>n2:
        print(n1)
    else:
        print(n2)
        
max_num(23,34)


# create fun to calculate simple interest

def simple_interest(principle_amt,rate,time):
    # principle_amt = eval(input("Enter priciple amt :"))
    # rate_interest = 10
    si = principle_amt*(rate/100)*time
    print(si)
    
simple_interest(10000,10,2)


# create a function to count number of character present in string

def count_str():
    str = 'ram'
    count = 0
    for char in str:
        count = count+1
    print(count)
    
count_str()


def count_str(str):
    str = 'ram'
    count = 0
    for char in str:
        count = count+1
    return count
print(count_str(str))
    


def count_str(str):
    
    count = 0
    for char in str:
        count = count+1
    print(count)
    
count_str("ram")



'''
type of parameter and argument

positional argument - > need to maintain the positon of argument in function defination

syntax:
def fname(p1,p2,p3): -> sequence of parameter
    pass
    
fname(v1,v2,v3) -> sequence of arguement 
fname(v3,v1,v2)

number of paramert reqired number of argument
'''

def full_name(f_name,m_name,l_name):
    full = f'{f_name} {m_name} {l_name}'
    print(full)



'''
keyword argument ->

value pass to function with parameter name

syntax:
def fname(p1,p2,p3): 
    pass
    
fname(p1=v1,p2=v2,p3=v3) 
fname(p1=v1,p2=v2,p3=v3) 

'''



# with both type
def full_name(f_name,m_name,l_name):
    full = f'{f_name} {m_name} {l_name}'
    print(full)



# positional arg.
full_name('ram','sham','suryvanshi')

# keyword arg.
full_name(f_name='ram',m_name='sham',l_name='suryvanshi')



'''
defaul argument ->
parameter with defual value


'''


def detail(nm,c,ins='The Kiran Academy'):
    data = f'''
    name :{nm}
    course :{c}
    institute : {ins}
    '''
    print(data)
    
detail('anu mane','data sicence')



'''

Parameter: Variable in function definition

Argument: Value passed to function


Parameter is a variable in function definition. Argument is the actual value passed to the function.
'''
# create a function to calculate to count number of repeated character


def str_count(str,char):
    count = 0
    for i in str:
        if i==char:
            count = count+1
    print(count)
str_count('anuradha','a')
        
        
        
    
    
   
def sen_word(sen, word): 
    count = 0
    word = sen.split()
    for i in word:
        if word==i:
            count =count +1 
    print(count)
sen_word('python is simple python is high level python is dynamiic','pyton')  
   
    

