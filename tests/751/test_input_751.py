import pytest
import importlib

test_cases = [
	('hello', 1),
	('journey before destination ', 3),
	(' i solemnly swear that i am up to no good', 10),
	(' adonalsium ', 1),
]

@pytest.mark.parametrize("frase, output", test_cases)

def test_quant_palavras(frase, output, solution):
	imp = importlib.import_module(solution)
	assert imp.quant_palavras(frase) == output
