import pytest
from tasks.task_11.program import func


@pytest.mark.parametrize(
    "lst,result",
    [
        ([], []),
        ([1, 1], []),
        ([1, 2, 1], [2]),
        (["a", 1, 2, "1", "a", "ab", 2], [1, "1", "ab"]),
    ],
)
def test_func(lst, result):
    assert func(lst) == result
