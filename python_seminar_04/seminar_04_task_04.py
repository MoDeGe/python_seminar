"""Задана натуральная степень k. Сформировать случайным 
образом список коэффициентов (значения от 0 до 100) многочлена 
и записать в файл многочлен степени k.
Пример:
- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0"""
from random import randint
from sympy import symbols
from math import prod

def write_file(st):
    with open('python_seminar_04/task04.txt', 'a') as data:
        data.write(st + "\n")

max_val = 100
k = int(input('Введите натуральную степень k: '))
# коэфф. при старшей степени не должен быть равен 0
koeff = [randint(-max_val, max_val) for i in range(k)] + [randint(1, max_val)]
x = symbols('x')
st = ' '
tp = (sum(map(prod,zip(koeff, [x**i for i in range(k + 1)]))), '= 0')
st = st.join(map(str, tp))
print(st)
write_file(st)
