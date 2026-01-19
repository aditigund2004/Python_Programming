# pratice set 1 
# customer_name = input("Enetr customer name :")
# number_tickets = eval(input("Enter number of tickets :"))

# cost_per_ticket = 250
# total_cost = number_tickets * cost_per_ticket

# print(f'''
#       Customer name : {customer_name}
#       Number os tickets : {number_tickets}
#       cost of per ticket : {cost_per_ticket} 
#       ticket price is : {total_cost}
#       ''')




# pratice set 2
emp_name = input("Enter name :")
current_salary = eval(input("Enter current salary :"))

HRA = current_salary * 20/100
DA = current_salary * 10/100

gross_salary = current_salary + HRA + DA 
tax = current_salary * 8/100
net_salary = gross_salary - tax
print(f'''
      Employee name :{emp_name}
      basic salary is : {current_salary}
      HRA is : {HRA}
      DA :{DA}
      gross salary : {gross_salary}
      net salary : {net_salary}
      ''' )




# practice set 3
# owwner_name = input("Enter Owner name :")
# length = eval(input("Enter wall length :"))
# width = eval(input("Enter wall width :"))

# area = length * width
# painting_cost = 15
# total_cost = area * painting_cost

# print(f'''
#       Owner name : {owwner_name}
#       length : {length}
#       Width : {width}
#       Area : {area}
#       painting cost per sq unit is :{painting_cost}
#       the total cost is :{total_cost} 
      
#       ''')


# practice set 4
# customer_name = input("Enter name :")
# recharge_amt = eval(input("Recharge amount:"))
# GST = 18
# final = recharge_amt * 18 / 100
# final_bill = final + recharge_amt

# print(f'''
#       Customer name : {customer_name}
#       the recharge amount is: {recharge_amt} 
#       the gst is :{final} 
#       final bill is :{final_bill} ''')


# practice set 5
# customer_name = input("Enter name :")
# food_item_price = eval(input("Enter food price: "))
# deliver_charge = 40
# GST = 5
# total_bill = food_item_price * 5 / 100
# total =  food_item_price + total_bill + deliver_charge 
# print(f'''
#       customer name: {customer_name} 
#       food price :{food_item_price} 
#       deliver charge :{deliver_charge} 
#       GST is {GST} : {total_bill} 
#       total bill is :{total}
#       ''')



# practice set 6
sender_name = input("Senders name :")
weigth = eval(input("Enter weigth :"))
charge_per_kg = 40
total_charge = weigth * charge_per_kg
print(f'''
      senders name : {sender_name}
      weigth is :{weigth}
      charger per kg is :{charge_per_kg}
      total charge is: {total_charge }
      ''')
 