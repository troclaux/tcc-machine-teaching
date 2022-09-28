from solution_26712 import *

import pytest

test_cases = [
	('', '###'),
	('a', '##a#'),
	('ab','#a#b#'),
	('abc','#a#bc#')
]

@pytest.mark.parametrize("s, output", test_cases)

def test_hashtag(s, output):
	assert hashtag(s) == output
