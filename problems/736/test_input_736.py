import import_stmts
import pytest

test_cases = [
	('1','','11'),
	('','1','11'),
	('','',''),
	('x','y','xyyx'),
	('1','2','1221'),
]

@pytest.mark.parametrize("a, b, output", test_cases)

def test_concatenacao(a, b, output, solution):
	solution_stmt = eval(solution)
	assert solution_stmt.concatenacao(a, b) == output
