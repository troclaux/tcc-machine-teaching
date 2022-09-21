from solution_26744 import *

import pytest

test_cases = [
	('', '###'),
	('ab','#a#b#'),
	('abc','#a#bc#'),
]

@pytest.mark.parametrize("s, output", test_cases)
def test_hashtag(s, output):
	assert hashtag(s) == output
