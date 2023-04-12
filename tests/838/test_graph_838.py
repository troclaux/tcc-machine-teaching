import sys
import pytest
import importlib

test_cases = [
	(12.0, 2.5, 4)
]

@pytest.mark.parametrize("a, b, output", test_cases)
def test_num_bombons(a, b, output, solution):
	imp = importlib.import_module(solution)
	assert imp.num_bombons(a, b) == output
