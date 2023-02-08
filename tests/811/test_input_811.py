import pytest
import importlib

test_cases = [
	([1, 2, 3], 2, 3, True),
	([1, 2, 3], 3, 2, True),
	([2, 1, 3], 2, 3, True),
	([2, 1, 3], 3, 2, True),
	([3, 1, 2], 2, 3, True),
	([3, 1, 2], 3, 2, True),
]

@pytest.mark.parametrize("lst, h, w, output", test_cases)
def test_colchao(lst, h, w, output, solution):
	imp = importlib.import_module(solution)
	assert imp.colchao(lst, h, w) == output
