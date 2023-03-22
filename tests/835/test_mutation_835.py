import pytest
import importlib

test_cases = [
    ([[9,9,9,9,9,9,9,9,9,10],
	[9,9,9,9,9,9,9,9,9,10],
	[9,9,9,9,9,1,9,9,9,10],
	[9,9,9,9,9,9,9,9,9,10],
	[9,9,9,9,9,9,9,9,9,10],
	[9,9,9,9,9,9,9,9,9,10]], (3, 1, 6))
]

@pytest.mark.parametrize("a, output", test_cases)
def test_melhor_volta(a, output, solution):
	imp = importlib.import_module(solution)
	assert imp.melhor_volta(a) == output