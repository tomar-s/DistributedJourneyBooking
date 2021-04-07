## importing 'mysql.connector' as mysql for convenient
import mysql.connector as mysql

mydb = mysql.connect(
  host="localhost",
  user="admin",
  password="admin",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("DROP TABLE TRIP_DETAILS")
