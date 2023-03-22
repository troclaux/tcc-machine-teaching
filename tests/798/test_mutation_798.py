import pytest
import importlib

test_cases = [
    ("dinheiro é dinheiro e vise versa",{'dinheiro': 2, 'é': 1, 'e': 1, 'vise': 1, 'versa': 1})
]

@pytest.mark.parametrize("a, output", test_cases)
def test_freq_palavras(a, output, solution):
	imp = importlib.import_module(solution)
	assert imp.freq_palavras(a) == output