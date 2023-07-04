# Напишите функцию Python, чтобы
# найти максимум трех чисел


def get_max(a, b):
    return a if a > b else b


def get_max1(a, b, c):
    return get_max(a, get_max(b, c))


print(get_max1(7, 11, 2))


def max_two(x, y):
    if x > y:
        return x
    return y


def max_three(x, y, z):
    return max_two(x, max_two(y, z))


print(max_three(221, 133, 432))
