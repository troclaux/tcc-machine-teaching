from solution_37112 import *

import pytest

test_cases = [
	((0, 0, 1, 1), (0, 0, 1, 1), True),
	((-2, -2, -1, -1), (0, 0, 1, 1), False),
	((0, 0, 1, 1), (-2, -2, -1, -1), False),
	((-2, -2, -1, -1), (-2, -2, -1, -1), True),
]

@pytest.mark.parametrize("tupla1, tupla2, output", test_cases)

def test_colisao(tupla1, tupla2, output):
	assert colisao(tupla1, tupla2) == output
