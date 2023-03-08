import pytest
import importlib

test_cases = [
	("bola", "a", 1, 3),
	("palavra", "a", 2, 3),
	("boa partida", "a", 3, 10),
	("boa noite", "a", 4, -1),
	("feliz natal", "g", 2, -1),
	("feliz", "g", 1, -1)
]

@pytest.mark.parametrize("frase, letra, ocorrencia, output", test_cases)

def test_posLetra(frase, letra, ocorrencia, output, solution):
	imp = importlib.import_module(solution)
	assert imp.posLetra(frase, letra, ocorrencia) == output
