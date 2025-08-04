import mysql.connector
from connection import mydb

c = mydb.cursor()

c.execute("CREATE DATABASE IF NOT EXISTS employee_db")

c.execute("USE employee_db")

 
employeetbl_create = """
CREATE TABLE tblemployee (
    empid INT NOT NULL AUTO_INCREMENT,
    empname VARCHAR(45),
    department VARCHAR(45),
    salary INT,
    PRIMARY KEY (empid)
)
"""
c.execute(employeetbl_create)

'''c.execute("DESC tblemployee")
for i in c.fetchall():
    print(i)'''

employeetbl_insert = """
INSERT INTO tblemployee (empname, department, salary)
VALUES (%s, %s, %s)
"""
data = [
    ("Vani", "HR", 100000),
    ("Krish", "Accounts", 60000),
    ("Aishwarya", "Sales", 25000),
    ("Govind", "Marketing", 40000)
]
c.executemany(employeetbl_insert, data)
mydb.commit()

c.execute("SELECT * FROM tblemployee")
for e in c.fetchall():
    print(e)

employeetbl_update = """
UPDATE tblemployee
SET salary = 115000
WHERE empid = 1
"""
c.execute(employeetbl_update)
mydb.commit()

c.execute("SELECT * FROM tblemployee WHERE empid = 1")
print("After update: ", c.fetchone())

c.close()
mydb.close()
