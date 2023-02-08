import pytest
import importlib

test_cases = [
    (3,9,15,1),
    (6,5,15,1),
    (6,9,9,1)
]

@pytest.mark.parametrize("a, b, c output", test_cases)
def test_bolos(a, b, c, output, solution):
	imp = importlib.import_module(solution)
	assert imp.bolos(a, b, c) == output