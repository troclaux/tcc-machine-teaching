import pytest
import importlib

test_cases = [
	("", {}),
	("Dinheiro", {"Dinheiro":1}),
	("sim sim", {"sim":2}),
	("esta certo", {"esta":1, "certo":1})
]

@pytest.mark.parametrize("a, output", test_cases)
def test_freq_palavras(a, output, solution):
	imp = importlib.import_module(solution)
	assert imp.freq_palavras(a) == output

