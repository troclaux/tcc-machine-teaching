import sys
import os

n = len(sys.argv)

problems_id = sys.argv
problems_id.pop(0)

for problem_id in problems_id:

	count_passed_criteria_tests = 0
	count_failed_criteria_tests = 0

	output_path = os.path.join(sys.path[0], "problems")
	output_path = os.path.join(output_path, problem_id)
	output_path = os.path.join(output_path, "output.txt")
	print(output_path)
	print(problem_id)
	# try to open file located in output_path, in read mode
	try:
		f = open(output_path, "r")
		print("File opened successfully")
		
		for line in f:
			#if string only contains dots, increment count_passed_criteria_tests
			line_list = line.split()
			print(line_list)
			if line_list[1].strip(".") == "":
				print("line is only dots")
				count_passed_criteria_tests += 1
			else:
				print("line is not only dots")
				count_failed_criteria_tests += 1
		
		print("Total: ", count_passed_criteria_tests + count_failed_criteria_tests)
		print("Quantidade de soluções que passaram: ", count_passed_criteria_tests)
		print("Quantidade de soluções que falharam: ", count_failed_criteria_tests)


	except IOError:
		print("File not accessible")
		continue

