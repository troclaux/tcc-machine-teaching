import pytest
import importlib

test_cases = [
	(1, 1.0),
	(9, 2.8289682539682537),
	(2, 1.5),
	(11, 3.0198773448773446),
	(12, 3.103210678210678),
	(0, 0),
]

@pytest.mark.parametrize("n, output", test_cases)
def test_soma_h(n, output, solution):
	imp = importlib.import_module(solution)
	assert imp.some_h(n) == output
