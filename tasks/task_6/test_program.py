import pytest

from tasks.task_6.program import func


@pytest.mark.parametrize(
    "num,result", [
        (1, 1),
        (12, 3),
        (654321, 21),
    ]
)
def test_func(num, result):
    assert func(num) == result
