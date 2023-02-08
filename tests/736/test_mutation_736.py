import pytest
import importlib

test_cases = [
	('eu','amo','euamoamoeu')
]

@pytest.mark.parametrize("a, b, output", test_cases)
def test_concatenacao(a, b, output, solution):
	imp = importlib.import_module(solution)
	assert imp.concatenacao(a, b) == output
