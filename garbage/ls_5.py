def sum_int(x):
    b = [int(v) for v in str(x)]
    print(sum(b))


sum_int(7575)

string = 'Python Software Foundation'
print(string.count('t'))

nums = [45, 55, 60, 37, 100, 105, 220]
g = []
for x in nums:
    if x % 5 == 0:
        g.append(x)
print(g)
