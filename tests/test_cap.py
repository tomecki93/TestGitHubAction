import pytest
from jobs.job_class import tech_func


@pytest.mark.parametrize("test_input,expected", [("tomek", "Tomek"), ("adam", "Adam")])
def test_capitalize2(test_input, expected):
    obj = tech_func()
    result = obj.capitalize2(test_input)

    assert expected == result
