import pytest
import importlib

test_cases = [
	([
      	[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
   		[2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
        [3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
        [4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
        [5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
        [6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
    ], (1, 1, 1)),
]

@pytest.mark.parametrize("a, output", test_cases)
def test_melhor_volta(a, output, solution):
	imp = importlib.import_module(solution)
	assert imp.melhor_volta(a) == output


