import pytest
import importlib

test_cases = [
	(0, 0, 0, 0),
	(0, 3, 5, 0),
	(2, 0, 5, 0),
	(2, 1, 1, 0),
	(2, 3, 0, 0),
	(2, 6, 5, 1),
]

@pytest.mark.parametrize("a, b, c, output", test_cases)

def test_bolos(a, b, c, output, solution):
	imp = importlib.import_module(solution)
	assert imp.bolos(a, b, c) == output
