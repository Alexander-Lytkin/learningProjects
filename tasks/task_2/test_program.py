import pytest

from tasks.task_2.program import func


@pytest.mark.parametrize(
    "int_list,n,result", [
        ([6, 2, 3, 4, 5], 3, [6, 4, 5]),
        ([1, 2, 3, 4, 5], 5, []),
        ([1, 2, 3, 4, 5], 0, [1, 2, 3, 4, 5]),
    ]
)
def test_func(int_list, n, result):
    assert func(int_list, n) == result
