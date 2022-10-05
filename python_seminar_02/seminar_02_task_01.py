"""Напишите программу, которая принимает на вход 
вещественное число и показывает сумму его цифр. Пример:
6782 -> 23
0,56 -> 11"""

n = float(input("Введите число: "))
sum1 = 0
sum2 = 0
nz = int(n // 1)
no = n % 1
while nz > 0:
    digit1 = nz % 10
    sum1 = sum1 + digit1
    nz = nz // 10
str_no = str(no).replace(".", "")
l_num = map(int,list(str_no))
sum2 = sum(l_num)
print("Сумма всех цифр = ", sum1 + sum2)
