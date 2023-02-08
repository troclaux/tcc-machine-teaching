import pytest
import importlib

test_cases = [
    ("Oi! Tudo bem? Tudo... Então tá bom.",4),
    ("Oi! Tudo bem? Tudo... Ok... Então tá bom.",5),
    ("Oi! Tudo bem? Então tá bom.",3)
]

@pytest.mark.parametrize("a, output", test_cases)
def test_conta_frases(a, output, solution):
	imp = importlib.import_module(solution)
	assert imp.conta_frases(a) == output

