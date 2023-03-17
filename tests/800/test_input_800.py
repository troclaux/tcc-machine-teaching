import pytest
import importlib

produtos = {
    'amaciante':4.99,
    'arroz':10.90,
    'biscoito':1.69,
    'cafe':6.98,
    'chocolate':3.79,
    'farinha':2.99
}


test_cases = [
	(["amaciante", "arroz", 'arroz', "biscoito", "cafe", 'biscoito' ,'arroz',"chocolate"], produtos, 51.84)
	(["farinha"], produtos, 2.99)
]

@pytest.mark.parametrize("compras, produto, output", test_cases)

def test_total(compras, produto, output, solution):
	imp = importlib.import_module(solution)
	assert imp.total(compras, produto) == output
