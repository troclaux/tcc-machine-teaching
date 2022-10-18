import pytest
import importlib

test_cases = [

	([1, 2], 2, [2])
	([-1.1, -3.3, -2.2], -1.1, [-1.1, -3.3, -2.2])
	([3, 5], 4, [])
]

@pytest.mark.parametrize("lista_numero, n, output", test_cases)

def test_filtraMultiplos(lista_numero, n, output, solution):
	imp = importlib.import_module(solution)
	assert imp.filtraMultiplos(lista_numero, n) == output
