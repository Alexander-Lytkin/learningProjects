import pytest

from tasks.task_7.program import func


@pytest.mark.parametrize(
    "str_1,str_2,result", [
        ("a", "abababa", 4),
        ("ab", "abababa", 3),
        ("aba", "abababa", 2),
        ("", "abababa", 8),
        ("c", "abababa", 0),
        ("", "", 1),
    ]
)
def test_func(str_1, str_2, result):
    assert func(str_1, str_2) == result
