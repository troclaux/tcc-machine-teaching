from solution_50914 import *

import pytest

def test_capital_case():
	assert concatenacao("A", "B") == "ABBA"

print(concatenacao("A", "B"))