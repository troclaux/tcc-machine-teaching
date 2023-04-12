import pytest
import importlib

test_cases = [
	(1, 1.0),
	(9, 2.83),
	(2, 1.5),
	(11, 3.02),
	(12, 3.10),
	(0, 0),
]

@pytest.mark.parametrize("n, output", test_cases)
def test_soma_h(n, output, solution):
	imp = importlib.import_module(solution)
	assert imp.soma_h(n) == output
