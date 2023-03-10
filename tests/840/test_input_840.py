import pytest
import importlib

test_cases = [
	(0, 0, 0, 0),
	(0, 3, 5, 0),
	(0, 11, 11, 0),
	(2, 0, 5, 0),
	(2, 3, 0, 0),
	(2, 11, 11, 2),
	(25, 8, 0, 0),
	(17, 3, 20, 3),
	(22, 0, 30, 0),
	(7, 9, 5, 1),
	(11, 17, 26, 5),
]

@pytest.mark.parametrize("a, b, c, output", test_cases)

def test_bolos(a, b, c, output, solution):
	imp = importlib.import_module(solution)
	assert imp.bolos(a, b, c) == output
