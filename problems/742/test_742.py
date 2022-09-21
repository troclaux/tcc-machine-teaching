from solution_57650 import *

import pytest

test_cases = [
	('hello world', 'i', 0, 'iello world'),
]

@pytest.mark.parametrize("s, x, i, output", test_cases)

def test_substitui(s, x, i, output):
	assert substitui(s, x, i) == output
