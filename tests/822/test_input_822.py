import pytest
import importlib

test_cases = [
	([1, 2, 3, 4, 5], 0),
	([-1.0, -1.0, -3.0, -2.0, -2.0], 2),
	([1, 1, 1, -2.0, -2.0, -2.0, 3, 3, 3, 3], 7),
]

@pytest.mark.parametrize("lista_numero, output", test_cases)

def test_repetidos(lista_numero, output, solution):
	imp = importlib.import_module(solution)
	assert imp.repetidos(lista_numero) == output
