# task 1

emp_name = input("Enter employee name: ")
basic_salary = float(input("Enter basic salary: "))
# Calculations
HRA = basic_salary * 20 / 100
DA = basic_salary * 50 / 100
gross_salary = basic_salary + HRA + DA
tax_deduction = gross_salary * 10 / 100
net_salary = gross_salary - tax_deduction

# Output
print(f"""
      Employee Name : {emp_name}
      Basic Salary  : {basic_salary}
      HRA (20%)     : {HRA}
      DA (50%)      : {DA}
      Gross Salary  : {gross_salary}
      Tax Deduction : {tax_deduction}
      Net Salary    : {net_salary}
""")



second task
from datetime import date
class Saving_Account:

    # class attributes
    bank_name = "BOI"
    IFSC_code = "BOI101"
    branch = "Karve Nagar"

    def __init__(self, nm, ac, bl):

        # instance attributes
        self.name = nm
        self.account_no = ac
        self.balance = bl
        self.transaction = {}

    def check_balance(self):
        print(f"Current Balance : {self.balance}")

    def deposit(self, amount):

        if isinstance(amount, (int, float)):

            if amount > 0:

                self.balance = self.balance + amount

                self.add_transaction("Deposit", amount)

                print(f"Deposit Successful! Balance : {self.balance}")

            else:
                print("Enter positive amount")

        else:
            print("Enter only numeric value")

    def withdraw(self, amount):

        if isinstance(amount, (int, float)):

            if amount > 0:

                if amount <= self.balance:

                    self.balance = self.balance - amount

                    self.add_transaction("Withdraw", amount)

                    print(f"Withdrawal Successful! Balance : {self.balance}")

                else:
                    print("Insufficient Balance")

            else:
                print("Enter positive value")

        else:
            print("Enter only numeric value")

    # add transaction
    def add_transaction(self, type, amount):

        tid = len(self.transaction) + 101

        dt = str(date.today())

        self.transaction[tid] = {
            "date": dt,
            "type": type,
            "amount": amount,
            "balance": self.balance
        }

    # show transaction history
    def show_transaction(self):

        print("-" * 105)

        print(f'{"ID":^20} {"Date":^20} {"Type":^20} {"Amount":^20} {"Balance":^20}')

        print("-" * 105)

        for tid in self.transaction:

            print(
                f'|{tid:^20}|'
                f'{self.transaction[tid]["date"]:^20}|'
                f'{self.transaction[tid]["type"]:^20}|'
                f'{self.transaction[tid]["amount"]:^20}|'
                f'{self.transaction[tid]["balance"]:^20}|'
            )

            print("-" * 105)



ram = Saving_Account("aditi Patil", 123456789011234, 20000)

ram.deposit(5000)

ram.withdraw(2000)

ram.check_balance()

ram.show_transaction()


# third task
# Task 3 : String Compression Algorithm
string = input("Enter a string : ")
compressed = ""
count = 1
for i in range(len(string)):

    if i < len(string) - 1 and string[i] == string[i + 1]:
        count += 1
    else:
        compressed = compressed + string[i] + str(count)
        count = 1
if len(compressed) < len(string):
    print("Compressed String :", compressed)
else:
    print("Original String :", string)