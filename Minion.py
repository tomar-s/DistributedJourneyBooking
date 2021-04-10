'''
This script -
checks no. of rows in a window of time for the combination of source, destination, route_taken
'''
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="toor",
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


def main():
    print(get_route_list("Dublin", "Galway"))

if __name__ == "__main__":
    main()
