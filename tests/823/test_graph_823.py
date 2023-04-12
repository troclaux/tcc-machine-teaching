import pytest
import importlib

test_cases = [
	([1], 2),
	([1,2], 3)
]

@pytest.mark.parametrize("a, output", test_cases)
def test_faltante(a, output, solution):
	imp = importlib.import_module(solution)
	assert imp.faltante(a) == output
