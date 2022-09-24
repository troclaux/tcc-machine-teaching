# para rodar este script no linux:
# chmod +x test_runner.sh
# ./test_runner.sh

reset

# for every problem id passed in the command line, run the tests
for problem_id in "$@"; do

	cd problems/$problem_id

	# run all files that start with solution_ and end with .py
	for file in solution_*.py; do
		echo "Running $file"
		# create variable str that saves the name of the file without the extension
		str=${file%.*}
		# remove the first 9 characters from the variable str
		import_file="from ${str} import *"
		solution_id=${str:9}
		echo "$import_file"
		#replace first line of test_$problem_id.py with $import_file
		sed -i "1s/.*/$import_file/" test_$problem_id.py
		echo "Running test_$problem_id.py"
		# write pytest output in a file
		# python3 -m pytest test_$problem_id.py> output.txt
		python3 -m pytest test_$problem_id.py

	done

done

