"""
Написать функцию func принимающую два списка
и возвращающую сортированный без дублей список
из элементов общих для двух списков
"""


def func(list_1, list_2):
    result = []
    for item in set(list_1):
        if item in set(list_2):
            result.append(item)
    return sorted(result)
