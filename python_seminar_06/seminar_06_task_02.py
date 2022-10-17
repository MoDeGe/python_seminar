"""Дана последовательность чисел. Получить список 
уникальных элементов заданной последовательности, 
список повторяемых и убрать дубликаты из заданной последовательности.
Пример:
[1, 2, 3, 5, 1, 5, 3, 10] => [2, 10] и [1, 3, 5] и [1, 2, 5, 3, 10]"""

from random import randint
from collections import Counter

def create_list(size, m, n):
    return [randint(m, n) for i in range(size)]

def get_unique_value(list):
    c = Counter(list)
    k = c.most_common()
    for tup in k:
        number = tup[0]
        cnt = tup[1]
        if cnt == 1:
            unique_value.append(number)
    return unique_value

def get_dup_value(list):
    c = Counter(list)
    k = c.most_common()
    for tup in k:
        number = tup[0]
        cnt = tup[1]
        if cnt > 1:
            dup_value.append(number)
    return dup_value 

def get_wo_dup_value(list):
    return [i for i in set(list)]

size = 10
m = 1
n = 10
unique_value = []
dup_value = []

origin = create_list(size, m, n)
print(origin)
print(30 * "-")
print(get_unique_value(origin))
print(get_dup_value(origin))
print(get_wo_dup_value(origin))
