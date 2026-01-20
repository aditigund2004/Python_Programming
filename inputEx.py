
'''
{place holder}.format(variable name)
'''

# name = input("Enter your name:")
# age = int(input("Enter your age:"))
# city = input("Enter city name")
# print('my name is: %s my age is: %d i am from: %s'%(name, age, city))
# print('my age is:',age)
# print('my name is {} i am {} year old and i am from {}'.format(name, age, city))


product_name = input('Enter product name:')
product_id = (input('Enetr product id:'))
price = (input('Enter product price:'))
product_qty = (input('Enter product qty:'))
# date_of_production = int(input('Production date:'))
print('Product name: {}\n product id: {}\n price: {}\n product qty:{}'.format(product_name, product_id, price,product_qty))
print('-'*36)

print('Product name: {2}\n product id: {1}\n price:\n {0} product qty:{3}'.format(product_name, product_id, price,product_qty))
print('-'*36)

print('Product name: {pn}\n product id: {pi}\n price:{p}\n  product qty:{pq}'.format(pn=product_name, pi=product_id, p=price,pq=product_qty))
print('-'*36)

print(f'product name:{product_name} \n produt id: {product_id}\n price:{price} \n product qty:{product_qty}')
print('-'*36)


emp_id = int(input('enter employee id:'))
emp_name = input('Enter employee name:')
emp_add = input('Enetr address:')
emp_mobile = int(input('Enter employee no:'))
emp_salary = float(input('Enter salary:'))
print(f'employee id:{emp_id} \n employee name: {emp_name}\n employee address:{emp_add} \n employee mobile no:{emp_mobile}\n employee salary {emp_salary}')
print('-'*100)

col1 = 'Roll'
col2 = 'Name'
col3 = 'Percentage'
print('-'*36)
print('|{:^10}|{:^10}|{:^10}|'.format(col1,col2,col3))
print('-'*36)

