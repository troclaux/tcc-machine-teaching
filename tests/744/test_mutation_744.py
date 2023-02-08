import pytest
import importlib

test_cases = [
	('Lucas','#Lu#cas#')
]

@pytest.mark.parametrize("a, output", test_cases)
def test_hastag(a, output, solution):
	imp = importlib.import_module(solution)
	assert imp.hastag(a) == output
