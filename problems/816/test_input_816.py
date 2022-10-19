import pytest
import importlib

test_cases = [
	([1, 2], 3, []),
	([-2, 1], -2, [1]),
	([2, 1], 0, [1, 2]),
]

@pytest.mark.parametrize("lista, n, output", test_cases)
def test_maiores(lista, n, output, solution):
	imp = importlib.import_module(solution)
	assert imp.maiores(lista, n) == output
