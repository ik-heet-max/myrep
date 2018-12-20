from math import sqrt
numbers = [4, 5, 84, -14, 169, 4096, 47, -123123]
roots = []
for i in numbers:
    if i < 0:
        pass
    elif sqrt(i) % 1 != 0:
        pass
    elif sqrt(1) % 1 == 0:
        roots.append(sqrt(i))
print(roots)