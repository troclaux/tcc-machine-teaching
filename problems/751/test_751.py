from solution_204984 import *

import pytest

test_cases = [
	("hello word", '2'),
	(" hello word", '2'),
	("hello word ", '2')
]


@pytest.mark.parametrize("frase, output", test_cases)
def test_quant_palavras(frase, output):
	assert quant_palavras(frase) == output
