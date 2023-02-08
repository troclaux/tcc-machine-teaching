import sys
import pytest
import importlib

test_cases = [
	(10, 4, 3)
]

@pytest.mark.parametrize("a, b, output", test_cases)
def test_carros(a, b, output, solution):
	imp = importlib.import_module(solution)
	assert imp.carros(a, b) == output
