import pytest
import importlib

test_cases = [
	('Lucas','x',2,'Luxas'),
    ('Lucas','x',0,'xucas'),
    ('Lucas','x',5,'i invalido')
]

@pytest.mark.parametrize("a, b, c, output", test_cases)
def test_substitui(a, b, c, output, solution):
	imp = importlib.import_module(solution)
	assert imp.substitui(a, b, c) == output
