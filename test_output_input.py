import os
import sys
import subprocess

os.system('reset')

for problem_id in sys.argv[1:]:

	os.chdir('problems')
	os.chdir(problem_id)

	os.system('> output_input.txt')

	pwd_list = sorted(os.listdir())

	for solution_filename in pwd_list:

		if 'solution_' not in solution_filename:
			continue

		solution_id = solution_filename[9:-3]


		test_filename = "test_input_" + problem_id + ".py"
		import_str = "from solution_" + solution_id + " import *\n"

		with open(test_filename, 'r', encoding='utf-8') as file:
			data = file.readlines()
			file.close()

		data[0] = import_str

		with open(test_filename, 'w', encoding='utf-8') as file:
			file.writelines(data)
			file.close()

		cmd = "pytest --tb=line " + test_filename
		# os.system(cmd)

		try:
			output_str = subprocess.check_output(cmd, shell=True).decode('utf-8')
			result = output_str.split("collected")[1]
			result = result.split("\n")
			result = result[2].split(" ")[1]
			print(f'{solution_id} {result}')
		except Exception as e:
			# print(f"ERROR {solution_id}:", e.output.decode('utf-8'))
			e_str = str(e)[-2]
			if e_str == '1':
				result = e.output.decode('utf-8').split("collected")[1]
				result = result.split("\n")
				result = result[2].split(" ")[1]
			elif e_str == '2':
				result = "ERROR"
			else:
				result = "UNKNOWN EXIT STATUS"

			print(f'{solution_id} {result}')

	os.chdir('..')
