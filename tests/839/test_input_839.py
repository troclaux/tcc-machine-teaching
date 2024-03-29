import pytest
import importlib

test_cases = [
	# Cada carro pode armazenar 5 pessoas
	# (passageiros, capacidade, número de carros necessários)
	(0, 10, 0),
	(7, 33, 1),
	(33, 10, 4),
	(10, 10, 1),
]

@pytest.mark.parametrize("passageiros, capacidade, output", test_cases)

def test_carros(passageiros, capacidade, output, solution):
	imp = importlib.import_module(solution)
	assert imp.carros(passageiros, capacidade) == output
