# pip install mysql-connector
# pip install mysql-connector-python
# pip install PyMySQL

# pip list -- show all packages

import mysql.connector

# conn = mysql.connector.connect(
#                 host = "localhost",
#                 user = "root",
#                 port = 3306,
#                 password = "root", # write your own password
#                 database = "1311db"  # optional
#                 )

# print("connection Sucessfully")

import pymysql

conn1 = pymysql.connect(
                host = "localhost",
                user = "root",
                port = 3306,
                password = "root", # write your own password
                database = "1311db"  # optional
)

print("connection Sucessfully")

cu = conn1.cursor()

sdb = "use 1311db"

cu.execute(sdb)

print("use database 1311db ")

create_table = """
                create table if not exists product_info(
                            pid int primary key,
                            pname varchar(250) not null,
                            price int not null
                    )
                """
cu.execute(create_table)

# pymysql.err.OperationalError: (1050, "Table 'product_info' already exists")

print("table create successfully")

describe_table = "desc product_info"

cu.execute(describe_table)

# for col in cu.fetchall():
#     print(col)

insert_data = """
                    insert into product_info (pid, pname, price)
                    values
                    (%s,%s,%s)
              """
data = [(1,"Python book",300),
        (2,"Django book",400),
        (3,"HTML & CSS book",500),
        (4,"MySQL book",650)
        ]
# cu.executemany(insert_data, data)

# TCL --Transcation control Language
    # Commit 
    # Rollback

# conn1.commit()

# print("data insert Sucessfully")

show_data = "select * from product_info "

cu.execute(show_data)

# print(cu.fetchall())

# for t_rows in cu.fetchall():
#     print(t_rows)

# print(cu.fetchone())
# print(cu.fetchone())

# print(cu.fetchmany(2))





cu.close()
conn1.close()
