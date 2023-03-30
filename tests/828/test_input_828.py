import pytest
import importlib

test_cases = [
	(1, False),
	(2, True),
	(97, True),
	(101, True),
	(100, False),
	(102, False)
]

@pytest.mark.parametrize("n, output", test_cases)

def test_primo(n, output, solution):
	imp = importlib.import_module(solution)
	assert imp.primo(n) == output
