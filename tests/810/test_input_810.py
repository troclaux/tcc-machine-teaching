import pytest
import importlib

test_cases = [
	('Hello! My name is Peter. Do you know where is the hospital? My problem is: I ate a lot of food, now I am feeling sick...', 'sick feeling am i now food of lot a ate i is problem my hospital the is where know you do peter is name my hello'),
	('hello-', 'hello'),
]

@pytest.mark.parametrize("frase, output", test_cases)

def test_inverte(frase, output, solution):
	imp = importlib.import_module(solution)
	assert imp.inverte(frase) == output
