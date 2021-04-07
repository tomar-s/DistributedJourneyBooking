'''
This script -
checks no. of rows in a window of time for the combination of source, destination, route_taken
'''
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="admin",
  password="admin",
  database="mydatabase"
)

mycursor = mydb.cursor()
mycursor.execute("SET time_zone='+01:00'")
query = "INSERT INTO trip_details (tripId, owner_unique_Id, source, destination, route_taken, vehicle_number) VALUES (%s, %s,%s, %s,%s, %s)"
val = ("14", "RD", "Dublin", "Galway", "NH4", "AR4789")
mycursor.execute(query, val)

mydb.commit()

number_of_rows = 0
mycursor.execute("SELECT * FROM trip_details")

for x in mycursor:
  print(x)
  number_of_rows = number_of_rows + 1
print(number_of_rows, "record(s) inserted.")
