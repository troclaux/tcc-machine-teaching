import pytest
import importlib

test_cases = [
	("ok", "oK"),
	("bom", "BoM"),
	("a", "a"),
	("boa", "Boa"),
	("tarde", "TaRDe"),
	("ae", "ae"),
	("b", "B"),
	("kd", "KD"),
	("a x", "a X"),
	("e kd", "e KD"),
	("e no", "e No"),
	("bom dia", "BoM Dia"),
	("ae ae", "ae ae"),
	("b x", "B X"),
	("kd x", "KD X"),
]

test_cases_each_choice = [
	("e", "e"),
	("x", "X"),
	("hello world", "HeLLo WoRLD"),
]

test_cases_pair_wise = [
	("ok","oK"),
	("nunca", "NuNCa"),
	("a", "a"),
	("b", "B"),
	("a b", "a B"),
	("a e", "a e"),
	("b c", "B C"),
	("e kd", "e KD"),
	("pai", "Pai"),
	("kd", "KD")
]

@pytest.mark.parametrize("frase, output", test_cases_pair_wise)

def test_uppCons(frase, output, solution):
	imp = importlib.import_module(solution)
	assert imp.uppCons(frase) == output
