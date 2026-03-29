# squre
def squre():
    number = int(input("Enter number :"))
    sq = number**2
    print(sq)

print("continue...")




# positive
def positive():
    num = int(input("Enter number to check the number :"))
    if num > 0 :
        print("positive",num)
    else:
        print("negative",num)


# divisible number
def divisible():
    number = eval(input("Enetr number to check number is divisible or not:"))
    if (number%3==0 and number%5==0):
        print("divisible by 3 and 5 ")
    elif (number%5==0):
        print("divisible by 5 ")
    elif (number%3==0 ):
        print("divisible by 3 ")
        
    else:
        print("not divisible by 3 and 5")

