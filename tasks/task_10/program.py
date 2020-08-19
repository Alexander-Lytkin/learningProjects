"""
Написать функцию func принимающую строку
и возвращающую список чисел встречающихся в строке
"""


def func(s):
    i = 0
    list_s = []
    while i < len(s):
        if s[i].isdigit():
            temp_str = ""
            while i < len(s):
                temp_str += s[i]
                i += 1
                if not s[i].isdigit():
                    list_s.append(int(temp_str))
                    break
        else:
            i += 1
    return list_s
