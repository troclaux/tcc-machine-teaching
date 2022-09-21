from solution_50914 import *

import pytest

test_cases = [
	('1','','1'),
	('','1','1'),
	('','',''),
	('x','y','xy'),
	('1','2','12'),
]

@pytest.mark.parametrize("a, b, output", test_cases)

def test_concatenacao(a, b, output):
	assert concatenacao(a, b) == output
