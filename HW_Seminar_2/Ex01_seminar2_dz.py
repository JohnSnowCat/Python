'''
Задача 10: На столе лежат n монеток.
Некоторые из них лежат вверх решкой, а некоторые – гербом.
Определите минимальное число монеток, которые нужно перевернуть,
чтобы все монетки были повернуты вверх одной и той же стороной.
Выведите минимальное количество монет, которые нужно перевернуть.
С клавиатуры вводятся число монет и сами монеты построчно.
Пример:
Ввод: 1 1 1 1 0 0 -> 2
'''
amount = int(input("Введи количество моент: "))
count = 0

for i in range(0, amount):
    coin = int(input("Введи сторону моентки: "))
    if coin == 1:
        count += 1
if amount - count <= count:
    print(amount - count)
elif amount - count > count:
    print(count)
