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

@pytest.mark.parametrize("passageiros, capacidade, output", test_cases)

def test_carros(passageiros, capacidade, output, solution):
	imp = importlib.import_module(solution)
	assert imp.carros(passageiros, capacidade) == output
