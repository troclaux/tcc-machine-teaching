import pytest
import importlib

test_cases = [
	(0, 1.5, 0),
	(1.5, 2, 1),
	(0, 1, 0),
	(3, 1.5, 2),
	(1.5, 1.5, 1),
	(1, 0.3, 3),
]

@pytest.mark.parametrize("dinheiro, preco, output", test_cases)

def test_num_bombons(dinheiro, preco, output, solution):
	imp = importlib.import_module(solution)
	assert imp.num_bombons(dinheiro, preco) == output
