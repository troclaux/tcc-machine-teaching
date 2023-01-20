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
	#os.system('> output_input.txt')
	open("output_input.txt", "w")

	pwd_list = sorted(os.listdir())
	
	test_str = "test_input_" + problem_id + ".py"
	values = []
	for i, solution_filename in enumerate(tqdm(pwd_list)):

		if 'solution_' not in solution_filename:	
			continue
		
		# extract solution id
		solution_id = solution_filename[9:-3]

		import_str = "solution_" + solution_id
		log_file = "log_" + solution_id + ".json"
		cmd = f"pytest {test_str} --tb=line --solution {import_str} --report-log=log.json --timeout=2"
		#cmd = f"pytest test_input_736.py --tb=line --solution solution_50911 --report-log=log.json --timeout=2"
		#os.system(cmd + " >> output_input.txt")
		#os.system(cmd)
		#subprocess.check_output(cmd, shell=True)
		subprocess.call(cmd)

		#f = open("log.json")
		#json_data = json.load(f)

		log = open("log.json", "r")
		lines = log.readlines()

		test_cases = int((len(lines) - 4)/3)
		result = ""
		new_outcome = 1
		for test in range(test_cases):
			if "passed" in lines[4 + 3 * (test)]:
				result = result + "P"
				continue
			elif "AssertionError" in lines[4 + 3 * (test)]:
				result = result + "F"
				new_outcome = 0
				continue
			result = result + "E"
			new_outcome = 0

		values.append((new_outcome, result, solution_id))

	insert_solution = "INSERT INTO solution (new_outcome, result) VALUES(%s ,%s) WHERE solution_id=%s"
	cursor.executemany(insert_solution, values)


	os.chdir('..')
