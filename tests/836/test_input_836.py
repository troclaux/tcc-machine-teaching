import pytest
import importlib

matriz = [
    ["ArthurMoreiraDeAlbuquerque", "0123456789", "TI", "(11) 99999-9999"],
    ["ChristianDeMagalhãesPereira", "9876543210", "Medicina", "(99) 88888-8888"],
    ["JoãoDaSilva", "1234567890", "Engenharia Mecatrônica", "+55 (88) 11111-1111"],
    ["PedroDaCosta", "0987654321", "contabilidade", "(11) 22222-2222"],
    ["MariaDeSouza", "0987654321", "contabilidade", "(11) 22222-2222"],
    ["PedroAlves", "1234567890", "engenharia de produção", "8172733881"]
]

test_cases = [
    ("contabilidade", matriz, [["PedroDaCosta", "0987654321", "contabilidade", "(11) 22222-2222"], ["MariaDeSouza", "0987654321", "contabilidade", "(11) 22222-2222"]]),
    ("engenharia de produção", matriz, [["PedroAlves", "1234567890", "engenharia de produção", "8172733881"]]),
    ("TI", matriz, [["ArthurMoreiraDeAlbuquerque", "0123456789", "TI", "(11) 99999-9999"]]),
    ("Engenharia Mecatrônica", matriz, [["JoãoDaSilva", "1234567890", "Engenharia Mecatrônica", "+55 (88) 11111-1111"]])
]

@pytest.mark.parametrize("setor, matriz, output", test_cases)

def test_busca(setor, matriz, output, solution):
	imp = importlib.import_module(solution)
	assert imp.busca(setor, matriz) == output
