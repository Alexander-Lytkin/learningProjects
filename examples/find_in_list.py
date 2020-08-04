def func(value, arr):
    for i, v in enumerate(arr):
        print("index:", i, "value:", v)
        print(v, "==", value, v == value)
        if v == value:
            return i


print(func(2, [55, 3, 7, 2, 8, 90]))
