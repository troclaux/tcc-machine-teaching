import pytest
import importlib

test_cases = [
	# Cada carro pode armazenar 5 pessoas
	# (passageiros, capacidade, número de carros necessários)
	(0, 1, 0),
	(2, 3, 1),
	(4, 2, 2),
	(3, 2, 2),
]

@pytest.mark.parametrize("lista_numero, n, output", test_cases)

def test_carros(lista_numero, n, output, solution):
	imp = importlib.import_module(solution)
	assert imp.carros(lista_numero, n) == output
