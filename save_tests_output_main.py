import os
import sys
import subprocess
from tqdm import tqdm
import mysql.connector
import importlib

def save_tests_output(criteria,problem_id):

	# Connect to the MySQL server
	#cnx = mysql.connector.connect(user='root', password='RootSenha', host='127.0.0.1', database='tcc_machine_teaching')
	cnx = mysql.connector.connect(user='root', password='RootSenha', host='127.0.0.1')
	#cnx.autocommit = True

	# Create a cursor to execute SQL statements
	cursor = cnx.cursor(buffered=True)

	# Try create database
	#try:
	#	cursor.execute("CREATE DATABASE tcc_machine_teaching")
	#except:
	#	print("db exists")

	# Connect to the MySQL Database
	cursor.execute("USE tcc_machine_teaching")

	directory = os.getcwd()
	path = os.path.join(directory, "problems")
	path = os.path.join(path, str(problem_id))

	pwd_list = sorted(os.listdir(path))
			
	test_str = f"test_{criteria}_{problem_id}.py"
	path_test = os.path.join(path, test_str)


	values_solution = []
	count = 0

	spec = importlib.util.spec_from_file_location(test_str, path_test)
	test = importlib.util.module_from_spec(spec)
	sys.modules["module.name"] = test
	spec.loader.exec_module(test)
	test_cases = len(test.test_cases)
	test_metrics = [0]*(test_cases*3)

	for i, solution_filename in enumerate(tqdm(pwd_list)):

		if 'solution_' not in solution_filename:	
			continue
		
		count += 1
		# extract solution id
		solution_id = solution_filename[9:-3]

		import_str = "solution_" + solution_id
		path_json = os.path.join(path, f"log_{criteria}.json")
		cmd = f"pytest {path_test} --tb=no --show-capture=no --solution {import_str} --report-log={path_json} --timeout=4"
		subprocess.call(cmd)

		log = open(f"{path_json}", "r")
		lines = log.readlines()

		test_cases_from_log = int((len(lines) - 4)/3)
		if test_cases_from_log == test_cases:
			result = ""
			new_outcome = 1
			for test_id in range(test_cases):
				if "passed" in lines[4 + 3 * (test_id)]:
					result = result + "P"
					test_metrics[(test_id)*3] = test_metrics[(test_id*3)] + 1
					continue
				elif "AssertionError" in lines[4 + 3 * (test_id)]:
					result = result + "F"
					test_metrics[(test_id*3)+1] = test_metrics[(test_id*3)+1] + 1
					new_outcome = 0
					continue
				result = result + "E"
				test_metrics[(test_id*3)+2] = test_metrics[(test_id*3)+2] + 1
				new_outcome = 0
		else:
			result = "TIMEOUT"
			new_outcome = 0

		values_solution.append((bool(new_outcome), result, int(solution_id)))

		#if count == 3:
		#	break
					
	for test_id in range(test_cases):
		insert_test = f"INSERT INTO test VALUES ({test_id},{problem_id},\"{criteria}\",{test_metrics[test_id*3]},{test_metrics[(test_id*3)+1]},{test_metrics[(test_id*3)+2]})"
		cursor.execute(insert_test)

	if "input" in criteria:
		insert_solution = f"UPDATE Solution_{problem_id} SET input_outcome = %s, input_result = %s WHERE solution_id = %s"
	elif "graph" in criteria:
		insert_solution = f"UPDATE Solution_{problem_id} SET graph_outcome = %s, graph_result = %s WHERE solution_id = %s"
	else:
		insert_solution = f"UPDATE Solution_{problem_id} SET mutation_outcome = %s, mutation_result = %s WHERE solution_id = %s"
			
	cursor.executemany(insert_solution, values_solution)
	cnx.commit()
	cursor.close()
	cnx.close()

#save_tests_output("graph",812)