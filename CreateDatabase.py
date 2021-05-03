## importing 'mysql.connector' as mysql for convenient
import mysql.connector as mysql

## connecting to the database using 'connect()' method
## it takes 3 required parameters 'host', 'user', 'passwd'
db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "example",
)

# Allow root user loging from anywhere
# UPDATE mysql.user SET host='%' WHERE user='root';

print(db) # it will print a connection object if everything is fine

# create database
mycursor = db.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS mydatabase")

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)
