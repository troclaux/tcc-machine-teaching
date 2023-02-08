import sys
import pytest
import importlib

test_cases = [
	("frase, sem. pontuação!", "frase sem pontuação")
]

@pytest.mark.parametrize("a, output", test_cases)
def test_retira_pontuacao(a, output, solution):
	imp = importlib.import_module(solution)
	assert imp.retira_pontuacao(a) == output
