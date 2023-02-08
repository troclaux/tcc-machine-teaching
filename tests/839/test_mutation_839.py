import pytest
import importlib

test_cases = [
    (12,3)
]

@pytest.mark.parametrize("a, output", test_cases)
def test_carros(a, output, solution):
	imp = importlib.import_module(solution)
	assert imp.carros(a) == output