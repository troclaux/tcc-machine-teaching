import pytest
import importlib

test_cases = [
	(1, False),
	(2, True),
	(97, True),
	(101, True),
	(100, False),
	(102, False),
]

@pytest.mark.parametrize("primo, output", test_cases)

def test_freq_palavras(primo, output, solution):
	imp = importlib.import_module(solution)
	assert imp.freq_palavras(primo) == output
