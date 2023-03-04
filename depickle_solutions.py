import pickle
import pandas as pd
from tqdm import tqdm
import os
import mysql.connector

problem_ids = [736, 742, 744, 751, 804, 806, 807, 809, 810, 811, 812, 815, 816, 817, 819, 820, 821, 822, 823, 824, 838, 839, 840, 842]
criteria = ["input", "graph", "mutation"]
# Connect to the MySQL server
#cnx = mysql.connector.connect(user='root', password='RootSenha', host='127.0.0.1', database='tcc_machine_teaching')
#cnx = mysql.connector.connect(user='root', password='RootSenha', host='127.0.0.1')
#cnx.autocommit = True

# Create a cursor to execute SQL statements
#cursor = cnx.cursor(buffered=True)

# Try create database
#try:
#  cursor.execute("CREATE DATABASE tcc_machine_teaching")
#except:
#  print("db exists")

# Connect to the MySQL Database
#cursor.execute("USE tcc_machine_teaching")

directory = os.getcwd()

def create_import_stmts():
    path = os.path.join(directory, "problems")
    for problem in sorted(os.listdir(path)):
        path_problem = os.path.join(path, problem)
        path_stmts = os.path.join(path_problem, "import_stmts.py")
        open(f"{path_stmts}", "w")

with open('solutions.pkl', 'rb') as f:
    data = pickle.load(f)

    create_import_stmts()
    #for problem_id in problem_ids:
    #    cursor.execute(f"TRUNCATE TABLE Solution_{problem_id}")
    #cursor.execute("TRUNCATE TABLE Test")
    values = []
    for i, enunciado in enumerate(tqdm(data)):
        problem_id = str(enunciado["problem_id"])
        solution_id = f"solution_{i+1}"
        if enunciado["outcome"] == "P":
            solution_outcome = 1
        else:
            solution_outcome = 0
        solution_id_path = f"solution_{i+1}.py"
        path = os.path.join(directory, "problems")
        path = os.path.join(path, problem_id)
        path_id = os.path.join(path, solution_id_path)
        path_stmts = os.path.join(path, "import_stmts.py")

        if not os.path.exists(path):
            os.makedirs(path)

        values.append((i+1,enunciado["problem_id"],solution_outcome))

        with open(path_id, 'w', encoding="utf-8") as g:
            g.write(enunciado["solution"])

        if i == 0:
            with open(path_stmts, 'w', encoding="utf-8") as h:
                h.write(f"try:\n\timport {solution_id} \nexcept:\n\tprint('{solution_id} IMPORT ERROR')\n")
                continue
        with open(path_stmts, 'a', encoding="utf-8") as h:
            h.write(f"try:\n\timport {solution_id} \nexcept:\n\tprint('{solution_id} IMPORT ERROR')\n")
        
    for i, problem_id in enumerate(tqdm(problem_ids)):
        values_temp = list(filter(lambda x: x[1] == problem_id, values))
        path_csv = os.path.join(directory, "CSV")
        path_csv =  os.path.join(path_csv, f"solution_{problem_id}.csv")
        df_solution = pd.read_csv(path_csv)
        df_solution = df_solution.iloc[0:0]
        df_value = pd.DataFrame(values_temp, columns=['solution_id','problem_id','old_outcome'])
        df_solution = pd.concat([df_solution, df_value], ignore_index=True)
        df_solution.to_csv(path_or_buf=path_csv, index=False)
        #insert_solution = f"INSERT INTO Solution_{problem_id} (solution_id, problem_id, old_outcome) VALUES(%s, %s, %s)"
        #cursor.executemany(insert_solution, values_temp)

    #insert_solution = "INSERT INTO solution (solution_id, problem_id, old_outcome) VALUES(%s, %s, %s)"
    #cursor.executemany(insert_solution, values)



