import pytest

from tasks.task_8.program import func


@pytest.mark.parametrize(
    "l,result", [
        ([], True),
        ([1, 2, 3], True),
        ([1, 1], False),
        ([2, 1, 2], False),
    ]
)
def test_func(l, result):
    assert func(l) == result
