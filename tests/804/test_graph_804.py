import pytest
import importlib

test_cases = [
	((1,3,5,7), ()),
	((2,3,5,7), (2,)),
	((1,4,5,7), (4,)),
	((2,4,5,7), (2,4,)),
	((1,3,6,7), (6,)),
	((1,4,6,7), (4,6,)),
	((1,3,5,8), (8,)),
	((1,3,6,8), (6,8,)),
]

@pytest.mark.parametrize("a, output", test_cases)
def test_filtra_pares(a, output, solution):
	imp = importlib.import_module(solution)
	assert imp.filtra_pares(a) == output
