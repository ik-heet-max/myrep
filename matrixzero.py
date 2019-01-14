import random
import pprint
size = int(input("Enter size of matrix: "))
matr = []
for rows in range(size):
    zero = random.randint(1, size - 1)
    row = []
    for i in range(zero):
        x = random.randint(1, 100)
        row.append(x)
    row.append(0)
    for i in range(size - zero - 1):
        x = random.randint(1, 100)
        row.append(x)
    matr.append(row)
pprint.pprint(matr)