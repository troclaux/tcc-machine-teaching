import pytest
import importlib

test_cases = [
	([[1,2], [3,4]], True),
	([], True)
]

@pytest.mark.parametrize("a, output", test_cases)
def test_eh_quadrada(a, output, solution):
	imp = importlib.import_module(solution)
	assert imp.eh_quadrada(a) == output