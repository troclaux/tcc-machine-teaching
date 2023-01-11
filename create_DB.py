import mysql.connector

# Connect to the MySQL server
#cnx = mysql.connector.connect(user='root', password='RootSenha', host='127.0.0.1', database='tcc_machine_teaching')
cnx = mysql.connector.connect(user='root', password='RootSenha', host='127.0.0.1')

# Create a cursor to execute SQL statements
cursor = cnx.cursor()

# Try create database
try:
  cursor.execute("CREATE DATABASE tcc_machine_teaching")
except:
  print("db exists")

# Connect to the MySQL Database
cursor.execute("USE tcc_machine_teaching")

cursor.execute("DROP TABLE solution")
cursor.execute("DROP TABLE test")

# Create the "Test" table
try:
  create_table_query = "CREATE TABLE Test ( test_id INTEGER PRIMARY KEY AUTO_INCREMENT, problem_id INTEGER, criteria_type VARCHAR(255), pass_count INTEGER, fail_count INTEGER, error_count INTEGER)"
  cursor.execute(create_table_query)
except:
  print("Test exists")

# Create the "Solution" table
try:
  create_table_query = "CREATE TABLE Solution (solution_id INTEGER PRIMARY KEY AUTO_INCREMENT, problem_id INTEGER, old_outcome BOOLEAN, new_outcome BOOLEAN, result VARCHAR(255))"
  cursor.execute(create_table_query)
except:
  print("Solution exists")

# FOREIGN KEY (test_id) REFERENCES Test(id)

# Commit the changes to the database
cnx.commit()

# Close the cursor and connection
cursor.close()
cnx.close()