import pytest
import importlib

test_cases = [
	('a', 'x', 0, 'x'),
	('ab', 'x', 1, 'ax'),
	('ab', 'x', 0, 'xb'),
]

@pytest.mark.parametrize("s, x, i, output", test_cases)

def test_substitui(s, x, i, output, solution):
	imp = importlib.import_module(solution)
	assert imp.substitui(s, x, i) == output
