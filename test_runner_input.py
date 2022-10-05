import os
import sys

for problem_id in sys.argv[1:]:

	os.chdir('problems')
	os.chdir(problem_id)

	pwd_list = sorted(os.listdir())

	for solution_filename in pwd_list:

		if 'solution_' not in solution_filename:
			continue


		print(os.getcwd())

		print(solution_filename)

		buffer = solution_filename.split('_')
		buffer = buffer[1].split('.')
		solution_id = buffer[0]

		test_filename = "test_input_" + problem_id + ".py"
		import_str = "from solution_" + solution_id + " import *"

	os.chdir('..')

