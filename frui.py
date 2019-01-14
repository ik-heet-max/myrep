fruits1 = ['лимон', 'киви', 'яблоко', 'банан', 'манго', 'слива', 'груша']
fruits2 = ['груша', 'инжир', 'слива', 'абрикос', 'персик']
fruits = []
for i in fruits1:
    for j in fruits2:
        if i == j:
            fruits.append(j)
print(fruits)