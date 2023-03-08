import pytest
import importlib

test_cases = [
	([1, 2, 3, 4, 5], [4, 5]),
	([5, 4, 3, 1, 1], [3, 4, 5]),
	([5, 3, 1, 2, 4], [4, 5]),
	([1.0, 2.0, 3.0, 4.0, 5.0], [4.0, 5.0]),
	([5.0, 4.0, 3.0, 1.0, 1.0], [3.0, 4.0, 5.0]),
	([5.0, 3.0, 1.0, 2.0, 3.0], [3.0, 3.0, 5.0]),
	([1, 2.0, 3, 4.0, 5, 5], [4.0, 5, 5]),
	([5, 4.0, 3, 2.0, 1], [4.0, 5]),
	([5, 3.0, 1, 2.0, 4], [4, 5]),
]

@pytest.mark.parametrize("notas_alunos, output", test_cases)

def test_acima_da_media(notas_alunos, output, solution):
	imp = importlib.import_module(solution)
	assert imp.acima_da_media(notas_alunos) == output
