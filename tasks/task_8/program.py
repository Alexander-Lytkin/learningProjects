"""
Написать функцию func принимающую список
и возвращающую True, если все значения списка уникальны, иначе False
"""


def func(les):
    unique_le = []
    for value in les:
        if value not in unique_le:
            unique_le.append(value)
    return unique_le == les
