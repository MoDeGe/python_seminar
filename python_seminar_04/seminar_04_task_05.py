"""Даны два файла, в каждом из которых находится запись многочлена. 
Задача - сформировать файл, содержащий сумму многочленов."""
import regex

def read_file(user_file):
    with open(user_file, 'r', encoding='utf-8') as pol:
        result = pol.read()
        return result

file1 = read_file('python_seminar_04/first.txt')
file2 = read_file('python_seminar_04/second.txt')

print(file1)
print(file2)

# попробовал регулярку, но что-то не получается. что-то сложно.
