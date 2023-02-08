import pytest
import importlib

test_cases = [
	('hello', 1),
	(' hello', 1),
	('hello ', 1),
	(' hello ', 1),
	('hello world', 2),
	(' hello world', 2),
	('hello world ', 2),
	(' hello world ', 2),
]

@pytest.mark.parametrize("frase, output", test_cases)

def test_quant_palavras(frase, output, solution):
	imp = importlib.import_module(solution)
	assert imp.quant_palavras(frase) == output
