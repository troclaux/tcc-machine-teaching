import pytest
import importlib

test_cases = [
	("", ""),
	("c", "c"),
	("a", "apa"),
	("cd", "cd"),
	("abcd", "apabcd")
]

@pytest.mark.parametrize("a, output", test_cases)
def test_lingua_p(a, output, solution):
	imp = importlib.import_module(solution)
	assert imp.lingua_p(a) == output


