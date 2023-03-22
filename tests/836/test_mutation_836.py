import pytest
import importlib

P = [["Lucas", "1171", "Contabilidade", "(21)99876541"],
	["Marcelo", "1172", "Financeiro", "(21)99876542"],
	["Dani", "1173", "Contabilidade", "(21)99876543"],
	["Andrea", "1174", "RecursosHumanos", "(21)99876544"]]

test_cases = [
    ("Contabilidade", P, [['Lucas', '1171', '(21)99876541'], ['Dani', '1173', '(21)99876543']])
]

@pytest.mark.parametrize("a, b, output", test_cases)
def test_busca(a, b, output, solution):
	imp = importlib.import_module(solution)
	assert imp.busca(a, b) == output