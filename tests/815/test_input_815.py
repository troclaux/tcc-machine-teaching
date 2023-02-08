import pytest
import importlib

test_cases = [
	([1, 2], 3, [1, 2, 3]),
	([1, 2], 1, [1, 1, 2]),
	([1, 2], 0, [0, 1, 2]),
	([1, 2], -1, [-1, 1, 2]),
	([-1, 0], 1, [-1, 0, 1]),
	([-1, 0], 0, [-1, 0, 0]),
	([-1, 0], -1, [-1, -1, 0]),
]

@pytest.mark.parametrize("lista_numero, n, output", test_cases)
def test_insere(lista_numero, n, output, solution):
	imp = importlib.import_module(solution)
	assert imp.insere(lista_numero, n) == output
