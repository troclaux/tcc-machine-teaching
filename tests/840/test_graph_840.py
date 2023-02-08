import sys
import pytest
import importlib

test_cases = [
	(4, 5, 10, 1)
]

@pytest.mark.parametrize("a, b, c, output", test_cases)
def test_bolos(a, b, c, output, solution):
	imp = importlib.import_module(solution)
	assert imp.bolos(a, b, c) == output
