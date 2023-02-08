import pytest
import importlib

test_cases = [
	([1,2,3,4,5], 3, [4, 5])
]

@pytest.mark.parametrize("a, b, output", test_cases)
def test_maiores(a, b, output, solution):
	imp = importlib.import_module(solution)
	assert imp.maiores(a, b) == output
