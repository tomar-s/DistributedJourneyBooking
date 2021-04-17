'''
This script -
checks no. of rows in a window of time for the combination of source, destination, route_taken
'''
import mysql.connector
import uuid

mydb = mysql.connector.connect(
  host="localhost",
  user="admin",
  password="admin",
  database="mydatabase"
)

mycursor = mydb.cursor()

def get_route_list(s, d):
  query = "select routeId from route_details where source LIKE '{}' and destination LIKE '{}'".format(s, d)
  mycursor.execute(query)
  number_of_rows = 0
  route_list = []
  for x in mycursor:
    for _x in x:
      route_list.append(_x)
      break
    number_of_rows = number_of_rows + 1
  print(number_of_rows, "routes found.")
  return route_list

def update_route_info(timeslot, route_id, date_requested):
  query = "select count from bookings_avail where timeslot = {} and route_id LIKE '{}' and date_requested LIKE '{}'".format(timeslot,route_id,date_requested)
  mycursor.execute(query)
  print(query)
  count = None
  route_avail = False
  for x in mycursor:
    for _x in x:
      count = _x

  if count and count < 600:
    route_avail = True
    query = "update bookings_avail set count = count + 1 where timeslot = {} and route_id = '{}' and date_requested = '{}'".format(timeslot,route_id,date_requested)
    mycursor.execute(query)
    mydb.commit()
  
  if not count:
    route_avail = True
    query = "INSERT INTO bookings_avail (timeslot,route_id,count,date_requested) VALUES (%s, %s,%s,%s)"
    val = (timeslot, route_id, 1, date_requested)
    mycursor.execute(query,val)
    mydb.commit()
    
  if route_avail:
    passIssue = str(uuid.uuid4())
  else:
    passIssue = "Route not available"

  return passIssue

def main():
  print(get_route_list("Dublin", "Galway"))

if __name__ == "__main__":
    main()
