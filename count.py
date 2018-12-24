# только считает слова

import string
i = 0
text = 'Кто мне покажет стриптиз, - тому peace. А кто покажет кулак, - тому fuck'
for punct in string.punctuation:
    while punct in text:
        text = text.replace(punct, '') # избавляемся от знаков препинания
words = text.split(' ')
for word in words:
    if len(word) != 0:                  # исключаем пробелы
        i += 1
    else:
        pass
print(i)