""" Задайте список из нескольких чисел. Напишите программу,
которая найдёт сумму элементов списка, стоящих на нечётной позиции.
Пример:
 [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
"""
num = [int(i) for i in input("input list: ").split()]
# num = [2, 3, 5, 9, 3]
odd_num = sum(num[1::2])
print(odd_num)
