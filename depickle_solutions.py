import pickle
from tqdm import tqdm
import os
import mysql.connector
# Connect to the MySQL server
#cnx = mysql.connector.connect(user='root', password='RootSenha', host='127.0.0.1', database='tcc_machine_teaching')
cnx = mysql.connector.connect(user='root', password='RootSenha', host='127.0.0.1')
cnx.autocommit = True

# Create a cursor to execute SQL statements
cursor = cnx.cursor(buffered=True)

# Try create database
try:
  cursor.execute("CREATE DATABASE tcc_machine_teaching")
except:
  print("db exists")

# Connect to the MySQL Database
cursor.execute("USE tcc_machine_teaching")


def create_import_stmts():
    path = os.path.join(directory, "problems")
    for problem in sorted(os.listdir(path)):
        path_problem = os.path.join(path, problem)
        path_stmts = os.path.join(path_problem, "import_stmts.py")
        open(f"{path_stmts}", "w")

with open('solutions.pkl', 'rb') as f:
    data = pickle.load(f)
    directory = os.getcwd()

    create_import_stmts()

    cursor.execute("TRUNCATE TABLE solution")
    cursor.execute("TRUNCATE TABLE test")
    values = []
    for i, enunciado in enumerate(tqdm(data)):
        problem_id = str(enunciado["problem_id"])
        solution_id = "solution_" + str(i)
        if enunciado["outcome"] == "P":
            solution_outcome = 1
        else:
            solution_outcome = 0
        solution_id_path = "solution_" + str(i) + ".py"
        path = os.path.join(directory, "problems")
        path = os.path.join(path, problem_id)
        path_id = os.path.join(path, solution_id_path)
        path_stmts = os.path.join(path, "import_stmts.py")

        if not os.path.exists(path):
            os.makedirs(path)

        values.append((enunciado["problem_id"],solution_outcome))

        with open(path_id, 'w', encoding="utf-8") as g:
            g.write(enunciado["solution"])


        with open(path_stmts, 'a', encoding="utf-8") as h:
            h.write(f"try:\n\timport {solution_id} \nexcept:\n\tprint('{solution_id} IMPORT ERROR')\n")
        

    insert_solution = "INSERT INTO solution (problem_id, old_outcome) VALUES(%s ,%s)"
    cursor.executemany(insert_solution, values)



