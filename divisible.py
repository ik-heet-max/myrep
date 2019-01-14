import random
randomList = []
for i in range(30):
    x = random.randint(-50, 50)
    randomList.append(x)
print(randomList)
print([x for x in randomList if x % 3 == 0 and x > 0 and x % 4 != 0])