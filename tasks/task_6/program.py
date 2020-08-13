"""
Написать функцию func принимающую целое число
и возвращающую сумму цифр этого числа
"""


def func(num):
    result = 0
    while num > 0:
        digit = num % 10
        num = num // 10
        result += digit
    return result
