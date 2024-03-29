import pytest
import importlib

test_cases = [
    ([],True),
	([[1,2,3],
	[4,5,6],
	[7,8,9]],True)
]

@pytest.mark.parametrize("a, output", test_cases)
def test_eh_quadrada(a, output, solution):
	imp = importlib.import_module(solution)
	assert imp.eh_quadrada(a) == output