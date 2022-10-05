"""Напишите программу, которая будет преобразовывать 
десятичное число в двоичное.
Пример:
- 45 -> 101101
- 3 -> 11
- 2 -> 10"""
n = int(input("Введите число: "))
N = n
d = ""
while n > 0:
    d = str(n%2) + d
    n = n//2
print(f"Число {str(N)} в двоичной системе {d}")
