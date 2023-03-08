import pytest
import importlib

test_cases = [
	([1, 2, 3, 4, 5], 2, [2, 4]),
	([1, 2, 3, 4, 5], -2.0, [2, 4]),
	([1.0, 2.0, 3.0, 4.0, 5.0], 2.0, [2.0, 4.0]),
	([1.0, 2.0, 3.0, 4.0, 5.0], -2, [2.0, 4.0]),
	([1, 2.0, 3, 4.0, 5], 2, [2.0, 4.0]),
	([1, 2.0, 3, 4.0, 5], -2.0, [2.0, 4.0]),
]

@pytest.mark.parametrize("lista_numero, n, output", test_cases)

def test_filtraMultiplos(lista_numero, n, output, solution):
	imp = importlib.import_module(solution)
	assert imp.filtraMultiplos(lista_numero, n) == output
