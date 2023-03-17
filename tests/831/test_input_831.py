import pytest
import importlib

test_cases = [
	('tu', 'tupu'),
	('PaLAvRA', 'papalapavrapa'),
	('proporção', 'propopoporçãpãopo'),
	('NÃO', 'nãpãopo'),
]

@pytest.mark.parametrize("palavra, output", test_cases)

def test_lingua_p(palavra, output, solution):
	imp = importlib.import_module(solution)
	assert imp.lingua_p(palavra) == output
