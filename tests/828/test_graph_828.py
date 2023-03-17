import pytest
import importlib

test_cases = [
	(1, False),
	(2, True),
	(3, True),
	(0, True),
    (4, False),
	(5, True)
]

@pytest.mark.parametrize("a, output", test_cases)
def test_primo(a, output, solution):
	imp = importlib.import_module(solution)
	assert imp.primo(a) == output


