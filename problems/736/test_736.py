from solution_50914 import *

import pytest

test_cases = [
	('1','','1'),
	('','1','1'),
	('','',''),
	('x','b','xb'),
	('1','y','1y')
]

@pytest.mark.parametrize("a, b, output", test_cases)

def test_concatenacao(a, b, output):
	assert concatenacao(a, b) == output
