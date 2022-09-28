from solution_50922 import *

import pytest

test_cases = [
	('1','','11'),
	('','1','11'),
	('','',''),
	('x','y','xyyx'),
	('1','2','1221'),
]

@pytest.mark.parametrize("a, b, output", test_cases)

def test_concatenacao(a, b, output):
	assert concatenacao(a, b) == output
