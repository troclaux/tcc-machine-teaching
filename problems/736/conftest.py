# from email.policy import default
import pytest

def pytest_addoption(parser):
        parser.addoption("--solution", action="store", default="accident")

def pytest_generate_tests(metafunc):
    option_value = metafunc.config.option.solution
    if 'solution' in metafunc.fixturenames and option_value is not None:
        metafunc.parametrize("solution", [option_value])