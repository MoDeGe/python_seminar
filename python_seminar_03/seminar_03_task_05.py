"""Задайте число. Составьте список чисел Фибоначчи, 
в том числе для отрицательных индексов.
Пример:
- для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
"""
m = int(input("Введите число: "))

def fib(n):
    if n in [1,2]:
        return 1
    else:
        return fib(n-1) + fib(n-2)

f_n = []
for e in range(1,m+1):
    f_n.append(fib(e))
# print(f_n)

nf_n = []
for e in range(1,m+1):
    nf_n.append((-1)**(e+1) * fib(e))
# print(nf_n[::-1])

str = nf_n[::-1] + f_n
str.insert(m, 0)
print(str)
