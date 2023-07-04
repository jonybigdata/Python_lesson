# Напишите программу на Python для обращения строки.


def revers(x):
    z = ""
    index = len(x)
    while index > 0:
        z += x[index - 1]
        index -= 1
    return z

print(revers("123456789"))
