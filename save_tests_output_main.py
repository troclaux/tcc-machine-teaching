import os
import sys
import subprocess
import pytest
import pandas as pd
from tqdm import tqdm
import importlib

def save_tests_output(criterion,problem_id):
	directory = os.getcwd()
	path_csv = os.path.join(directory, "CSV")
	path_csv_solution = os.path.join(path_csv, f"solution_{problem_id}.csv")
	path_csv_test = os.path.join(path_csv, f"test_{problem_id}.csv")
	#path_csv = os.path.join(path_csv, str(problem_id))
	path = os.path.join(directory, "problems")
	path = os.path.join(path, str(problem_id))

	pwd_list = sorted(os.listdir(path))
			
	test_str = f"test_{criterion}_{problem_id}.py"
	path_test = os.path.join(path, test_str)


	#values_solution = []
	#values_solution = 	pd.DataFrame({'new_outcome': pd.Series(dtype='bool_'),
    #               		'result': pd.Series(dtype='str'),
    #               		'solution_id': pd.Series(dtype='int')})
	#count = 0
	#new_row = {'new_outcome':1, 'result':'test', 'solution_id':1}
	#values_solution = values_solution.append([0, "test", 1])
	#values_solution = values_solution.append(new_row, ignore_index=True)
	#print(values_solution)

	spec = importlib.util.spec_from_file_location(test_str, path_test)
	test = importlib.util.module_from_spec(spec)
	sys.modules["module.name"] = test
	spec.loader.exec_module(test)
	test_cases = len(test.test_cases)
	test_metrics = [0]*(test_cases*4)
	df_solution = pd.read_csv(path_csv_solution)

	#count = 0
	for i, solution_filename in enumerate(tqdm(pwd_list)):

		if 'solution_' not in solution_filename:	
			continue
		
		
		#count += 1
		# extract solution id
		solution_id = solution_filename[9:-3]

		import_str = "solution_" + solution_id
		path_json = os.path.join(path, f"log_{criterion}.json")
		cmd = f"pytest {path_test} --tb=no --show-capture=no --solution {import_str} --report-log={path_json} --timeout=1"
		#pytest test_input_820.py --tb=no --show-capture=no --solution solution_102115 --report-log=log_input.json --timeout=2
		subprocess.run(cmd, shell=True)

		log = open(f"{path_json}", "r")
		lines = log.readlines()

		test_cases_from_log = int((len(lines) - 4)/3)
		if test_cases_from_log == test_cases:
			result = ""
			new_outcome = 1
			for test_id in range(test_cases):
				if "passed" in lines[4 + 3 * (test_id)]:
					result = result + "P"
					test_metrics[test_id*4] = test_metrics[(test_id*4)] + 1
					continue
				elif "AssertionError" in lines[4 + 3 * (test_id)]:
					result = result + "F"
					test_metrics[(test_id*4)+1] = test_metrics[(test_id*4)+1] + 1
					new_outcome = 0
					continue
				elif "Timeout" in lines[4 + 3 * (test_id)]:
					result = result + "T"
					test_metrics[(test_id*4)+2] = test_metrics[(test_id*4)+2] + 1
					new_outcome = 0
					continue
				result = result + "E"
				test_metrics[(test_id*4)+3] = test_metrics[(test_id*4)+3] + 1
				new_outcome = 0
		else:
			result = "FAIL"
			new_outcome = 0
		#else:
		#	result = "TIMEOUT"
		#	test_metrics[(test_id*4)+2] = test_metrics[(test_id*4)+2] + 1
		#	new_outcome = 0
		
		#new_row = {'new_outcome':bool(new_outcome), 'result':result, 'solution_id':int(solution_id)}
		#values_solution = values_solution.append(new_row, ignore_index=True)
		if criterion == "input":
			df_solution.loc[df_solution['solution_id'] == int(solution_id), ['input_outcome','input_result']] = bool(new_outcome),result
		elif criterion == "graph":
			df_solution.loc[df_solution['solution_id'] == int(solution_id), ['graph_outcome','graph_result']] = bool(new_outcome),result
		else:
			df_solution.loc[df_solution['solution_id'] == int(solution_id), ['mutation_outcome','mutation_result']] = bool(new_outcome),result

		#if count == 3:
		#	break
	#values_solution = pd.DataFrame (values_solution, columns = ['new_outcome','result','solution_id'])
	df_solution.to_csv(path_or_buf=path_csv_solution, index=False)
	for test_id in range(test_cases):
		if test_id == 0:
			df_test = pd.read_csv(path_csv_test)
			df_test = df_test.drop(df_test[df_test.criteria_type == criterion].index)
		df_test_id = [test_id, problem_id, criterion, test_metrics[test_id*4], test_metrics[(test_id*4)+1], test_metrics[(test_id*4)+2], test_metrics[(test_id*4)+3]]
		#new_row = {'test_id':test_id,'problem_id':problem_id,'criteria_type':criteria,'pass_count':test_metrics[test_id*4], 'fail_count':test_metrics[(test_id*4)+1], 'error_count':test_metrics[(test_id*4)+2]}
		#df_test = df_test.append(new_row, ignore_index=True)
		df_value = pd.DataFrame([df_test_id], columns=['test_id','problem_id','criteria_type','pass_count','fail_count','timeout_count','error_count'])
		df_test = pd.concat([df_test, df_value], ignore_index=True)
	df_test.to_csv(path_or_buf=path_csv_test, index=False)
	df_solution.to_csv(path_or_buf=path_csv_solution, index=False)


#save_tests_output("input",742)
#save_tests_output("graph",742)
save_tests_output("mutation",840)