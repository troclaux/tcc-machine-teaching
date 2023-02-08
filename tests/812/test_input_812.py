import pytest
import importlib

test_cases = [
	('Olá, hoje cheguei no trabalho e perguntei ao meu chefe: - Preciso voltar mais cedo; já que preciso sair 16 horas', 'Olá  hoje cheguei no trabalho e perguntei ao meu chefe    Preciso voltar mais cedo  já que preciso sair 16 horas'),
	('Boa noite.', 'Boa noite '),
]

@pytest.mark.parametrize("str, output", test_cases)

def test_retira_pontuacao(str, output, solution):
	imp = importlib.import_module(solution)
	assert imp.retira_pontuacao(str) == output
