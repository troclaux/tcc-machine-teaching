import pytest
import importlib

test_cases = [
	([1,2,3,4,5,6,7,8,9,10], [5,6,7,8,9,10])
]

@pytest.mark.parametrize("a, output", test_cases)
def test_acima_da_media(a, output, solution):
	imp = importlib.import_module(solution)
	assert imp.acima_da_media(a) == output
