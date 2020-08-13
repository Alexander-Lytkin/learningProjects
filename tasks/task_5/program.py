"""
Написать функцию func принимающую словарь
с строковами ключами и целочисленными значениями
и возвращающую сортированный по значениям словарь
"""


def func(d):
    sorted_d = sorted(d.items(), key=lambda para: para[1])
    return dict(sorted_d)
