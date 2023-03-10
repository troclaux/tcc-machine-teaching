import pytest
import importlib


# C, Ce, Cs, Fv, Fe, Fs
# C = número de vitórias do Cormengo
# Ce = número de empates do Cormengo
# Cs = número de saldo de gols do Cormengo
# Fv = número de vitórias do Flaminthians
# Fe = número de empates do Flaminthians
# Fs = número de saldo de gols do Flaminthians

# Vitória = 3 pontos
# Empate = 1 ponto

# Pontos >>> gols

# Entrada: 10,5,18,11,2,18 ; Saı́da: ’Empate’
# Entrada: 10,5,18,11,1,18 ; Saı́da: ’Cormengo’
# Entrada: 9,5,-1,10,2,10 ; Saı́da: ’Flaminthias’

test_cases = [
	(0, 0, 0, 0, 0, 0, 'Empate'),
	(10, 5, 10, 8, 11, 11, 'Flaminthias'),
	(5, 20, -1, 11, 2, -5, 'Cormengo'),
]

@pytest.mark.parametrize("lista, output", test_cases)

def test_pontos_por_time(lista, output, solution):
	imp = importlib.import_module(solution)
	assert imp.pontos_por_time(lista) == output
