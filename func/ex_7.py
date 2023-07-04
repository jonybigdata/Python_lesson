"""Напишите функцию Python, которая принимает строку и
рассчитывает количество букв верхнего и нижнего регистра.
Пример строки : «Быстрая Лиса Бровей»"""


def get_count(x):
    low = 0
    up = 0
    for z in x:
        if z.islower():
            low += 1
    for z in x:
        if z.isupper():
            up += 1
    return low, up


print(get_count("Быстрая Лиса Бровей"))


def str_test(x):
    d = {"Upper": 0, "Lower": 0}
    for z in x:
        if z.islower():
            d["Upper"] += 1
        elif z.isupper():
            d["Lower"] += 1
        else:
            pass
    print("Оригинальная строка: x")
    print("Вверхний регистр: ", d["Upper"])
    print("Нижний регистр: ", d["Lower"])
    

print(str_test("Быстрая Лиса Бровей"))
