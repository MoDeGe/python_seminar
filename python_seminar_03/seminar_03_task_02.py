"""Напишите программу, которая найдёт произведение 
пар чисел списка. Парой считаем первый и последний элемент, 
второй и предпоследний и т.д.
Пример:
- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]"""
num = [int(i) for i in input("input list: ").split()]
print(num)
P = []
if len(num)%2 == 0:
    P = [num[i]*num[-1-i] for i in range(len(num)//2)]
else:
    P = [num[i]*num[-1-i] for i in range(len(num)//2)]
    P.append(num[len(num)//2]*num[len(num)//2])
print(P)
