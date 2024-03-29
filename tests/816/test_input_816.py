import pytest
import importlib

test_cases = [
	([2, 0, 3, 1], 2, [3]),
	([2, 0, 3, 1], -1, [0, 1, 2, 3]),
	([1, 3, -1, 2, 0], 2, [3]),
	([1, 3, -1, 2, 0], -1, [0, 1, 2, 3]),
	([1, 3, -1, 2, 0], 4, []),
]

@pytest.mark.parametrize("lista, n, output", test_cases)
def test_maiores(lista, n, output, solution):
	imp = importlib.import_module(solution)
	assert imp.maiores(lista, n) == output
