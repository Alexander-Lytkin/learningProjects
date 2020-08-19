"""
Написать функцию func принимающую словарь
с строковыми ключами и числовыми значениями
и возвращающую отсортированный список из трех ключей
с самыми высокими значениями
"""


def func(d_dict):
    sorted_dict = sorted(d_dict, key=d_dict.get, reverse=True)
    return sorted(sorted_dict[:3])
