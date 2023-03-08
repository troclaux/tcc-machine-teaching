import pytest
import importlib

test_cases = [
	(0, 1),
	(1, 1),
	(2, 2),
	(5, 120),
	(6, 720),
	(7, 5040),
]

@pytest.mark.parametrize("numero, output", test_cases)
def test_fatorial(numero, output, solution):
	imp = importlib.import_module(solution)
	assert imp.fatorial(numero) == output
