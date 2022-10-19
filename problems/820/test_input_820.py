import pytest
import importlib

test_cases = [
	("ola", "a", 1, 2),
	("boa noite", "u", 2, -1),
	("boa noite", "o", 2, 5),
	("ola", "e", 2, -1),
	("boa noite", "u", 1, -1),
]

@pytest.mark.parametrize("frase, letra, ocorrencia, output", test_cases)

def test_posLetra(frase, letra, ocorrencia, output, solution):
	imp = importlib.import_module(solution)
	assert imp.posLetra(frase, letra, ocorrencia) == output
