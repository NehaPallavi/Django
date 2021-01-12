import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="Sanal@1010", database="db_demo")
print(mydb)

cursor = mydb.cursor()
insert_query = "Insert into employee(name, sal) values (%s, %s)"
data = [("Manoj", 10000), ("Kavitha", 40000), ("Rakesh", 60000)]
cursor.executemany(insert_query, data)
mydb.commit()

cursor.execute("Select * from employee")

for name, sal in cursor:
    print(name, sal, sep="-->")
