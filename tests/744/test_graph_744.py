import pytest
import importlib

test_cases = [
	("teste", "#te#ste#")
]

@pytest.mark.parametrize("a, output", test_cases)
def test_hashtag(a, output, solution):
	imp = importlib.import_module(solution)
	assert imp.hashtag(a) == output
