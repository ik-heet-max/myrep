from random import randint
ran = []
n = int(input("Введите число: "))
for i in range(n):
    ran.append(randint(-100, 100))
print(ran)