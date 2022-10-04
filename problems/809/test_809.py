from solution_182601 import *

import pytest

test_cases = [
	('Meu deus! Que horas são? Vou perder a minha aula...', 3),
	('Olá.', 1)
]

@pytest.mark.parametrize("lista1, lista2, output", test_cases)

def test_intercala(lista1, lista2, output):
	assert intercala(lista1, lista2) == output
