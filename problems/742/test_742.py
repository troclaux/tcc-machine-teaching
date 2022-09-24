from solution_57655 import *

import pytest

test_cases = [
	('a', 'x', 0, 'a'),
	('ab', 'x', 1, 'ax'),
	('ab', 'x', 0, 'xb'),
]

@pytest.mark.parametrize("s, x, i, output", test_cases)

def test_substitui(s, x, i, output):
	assert substitui(s, x, i) == output
