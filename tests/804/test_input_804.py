import pytest
import importlib

test_cases = [
	((0, 2, 4, 6), (0, 2, 4, 6)),
	((0, 1, 2, 3), (0, 2)),
	((1, 3, 5, 7), ()),
	((-2, 0, 2, 4), (-2, 0, 2, 4)),
	((-2, -1, 0, 1), (-2, 0)),
	((-7, -5, -3, -1), ())
]

@pytest.mark.parametrize("tupla, output", test_cases)

def test_filtra_pares(tupla, output, solution):
	imp = importlib.import_module(solution)
	assert imp.filtra_pares(tupla) == output
