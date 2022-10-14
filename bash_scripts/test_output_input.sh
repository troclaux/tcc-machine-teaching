
reset

# for every problem id passed in the command line, run the tests
for problem_id in "$@"; do

	cd problems/$problem_id
	count_solutions = 0
	> output_input.txt

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
		sed -i "1s/.*/$import_file/" test_input_$problem_id.py
		echo "Running test_$problem_id.py"
		# write pytest output in a file
		# python3 -m pytest test_$problem_id.py> output.txt
		output=`python3 -m pytest --timeout=2 test_input_$problem_id.py`
		# save the word after test_$problem_id.py in the variable output
		output=${output#*test_input_$problem_id.py }
		# save the first word in output in the variable result
		result=${output%% *}
		echo "result: $result"
		# if result contains only . or F characters, then the test passed
		if [[ $result =~ ^[.F]+$ ]]; then
			echo "valid pytest output for solution $solution_id"
			echo "$solution_id $result" >> output_input.txt
		else
			echo "invalid pytest output for solution $solution_id"
			echo "$solution_id ERROR" >> output_input.txt
		fi
	done
done

