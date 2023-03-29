import pytest
import importlib

test_cases = [
	([[1]], True),
	([], True),
	([[1],[2]], False),
	([[30, 40]], False),
	([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]], True),
]

@pytest.mark.parametrize("matriz, output", test_cases)

def test_lingua_p(matriz, output, solution):
	imp = importlib.import_module(solution)
	assert imp.lingua_p(matriz) == output

