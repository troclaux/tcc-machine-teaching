import pytest
import importlib

test_cases = [
    ([25,120,220],200,100, True),
    ([100,120,220],200,100, True),
    ([25,200,220],200,100, True)
]

@pytest.mark.parametrize("a, b, c, output", test_cases)
def test_colchao(a, b, c, output, solution):
	imp = importlib.import_module(solution)
	assert imp.colchao(a, b, c) == output