from solution_205005 import *

import pytest

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

def test_quant_palavras(frase, output):
	assert quant_palavras(frase) == output
