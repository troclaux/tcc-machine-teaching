import pytest
import importlib

test_cases = [
    ("Nossa, como eu gosto de chocolate","chocolate de gosto eu como nossa")
]

@pytest.mark.parametrize("a, output", test_cases)
def test_inverte(a, output, solution):
	imp = importlib.import_module(solution)
	assert imp.inverte(a) == output