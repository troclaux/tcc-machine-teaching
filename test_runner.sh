# para rodar este script no linux:
# chmod +x test_runner.sh
# ./test_runner.sh

cd problems/736

# run all files that start with solution_ and end with .py
for file in solution_*.py; do
	echo "Running $file"
	#pytest test_736.py
done

