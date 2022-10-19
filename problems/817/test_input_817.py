import pytest
import importlib

test_cases = [
	([1, 2, 4, 5, 6], [4, 5, 6]),
	([1, 2, 4, 5, 6, 7], [5, 6, 7]),
	([1.1, 2, 4, 5, 6], [4, 5, 6]),
	([1.1, 2, 4, 5, 6, 7], [5, 6, 7]),
	([1, 1, 5, 5.5, 6, 7.7], [5, 5.5, 6, 7.7]),
	([1.1, 2, 2.2], [2, 2.2]),
	([1, 2], [2]),
	([1, 2, 2], [2, 2]),
]

@pytest.mark.parametrize("notas_alunos, output", test_cases)

def test_acima_da_media(notas_alunos, output, solution):
	imp = importlib.import_module(solution)
	assert imp.acima_da_media(notas_alunos) == output
