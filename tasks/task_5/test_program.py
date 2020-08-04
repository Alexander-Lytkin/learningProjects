import pytest

from tasks.task_5.program import func


@pytest.mark.parametrize(
    "d,result", [
        ({}, {}),
        ({"a": 4, "b": 1, "c": 3, "d": 2}, {"b": 1, "d": 2, "c": 3, "a": 4}),
    ]
)
def test_func(d, result):
    assert func(d) == result
