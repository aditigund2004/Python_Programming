import mysql.connector
con=mysql.connector.connect(host='localhost',password='root',user='root')
if con.is_connected():
    print("connected")
