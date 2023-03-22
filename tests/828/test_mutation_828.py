import pytest
import importlib

test_cases = [
    (1,False),
    (7,True),
	(10,False)
]

@pytest.mark.parametrize("a, output", test_cases)
def test_primo(a, output, solution):
	imp = importlib.import_module(solution)
	assert imp.primo(a) == output