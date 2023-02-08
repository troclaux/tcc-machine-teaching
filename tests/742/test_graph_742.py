import pytest
import importlib

test_cases = [
	("teste","a",5, "i inválido"),
	("teste","o",4, "testo")
]

@pytest.mark.parametrize("a, b, c,output", test_cases)
def test_substitui(a, b, c, output, solution):
	imp = importlib.import_module(solution)
	assert imp.substitui(a, b, c) == output
