import pytest
import importlib

test_cases = [
    ("Olá! Tudo bem? Importa-se de me dizer que horas são...", "Olá  Tudo bem  Importa se de me dizer que horas são   ")
]

@pytest.mark.parametrize("a, output", test_cases)
def test_retira_pontuacao(a, output, solution):
	imp = importlib.import_module(solution)
	assert imp.retira_pontuacao(a) == output