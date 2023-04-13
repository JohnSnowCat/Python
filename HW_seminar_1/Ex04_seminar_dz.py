'''
Задача 8: Требуется определить,
можно ли от шоколадки размером n × m долек отломить k долек,
если разрешается сделать один разлом по прямой между дольками
(то есть разломить шоколадку на два прямоугольника).
Числа вводятся построчно.

*Пример:*
3 2 4 -> yes
3 2 1 -> no
'''
# 1 способ

weight = int(input('Введи шириу шоколадки: '))
length = int(input('Введи длину шоколадки: '))
piece = int(input('Введи желаемый размер шоколадки: '))
if weight > length:
    temp = weight
    weight = length
    length = temp

if piece >= 1 and piece <= weight * length - weight and (
        piece % weight == 0 or piece % length == 0):
    print(f"YES! От шоколадки {weight} на {length} можно отломить {piece} плиток")
else:
    print("No! Такой кусок не отломить!")

# 2 способ

# weight = int(input('Введи шириу шоколадки: '))
# length = int(input('Введи длину шоколадки: '))
# piece = int(input('Введи желаемый размер шоколадки: '))
# if piece < weight * length and (piece % weight or piece % length):
#     print(f"YES! От шоколадки {weight} на {length} можно отломить {piece} плиток")
# else:
#     print("No! Такой кусок не отломить!")
