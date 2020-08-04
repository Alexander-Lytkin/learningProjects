import pytest

from tasks.task_10.program import func


@pytest.mark.parametrize(
    "s,result", [
        ("", []),
        ("ab c def", []),
        ("a1 b2 3 de4f", [1, 2, 3, 4]),
        ("a11 b234 3 de456f", [11, 234, 3, 456]),
    ]
)
def test_func(s, result):
    assert func(s) == result
