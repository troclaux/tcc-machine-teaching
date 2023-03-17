import mysql.connector

problem_ids = [736, 742, 744, 751, 798, 800, 804, 806, 807, 809, 810, 811, 812, 815, 816, 817, 819, 820, 821, 822, 823, 824, 827, 828, 829, 831, 832, 833, 834, 835, 836, 838, 839, 840, 842]

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
for problem_id in problem_ids:
    cursor.execute(f"DROP TABLE IF EXISTS Solution_{problem_id}")
cursor.execute("DROP TABLE IF EXISTS Solution")
cursor.execute("DROP TABLE IF EXISTS Test")

# Create the "Test" table
try:
  create_table_query = "CREATE TABLE Test ( test_id INTEGER, problem_id INTEGER, criteria_type VARCHAR(255), pass_count INTEGER, fail_count INTEGER, error_count INTEGER)"
  cursor.execute(create_table_query)
except:
  print("Test exists")

# Create the "Solution" table
for problem_id in problem_ids:
  try:
    create_table_query = f"CREATE TABLE Solution_{problem_id} (solution_id INTEGER PRIMARY KEY, problem_id INTEGER, old_outcome BOOLEAN, input_outcome BOOLEAN, graph_outcome BOOLEAN, mutation_outcome BOOLEAN, input_result VARCHAR(255), graph_result VARCHAR(255), mutation_result VARCHAR(255))"
    cursor.execute(create_table_query)
  except:
    print(f"Solution_{problem_id} exists")

# FOREIGN KEY (test_id) REFERENCES Test(id)

# Commit the changes to the database
cnx.commit()

# Close the cursor and connection
cursor.close()
cnx.close()