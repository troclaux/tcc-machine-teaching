import pytest
import importlib

test_cases = [
    ([1,2,3,4,5,6,7,8,9],2,[2,4,6,8])
]

@pytest.mark.parametrize("a, b, output", test_cases)
def test_filtraMultiplos(a, b, output, solution):
	imp = importlib.import_module(solution)
	assert imp.filtraMultiplos(a, b) == output