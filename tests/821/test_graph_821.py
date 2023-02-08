import pytest
import importlib

test_cases = [
	(0, 1),
	(3, 6)
]

@pytest.mark.parametrize("a, output", test_cases)
def test_fatorial(a, output, solution):
	imp = importlib.import_module(solution)
	assert imp.fatorial(a) == output