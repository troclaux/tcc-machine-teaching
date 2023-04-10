import pytest
import importlib

test_cases = [
	("quantas frases temos? Uma complicação! Não sei dizer.", 3)
]

@pytest.mark.parametrize("a, output", test_cases)
def test_conta_frases(a, output, solution):
	imp = importlib.import_module(solution)
	assert imp.conta_frases(a) == output
