"""
Написать функцию func принимающую список чисел int_list и число n
и возвращающую список с элементами списка int_list больше n
"""


def func(int_list, n):
    result = []
    for num in int_list:
        if num > n:
            result.append(num)
    return result
