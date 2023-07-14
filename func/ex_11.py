def int_i(lst):
    f = []
    for x in lst:
        if x % 2 == 0:
            f.append(x)
    return f

print(int_i([1, 2, 3, 4, 5, 6, 7, 8, 9]))
