import pytest
import importlib

test_cases = [
	("A frase esta invertida", "invertida esta frase a")
]

@pytest.mark.parametrize("a, output", test_cases)
def test_invertefrase(a, output, solution):
	imp = importlib.import_module(solution)
	assert imp.invertefrase(a) == output
