import pytest
import importlib

test_cases = [
	('Meu deus! Que horas são? Vou perder a minha aula...', 3),
	('Olá.', 1)
]

@pytest.mark.parametrize("a, output", test_cases)

def test_conta_frases(a, output, solution):
	imp = importlib.import_module(solution)
	assert imp.conta_frases(a) == output
