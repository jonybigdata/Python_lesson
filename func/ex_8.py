"""Напишите функцию Python, которая берет список и возвращает
новый список с уникальными элементами первого списка"""


def get_exus(x):
    y = set(x)
    return list(y)


print((get_exus([1, 2, 3, 3, 3, 3, 4, 5])))


def unic(x):
    num = []
    for z in x:
        if z not in num:
            num.append(z)
    return num



print((unic([1, 2, 3, 3, 3, 3, 4, 5])))