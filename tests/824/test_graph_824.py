import pytest
import importlib

test_cases = [
	("", ""),
	("c", "C"),
	("ae", "ae")
]

@pytest.mark.parametrize("a, output", test_cases)
def test_uppCons(a, output, solution):
	imp = importlib.import_module(solution)
	assert imp.uppCons(a) == output
