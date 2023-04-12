import pytest
import importlib

test_cases = [
	([[1,2]], 1.5),
	([[1,2], [3,4]], 2.5)
]

@pytest.mark.parametrize("a, output", test_cases)
def test_media_matriz(a, output, solution):
	imp = importlib.import_module(solution)
	assert imp.media_matriz(a) == output


