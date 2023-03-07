import pytest
import importlib

test_cases = [
	([1, 2, 3], 1, [1, 1, 2, 3]),
	([-2, -1, 3, 4], -1, [-2, -1, -1, 3, 4]),
	([1, 2, 5], 4, [1, 2, 4, 5]),
	([-2, 1, 5], -3, [-3, -2, 1, 5]),
	([1, 2, 3], 4, [1, 2, 3, 4]),
	([-4, -3, -2, -1], -1, [-4, -3, -2, -1, -1]),
]

@pytest.mark.parametrize("lista_numero, n, output", test_cases)
def test_insere(lista_numero, n, output, solution):
	imp = importlib.import_module(solution)
	assert imp.insere(lista_numero, n) == output
