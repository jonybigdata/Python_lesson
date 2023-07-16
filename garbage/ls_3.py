d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
x = d.values()

print(sorted(x))
g = []
for a in d.values():
    g.append(a)
v = sorted(g)
print(v)

z = []
for b in v[::-1]:
    z.append(b)
print(z)