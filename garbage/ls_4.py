def xxx(x):
    y = []
    for v in x:
        y.append(v)
    print (y)
    g = tuple(y)
    print(g)



c = (input("Последовательнность числе: "))
print(xxx(c))


lst = [1, 2, 4, 5, 6, 7, 8]
print(f'Первый: {lst[0]}; Последний: {lst[-1]}')