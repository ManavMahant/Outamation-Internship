import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Manav@026",
  database="studentdb"
)
my_cursor = mydb.cursor()
print("Connection Succesfull.")
