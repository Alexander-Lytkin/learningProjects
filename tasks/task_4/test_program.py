import pytest

from tasks.task_4.program import func


@pytest.mark.parametrize(
    "list_1,list_2,result", [
        ([], [], []),
        ([1], [2], []),
        ([4, 2, 1, 3, 1], [2, 1, 2], [1, 2]),
    ]
)
def test_func(list_1, list_2, result):
    assert func(list_1, list_2) == result
