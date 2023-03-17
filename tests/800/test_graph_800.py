import pytest
import importlib

test_cases = [
	([], {"cafe":0.99}, 0),
	(["cafe"], {"leite":1}, 0),
    (["cafe", "leite"], {"leite":2.5}, 2.5),
    (["leite", "cafe"], {"leite":2.5}, 2.5),
    (["cafe", "leite"], {"cafe":0.99, "leite":1}, 1.99),
    (["cafe"], {"cafe":0.99}, 0.99),
]

@pytest.mark.parametrize("a, b, output", test_cases)
def test_total(a, b, output, solution):
	imp = importlib.import_module(solution)
	assert imp.total(a, b) == output
