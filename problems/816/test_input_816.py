import pytest
import importlib

test_cases = [
	([1, 2], 3, []),
	([-2, 1], -2, [1]),
	([2, 1], 0, [1, 2]),
]

@pytest.mark.parametrize("lista_numero, n, output", test_cases)
def test_maiores(lst, n, output, solution):
	imp = importlib.import_module(solution)
	assert imp.maiores(lst, n) == output
