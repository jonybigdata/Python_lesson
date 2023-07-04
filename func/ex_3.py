# Напишите функцию Python для умножения всех чисел в списке.
def sum_x(x):
    num = 1
    for y in x:
        num *= y
    return num


print(sum_x([8, 2, 3, -1, 7]))