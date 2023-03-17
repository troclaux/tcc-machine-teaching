import pytest
import importlib

test_cases = [
	(-1, 0),
	(0, 0),
	(5, 2)
]

@pytest.mark.parametrize("a, output", test_cases)
def test_qtd_divisores(a, output, solution):
	imp = importlib.import_module(solution)
	assert imp.qtd_divisores(a) == output
