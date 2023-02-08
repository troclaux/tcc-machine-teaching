import pytest
import importlib

test_cases = [
	("teste unico", 2)
]

@pytest.mark.parametrize("a, output", test_cases)
def test_quant_palavras(a, output, solution):
	imp = importlib.import_module(solution)
	assert imp.quant_palavras(a) == output
