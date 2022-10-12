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

		import_str = " import_stmts.solution_" + solution_id

		os.system("pytest --tb=line --solution " + import_str)

	os.chdir('..')

