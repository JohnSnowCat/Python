'''
Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

*Пример:*
5
    1 2 3 4 5
    3
    -> 1
'''
from random import randint

array = list()
length = int(input('Введите размер массива: '))

for i in range(length):
    value = randint(1, 3)
    array.append(value)
print(array)

number = int(input('Введите искомое значение: '))
result = [i for i in array if i == number]
print(len(result))

# Вариант 2

# count = 0
# for i in array:
#     if i == number:
#         count += 1
# print(f"Искомое значение {number} встречается в списке {array} {count} раз")
