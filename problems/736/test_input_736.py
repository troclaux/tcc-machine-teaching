import pytest
import importlib

test_cases = [
	('1', '', '11'),
	('', '1', '11'),
	('', '', ''),
	('ab', 'cd', 'abcdcdab'),
	('12', '34', '12343412'),
]

@pytest.mark.parametrize("a, b, output", test_cases)
def test_concatenacao(a, b, output, solution):
	imp = importlib.import_module(solution)
	assert imp.concatenacao(a, b) == output
