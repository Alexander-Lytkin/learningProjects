import pytest
from tasks.task_9.program import func


@pytest.mark.parametrize(
    "d,result",
    [
        ({"a": 0, "b": 2, "c": 1, "d": 6, "e": 3}, ["b", "d", "e"]),
        ({"a": 0, "d": 6, "b": 2, "c": 1, "e": 3}, ["b", "d", "e"]),
        ({"a": 0, "d": 0, "b": 0, "c": 0, "e": 0}, ["a", "b", "d"]),
        ({"a": 0, "d": 6}, ["a", "d"]),
        ({}, []),
    ],
)
def test_func(d, result):
    assert func(d) == result
