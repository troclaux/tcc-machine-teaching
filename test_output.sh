# para rodar este script no linux:
# chmod +x test_output.sh
# ./test_output.sh

reset

# for every problem id passed in the command line, run the tests
for problem_id in "$@"; do

	cd problems/$problem_id
	count_solutions = 0
	> output.txt

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
		output=`python3 -m pytest test_$problem_id.py`
		# save the word after test_$problem_id.py in the variable output
		output=${output#*test_$problem_id.py }
		# save the first word in ouput in the variable result
		result=${output%% *}
		echo "result: $result"
		# echo "output: $output"
		count_perfect_solutions=0
		# if result contains only . or F characters, then the test passed
		if [[ $result =~ ^[.F]+$ ]]; then
			echo "valid pytest output for solution $solution_id"
			# solution_id .F.F.
			echo "$solution_id $result" >> output.txt
			# if result contains only . characters, then increment count_perfect_solutions
			if [[ $result =~ ^[.]+$ ]]; then
				count_perfect_solutions=$((count_perfect_solutions+1))
			fi
		else
			echo "invalid pytest output for solution $solution_id"
			echo "$solution_id ERROR" >> output.txt
		fi
		# invalid output in solution_50936.py
		echo "total number of solutions: $count_solutions"
		echo "perfect solutions: $count_perfect_solutions"
	done
done

