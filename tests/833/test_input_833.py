import pytest
import importlib

test_cases = [
    (1, [[1, 1]], 2),
    (-1, [], 0),
    (0, [], 0),
    (1, [], 0),
    (0, [[1]], 0),
    (1, [[1]], 1),
    (0, [[0, 0]], 2),
    (-1, [[-1]], 1),
    (-1, [[-1, -1]], 2),
    (1, [[2, 3]], 0),
    (1, [[1, 2]], 1)
]

@pytest.mark.parametrize("numero, matriz, output", test_cases)

def test_conta_numero(numero, matriz, output, solution):
    imp = importlib.import_module(solution)
    assert imp.conta_numero(numero, matriz) == output

