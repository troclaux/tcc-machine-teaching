import pytest
import importlib

test_cases = [
    ([1,3,5],[2,4,6],[1,2,3,4,5,6])
]

@pytest.mark.parametrize("a, b, output", test_cases)
def test_intercala(a, b, output, solution):
	imp = importlib.import_module(solution)
	assert imp.intercala(a, b) == output

