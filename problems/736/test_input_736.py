#import import_stmts
import sys
import pytest
import importlib

test_cases = [
	('1', '', '11'),
	('', '1', '11'),
	('', '', ''),
	('x', 'y', 'xyyx'),
	('1', '2', '1221'),
]

@pytest.mark.parametrize("a, b, output", test_cases)
def test_concatenacao(a, b, output, solution):
	imp = importlib.import_module(solution)
	assert imp.concatenacao(a, b) == output
