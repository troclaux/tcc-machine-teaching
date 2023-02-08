import pytest
import importlib

test_cases = [
	([200,300,400], 200, 100, False),
	([130,150,200], 200, 100, False),
	([50,100,200], 200, 100, True)
]

@pytest.mark.parametrize("a, b, c, output", test_cases)
def test_colchao(a, b, c, output, solution):
	imp = importlib.import_module(solution)
	assert imp.colchao(a, b, c) == output
