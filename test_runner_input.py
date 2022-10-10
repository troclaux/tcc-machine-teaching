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

		solution_id = solution_filename[9:-3]

		test_filename = "test_input_" + problem_id + ".py"
		import_str = "from solution_" + solution_id + " import *\n"

		with open(test_filename, 'r', encoding='utf-8') as file:
			data = file.readlines()

		print(data)
		data[0] = import_str

		with open(test_filename, 'w', encoding='utf-8') as file:
			file.writelines(data)

		os.system("pytest --tb=line " + test_filename)
		# run previous command and save 

	os.chdir('..')

