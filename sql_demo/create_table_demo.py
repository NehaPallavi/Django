import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="Sanal@1010", database="db_demo")
print(mydb)

cursor = mydb.cursor()
# cursor.execute("drop table employee")
cursor.execute("create table employee(name varchar(200), sal int(20))")
cursor.execute("show tables")

for tb in cursor:
    print(tb)
