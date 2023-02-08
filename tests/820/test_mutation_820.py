import pytest
import importlib

test_cases = [
    ('mariana come banana', 'a', 3, 6),
    ('mariana come banana', 'e', 2, -1)
]

@pytest.mark.parametrize("a, b, c, output", test_cases)
def test_posLetra(a, b, c, output, solution):
	imp = importlib.import_module(solution)
	assert imp.posLetra(a, b, c) == output