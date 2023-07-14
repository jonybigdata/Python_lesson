# Рекурсия повторение

def fact(x):
    if x == 0:
        return 1
    else:
        return x * fact(x - 1)


# 3 = 3*2*1 = 6
# 6 = (6-1) * (5 -1)


print(fact(5))
