"""
Написать функцию func принимающую на вход имя и возвращающую "Hello, <name>!"
Если имя не указано вернуть "Hello, World!"
"""


def func(name=None):
    if name:
        return f"Hello, {name}!"
    else:
        return "Hello, World!"
