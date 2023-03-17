import pytest
import importlib

test_cases = [
	(2, [], 0),
	(2, [[1,2]], 1),
	(2, [[1,2], [3,4]], 1)
]

@pytest.mark.parametrize("a, b, output", test_cases)
def test_conta_numero(a, b, output, solution):
	imp = importlib.import_module(solution)
	assert imp.conta_numero(a, b) == output


