import pytest
import importlib

test_cases = [
	(5, 120),
	(4, 24),
	(0, 1),
]

@pytest.mark.parametrize("numero, output", test_cases)
def test_fatorial(numero, output, solution):
	imp = importlib.import_module(solution)
	assert imp.fatorial(numero) == output
