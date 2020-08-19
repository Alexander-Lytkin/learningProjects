"""
Написать функцию func принимающую список
и возвращающую список уникальных значений
"""


def func(le):
    dict_le = {}
    for value in le:
        if not dict_le.get(value):
            dict_le[value] = 1
        else:
            dict_le[value] += 1
    values = dict_le.items()
    return [key for key, value in values if value == 1]
