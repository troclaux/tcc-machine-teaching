import os
import sys
import subprocess

for problem_id in sys.argv[1:]:

	os.chdir('problems')
	os.chdir(problem_id)
	os.system('> output_input.txt')

	pwd_list = sorted(os.listdir())

	for solution_filename in pwd_list:

		if 'solution_' not in solution_filename:
			continue

		solution_id = solution_filename[9:-3]

		import_str = " import_stmts.solution_" + solution_id
		cmd = "pytest --tb=line --solution " + import_str
		# os.system(cmd + " >> output_input.txt")

		try:
			output_str = subprocess.check_output(cmd, shell=True).decode('utf-8')
			result = output_str.split("\n")[6]
			result = result.split(" ")[1]

		except Exception as e:
			# print(f"ERROR {solution_id}:", e.output.decode('utf-8'))

			e_str = str(e)[-2]

			if e_str == '1':
				output_str = e.output.decode('utf-8')
				result = output_str.split("\n")[6]
				result = result.split(" ")[1]
			elif e_str == '2':
				result = "ERROR"
			else:
				result = "UNKNOWN EXIT STATUS"

		print(f'SOLUTION {solution_id}: {result}')

	os.chdir('..')
