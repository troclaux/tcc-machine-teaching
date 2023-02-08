import pytest
import importlib

test_cases = [
	([1], 0),
	([1], 1),
	([1], 1)
]

@pytest.mark.parametrize("a, output", test_cases)
def test_repetidos(a, output, solution):
	imp = importlib.import_module(solution)
	assert imp.repetidos(a) == output