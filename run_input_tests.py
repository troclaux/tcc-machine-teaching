import os
import sys
from tqdm import tqdm

for problem_id in sys.argv[1:]:

	os.chdir('problems')
	os.chdir(problem_id)

	pwd_list = sorted(os.listdir())

	test_str = "test_input_" + problem_id + ".py"

	for i, solution_filename in enumerate(tqdm(pwd_list)):

		if 'solution_' not in solution_filename:
			continue

		print(os.getcwd())
		print(solution_filename)

		#extract solution id
		solution_id = solution_filename[9:-3]
		import_str = "solution_" + solution_id
		# define the command to run
		cmd = f"pytest {test_str} --tb=line --solution {import_str} --timeout=2"
		# run test command
		os.system(cmd)

	os.chdir('..')

