import pytest
import importlib

test_cases = [
	([10, 20, 30], 50, 50, True),
	([1, 10, 20], 5, 5, False),
	([10, 20, 30], 5, 5, False),
	([1, 10, 15], 5, 20, True),
	([1, 10, 15], 20, 5, True),
	([10, 10, 30], 20, 5, False),
	([10, 10, 30], 5, 20, False),
	([10, 30, 40], 20, 5, False),
	([10, 30, 40], 5, 20, False),
]

@pytest.mark.parametrize("lst, h, w, output", test_cases)
def test_colchao(lst, h, w, output, solution):
	imp = importlib.import_module(solution)
	assert imp.colchao(lst, h, w) == output
