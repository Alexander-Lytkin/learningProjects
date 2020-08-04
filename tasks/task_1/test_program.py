from tasks.task_1.program import func


class TestFunc:
    def test_func_with_name(self):
        assert func("Вася") == "Hello, Вася!"

    def test_func_without_name(self):
        assert func() == "Hello, World!"
