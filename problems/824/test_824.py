from solution_121511 import *

import pytest

test_cases = [
	("hello world", "HeLLo WoRLD"),

]

@pytest.mark.parametrize("frase, output", test_cases)

def test_uppCons(frase, output):
	assert uppCons(frase) == output
