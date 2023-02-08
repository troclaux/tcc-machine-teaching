import pytest
import importlib

test_cases = [
    (2, 1, 2, 3, 2, 1, "Flaminthias"),
    (3, 2, 1, 2, 1, 2, "Cormengo"),
    (3, 1, 1, 3, 2, 2, "Flaminthias"),
    (1, 1, 1, 0, 3, 2, "Cormengo"),
    (0, 3, 2, 1, 1, 1, "Flaminthias"),
    (3, 1, 1, 3, 1, 1, "Empate"),
    (3, 3, 2, 3, 3, 3, "Flaminthias"),
    (4, 4, 4, 5, 4, 4, "Flaminthias")
]

@pytest.mark.parametrize("a, b, c, d, e, f, output", test_cases)
def test_pontos_por_time(a, b, c, d, e, f, output, solution):
	imp = importlib.import_module(solution)
	assert imp.pontos_por_time(a, b, c, d, e, f) == output