import pytest
import importlib

test_cases = [
    ('abcdefghi','aBCDeFGHi')
]

@pytest.mark.parametrize("a, output", test_cases)
def test_uppCons(a, output, solution):
	imp = importlib.import_module(solution)
	assert imp.uppCons(a) == output