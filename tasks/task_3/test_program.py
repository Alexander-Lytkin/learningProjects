import pytest
from tasks.task_3.program import func


@pytest.mark.parametrize(
    "secs,result",
    [
        (59, "0:0:0:59"),
        (60, "0:0:1:0"),
        (3599, "0:0:59:59"),
        (3600, "0:1:0:0"),
        (86399, "0:23:59:59"),
        (86400, "1:0:0:0"),
        (1234567, "14:6:56:7"),
    ],
)
def test_func(secs, result):
    assert func(secs) == result
