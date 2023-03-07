import pytest
import importlib

test_cases = [
	('Durante meu expediente, disse ao meu chefe: - Preciso voltar mais cedo; já que preciso sair 16 horas... Mas já são 17 horas! Como pude esquecer de olhar o relógio?', 'Durante meu expediente  disse ao meu chefe    Preciso voltar mais cedo  já que preciso sair 16 horas    Mas já são 17 horas  Como pude esquecer de olhar o relógio '),
	('Olá.', 'Olá '),
]

@pytest.mark.parametrize("str, output", test_cases)

def test_retira_pontuacao(str, output, solution):
	imp = importlib.import_module(solution)
	assert imp.retira_pontuacao(str) == output
