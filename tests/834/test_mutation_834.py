import pytest
import importlib

test_cases = [
    ([[1,2,4],
	[1,2,3],
	[1,2,3]],2.11)
]

@pytest.mark.parametrize("a, output", test_cases)
def test_media_matriz(a, output, solution):
	imp = importlib.import_module(solution)
	assert imp.media_matriz(a) == output