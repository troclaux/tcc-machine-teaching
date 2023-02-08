import pytest
import importlib

test_cases = [
	([0], 2, []),
	([1], 2, []),
	([2], 2, [2]),
	([2,4], 2, [2,4])
]

@pytest.mark.parametrize("a, b, output", test_cases)
def test_filtraMultiplos(a, b, output, solution):
	imp = importlib.import_module(solution)
	assert imp.filtraMultiplos(a, b) == output