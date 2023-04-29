import pytest
import importlib

test_cases = [
  ([1, 3, 5], [2, 4, 6], [1, 2, 3, 4, 5, 6]),
  ([1, 2, 3], ['a', 'b', 'c'], [1, 'a', 2, 'b', 3, 'c']),
  ([1, 2, 4], ['a', 3, 'b'], [1, 'a', 2, 3, 4, 'b']),
  (['a', 'b', 'c'], [1, 2, 3], ['a', 1, 'b', 2, 'c', 3]),
  (['a', 'c', 'e'], ['b', 'd', 'f'], ['a', 'b', 'c', 'd', 'e', 'f']),
  (['a', 'c', 'e'], ['b', 'd', 1], ['a', 'b', 'c', 'd', 'e', 1]),
  (['a', 2, 'b'], [1, 3, 4], ['a', 1, 2, 3, 'b', 4]),
  ([1, 2, 'c'], ['a', 'b', 'c'], [1, 'a', 2, 'b', 'c', 'c']),
  ([1, 2, 'c'], ['a', 'b', 3], [1, 'a', 2, 'b', 'c', 3])
]

@pytest.mark.parametrize("lista1, lista2, output", test_cases)

def test_intercala(lista1, lista2, output, solution):
	imp = importlib.import_module(solution)
	assert imp.intercala(lista1, lista2) == output
