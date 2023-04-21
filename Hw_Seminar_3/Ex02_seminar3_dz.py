'''
Задача 18: Требуется найти в массиве A[1..N]
самый близкий по величине элемент к заданному числу X.
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X.
Если таких значений больше одного, вывести первый найденный.

*Пример:*
5
    1 2 3 4 5
    6
    -> 5
'''
from random import randint

length = int(input('Введи размер массива: '))
number = int(input('Введи искомое число: '))
array = list()

for i in range(length):
    value = randint(-1, 1)
    array.append(value)
print(array)

list_difference = [(abs(i - number)) for i in array]
print(list_difference)
print(array[(list_difference.index(min(list_difference)))])

# Вариант 2

# min = 100
# list_difference = list()
# for i in array:
#     list_difference.append(abs(i - number))

# for i in list_difference:
#     if i < min:
#       min = i
# print(array[list_difference.index(min)])