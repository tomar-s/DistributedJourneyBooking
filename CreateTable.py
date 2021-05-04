## importing 'mysql.connector' as mysql for convenient
import mysql.connector as mysql
import Credentials as creds

mydb = mysql.connect(
  host=server["host"],
  user=server["user"],
  password=server["password"],
  database=server["database"]
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE TRIP_DETAILS (tripId VARCHAR(255) PRIMARY KEY, owner_unique_Id VARCHAR(255), source VARCHAR(255), destination VARCHAR(255), route_taken VARCHAR(255), vehicle_number VARCHAR(255), created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)")
mycursor.execute("CREATE TABLE ROUTE_DETAILS (routeId VARCHAR(255) PRIMARY KEY, source VARCHAR(255), destination VARCHAR(255))")
mycursor.execute("CREATE TABLE BOOKINGS_AVAIL(timeslot INT, route_id VARCHAR(255), count INT CHECK (count BETWEEN 1 and 49), date_requested DATE)")
mycursor.execute("CREATE TABLE USER_PROFILE(owner_unique_Id VARCHAR(255) PRIMARY KEY, user_token VARCHAR(255))")
