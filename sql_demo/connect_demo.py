import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="Sanal@1010")

print(mydb)

if mydb:
    print("Connection Successful")
else:
    print("Connection Unsuccessful")
# #
cursor = mydb.cursor()
# cursor.execute("drop database db_demo")
cursor.execute("create database db_demo123")
cursor.execute("show databases")
for db in cursor:
    print(db)