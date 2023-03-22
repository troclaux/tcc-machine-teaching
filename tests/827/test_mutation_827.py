import pytest
import importlib

test_cases = [
    (10,4)
]

@pytest.mark.parametrize("a, output", test_cases)
def test_qtd_divisores(a, output, solution):
	imp = importlib.import_module(solution)
	assert imp.qtd_divisores(a) == output