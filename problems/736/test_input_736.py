import import_stmts
import sys
import pytest
import importlib

test_cases = [
	('1','','11'),
	('','1','11'),
	('','',''),
	('x','y','xyyx'),
	('1','2','1221'),
]

# imp = importlib.import_module(import_stmt)

@pytest.mark.parametrize("a, b, output", test_cases)

def test_concatenacao(a, b, output, solution):
	solution_stmt = eval(solution)
	assert solution_stmt.concatenacao(a, b) == output
