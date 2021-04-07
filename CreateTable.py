## importing 'mysql.connector' as mysql for convenient
import mysql.connector as mysql

mydb = mysql.connect(
  host="localhost",
  user="admin",
  password="admin",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE TRIP_DETAILS (tripId VARCHAR(255) PRIMARY KEY, owner_unique_Id VARCHAR(255), source VARCHAR(255), destination VARCHAR(255), route_taken VARCHAR(255), vehicle_number VARCHAR(255), created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)")
