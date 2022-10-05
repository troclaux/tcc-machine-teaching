import os
import sys


# loop through vector skipping first element
for problem_id in sys.argv[1:]:

	os.chdir('problems')
	# list all directories in working directory
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
		# print(solution_id)

		# open test_input_problem_id.py and replace first line with solution_id
		# print working directory
		# import_str = "from solution_" + solution_id + " import *"

		# replace first line with import_str

		# os.system('pytest test_input_' + problem_id + '.py')

	os.chdir('..')

