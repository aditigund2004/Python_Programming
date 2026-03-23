#string fomatting

mrp = 40000
dis = 10
dis_price = mrp * dis / 100
sel_price = mrp - dis_price
print("MRP :", mrp, "Discount :",dis, "Selling price :",sel_price)

print('mrp : %d discount : %d selling price : %d'%(mrp, dis, sel_price))
print('---------------------------------------------------------')

'''
place holder
synatx:
  'msg %d msg %d msg %d'(v1,v2,v3)
%d - integer

'''


#simple interest
#loan
principle_amount = 100000
#intererst or vyaj
rate_interest = 10

time = 1
simple_interest = principle_amount * (rate_interest / 100) * time
#total amount to return
total_amount = principle_amount + simple_interest

print(total_amount)
print(simple_interest)
print(principle_amount)

print('Total Amount to Return : %d \n Rate of Interest :%d \n Simple Interest : %d'%(total_amount, simple_interest, principle_amount))


n1 = 10.5
n2 = 4.6
sum = n1+ n2
print('sum of %0.2f \nand %0.3f is \n%0.1f'%(n1,n2,sum))


name = "aditi"
age = 22
city = "pandharpur"

print('My name is %s and i am %d years old and i am from %s'%(name, age, city))