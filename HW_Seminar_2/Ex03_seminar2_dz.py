'''
Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2^k), не превосходящие числа N.

Пример:
Ввод: 13 -> 1, 2, 4, 8
'''

number = int(input('Введите число: '))
pow = 0
while (2 ** pow <= number):
    print(2 ** pow, end=" ")
    pow += 1
