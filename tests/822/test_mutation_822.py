import pytest
import importlib

test_cases = [
    ([1,4,3,3,2,3,3,3,3,5,4,6,6,7,6,8,8,7],6)
]

@pytest.mark.parametrize("a, output", test_cases)
def test_repetidos(a, output, solution):
	imp = importlib.import_module(solution)
	assert imp.repetidos(a) == output