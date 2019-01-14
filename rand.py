import random
randomList = [random.randint(0, 50) for i in range(10)]
print(randomList)
print([i**2 for i in randomList])