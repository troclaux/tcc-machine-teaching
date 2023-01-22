import os
import sys
import subprocess
import json
from tqdm import tqdm
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

for problem_id in sys.argv[1:]:

	os.chdir('problems')
	os.chdir(problem_id)
	open("output_input.txt", "w")

	pwd_list = sorted(os.listdir())
	
	test_str = "test_input_" + problem_id + ".py"
	values_solution = []
	values_test = []

	for i, solution_filename in enumerate(tqdm(pwd_list)):

		if 'solution_' not in solution_filename:	
			continue
		
		# extract solution id
		solution_id = solution_filename[9:-3]

		import_str = "solution_" + solution_id
		cmd = f"pytest {test_str} --tb=line --solution {import_str} --report-log=log.json --timeout=2"
		subprocess.call(cmd)

		log = open("log.json", "r")
		lines = log.readlines()

		test_cases = int((len(lines) - 4)/3)
		if 'test_metrics' not in locals():
			test_metrics = [0]*(test_cases*3)

		result = ""
		new_outcome = 1
		for test_id in range(test_cases):
			temp = 4 + 3 * (test_id)
			print(lines[temp])
			if "passed" in lines[4 + 3 * (test_id)]:
				result = result + "P"
				test_metrics[test_id*3] = test_metrics[(test_id*3)] + 1
				continue
			elif "AssertionError" in lines[4 + 3 * (test_id)]:
				result = result + "F"
				test_metrics[(test_id*3)+1] = test_metrics[(test_id*3)+1] + 1
				new_outcome = 0
				continue
			result = result + "E"
			test_metrics[(test_id*3)+2] = test_metrics[(test_id*3)+2] + 1
			new_outcome = 0

			values_solution.append((new_outcome, result, solution_id))

		if "solution_50921" in solution_filename:
			break
			
	for test_id in range(test_cases):
		if "input" in os.path.basename(__file__):
			criteria = "input"
		elif "graph" in os.path.basename(__file__):
			criteria = "graph"
		else:
			criteria = "mutation"

		insert_test = f"INSERT INTO test ({test_id},{problem_id},{criteria},{test_metrics[test_id*3]},{test_metrics[(test_id*3)+1]},{test_metrics[(test_id*3)+2]})"
		cursor.execute(insert_test)

	insert_solution = "INSERT INTO solution (new_outcome, result) VALUES(%s ,%s) WHERE solution_id=%s"
	cursor.executemany(insert_solution, values_solution)

