import os
import sys

for problem_id in sys.argv[1:]:

	os.chdir('problems')
	os.chdir(problem_id)

	pwd_list = sorted(os.listdir())

	test_str = "test_input_" + problem_id + ".py"

	for solution_filename in pwd_list:

		if 'solution_' not in solution_filename:
			continue

		print(os.getcwd())
		print(solution_filename)

		#extract solution id
		solution_id = solution_filename[9:-3]
		import_str = " import_stmts.solution_" + solution_id
		# define the command to run
		cmd = f"pytest {test_str} --tb=line --solution {import_str} --timeout=2"
		# run test command
		os.system(cmd)

	os.chdir('..')

