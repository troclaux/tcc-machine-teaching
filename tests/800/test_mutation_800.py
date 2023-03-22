import pytest
import importlib

lista_de_compras = ["biscoito", "chocolate", "farinha"]
produtos = {
"amaciante":4.99,
"arroz":10.90,
"biscoito":1.69,
"cafe":6.98,
"chocolate":3.79,
"farinha":2.99
}

test_cases = [
    (lista_de_compras, produtos,8.47)
]

@pytest.mark.parametrize("a, b, output", test_cases)
def test_total(a, b, output, solution):
	imp = importlib.import_module(solution)
	assert imp.total(a, b) == output