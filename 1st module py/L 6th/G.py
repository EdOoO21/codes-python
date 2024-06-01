import re
from collections import Counter


def find_most_common_words(text, num):
    pattern = re.compile('[a-zA-Zа-яА-Я]+')
    match = re.findall(pattern, text)
    counter = Counter(match)
    counter = sorted(counter.items(), key=lambda item: -item[1])
    return counter[:num]


print(find_most_common_words('Также Также в тексте тексте тексте могут встречаться числа и иные символы, не относящиеся к словами (например, знаки препинания). Учесть это вам помогут старые добрые регулярные выражения (модуль re).',2))