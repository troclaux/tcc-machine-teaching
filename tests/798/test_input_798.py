import pytest
import importlib

test_cases = [
	('adonalsium', {'adonalsium': 1}),
	('life is what happens to us while we are making other plans', {'life': 1, 'is': 1, 'what': 1, 'happens': 1, 'to': 1, 'us': 1, 'while': 1, 'we': 1, 'are': 1, 'making': 1, 'other': 1, 'plans': 1}),
	('dance dance dance', {'dance': 3}),
	('tell me what you pay attention to and I will tell you who you are', {'tell': 2, 'me': 1, 'what': 1, 'you': 3, 'pay': 1, 'attention': 1, 'to': 1, 'and': 1, 'I': 1, 'will': 1, 'who': 1, 'are': 1}),
]

@pytest.mark.parametrize("frase, output", test_cases)

def test_freq_palavras(frase, output, solution):
	imp = importlib.import_module(solution)
	assert imp.freq_palavras(frase) == output
