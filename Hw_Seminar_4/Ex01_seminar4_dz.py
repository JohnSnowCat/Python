'''
Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа. n — кол-во элементов первого множества.
m — кол-во элементов второго множества.
Затем пользователь вводит сами элементы множеств.
'''

number1 = int(input('Введи размер первого массива данных: '))
number2 = int(input('Введи размер второго массива данных: '))

list_first = list_second = []

# 1 вариант заполнения массива
for i in range(number1):
    list_first.append(int(input('Введи значение первого массива данных: ')))
print(list_first)

# 2 вариант заполнения массива
list_second = [int(input('Введи значения второго массива: '))
               for _ in range(0, number2)]
print(list_second)

result = list(set(list_first) & set(list_second))

print(result)