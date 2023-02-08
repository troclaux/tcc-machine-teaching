import pytest
import importlib

test_cases = [
	([1, 2, 2], 1),
	([-1, -1, 3], 1),
	([1.1, 2.2, 2.2], 1),
	([2.2, 1.1, 2.2], 0),
	([-1.1, 2.2, 3.3], 0),
	([1], 0),
	([-1], 0),
	([1.1], 0),
	([-1.1], 0),
]

@pytest.mark.parametrize("lista_numero, output", test_cases)

def test_repetidos(lista_numero, output, solution):
	imp = importlib.import_module(solution)
	assert imp.repetidos(lista_numero) == output
