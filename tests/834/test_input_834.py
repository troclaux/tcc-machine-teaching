import pytest
import importlib

test_cases = [
	([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 5.0),
	([[-5]], -5.0),
	([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]], 8.5),
	([[1]], 1.0),
	([[-1, -2], [-3, -4], [-5,-6]], -3.5),
	([[1, 2, 0], [0, 5, 6], [7, 0, 9], [10, 11, 0]], 4.25),
	([[-1, 2, 3, -4], [5, -6, -7, 8], [9, -10, -11, -12]], -2.0),
	([[30, 95]], 62.5)
]

@pytest.mark.parametrize("matriz, output", test_cases)

def test_media_matriz(matriz, output, solution):
	imp = importlib.import_module(solution)
	assert imp.media_matriz(matriz) == output

