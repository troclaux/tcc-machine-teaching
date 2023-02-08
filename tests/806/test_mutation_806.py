import pytest
import importlib

test_cases = [
	((0,0,1,1),(0,0,1,1),True),
    ((0,0,4,2),(4,2,9,5),True),
    ((4,2,9,5),(2,1,4,2),True),
    ((5,3,6,4),(1,3,3,6),False),
    ((3,5,4,6),(3,1,6,3),False)
]

@pytest.mark.parametrize("a, b, output", test_cases)
def test_colisao(a, b, output, solution):
	imp = importlib.import_module(solution)
	assert imp.colisao(a, b) == output