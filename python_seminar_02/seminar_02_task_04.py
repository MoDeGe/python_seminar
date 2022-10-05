n = int(input('Введите число '))
list = []

for i in range(-n, n+1):
    list.append(i)

result = 1
patch = 'file.txt'
data = open(patch, 'r')

for line in data:
    pos = int(line)
    result *= list[pos]
print(f"Результат перемножения чисел: {result}")
