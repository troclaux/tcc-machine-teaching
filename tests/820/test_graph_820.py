import pytest
import importlib

test_cases = [
	("", "e", 1, -1),
	("e", "a", 1, -1),
	("banana", "b", 1, 0),
	("banana", "b", 2, -1)
]

@pytest.mark.parametrize("a, b, c, output", test_cases)
def test_posLetra(a, b, c, output, solution):
	imp = importlib.import_module(solution)
	assert imp.posLetra(a, b, c) == output