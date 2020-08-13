"""
Написать функцию func принимающую число секунд
и возвращающую строку вида дни:часы:минуты:секунды
"""


def func(secs):
    d = secs // (60 * 60 * 24)
    h = secs // (60 * 60) % 24
    m = secs // 60 % 60
    s = secs % 60

    return f"{d}:{h}:{m}:{s}"
