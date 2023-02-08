import pytest
import importlib

test_cases = [
	("Teste","Sucesso", "TesteSucessoSucessoTeste")
]

@pytest.mark.parametrize("a, b, output", test_cases)
def test_concatenacao(a, b, output, solution):
	imp = importlib.import_module(solution)
	assert imp.concatenacao(a, b) == output
