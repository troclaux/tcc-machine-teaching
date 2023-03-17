import sys
import pytest
import importlib

test_cases = [
	("RecursosHumanos", [[]], []),
	("RecursosHumanos", [["AdalbertoFerreira", 1091982, "Contabilidade", "(21)99281 - 2983"]], []),
	("RecursosHumanos", [["AdalbertoFerreira", 1091982, "Contabilidade", "(21)99281 - 2983"], ["FlaviaAmorim", 1128938, "Contabilidade", "(22)99273 - 9404"]], []),
	("RecursosHumanos", [["JulianaVasconcelos", 1111722, "RecursosHumanos", "(21)99848 - 1902"], ["FlaviaAmorim", 1128938, "Contabilidade", "(22)99273 - 9404"]], [['JulianaVasconcelos', 1111722, '(21)99848 - 1902']]),
	("RecursosHumanos", [["JulianaVasconcelos", 1111722, "RecursosHumanos", "(21)99848 - 1902"]], [['JulianaVasconcelos', 1111722, '(21)99848 - 1902']]),
]

@pytest.mark.parametrize("a, b, output", test_cases)
def test_busca(a, b, output, solution):
	imp = importlib.import_module(solution)
	assert imp.busca(a, b) == output
