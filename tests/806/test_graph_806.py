import pytest
import importlib

#x_inf_esq1, y_inf_esq1, x_sup_dir1, y_sup_dir1 = ret1
#x_inf_esq2, y_inf_esq2, x_sup_dir2, y_sup_dir2 = ret2

test_cases = [
	((1,1,0,0), (0,0,0,0), False),
	((1,1,1,1), (1,2,1,1), False),
	((3,3,3,3), (5,3,3,3), False),
	((2,2,2,2), (2,2,2,2), True),
]

@pytest.mark.parametrize("a, b, output", test_cases)
def test_colisao(a, b, output, solution):
	imp = importlib.import_module(solution)
	assert imp.colisao(a, b) == output
