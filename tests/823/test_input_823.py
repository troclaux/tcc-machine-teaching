import pytest
import importlib

test_cases = [
	([2, 3, 4, 5, 6], 1),
	([1, 2, 3, 4, 5], 6),
	([1, 2, 3, 5, 6], 4),
	([6, 5, 4, 3, 2], 1),
	([5, 4, 3, 2, 1], 6),
	([6, 5, 4, 3, 1], 2),
	([5, 6, 3, 4, 2], 1),
	([3, 4, 5, 1, 2], 6),
	([4, 2, 1, 6, 5], 3),
]

@pytest.mark.parametrize("lista_numero, output", test_cases)

def test_faltante(lista_numero, output, solution):
	imp = importlib.import_module(solution)
	assert imp.faltante(lista_numero) == output
