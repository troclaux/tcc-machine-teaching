import pytest
import importlib

test_cases = [
	('a', 'b', 0, 'b'),
	('c', 'd', 0, 'd'),
	('efgh ijkl mnop', 'q', 0, 'qfgh ijkl mnop'),
	('palavra', 'x', 6, 'palavrx'),
	('rst uvwxy', 'z', 8, 'rst uvwxz'),
]

@pytest.mark.parametrize("s, x, i, output", test_cases)

def test_substitui(s, x, i, output, solution):
	imp = importlib.import_module(solution)
	assert imp.substitui(s, x, i) == output
