import pytest
import importlib

test_cases = [
	(96, 12),
	(2, 2),
	(102, 8),
	(101, 2),
]

@pytest.mark.parametrize("n, output", test_cases)

def test_qtd_divisores(n, output, solution):
	imp = importlib.import_module(solution)
	assert imp.qtd_divisores(n) == output
