import pytest
import importlib

# Input:
# [['Cormengo', 'Flamínthians', [1, 0]], ['Flamínthians', 'Cormengo', [2, 2]]]

# Output:
# {'Cormengo': 4, 'Flamínthians': 1}

test_cases = [
	([['Cormengo', 'Flamínthians', [1, 0]], ['Flamínthians', 'Cormengo', [2, 2]]], {'Cormengo': 4, 'Flamínthians': 1}),
	([['Cormengo', 'Flamínthians', [0, 1]], ['Flamínthians', 'Cormengo', [2, 2]]], {'Cormengo': 1, 'Flamínthians': 4}),
	([['Cormengo', 'Flamínthians', [1, 1]], ['Flamínthians', 'Cormengo', [2, 2]]], {'Cormengo': 2, 'Flamínthians': 2}),
	([['Cormengo', 'Flamínthians', [1, 0]], ['Flamínthians', 'Cormengo', [2, 1]]], {'Cormengo': 3, 'Flamínthians': 3}),
	([['Cormengo', 'Flamínthians', [0, 1]], ['Flamínthians', 'Cormengo', [2, 1]]], {'Cormengo': 0, 'Flamínthians': 6}),
	([['Cormengo', 'Flamínthians', [1, 1]], ['Flamínthians', 'Cormengo', [2, 1]]], {'Cormengo': 1, 'Flamínthians': 4}),
	([['Cormengo', 'Flamínthians', [1, 0]], ['Flamínthians', 'Cormengo', [1, 2]]], {'Cormengo': 6, 'Flamínthians': 0}),
	([['Cormengo', 'Flamínthians', [0, 1]], ['Flamínthians', 'Cormengo', [1, 2]]], {'Cormengo': 3, 'Flamínthians': 3}),
	([['Cormengo', 'Flamínthians', [1, 1]], ['Flamínthians', 'Cormengo', [1, 2]]], {'Cormengo': 4, 'Flamínthians': 1}),
]

@pytest.mark.parametrize("lista, output", test_cases)

def test_pontos_por_time(lista, output, solution):
	imp = importlib.import_module(solution)
	assert imp.pontos_por_time(lista) == output
