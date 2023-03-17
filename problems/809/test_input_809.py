import pytest
import importlib

test_cases = [
	([1, 3, 5], [2, 4, 6], [1, 2, 3, 4, 5, 6]),
	(['a', 'b', 'c'], [1, 2, 3], ['a', 1, 'b', 2, 'c', 3]),
	([1, 2, 'c'], ['a', 'b', 'c'], [1, 'a', 2, 'b', 'c', 'c']),
	(['a', 'b', 'c'], ['a', 'b', 'c'], ['a', 'a', 'b', 'b', 'c', 'c']),
	([1, 2, 3], [1, 2, 3], [1, 1, 2, 2, 3, 3]),
	([1, 2, 3], ['a', 'b', 'c'], [1, 'a', 2, 'b', 3, 'c']),
]

@pytest.mark.parametrize("lista1, lista2, output", test_cases)

def test_intercala(lista1, lista2, output, solution):
	imp = importlib.import_module(solution)
	assert imp.intercala(lista1, lista2) == output
