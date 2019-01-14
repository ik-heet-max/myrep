import random
myFile = open(r"C:\Users\User\a_random_two_and_a_half_thousand_digit_number.txt", "w+")
randomList = []
for i in range(2500):
    if i == 0:
        x = random.randint(1, 9)
    else:
        x = random.randint(0, 9)
    randomList.append(x)
text = ''.join(map(str, randomList))
print(text)
myFile.write(text)
myFile.close()