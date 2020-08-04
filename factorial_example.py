"""
5! = 5*4*3*2*1 = 120
"""


def factorial_1(num):
    if num == 1:
        return num
    else:
        return num * factorial_1(num-1)


def factorial_2(num):
    result = 1
    while num:
        result *= num
        num -= 1
    return result


print(factorial_1(5))
print(factorial_2(5))
