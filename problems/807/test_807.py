from solution_211714 import *

import pytest

test_cases = [
	('Meu deus! Que horas são? Vou perder a minha aula...', 3),
	('Olá.', 1)
]

@pytest.mark.parametrize("a, output", test_cases)

def test_conta_frases(a, output):
	assert conta_frases(a) == output
