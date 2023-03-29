import pytest
import importlib

# test_cases_all_comb = [
# 	("ok", "oK"),
# 	("bom", "BoM"),
# 	("a", "a"),
# 	("boa", "Boa"),
# 	("tarde", "TaRDe"),
# 	("ae", "ae"),
# 	("b", "B"),
# 	("kd", "KD"),
# 	("a x", "a X"),
# 	("e kd", "e KD"),
# 	("e no", "e No"),
# 	("bom dia", "BoM Dia"),
# 	("ae ae", "ae ae"),
# 	("b x", "B X"),
# 	("kd x", "KD X"),
# ]

# test_cases_each_choice = [
# 	("e", "e"),
# 	("x", "X"),
# 	("hello world", "HeLLo WoRLD"),
# ]

test_cases = [
	("aeiou", "aeiou"),
	("bcdfgh", "BCDFGH"),
	("palavra", "PaLaVRA"),
	("aeiou ou", "aeiou ou"),
	("bcdfgh jklmn", "BCDFGH JKLMN"),
	("exemplo de frase", "eXeMPLo De FRaSe"),
]

@pytest.mark.parametrize("frase, output", test_cases)

def test_uppCons(frase, output, solution):
	imp = importlib.import_module(solution)
	assert imp.uppCons(frase) == output
