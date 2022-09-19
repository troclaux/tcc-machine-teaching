# para rodar este script no linux:
# chmod +x test_runner.sh
# ./test_runner.sh

cd problems/736

# run all files that start with solution_ and end with .py
for file in solution_*.py; do
	echo "Running $file"
	# create variable str that saves the name of the file without the extension
	str=${file%.*}
	# remove the first 9 characters from the variable str
	# solution_id=${str:9}
	import_file="from ${str} import *"
	echo "$import_file"
	#pytest test_736.py
done

