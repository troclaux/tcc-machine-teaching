import pytest
import importlib

test_cases = [
	([1, 3], 2),
	([1, 3, 4], 2),
	([5, 3], 4),
	([5, 3, 2], 4),
]

@pytest.mark.parametrize("lista_numero, output", test_cases)

def test_faltante(lista_numero, output, solution):
	imp = importlib.import_module(solution)
	assert imp.faltante(lista_numero) == output
