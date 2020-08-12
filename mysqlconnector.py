import mysql.connector

# Create the connection object
myconn = mysql.connector.connect(host="localhost", user="root", passwd="google")

# creating the cursor object
cur = myconn.cursor()

try:
    dbs = cur.execute("show databases")
except:
    myconn.rollback()
for x in cur:
    print(x)
myconn.close()