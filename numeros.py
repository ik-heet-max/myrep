n = [2, 4, 6, 5, 228, 69]
new = []
for i in n:
    if i % 2 == 0:
        new.append(i/4)
    elif i % 2 != 0:
        new.append(i*2)
print(new)
