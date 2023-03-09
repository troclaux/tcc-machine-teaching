import pytest
import importlib

test_cases = [
	(0, 10, 0),
	(7.5, 7.5, 1.0),
	(10, 7.5, 1.0),
]

@pytest.mark.parametrize("dinheiro, preco, output", test_cases)

def test_num_bombons(dinheiro, preco, output, solution):
	imp = importlib.import_module(solution)
	assert imp.num_bombons(dinheiro, preco) == output
