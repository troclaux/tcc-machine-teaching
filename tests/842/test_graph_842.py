import pytest
import importlib

test_cases = [
	(3, 2, 2, 2, 2, 2, "Cormengo"),
	(1, 1, 1, 2, 1, 1, "Flaminthias"),
	(0, 0, 1, 0, 0, 0, "Cormengo"),
	(2, 2, 2, 2, 2, 3, "Flaminthias"),
	(0, 0, 0, 0, 0, 0, "Empate"),
]

@pytest.mark.parametrize("a, b, c, d, e, f, output", test_cases)
def test_pontos_por_time(a, b, c, d, e, f, output, solution):
	imp = importlib.import_module(solution)
	assert imp.pontos_por_time(a, b, c, d, e, f) == output
