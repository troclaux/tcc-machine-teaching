import pytest
import importlib

test_cases = [
    ([5,5.4,4,5.1,7],[5.4,7])
]

@pytest.mark.parametrize("a, output", test_cases)
def test_acima_da_media(a, output, solution):
	imp = importlib.import_module(solution)
	assert imp.acima_da_media(a) == output