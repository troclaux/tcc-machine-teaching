from solution_204986 import *

import pytest

test_cases = [
	("hello world", '2'),
	(" hello world", '2'),
	("hello world ", '2')
]


@pytest.mark.parametrize("frase, output", test_cases)
def test_quant_palavras(frase, output):
	assert quant_palavras(frase) == output
