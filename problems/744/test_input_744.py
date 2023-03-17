import pytest
import importlib

test_cases = [
	('', '###'),
	('a', '##a#'),
	('ab','#a#b#'),
	('abc','#a#bc#')
]

@pytest.mark.parametrize("s, output", test_cases)

def test_hashtag(s, output, solution):
	imp = importlib.import_module(solution)
	assert imp.hashtag(s) == output
