# Напишите функцию Python для вычисления
# факториала числа (неотрицательное целое число).
# Функция принимает число в качестве аргумента


def factorial(x):
    b = []
    x += 1
    while x > 1:
        x -= 1
        b.append(x)

    num = 1
    for z in b:
        num *= z
    return num

print(factorial(6))


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
n=int(input("Input a number to compute the factiorial : "))
print(factorial(n))