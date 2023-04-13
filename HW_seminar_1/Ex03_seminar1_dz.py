# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.

# *Пример:*
# 385916 -> yes
# 123456 -> no


number = int(input("Введите 6-ти значный номер билета: "))
sum1 = 0
sum2 = 0
case1 = number // 1000
case2 = number % 1000

while case1 > 0 and case2 > 0:
    sum1 = sum1 + case1 % 10
    case1 //= 10
    sum2 = sum2 + case2 % 10
    case2 //= 10
if sum1 == sum2:
    print("Билет счастливый")
else:
    print("Билет не счастливый")



    # 1 способ

ticket_num = int(input('Введите номер билета: '))
first3 = (ticket_num // 100000 +
          ticket_num // 10000 % 10 +
          ticket_num // 1000 % 10)

second3 = (ticket_num // 100 % 10 +
           ticket_num // 10 % 10 +
           ticket_num % 10)

if first3 == second3:
    print('YES')
else:
    print('NO')

# 2 способ
ticket_num = input('Введите номер билета: ')
first3 = 0
second3 = 0
for i in range(len(ticket_num)//2):
    first3 += int(ticket_num[i])
    second3 += int(ticket_num[::-1][i])  # 123456 -> 654321 -> 6, 5, 4
if first3 == second3:
    print('YES')
else:
    print('NO')

# 'abc'[0] -> 'a'
# 'abc'[0:2] -> 'ab'
# 'abc'[0:3:2] -> 'ac'