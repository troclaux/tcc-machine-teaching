import pytest
import importlib

test_cases = [
	(0, 0),
	(1, 1.0),
	(2, 1.5)
]

@pytest.mark.parametrize("a, output", test_cases)
def test_soma_h(a, output, solution):
	imp = importlib.import_module(solution)
	assert imp.soma_h(a) == output
