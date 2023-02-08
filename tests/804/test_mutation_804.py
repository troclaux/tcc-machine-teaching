import pytest
import importlib

test_cases = [
	((2,4,6,8),(2,4,6,8))
]

@pytest.mark.parametrize("a, output", test_cases)
def test_filtra_pares(a, output, solution):
	imp = importlib.import_module(solution)
	assert imp.filtra_pares(a) == output
